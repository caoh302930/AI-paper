# AI Paper 主题总览

先扫本文件了解每篇在讲什么，再点进具体目录读 `02_解析.md`。

- 论文数（有 arXiv）: **33**
- 更新时间: `2026-08-17T19:17:29+08:00`

## 目录

- [RAG / 检索增强](#RAG--检索增强)（11）
- [LLM 安全](#LLM-安全)（5）
- [推理 / 思维链](#推理--思维链)（10）
- [训练 / 对齐 / 蒸馏](#训练--对齐--蒸馏)（4）
- [自动科研](#自动科研)（1）
- [评测 / Benchmark](#评测--Benchmark)（2）

## RAG / 检索增强

### XRAG: eXamining the Core - Benchmarking Foundational Components in Advanced Retrieval-Augmented Generation

- **一句话:** 这篇论文针对当前 RAG（检索增强生成）领域“各自为战、无法公平对比”的痛点，提出了 **XRAG** 框架。它不仅仅是一个工具库，更是一个**系统性的基准测试平台**，将高级 RAG 拆解为四个核心阶段（预检索、检索、后检索、生成）和五种智能体编排策略，在统一的数据集和 40 个指标下进行了大规模公平测评。核心发现…
- **arXiv:** [2412.15529](https://arxiv.org/abs/2412.15529)
- **视频:** [BV1GbGg67Enx](https://www.bilibili.com/video/BV1GbGg67Enx)
- **发布:** 2026-08-01T17:09:37
- **精读:** [papers/2026/08/2412_15529/02_解析.md](papers/2026/08/2412_15529/02_解析.md) · [可以做什么](papers/2026/08/2412_15529/03_可以做什么.md)

### Agent-as-a-Router: Agentic Model Routing for Coding Tasks

- **一句话:** 这篇论文提出了一种名为 **Agent-as-a-Router** 的新框架，旨在解决多模型环境下的代码任务路由问题。它不再将路由视为一次性的静态分类，而是将其构建为一个持续运行的 **Context-Action-Feedback (C-A-F)** 循环，让路由器在执行过程中不断积累“实战经验”，从而越用越准。
- **arXiv:** [2606.22902](https://arxiv.org/abs/2606.22902)
- **视频:** [BV1gkKa6xEna](https://www.bilibili.com/video/BV1gkKa6xEna)
- **发布:** 2026-07-22T01:07:43
- **精读:** [papers/2026/07/2606_22902/02_解析.md](papers/2026/07/2606_22902/02_解析.md) · [可以做什么](papers/2026/07/2606_22902/03_可以做什么.md)

### SkillRAE: Agent Skill-Based Context Compilation for Retrieval-Augmented Execution

- **一句话:** 这篇论文指出现有检索增强执行（RAE）系统的一个致命盲区：仅仅“检索”到相关技能是不够的，如果直接把技能原文扔给大模型，往往因为上下文冗长、缺乏任务特定的约束指引而导致执行失败。SkillRAE 提出了一种“在线编译”机制，它像一位经验丰富的老手，把检索到的技能、细粒度的子单元证据（如文件约定、约束条件）以及任务目标…
- **arXiv:** [2605.10114](https://arxiv.org/abs/2605.10114)
- **视频:** [BV1M9N86jEan](https://www.bilibili.com/video/BV1M9N86jEan)
- **发布:** 2026-07-14T23:52:15
- **精读:** [papers/2026/07/2605_10114/02_解析.md](papers/2026/07/2605_10114/02_解析.md) · [可以做什么](papers/2026/07/2605_10114/03_可以做什么.md)

### EvolveR: Self-Evolving LLM Agents through an Experience-Driven Lifecycle

- **一句话:** EvolveR 是一个让大语言模型智能体（LLM Agent）实现“自我进化”的框架。它不再让智能体每次任务结束后就“失忆”，而是通过一个闭环生命周期：在线交互收集轨迹 $\rightarrow$ 离线自我蒸馏提炼可复用原则 $\rightarrow$ 利用强化学习（GRPO）更新策略，从而让智能体从自己的成功与失败…
- **arXiv:** [2510.16079](https://arxiv.org/abs/2510.16079)
- **视频:** [BV1coTi6xEM7](https://www.bilibili.com/video/BV1coTi6xEM7)
- **发布:** 2026-07-01T22:14:57
- **精读:** [papers/2026/07/2510_16079/02_解析.md](papers/2026/07/2510_16079/02_解析.md) · [可以做什么](papers/2026/07/2510_16079/03_可以做什么.md)

### Variation in Verification: Understanding Verification Dynamics in Large Language Models

- **一句话:** 这篇论文挑战了"LLM 作为裁判（LLM-as-a-Judge）是免费保险”的直觉，深入剖析了在大模型测试时扩展（Test-Time Scaling, TTS）中，生成式验证器（Generative Verifier）的表现究竟受什么控制。研究发现，验证效果并非单纯由验证器模型的大小决定，而是由**问题难度**、**…
- **arXiv:** [2509.17995](https://arxiv.org/abs/2509.17995)
- **视频:** [BV16rjh6YE2x](https://www.bilibili.com/video/BV16rjh6YE2x)
- **发布:** 2026-06-19T02:27:09
- **精读:** [papers/2026/06/2509_17995/02_解析.md](papers/2026/06/2509_17995/02_解析.md) · [可以做什么](papers/2026/06/2509_17995/03_可以做什么.md)

### SkillGraph: Skill-Augmented Reinforcement Learning for Agents via Evolving Skill Graphs

- **一句话:** 这篇论文提出了一种名为 **SkillGraph** 的框架，旨在解决大语言模型（LLM）智能体在复杂任务中“只会单点检索，不懂组合规划”的痛点。它不再将技能（Skill）视为孤立的条目，而是构建一个**有向依赖图**，让技能之间通过“前置条件”、“增强”、“共现”等关系连接。在训练过程中，这个图与智能体的策略（Po…
- **arXiv:** [2605.12039](https://arxiv.org/abs/2605.12039)
- **视频:** [BV1s1GH6NEKa](https://www.bilibili.com/video/BV1s1GH6NEKa)
- **发布:** 2026-05-24T22:45:22
- **精读:** [papers/2026/05/2605_12039/02_解析.md](papers/2026/05/2605_12039/02_解析.md) · [可以做什么](papers/2026/05/2605_12039/03_可以做什么.md)

### Learning How and What to Memorize: Cognition-Inspired Two-Stage Optimization for Evolving Memory

- **一句话:** 这篇论文提出了一种名为 **MemCoE** 的框架，旨在解决大语言模型（LLM）智能体在长期对话中如何有效管理记忆的问题。核心思想是模仿人类大脑的“前额叶 - 海马体”分工，将记忆管理拆解为两个阶段：先学习“如何组织记忆”（制定全局指南），再学习“具体记什么”（执行更新策略）。通过这种两阶段优化，MemCoE 在…
- **arXiv:** [2605.00702](https://arxiv.org/abs/2605.00702)
- **视频:** [BV1EnLH6AEz5](https://www.bilibili.com/video/BV1EnLH6AEz5)
- **发布:** 2026-05-19T08:00:05
- **精读:** [papers/2026/05/2605_00702/02_解析.md](papers/2026/05/2605_00702/02_解析.md) · [可以做什么](papers/2026/05/2605_00702/03_可以做什么.md)

### RF-Mem: 熟悉度驱动的快慢双路径记忆检索

- **一句话:** 这篇论文提出了一种名为 **RF-Mem** 的个性化大语言模型（LLM）记忆检索框架。它受认知科学中“熟悉度（Familiarity）”与“回忆（Recollection）”双过程理论的启发，不再对所有问题都使用单一的检索策略，而是根据当前查询与记忆的“熟悉程度”动态切换：简单问题走“快路径”（直接 Top-K 检…
- **arXiv:** [2603.09250](https://arxiv.org/abs/2603.09250)
- **视频:** [BV1WuLH66EHg](https://www.bilibili.com/video/BV1WuLH66EHg)
- **发布:** 2026-05-18T08:00:05
- **精读:** [papers/2026/05/2603_09250/02_解析.md](papers/2026/05/2603_09250/02_解析.md) · [可以做什么](papers/2026/05/2603_09250/03_可以做什么.md)

### MemGAS: 从单一粒度到多粒度关联与自适应选择

- **一句话:** 本文提出 MemGAS，一种用于对话智能体的长期记忆框架，其核心突破在于不再依赖单一的对话切片（如仅按会话或仅按轮次），而是构建包含“会话、轮次、摘要、关键词”的**多粒度记忆单元**。通过高斯混合模型（GMM）动态建立不同记忆单元间的关联图，并利用基于熵的路由器（Router）根据查询的不确定性自适应选择最合适的粒…
- **arXiv:** [2505.19549](https://arxiv.org/abs/2505.19549)
- **视频:** [BV1T7LE6BERV](https://www.bilibili.com/video/BV1T7LE6BERV)
- **发布:** 2026-05-17T16:42:45
- **精读:** [papers/2026/05/2505_19549/02_解析.md](papers/2026/05/2505_19549/02_解析.md) · [可以做什么](papers/2026/05/2505_19549/03_可以做什么.md)

### IceBreaker for Conversational Agents: Breaking the First-Message Barrier with Personalized Starters

- **一句话:** 这篇论文解决了一个非常实际但常被忽视的问题：当用户打开一个 AI 对话助手却不知道该说什么时（“冷启动”时刻），系统如何主动给出一个**个性化的开场问题**来打破僵局。作者提出了 **IceBreaker** 框架，通过两步走策略：先像人类破冰一样“唤起共鸣”（从历史会话中提炼用户真正感兴趣的触发点），再“刺激互动”…
- **arXiv:** [2604.18375](https://arxiv.org/abs/2604.18375)
- **视频:** [BV1y75J6YEeX](https://www.bilibili.com/video/BV1y75J6YEeX)
- **发布:** 2026-05-12T08:00:05
- **精读:** [papers/2026/05/2604_18375/02_解析.md](papers/2026/05/2604_18375/02_解析.md) · [可以做什么](papers/2026/05/2604_18375/03_可以做什么.md)

### Recursive Language Models (RLM)

- **一句话:** 这篇论文提出了一种名为**递归语言模型（Recursive Language Models, RLMs）**的新推理范式，旨在突破大语言模型（LLM）上下文窗口的硬性限制。其核心思想是将超长提示词（Prompt）视为“外部环境”中的变量，让模型通过编写代码在 REPL（交互式编程环境）中递归地调用自身，从而处理远超其…
- **arXiv:** [2512.24601](https://arxiv.org/abs/2512.24601)
- **视频:** [BV1TrAezPEvC](https://www.bilibili.com/video/BV1TrAezPEvC)
- **发布:** 2026-03-01T12:00:15
- **精读:** [papers/2026/03/2512_24601/02_解析.md](papers/2026/03/2512_24601/02_解析.md) · [可以做什么](papers/2026/03/2512_24601/03_可以做什么.md)

## LLM 安全

### Stealing Reasoning Traces from Proprietary LLM APIs

- **一句话:** 这篇论文揭示了一个惊人的安全漏洞：主流大模型厂商（Anthropic, OpenAI, Google）为了保护知识产权，将模型的“思维链”（Chain-of-Thought, CoT）加密后返回给客户端。然而，由于架构设计缺陷，这些加密块在不同会话、不同用户甚至不同模型之间完全通用。攻击者只需将强模型（如 Opus）…
- **arXiv:** [2608.09867](https://arxiv.org/abs/2608.09867)
- **视频:** [BV1VEgj6hEiv](https://www.bilibili.com/video/BV1VEgj6hEiv)
- **发布:** 2026-08-13T00:05:02
- **精读:** [papers/2026/08/2608_09867/02_解析.md](papers/2026/08/2608_09867/02_解析.md) · [可以做什么](papers/2026/08/2608_09867/03_可以做什么.md)

### How much do language models memorize?

- **一句话:** 这篇论文提出了一种基于信息论（柯尔莫哥洛夫复杂度）的新方法，将大模型的“记忆”严格拆解为“非意图记忆”（死记硬背训练数据）和“泛化”（学习数据背后的规律）。通过这种拆解，作者首次量化了现代 Transformer 语言模型的**记忆容量上限约为每个参数 3.6 比特**（bits-per-parameter）。
- **arXiv:** [2505.24832](https://arxiv.org/abs/2505.24832)
- **视频:** [BV1s2Mh6DEHr](https://www.bilibili.com/video/BV1s2Mh6DEHr)
- **发布:** 2026-07-07T23:40:52
- **精读:** [papers/2026/07/2505_24832/02_解析.md](papers/2026/07/2505_24832/02_解析.md) · [可以做什么](papers/2026/07/2505_24832/03_可以做什么.md)

### Automatic Prompt Optimization with "Gradient Descent" and Beam Search (ProTeGi)

- **一句话:** 这篇论文提出了一种名为 **ProTeGi** (Prompt Optimization with Textual Gradients) 的框架，旨在解决大语言模型（LLM）提示词（Prompt）编写依赖人工试错的问题。它不修改模型参数，而是通过模拟“梯度下降”的过程，利用 LLM 自身生成自然语言的“梯度”（即对当…
- **arXiv:** [2305.03495](https://arxiv.org/abs/2305.03495)
- **视频:** [BV1sJEZ6nEWn](https://www.bilibili.com/video/BV1sJEZ6nEWn)
- **发布:** 2026-06-10T23:48:51
- **精读:** [papers/2026/06/2305_03495/02_解析.md](papers/2026/06/2305_03495/02_解析.md) · [可以做什么](papers/2026/06/2305_03495/03_可以做什么.md)

### FedTextGrad: 联邦学习中的文本梯度优化

- **一句话:** 这篇论文提出了一种名为 **FedTextGrad** 的新范式，旨在解决黑盒大语言模型（LLM）在联邦学习（FL）场景下无法进行传统数值梯度反向传播的问题。它利用 TextGrad 框架，让客户端通过自然语言反馈（文本梯度）本地优化提示词（Prompt），服务器端则通过基于“均匀信息密度（UID）”原则的摘要技术聚…
- **arXiv:** [2502.19980](https://arxiv.org/abs/2502.19980)
- **视频:** [BV17aE26kEte](https://www.bilibili.com/video/BV17aE26kEte)
- **发布:** 2026-06-10T00:05:51
- **精读:** [papers/2026/06/2502_19980/02_解析.md](papers/2026/06/2502_19980/02_解析.md) · [可以做什么](papers/2026/06/2502_19980/03_可以做什么.md)

### SkillForge: Forging Domain-Specific, Self-Evolving Agent Skills in Cloud Technical Support

- **一句话:** SkillForge 是一个针对企业云技术支持场景的“自我进化”框架，旨在解决大模型智能体（Agent）技能（Skill）难以初始化且无法根据真实反馈持续优化的问题。它通过“领域情境化技能创建器”生成高质量初始技能，并利用“失败归因 - 根因诊断 - 最小修改”的自动化闭环，让技能在真实工单反馈中不断迭代升级。
- **arXiv:** [2604.08618](https://arxiv.org/abs/2604.08618)
- **视频:** [BV1zG5F6NE5g](https://www.bilibili.com/video/BV1zG5F6NE5g)
- **发布:** 2026-06-02T08:00:12
- **精读:** [papers/2026/06/2604_08618/02_解析.md](papers/2026/06/2604_08618/02_解析.md) · [可以做什么](papers/2026/06/2604_08618/03_可以做什么.md)

## 推理 / 思维链

### SAE as a Crystal Ball: Interpretable Features Predict Cross-domain Transferability of LLMs without Training

- **一句话:** 这篇论文提出了一种名为 **STS (SAE-based Transferability Score)** 的新指标，旨在**在不进行实际微调（SFT）的情况下**，预判大语言模型在特定领域微调后，其能力会如何“转移”到其他无关领域（即哪些领域会受益，哪些会受损）。核心洞察是：微调只会改变稀疏自编码器（SAE）中极少…
- **arXiv:** [2603.02908](https://arxiv.org/abs/2603.02908)
- **视频:** [BV1iRKG61EeH](https://www.bilibili.com/video/BV1iRKG61EeH)
- **发布:** 2026-07-16T19:00:17
- **精读:** [papers/2026/07/2603_02908/02_解析.md](papers/2026/07/2603_02908/02_解析.md) · [可以做什么](papers/2026/07/2603_02908/03_可以做什么.md)

### Skill0.5: Joint Skill Internalization and Utilization for Out-of-Distribution Generalization in Agentic Reinforcement Learning

- **一句话:** 这篇论文提出了一种名为 **Skill0.5** 的强化学习框架，旨在解决智能体（Agent）在面对未知任务（OOD）时，如何处理“技能”的难题。核心思想是**差异化对待技能**：将通用的、基础性的推理技能“内化”进模型参数中，而将随任务变化的具体执行技能保留在提示词（Prompt）中动态调用。通过一个“难度感知路由…
- **arXiv:** [2605.28424](https://arxiv.org/abs/2605.28424)
- **视频:** [BV18eNg6tEdm](https://www.bilibili.com/video/BV18eNg6tEdm)
- **发布:** 2026-07-12T16:25:09
- **精读:** [papers/2026/07/2605_28424/02_解析.md](papers/2026/07/2605_28424/02_解析.md) · [可以做什么](papers/2026/07/2605_28424/03_可以做什么.md)

### AJ-Bench: Benchmarking Agent-as-a-Judge for Environment-Aware Evaluation

- **一句话:** 这篇论文提出了 **AJ-Bench**，这是首个专门用于评测“裁判智能体”（Agent-as-a-Judge）的基准测试。它打破了传统裁判仅靠阅读文本进行判断的局限，要求裁判智能体必须**主动进入环境**（如搜索引擎、文件系统、图形界面），调用工具去“取证”，从而验证被评测智能体（Task-Solving Agen…
- **arXiv:** [2604.18240](https://arxiv.org/abs/2604.18240)
- **视频:** [BV1VmTc61EC8](https://www.bilibili.com/video/BV1VmTc61EC8)
- **发布:** 2026-07-01T00:04:16
- **精读:** [papers/2026/07/2604_18240/02_解析.md](papers/2026/07/2604_18240/02_解析.md) · [可以做什么](papers/2026/07/2604_18240/03_可以做什么.md)

### EvoMAS: Evolutionary Generation of Multi-Agent Systems

- **一句话:** EvoMAS 提出了一种全新的范式：不再直接生成可执行代码，而是将多智能体系统（MAS）的构建转化为“结构化配置”的进化搜索问题。它利用遗传算法（选择、变异、交叉）结合执行反馈，自动进化出包含角色定义、模型分配、提示词、工具集和通信拓扑的完整系统配置，从而在推理、代码和工具调用任务上显著超越人工设计和现有自动方法。
- **arXiv:** [2602.06511](https://arxiv.org/abs/2602.06511)
- **视频:** [BV1UcTP6CEzo](https://www.bilibili.com/video/BV1UcTP6CEzo)
- **发布:** 2026-06-28T00:58:39
- **精读:** [papers/2026/06/2602_06511/02_解析.md](papers/2026/06/2602_06511/02_解析.md) · [可以做什么](papers/2026/06/2602_06511/03_可以做什么.md)

### Skill-MAS: Evolving Meta-Skill for Automatic Multi-Agent Systems

- **一句话:** Skill-MAS 提出了一种全新的多智能体系统（MAS）构建范式：将“如何编排多智能体”这一高层能力抽象为一份可自动进化的**元技能（Meta-Skill）**文档。它不修改大模型参数，而是通过“多轨迹执行”收集数据，再经“选择性反思”提炼通用策略，从而让冻结的强模型在推理时也能像人类专家一样积累经验。
- **arXiv:** [2606.18837](https://arxiv.org/abs/2606.18837)
- **视频:** [BV16GjU6jEdP](https://www.bilibili.com/video/BV16GjU6jEdP)
- **发布:** 2026-06-23T23:28:58
- **精读:** [papers/2026/06/2606_18837/02_解析.md](papers/2026/06/2606_18837/02_解析.md) · [可以做什么](papers/2026/06/2606_18837/03_可以做什么.md)

### Harnessing Agentic Evolution (AEvo)

- **一句话:** 这篇论文提出了一种名为 **AEvo** 的框架，旨在解决智能体（Agent）在长程进化过程中容易“迷失方向”或陷入局部最优的问题。核心思想是将“进化过程本身”建模为一个交互式环境，由一个**元智能体（Meta-Agent）**来观察历史轨迹并修改“进化机制”（即如何生成下一个候选者的规则），而不是直接生成候选者。
- **arXiv:** [2605.13821](https://arxiv.org/abs/2605.13821)
- **视频:** [BV17w7y6aEKN](https://www.bilibili.com/video/BV17w7y6aEKN)
- **发布:** 2026-06-06T00:26:37
- **精读:** [papers/2026/06/2605_13821/02_解析.md](papers/2026/06/2605_13821/02_解析.md) · [可以做什么](papers/2026/06/2605_13821/03_可以做什么.md)

### OFA-MAS: One-for-All Multi-Agent System Topology Design based on Mixture-of-Experts Graph Generative Models

- **一句话:** 这篇论文提出了一种名为 **OFA-MAS** 的通用框架，旨在解决多智能体系统（MAS）中“为每个任务单独设计协作拓扑”的低效问题。它通过一个统一的图生成模型，根据自然语言描述的任务，自动为不同领域的任务（如数学推理、代码生成、知识问答）生成最优的 Agent 角色组合与协作图结构。
- **arXiv:** [2601.12996](https://arxiv.org/abs/2601.12996)
- **视频:** [BV1esVN6BENH](https://www.bilibili.com/video/BV1esVN6BENH)
- **发布:** 2026-05-26T22:24:14
- **精读:** [papers/2026/05/2601_12996/02_解析.md](papers/2026/05/2601_12996/02_解析.md) · [可以做什么](papers/2026/05/2601_12996/03_可以做什么.md)

### From Context to Skills: Can Language Models Learn from Context Skillfully? (Ctx2Skill)

- **一句话:** 这篇论文提出了一种名为 **Ctx2Skill** 的框架，旨在解决大语言模型（LLM）在面对复杂、未知的长上下文文档时，难以自动提取并内化关键规则与流程的问题。其核心创新在于设计了一个**零标注、无外部反馈**的“自博弈”（Self-Play）系统，通过挑战者（Challenger）与推理者（Reasoner）的对…
- **arXiv:** [2604.27660](https://arxiv.org/abs/2604.27660)
- **视频:** [BV11vG669EyX](https://www.bilibili.com/video/BV11vG669EyX)
- **发布:** 2026-05-23T22:59:19
- **精读:** [papers/2026/05/2604_27660/02_解析.md](papers/2026/05/2604_27660/02_解析.md) · [可以做什么](papers/2026/05/2604_27660/03_可以做什么.md)

### SkVM: Revisiting Language VM for Skills across Heterogenous LLMs and Harnesses

- **一句话:** SkVM 提出了一种将大模型（LLM）智能体中的"Skill（技能）”从非结构化的提示词（Prompt）转化为可编译、可优化的系统组件的新范式。它通过类似传统编译器的“提前编译（AOT）”和“即时编译（JIT）”机制，解决了技能在不同模型和运行环境间移植性差、执行效率低的问题。实验显示，SkVM 能将任务完成率平均提…
- **arXiv:** [2604.03088](https://arxiv.org/abs/2604.03088)
- **视频:** [BV1qJZcBrE3p](https://www.bilibili.com/video/BV1qJZcBrE3p)
- **发布:** 2026-04-26T17:30:19
- **精读:** [papers/2026/04/2604_03088/02_解析.md](papers/2026/04/2604_03088/02_解析.md) · [可以做什么](papers/2026/04/2604_03088/03_可以做什么.md)

### ADOPT: Adaptive Dependency-Guided Joint Prompt Optimization for Multi-Step LLM Pipelines

- **一句话:** ADOPT 提出了一种自适应依赖导向的联合提示优化框架，旨在解决多步大语言模型（LLM）工作流中“只有最终结果有标签，中间步骤无监督”的难题。它通过模拟微积分中的偏导数计算，将最终任务的错误信号分解为每个步骤的局部优化方向，并利用 Shapley 值动态分配优化资源，从而像训练神经网络一样高效地训练整个工作流的提示词。
- **arXiv:** [2512.24933](https://arxiv.org/abs/2512.24933)
- **视频:** [BV1PX6zBQERH](https://www.bilibili.com/video/BV1PX6zBQERH)
- **发布:** 2026-01-30T23:18:01
- **精读:** [papers/2026/01/2512_24933/02_解析.md](papers/2026/01/2512_24933/02_解析.md) · [可以做什么](papers/2026/01/2512_24933/03_可以做什么.md)

## 训练 / 对齐 / 蒸馏

### TuneAhead: 微调前的“体检报告”

- **一句话:** TuneAhead 提出了一种在完整微调开始前，仅通过静态数据特征和极短（100 步）的探针训练，就能高精度预测大模型微调最终性能的方法。它不仅能给出预测分数，还能通过 SHAP 值诊断失败原因（如数据冗余或优化不稳定），从而帮助研究者避免浪费 GPU 资源。
- **arXiv:** [2606.17660](https://arxiv.org/abs/2606.17660)
- **视频:** [BV1GSTy6AEpq](https://www.bilibili.com/video/BV1GSTy6AEpq)
- **发布:** 2026-07-05T23:48:54
- **精读:** [papers/2026/07/2606_17660/02_解析.md](papers/2026/07/2606_17660/02_解析.md) · [可以做什么](papers/2026/07/2606_17660/03_可以做什么.md)

### Unveiling the Visual Counting Bottleneck in Vision-Language Models

- **一句话:** 这篇论文揭示了一个反直觉的现象：大型视觉语言模型（VLM）在视觉计数任务上的失败，并非因为它们“看不见”物体或“不懂”数量概念，而是因为它们无法将视觉感知到的数量映射到正确的数字符号上。作者通过解构计数过程，提出了“破碎的数量假设”（Fractured Magnitude Hypothesis），指出视觉和文本模态在…
- **arXiv:** [2605.30170](https://arxiv.org/abs/2605.30170)
- **视频:** [BV1DqJA6VE6c](https://www.bilibili.com/video/BV1DqJA6VE6c)
- **发布:** 2026-06-15T20:00:08
- **精读:** [papers/2026/06/2605_30170/02_解析.md](papers/2026/06/2605_30170/02_解析.md) · [可以做什么](papers/2026/06/2605_30170/03_可以做什么.md)

### CoEvolve: Training LLM Agents via Agent-Data Mutual Evolution

- **一句话:** CoEvolve 提出了一种让大语言模型（LLM）智能体与其训练数据分布“共同进化”的强化学习框架。它打破了传统 RL 训练中数据静态不变的局限，通过从智能体的失败轨迹中提取“遗忘”、“边界”和“稀有”三种信号，动态指导新任务的合成与验证，从而形成“训练 - 反馈 - 数据更新”的闭环。
- **arXiv:** [2604.15840](https://arxiv.org/abs/2604.15840)
- **视频:** [BV1paVJ6FEZe](https://www.bilibili.com/video/BV1paVJ6FEZe)
- **发布:** 2026-05-31T16:44:11
- **精读:** [papers/2026/05/2604_15840/02_解析.md](papers/2026/05/2604_15840/02_解析.md) · [可以做什么](papers/2026/05/2604_15840/03_可以做什么.md)

### Agentic Harness Engineering (AHE): 可观测体系驱动的编码智能体自进化

- **一句话:** 这篇论文提出了一种名为 **AHE (Agentic Harness Engineering)** 的闭环系统，旨在解决编码智能体（Coding Agent）的“外围工程”（Harness）难以自动优化的问题。传统上，智能体的提示词、工具、中间件和记忆机制依赖人工经验迭代，而 AHE 通过构建“组件、经验、决策”三大…
- **arXiv:** [2604.25850](https://arxiv.org/abs/2604.25850)
- **视频:** [BV1n9Gd6oEUK](https://www.bilibili.com/video/BV1n9Gd6oEUK)
- **发布:** 2026-05-26T00:31:47
- **精读:** [papers/2026/05/2604_25850/02_解析.md](papers/2026/05/2604_25850/02_解析.md) · [可以做什么](papers/2026/05/2604_25850/03_可以做什么.md)

## 自动科研

### PiEvo: Principle-Evolvable Scientific Discovery via Uncertainty Minimization

- **一句话:** PiEvo 提出了一种让科学智能体“进化”其底层科学原理的框架，而非在固定的先验假设中盲目搜索。它通过识别实验中的“异常证据”（即现有理论无法解释的数据），动态扩充原理空间，从而打破智能体因固守错误先验而陷入的局部最优陷阱。
- **arXiv:** [2602.06448](https://arxiv.org/abs/2602.06448)
- **视频:** [BV1iMGP6qECz](https://www.bilibili.com/video/BV1iMGP6qECz)
- **发布:** 2026-07-31T23:30:29
- **精读:** [papers/2026/07/2602_06448/02_解析.md](papers/2026/07/2602_06448/02_解析.md) · [可以做什么](papers/2026/07/2602_06448/03_可以做什么.md)

## 评测 / Benchmark

### MUSE-Autoskill: Self-Evolving Agents via Skill Creation, Memory, Management, and Evaluation

- **一句话:** 这篇论文提出了一种名为 **MUSE-Autoskill** 的智能体框架，它不再把“技能（Skill）”看作是一次性生成的代码片段，而是将其视为具有完整生命周期的长期资产。该系统能自动创建、记忆、管理、评估和修补技能，让智能体在解决复杂任务时能像人类专家一样积累和复用经验。
- **arXiv:** [2605.27366](https://arxiv.org/abs/2605.27366)
- **视频:** [BV1geVD6FETm](https://www.bilibili.com/video/BV1geVD6FETm)
- **发布:** 2026-06-01T08:00:13
- **精读:** [papers/2026/06/2605_27366/02_解析.md](papers/2026/06/2605_27366/02_解析.md) · [可以做什么](papers/2026/06/2605_27366/03_可以做什么.md)

### Continual Harness: Online Adaptation for Self-Improving Foundation Agents

- **一句话:** 这篇论文提出了一种名为 **Continual Harness** 的框架，旨在解决具身智能体（Embodied Agents）在长程任务中无法像代码智能体那样自动优化其“脚手架”（Harness）的问题。核心突破在于：智能体无需重置环境，就能在单次游戏过程中，通过观察失败轨迹，实时自动重写自己的系统提示词、子智能体…
- **arXiv:** [2605.09998](https://arxiv.org/abs/2605.09998)
- **视频:** [BV1NTG26MEGv](https://www.bilibili.com/video/BV1NTG26MEGv)
- **发布:** 2026-05-27T21:56:58
- **精读:** [papers/2026/05/2605_09998/02_解析.md](papers/2026/05/2605_09998/02_解析.md) · [可以做什么](papers/2026/05/2605_09998/03_可以做什么.md)
