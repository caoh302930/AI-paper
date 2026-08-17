"""Theme taxonomy for DIGEST.md grouping."""
from __future__ import annotations

import re

# order = display order in DIGEST.md
THEME_ORDER = [
    "Agent / 智能体",
    "RAG / 检索增强",
    "LLM 安全",
    "推理 / 思维链",
    "训练 / 对齐 / 蒸馏",
    "自动科研",
    "多模态",
    "评测 / Benchmark",
    "系统 / 工程",
    "其他",
]

_RULES: list[tuple[str, list[str]]] = [
    ("LLM 安全", [r"安全", r"jailbreak", r"越狱", r"攻击", r"steal", r"隐私", r"对齐攻击", r"red.?team"]),
    ("自动科研", [r"自动科研", r"AI4Research", r"科研.?Agent", r"scientific discovery", r"EvoSci", r"PiEvo", r"A2DEPT"]),
    ("RAG / 检索增强", [r"\bRAG\b", r"检索", r"retriev", r"XRAG", r"MA-RAG"]),
    ("推理 / 思维链", [r"思维链", r"\bCoT\b", r"reasoning", r"推理", r"o1", r"test.?time"]),
    ("训练 / 对齐 / 蒸馏", [r"蒸馏", r"distill", r"SFT", r"RLHF", r"对齐", r"微调", r"训练"]),
    ("多模态", [r"多模态", r"multimodal", r"vision", r"VLM", r"图像", r"视频理解"]),
    ("评测 / Benchmark", [r"benchmark", r"评测", r"评估", r"leaderboard"]),
    ("系统 / 工程", [r"系统", r"工程", r"serving", r"infra", r"框架", r"Harness", r"Cordis"]),
    ("Agent / 智能体", [r"\bAgent\b", r"智能体", r"multi.?agent", r"工具调用", r"tool.?use", r"自进化"]),
]


def classify_theme(*texts: str) -> str:
    blob = "\n".join(t for t in texts if t)
    for theme, patterns in _RULES:
        for p in patterns:
            if re.search(p, blob, flags=re.I):
                return theme
    return "其他"


def extract_blurb(parse_md: str, max_len: int = 160) -> str:
    """Pull a one-liner from deep-reading notes."""
    if not parse_md:
        return ""
    # prefer TL;DR section first paragraph
    m = re.search(
        r"##\s*TL;DR[^\n]*\n+(.*?)(?:\n##|\n\*\*Main|\Z)",
        parse_md,
        flags=re.S | re.I,
    )
    text = ""
    if m:
        text = m.group(1).strip()
    if not text:
        for line in parse_md.splitlines():
            line = line.strip()
            if line and not line.startswith("#") and not line.startswith("**Authors"):
                text = line
                break
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"^\*\*.*?\*\*\s*", "", text)
    if len(text) > max_len:
        text = text[: max_len - 1].rstrip() + "…"
    return text
