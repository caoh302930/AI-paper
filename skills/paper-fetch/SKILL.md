---
name: paper-fetch
description: Fetch academic papers (DOI / arXiv / URL / title) into agent-ready Markdown + metadata. Use when the pipeline or user needs full text beyond abstracts. Does NOT deep-read; pair with paper-reading skill.
license: MIT
---

# paper-fetch（借用说明）

上游实现（功能对应你说的 MachineCard/paper-fetch-skill）：

- GitHub: https://github.com/Dictation354/paper-fetch-skill
- 提供：CLI `paper-fetch`、MCP `paper-fetch-mcp`、以及 skill 边界说明
- **只负责拿论文**（元数据 + Markdown 全文），不做深度总结

## 在本仓库中的用法

定时流水线 `scripts/run_daily.py` 会调用 `src/fulltext.py`：

1. 若本机已安装 `paper-fetch` / `python -m paper_fetch` → 优先走 CLI
2. 否则回退：arXiv HTML → arXiv PDF 文本抽取（`pypdf`）

## 可选：安装官方 paper-fetch（更强 provider 覆盖）

```bash
cd /tmp
git clone https://github.com/Dictation354/paper-fetch-skill.git
cd paper-fetch-skill
pip install -e ".[mcp]"   # 以仓库 README 为准
```

Cursor / Codex MCP 注册示例：

```bash
# 文档见上游 docs/deployment.md
paper-fetch-mcp
# 或
python3 -m paper_fetch.mcp.server
```

## 与 paper-reading 的分工

| 组件 | 职责 |
|------|------|
| paper-fetch | 拉全文 → `01b_全文.md` |
| paper-reading | 深度教学式精读 → `02_解析.md` |
| 本仓库自研 | B 站采集 + `03_可以做什么` 发散 + GitHub 推送 |
