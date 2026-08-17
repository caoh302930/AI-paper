"""Deep paper reading (lobehub/shuaiqi361 paper-reading style) + divergent ideas."""
from __future__ import annotations

from openai import OpenAI

from . import ROOT, env

SYSTEM = """你是一名认真的 AI 研究方向高级博士生助教。目标是**教学，不是罗列摘要**。
用简体中文。遵循 Feynman（讲明白）+ Pareto（把 80% 篇幅给真正关键的 20%）。
禁止编造实验数字；读不到的内容必须标注「信息不足 / 未在全文中核实」。
数学用 `$...$` / `$$...$$`，比较符用 `\\lt`/`\\gt`。"""


def _client() -> OpenAI:
    return OpenAI(
        base_url=env("LLM_BASE_URL"),
        api_key=env("LLM_API_KEY") or "EMPTY",
        timeout=600.0,
        max_retries=3,
    )


def _load_template_hints() -> str:
    p = ROOT / "skills/paper-reading/references/output-template.md"
    if p.exists():
        # keep prompt bounded
        return p.read_text(encoding="utf-8")[:6000]
    return ""


def generate_ideas(*, video: dict, paper: dict, parse_md: str) -> str:
    """Second-pass divergent ideas (keeps 解析 from eating the token budget)."""
    arxiv = paper.get("arxiv") or {}
    paper_title = arxiv.get("title") or video.get("title") or ""
    user = f"""基于下面论文精读笔记，写「可以做什么」发散篇（简体中文，务实具体）。

论文: {paper_title}
视频: {video.get('title')} | {video.get('url')}

精读笔记（可截断）:
{parse_md[:12000]}

输出 Markdown，必须包含：
# 可以做什么
## 可迁移到的场景（≥4）
## 可立刻试的小实验（≥3，含输入/步骤/期望输出）
## 产品 / Agent 灵感
## 跟现有系统怎么接
## 风险与坑
## 跟进清单
不要重复精读正文。
"""
    resp = _client().chat.completions.create(
        model=env("LLM_MODEL", "qwen3.5-397b-a17b"),
        messages=[
            {"role": "system", "content": "你是 AI 产品/研究顾问。输出可执行想法，少空话。"},
            {"role": "user", "content": user},
        ],
        temperature=0.5,
        max_tokens=3072,
    )
    return re_strip_think((resp.choices[0].message.content or "").strip())


def generate_analysis(*, video: dict, paper: dict, fulltext: dict | None = None) -> tuple[str, str]:
    arxiv = paper.get("arxiv") or {}
    extracted = paper.get("extracted") or {}
    paper_title = arxiv.get("title") or video.get("title") or ""
    abstract = arxiv.get("summary") or ""
    authors = ", ".join(arxiv.get("authors") or [])
    links = []
    if arxiv.get("abs_url"):
        links.append(arxiv["abs_url"])
    if arxiv.get("pdf_url"):
        links.append(arxiv["pdf_url"])
    links.extend(extracted.get("urls") or [])

    ft = fulltext or {}
    body = (ft.get("markdown") or "")[:90000]
    body_note = (
        f"全文来源: {ft.get('source')} | chars≈{ft.get('chars')} | path={ft.get('path')}"
        if ft.get("ok")
        else f"全文不可用: {ft.get('error') or 'unknown'} —— 只能依据摘要+视频简介，并在文中明确标注可信度降级。"
    )

    template = _load_template_hints()
    model = env("LLM_MODEL", "qwen3.5-397b-a17b")

    user = f"""请对下面论文做**深度教学式精读**（参考 paper-reading skill）。本轮**只输出解析**，不要写「可以做什么」。

## 来源视频（线索，不是全文）
- UP: {video.get('up_name')}
- 标题: {video.get('title')}
- 链接: {video.get('url')}
- 简介:
{(video.get('description') or '')[:3500]}

## 论文元数据
- 标题: {paper_title}
- 作者: {authors}
- arXiv: {arxiv.get('arxiv_id') or '未知'}
- 链接: {', '.join(links) or '无'}
- 摘要:
{abstract[:5000] or '（无）'}

## 全文材料
{body_note}

### 正文（可能被截断）
{body or '（无全文，仅摘要）'}

## 输出模板约束（务必遵守结构）
{template}

---

请严格按分隔符输出（不要外层代码块）：

<<<PARSE>>>
# 解析（深度精读）

按 skill 骨架写完整笔记，目标 **2500–4000 汉字**（可因材料不足略短，但不得只剩提纲）：

1. Header（标题/作者/venue/链接）
2. TL;DR and contributions（含 named baselines / datasets / 具体数字；没有就写「全文未给出」）
3. What matters, what doesn't（🎯/🔧/📎/⚠️/🔕）
4. Context and prerequisites（**用段落教学**，禁止定义列表敷衍）
5. Method
   - The big picture (layman version)
   - The walkthrough（动机→步骤→符号白话；load-bearing prior work 内联 3–5 句 brief）
6. Challenges in the field — and what this work addresses
7. Experiments and results（具体数字；没有则明确说缺失）
8. Code highlights（有仓库则写，并标注 Reviewed / Inferred / not released）
9. Open questions and limitations
10. 与 B 站讲解的对照（视频强调了什么、可能简化/遗漏了什么）

文末加一行：`可信度: 高/中/低（依据：全文/仅摘要/仅视频）`
<<<END_PARSE>>>
"""

    resp = _client().chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": user},
        ],
        temperature=0.35,
        max_tokens=8192,
    )
    content = re_strip_think((resp.choices[0].message.content or "").strip())
    parse = _between(content, "<<<PARSE>>>", "<<<END_PARSE>>>") or content
    ideas = generate_ideas(video=video, paper=paper, parse_md=parse)
    return parse.strip(), ideas.strip()


def re_strip_think(text: str) -> str:
    import re

    return re.sub(r"<think>[\s\S]*?</think>", "", text, flags=re.I).strip()


def _between(text: str, start: str, end: str) -> str:
    if start not in text or end not in text:
        return ""
    return text.split(start, 1)[1].split(end, 1)[0].strip()
