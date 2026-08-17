# AI Paper 主题总览

先扫本文件了解每篇在讲什么，再点进具体目录读 `02_解析.md`。

- 论文数（有 arXiv）: **3**
- 更新时间: `2026-08-17T10:18:49+08:00`

## 目录

- [RAG / 检索增强](#RAG--检索增强)（1）
- [LLM 安全](#LLM-安全)（1）
- [自动科研](#自动科研)（1）

## RAG / 检索增强

### XRAG: eXamining the Core - Benchmarking Foundational Components in Advanced Retrieval-Augmented Generation

- **一句话:** 这篇论文针对当前 RAG（检索增强生成）领域“各自为战、无法公平对比”的痛点，提出了 **XRAG** 框架。它不仅仅是一个工具库，更是一个**系统性的基准测试平台**，将高级 RAG 拆解为四个核心阶段（预检索、检索、后检索、生成）和五种智能体编排策略，在统一的数据集和 40 个指标下进行了大规模公平测评。核心发现…
- **arXiv:** [2412.15529](https://arxiv.org/abs/2412.15529)
- **视频:** [BV1GbGg67Enx](https://www.bilibili.com/video/BV1GbGg67Enx)
- **发布:** 2026-08-01T17:09:37
- **精读:** [papers/2026/08/2412_15529/02_解析.md](papers/2026/08/2412_15529/02_解析.md) · [可以做什么](papers/2026/08/2412_15529/03_可以做什么.md)

## LLM 安全

### Stealing Reasoning Traces from Proprietary LLM APIs

- **一句话:** 这篇论文揭示了一个惊人的安全漏洞：主流大模型厂商（Anthropic, OpenAI, Google）为了保护知识产权，将模型的“思维链”（Chain-of-Thought, CoT）加密后返回给客户端。然而，由于架构设计缺陷，这些加密块在不同会话、不同用户甚至不同模型之间完全通用。攻击者只需将强模型（如 Opus）…
- **arXiv:** [2608.09867](https://arxiv.org/abs/2608.09867)
- **视频:** [BV1VEgj6hEiv](https://www.bilibili.com/video/BV1VEgj6hEiv)
- **发布:** 2026-08-13T00:05:02
- **精读:** [papers/2026/08/2608_09867/02_解析.md](papers/2026/08/2608_09867/02_解析.md) · [可以做什么](papers/2026/08/2608_09867/03_可以做什么.md)

## 自动科研

### PiEvo: Principle-Evolvable Scientific Discovery via Uncertainty Minimization

- **一句话:** PiEvo 提出了一种让科学智能体“进化”其底层科学原理的框架，而非在固定的先验假设中盲目搜索。它通过识别实验中的“异常证据”（即现有理论无法解释的数据），动态扩充原理空间，从而打破智能体因固守错误先验而陷入的局部最优陷阱。
- **arXiv:** [2602.06448](https://arxiv.org/abs/2602.06448)
- **视频:** [BV1iMGP6qECz](https://www.bilibili.com/video/BV1iMGP6qECz)
- **发布:** 2026-07-31T23:30:29
- **精读:** [papers/2026/07/2602_06448/02_解析.md](papers/2026/07/2602_06448/02_解析.md) · [可以做什么](papers/2026/07/2602_06448/03_可以做什么.md)
