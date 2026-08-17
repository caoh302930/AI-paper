# AI Paper 主题总览

先扫本文件了解每篇在讲什么，再点进具体目录读 `02_解析.md`。

- 论文数（有 arXiv）: **1**
- 更新时间: `2026-08-17T09:59:07+08:00`

## 目录

- [LLM 安全](#LLM-安全)（1）

## LLM 安全

### Stealing Reasoning Traces from Proprietary LLM APIs

- **一句话:** 这篇论文揭示了一个惊人的安全漏洞：主流大模型厂商（Anthropic, OpenAI, Google）为了保护知识产权，将模型的“思维链”（Chain-of-Thought, CoT）加密后返回给客户端。然而，由于架构设计缺陷，这些加密块在不同会话、不同用户甚至不同模型之间完全通用。攻击者只需将强模型（如 Opus）…
- **arXiv:** [2608.09867](https://arxiv.org/abs/2608.09867)
- **视频:** [BV1VEgj6hEiv](https://www.bilibili.com/video/BV1VEgj6hEiv)
- **发布:** 2026-08-13T00:05:02
- **精读:** [papers/2026/08/2608_09867/02_解析.md](papers/2026/08/2608_09867/02_解析.md) · [可以做什么](papers/2026/08/2608_09867/03_可以做什么.md)
