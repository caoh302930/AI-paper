"""Call OpenAI-compatible LLM to generate 解析 + 可以做什么."""
from __future__ import annotations

from openai import OpenAI

from . import env

SYSTEM = """你是一名 AI 研究员助理。目标：帮助读者快速理解论文并跟上前沿。
用简体中文。务实、具体，少空话。不要编造论文里没有的实验数字。
若信息不足，明确写「信息不足」。"""


def _client() -> OpenAI:
    return OpenAI(base_url=env("LLM_BASE_URL"), api_key=env("LLM_API_KEY") or "EMPTY")


def generate_analysis(*, video: dict, paper: dict) -> tuple[str, str]:
    arxiv = paper.get("arxiv") or {}
    extracted = paper.get("extracted") or {}
    paper_title = arxiv.get("title") or video.get("title") or ""
    abstract = arxiv.get("summary") or ""
    authors = ", ".join(arxiv.get("authors") or [])
    links = []
    if arxiv.get("abs_url"):
        links.append(arxiv["abs_url"])
    links.extend(extracted.get("urls") or [])

    user = f"""根据以下来源，分别产出两段 Markdown（不要包在代码块里）。

## 来源视频
- UP: {video.get('up_name')}
- 标题: {video.get('title')}
- 链接: {video.get('url')}
- 简介:
{video.get('description','')[:4000]}

## 论文信息
- 标题: {paper_title}
- 作者: {authors}
- arXiv: {arxiv.get('arxiv_id') or '未知'}
- 链接: {', '.join(links) or '无'}
- 摘要:
{abstract[:6000] or '（无摘要，请主要依据视频简介谨慎推断，并标注不确定）'}

请严格按下面分隔符输出：

<<<PARSE>>>
# 解析
## 一句话结论
（1-2 句）

## 要解决什么问题
## 核心方法（白话）
## 和现有路线差在哪
## 实验/证据亮点（不确定就写不确定）
## 是否值得深读
- 评级: 高 / 中 / 低
- 理由:
<<<END_PARSE>>>

<<<IDEAS>>>
# 可以做什么
## 可迁移到的场景
（至少 3 条，具体）

## 可立刻试的小实验
（至少 2 条，写清输入输出）

## 产品 / Agent 灵感
## 风险与坑
## 跟进清单
（想继续跟的话下一步读什么 / 盯什么）
<<<END_IDEAS>>>
"""

    model = env("LLM_MODEL", "qwen3.5-397b-a17b")
    resp = _client().chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": user},
        ],
        temperature=0.4,
        max_tokens=4096,
    )
    content = (resp.choices[0].message.content or "").strip()
    parse = _between(content, "<<<PARSE>>>", "<<<END_PARSE>>>") or content
    ideas = _between(content, "<<<IDEAS>>>", "<<<END_IDEAS>>>") or (
        "# 可以做什么\n\n（模型未按格式输出，请人工补全）\n"
    )
    return parse.strip(), ideas.strip()


def _between(text: str, start: str, end: str) -> str:
    if start not in text or end not in text:
        return ""
    return text.split(start, 1)[1].split(end, 1)[0].strip()
