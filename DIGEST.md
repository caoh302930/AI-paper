# AI Paper 主题总览

先扫本文件了解每篇在讲什么，再点进具体目录读 `02_解析.md`。

- 论文数（有 arXiv）: **53**
- 更新时间: `2026-09-06T00:19:50+08:00`

## 目录

- [RAG / 检索增强](#RAG--检索增强)（16）
- [LLM 安全](#LLM-安全)（7）
- [推理 / 思维链](#推理--思维链)（20）
- [训练 / 对齐 / 蒸馏](#训练--对齐--蒸馏)（4）
- [自动科研](#自动科研)（3）
- [评测 / Benchmark](#评测--Benchmark)（3）

## RAG / 检索增强

### WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill Evolution

- **一句话:** WikiSkill 提出了一种让 AI 智能体（Agent）像人类写维基百科一样积累经验的框架：它不再让技能进化仅依赖上一轮的“试错”，而是引入一个**持久化的 Wiki 层**，将每次执行中的失败模式、成功策略和历史提案整理成结构化知识，供后续的技能提案者（Skill Proposer）参考。这种方法显著提升了技能…
- **arXiv:** [2608.27454](https://arxiv.org/abs/2608.27454)
- **视频:** [BV1d1tJ6HEAs](https://www.bilibili.com/video/BV1d1tJ6HEAs)
- **发布:** 2026-09-03T08:30:02
- **精读:** [papers/2026/09/2608_27454/02_解析.md](papers/2026/09/2608_27454/02_解析.md) · [可以做什么](papers/2026/09/2608_27454/03_可以做什么.md)

### Just-In-Time Reinforcement Learning (JitRL)

- **一句话:** JitRL 提出了一种**无需梯度更新**的测试时策略优化框架，让冻结权重的 LLM Agent 能通过检索历史经验记忆，实时估计动作优势并直接调整输出概率，实现“边做边学”。该方法在 WebArena 和 Jericho 等复杂任务中，不仅超越了所有免训练基线，还击败了昂贵的微调强化学习方案（如 WebRL），同时…
- **arXiv:** [2601.18510](https://arxiv.org/abs/2601.18510)
- **视频:** [BV1fQ8669EK5](https://www.bilibili.com/video/BV1fQ8669EK5)
- **发布:** 2026-08-22T11:30:06
- **精读:** [papers/2026/08/2601_18510/02_解析.md](papers/2026/08/2601_18510/02_解析.md) · [可以做什么](papers/2026/08/2601_18510/03_可以做什么.md)

### XRAG: eXamining the Core - Benchmarking Foundational Components in Advanced Retrieval-Augmented Generation

- **一句话:** 这篇论文针对当前 RAG（检索增强生成）领域“各自为战、无法公平对比”的痛点，提出了 **XRAG** 框架。它不仅仅是一个工具库，更是一个**系统性的基准测试平台**，将高级 RAG 拆解为四个核心阶段（预检索、检索、后检索、生成）和五种智能体编排策略，在统一的数据集和 40 个指标下进行了大规模公平测评。核心发现…
- **arXiv:** [2412.15529](https://arxiv.org/abs/2412.15529)
- **视频:** [BV1GbGg67Enx](https://www.bilibili.com/video/BV1GbGg67Enx)
- **发布:** 2026-08-01T17:09:37
- **精读:** [papers/2026/08/2412_15529/02_解析.md](papers/2026/08/2412_15529/02_解析.md) · [可以做什么](papers/2026/08/2412_15529/03_可以做什么.md)

### MA-RAG: 从冲突到共识——多轮智能体医疗推理

- **一句话:** 本文提出 MA-RAG（Multi-Round Agentic RAG），一种用于复杂医疗推理的多轮智能体框架。它不再依赖不可靠的“词级置信度”来决定何时检索，而是利用模型内部生成的多个候选答案之间的**语义冲突**作为信号，主动触发检索以填补知识缺口，并通过排序机制优化历史上下文，最终将分歧收敛为高保真的共识。
- **arXiv:** [2603.03292](https://arxiv.org/abs/2603.03292)
- **视频:** [BV1yM3b6SEx8](https://www.bilibili.com/video/BV1yM3b6SEx8)
- **发布:** 2026-07-30T23:27:50
- **精读:** [papers/2026/07/2603_03292/02_解析.md](papers/2026/07/2603_03292/02_解析.md) · [可以做什么](papers/2026/07/2603_03292/03_可以做什么.md)

### MedRGAG: 从检索到生成——统一外部与参数化知识的医学问答框架

- **一句话:** 本文提出 MedRGAG，一种针对医学问答的统一框架，旨在解决传统检索增强生成（RAG）知识覆盖不全和生成增强生成（GAG）容易产生幻觉的两大痛点。该框架通过“知识引导的上下文补全”和“知识感知的文档选择”两个核心模块，动态融合外部检索证据与模型内部参数知识，在五个医学基准测试中平均提升了 12.5%（对比 MedR…
- **arXiv:** [2510.18297](https://arxiv.org/abs/2510.18297)
- **视频:** [BV1QEgx6HEyF](https://www.bilibili.com/video/BV1QEgx6HEyF)
- **发布:** 2026-07-23T23:54:53
- **精读:** [papers/2026/07/2510_18297/02_解析.md](papers/2026/07/2510_18297/02_解析.md) · [可以做什么](papers/2026/07/2510_18297/03_可以做什么.md)

### SE-GA: Memory-Augmented Self-Evolution for GUI Agents

- **一句话:** 这篇论文提出了一种名为 SE-GA 的框架，旨在解决图形用户界面（GUI）智能体在长程多步任务中因上下文窗口限制和策略静态化而导致的失败问题。其核心创新在于将“测试时层级记忆检索”（TTME）与“记忆增强的自进化训练”（MASE）闭环结合，让智能体不仅能“记住”历史经验，还能通过自我复盘将非参数化的经验转化为参数化的…
- **arXiv:** [2605.16883](https://arxiv.org/abs/2605.16883)
- **视频:** [BV1HJKa63EMx](https://www.bilibili.com/video/BV1HJKa63EMx)
- **发布:** 2026-07-22T19:00:16
- **精读:** [papers/2026/07/2605_16883/02_解析.md](papers/2026/07/2605_16883/02_解析.md) · [可以做什么](papers/2026/07/2605_16883/03_可以做什么.md)

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

### TokenPilot: Cache-Efficient Context Management for LLM Agents

- **一句话:** TokenPilot 是一个专为长会话 LLM Agent 设计的上下文管理框架，其核心洞察在于：单纯压缩文本（减少 Token 数量）往往会破坏 Prompt 的前缀连续性，导致后端 KV Cache 失效，反而增加了计算成本。该框架通过“全局稳定前缀”和“局部生命周期感知”双重机制，在大幅减少输入 Token 的…
- **arXiv:** [2606.17016](https://arxiv.org/abs/2606.17016)
- **视频:** [BV19Btf6bEUa](https://www.bilibili.com/video/BV19Btf6bEUa)
- **发布:** 2026-09-04T08:30:02
- **精读:** [papers/2026/09/2606_17016/02_解析.md](papers/2026/09/2606_17016/02_解析.md) · [可以做什么](papers/2026/09/2606_17016/03_可以做什么.md)

### Cheating Automatic LLM Benchmarks: Null Models Achieve High Win Rates

- **一句话:** 这篇论文揭示了一个令人不安的事实：当前主流的自动大语言模型（LLM）评测基准（如 AlpacaEval 2.0, Arena-Hard-Auto, MT-Bench）极其脆弱，甚至可以被一个**没有任何训练参数、对任何指令都只输出固定乱码的“空模型”（Null Model）**彻底攻破。研究者构造了一种结构化的作弊响…
- **arXiv:** [2410.07137](https://arxiv.org/abs/2410.07137)
- **视频:** [BV15Q8w63EkN](https://www.bilibili.com/video/BV15Q8w63EkN)
- **发布:** 2026-08-21T01:05:28
- **精读:** [papers/2026/08/2410_07137/02_解析.md](papers/2026/08/2410_07137/02_解析.md) · [可以做什么](papers/2026/08/2410_07137/03_可以做什么.md)

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

### Popular but Wrong: Understanding and Mitigating LLM Overconfidence through Knowledge Popularity

- **一句话:** 这篇论文揭示了一个反直觉的现象：大语言模型（LLM）在“一本正经胡说八道”时，往往是因为它生成的错误答案比正确答案更“流行”或与问题实体在训练数据中“共现”得更频繁。作者提出利用这种“流行度”信号来校准模型的置信度，显著降低了模型对错误答案的过度自信。
- **arXiv:** [2505.17537](https://arxiv.org/abs/2505.17537)
- **视频:** [BV15xbL6kEt1](https://www.bilibili.com/video/BV15xbL6kEt1)
- **发布:** 2026-09-05T22:03:18
- **精读:** [papers/2026/09/2505_17537/02_解析.md](papers/2026/09/2505_17537/02_解析.md) · [可以做什么](papers/2026/09/2505_17537/03_可以做什么.md)

### SMetric: Rethink LLM Scheduling for Serving Agents with Balanced Session-centric Scheduling

- **一句话:** 这篇论文针对大语言模型（LLM）在"Agent 服务”场景下的调度难题，提出了一种名为 **SMetric** 的新调度策略。核心发现是：Agent 的会话（Session）具有极强的局部性，后续请求几乎总是复用同一实例上的 KV Cache，导致现有“缓存优先”策略造成严重的负载不均。SMetric 通过“首轮负载…
- **arXiv:** [2607.08565](https://arxiv.org/abs/2607.08565)
- **视频:** [BV1qati6NE5t](https://www.bilibili.com/video/BV1qati6NE5t)
- **发布:** 2026-09-04T16:25:32
- **精读:** [papers/2026/09/2607_08565/02_解析.md](papers/2026/09/2607_08565/02_解析.md) · [可以做什么](papers/2026/09/2607_08565/03_可以做什么.md)

### SKILL.state: Scalable Long-Horizon Agent Skills

- **一句话:** 这篇论文提出了一种名为 **SKILL.state** 的运行时架构，旨在解决大语言模型（LLM）智能体在执行长周期任务时，因不断追加历史对话导致上下文爆炸、推理延迟增加以及“上下文中毒”（即旧信息干扰新判断）的问题。它不再依赖不断增长的对话历史，而是维护一个显式的、结构化的**执行状态（Execution Stat…
- **arXiv:** [2608.26263](https://arxiv.org/abs/2608.26263)
- **视频:** [BV1cVtn6AEZ3](https://www.bilibili.com/video/BV1cVtn6AEZ3)
- **发布:** 2026-09-02T14:47:31
- **精读:** [papers/2026/09/2608_26263/02_解析.md](papers/2026/09/2608_26263/02_解析.md) · [可以做什么](papers/2026/09/2608_26263/03_可以做什么.md)

### JIT-Agent: Scaling Harness Intelligence via Just-in-Time Harness Evolution

- **一句话:** 这篇论文提出了一种名为 **JIT-Agent** 的新范式，它不再依赖人工预先设计固定的智能体框架（Harness），而是训练一个专门的“元模型”，在推理时根据具体任务**即时生成**（Just-in-Time）最适合的框架配置。该框架将智能体能力拆解为记忆、规划、动作和能力编排四个模块，通过三阶段训练（定制、修复…
- **arXiv:** [2608.25593](https://arxiv.org/abs/2608.25593)
- **视频:** [BV1hzt36WEgR](https://www.bilibili.com/video/BV1hzt36WEgR)
- **发布:** 2026-09-01T16:48:30
- **精读:** [papers/2026/09/2608_25593/02_解析.md](papers/2026/09/2608_25593/02_解析.md) · [可以做什么](papers/2026/09/2608_25593/03_可以做什么.md)

### CacheRoute: Planned Prefix-Affinity Routing for Large-Scale LLM Serving

- **一句话:** CacheRoute 解决了一个看似矛盾的问题：在大模型推理服务中，为了利用“前缀缓存（Prefix KV Cache）”加速，我们需要把相同业务前缀的请求路由到同一台机器；但为了负载均衡，我们又希望请求分散到所有机器。传统的“随机负载均衡”会打散缓存，而“固定亲和性路由”又会导致热点机器队列拥堵。CacheRout…
- **arXiv:** [2608.19677](https://arxiv.org/abs/2608.19677)
- **视频:** [BV1mi4y66ECi](https://www.bilibili.com/video/BV1mi4y66ECi)
- **发布:** 2026-08-29T16:48:47
- **精读:** [papers/2026/08/2608_19677/02_解析.md](papers/2026/08/2608_19677/02_解析.md) · [可以做什么](papers/2026/08/2608_19677/03_可以做什么.md)

### LLM-as-a-Verifier: A General-Purpose Verification Framework

- **一句话:** 本文提出了一种名为 **LLM-as-a-Verifier** 的通用验证框架，核心思想是将“验证”本身视为一个可扩展的计算维度。不同于传统方法让大模型输出离散的分数（如 1-5 分），该方法直接利用模型对评分 Token 的完整概率分布计算期望值，从而获得连续的细粒度奖励信号。通过扩展评分粒度、重复评估和标准分解三…
- **arXiv:** [2607.05391](https://arxiv.org/abs/2607.05391)
- **视频:** [BV1W2896iEwe](https://www.bilibili.com/video/BV1W2896iEwe)
- **发布:** 2026-08-26T15:17:20
- **精读:** [papers/2026/08/2607_05391/02_解析.md](papers/2026/08/2607_05391/02_解析.md) · [可以做什么](papers/2026/08/2607_05391/03_可以做什么.md)

### EPC-AW：多智能体动作都对，为何仍会失败？计划出了问题

- **一句话:** 这篇论文指出，多智能体系统（Multi-Agent Systems）常出现一种隐蔽的失败：所有工具调用和动作执行都完美无误，但最终任务依然失败。原因在于规划者（Planner）在信息不全时**高估了自己的认知**，制定了一个看似可行、实则无法获取关键证据的计划。作者提出了 **EPC-AW**（Epistemic P…
- **arXiv:** [2605.23414](https://arxiv.org/abs/2605.23414)
- **视频:** [BV1nf8265EZ8](https://www.bilibili.com/video/BV1nf8265EZ8)
- **发布:** 2026-08-22T21:52:07
- **精读:** [papers/2026/08/2605_23414/02_解析.md](papers/2026/08/2605_23414/02_解析.md) · [可以做什么](papers/2026/08/2605_23414/03_可以做什么.md)

### RE-TRAC: REcursive TRAjectory Compression for Deep Search Agents

- **一句话:** 这篇论文提出了一种名为 **RE-TRAC**（递归轨迹压缩）的新框架，旨在解决大语言模型（LLM）智能体在深度搜索任务中因上下文过长而导致的“遗忘”和“探索不足”问题。它不再让智能体每次尝试都从头开始，而是在每轮搜索结束后，将漫长的对话历史压缩成一份**结构化状态笔记**（包含已验证事实、未解疑点、失败尝试），并以…
- **arXiv:** [2602.02486](https://arxiv.org/abs/2602.02486)
- **视频:** [BV1QBgi6EEeV](https://www.bilibili.com/video/BV1QBgi6EEeV)
- **发布:** 2026-07-25T00:40:33
- **精读:** [papers/2026/07/2602_02486/02_解析.md](papers/2026/07/2602_02486/02_解析.md) · [可以做什么](papers/2026/07/2602_02486/03_可以做什么.md)

### Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity

- **一句话:** 这篇论文指出，大语言模型（LLM）在经历人类反馈强化学习（RLHF）对齐后，输出变得“无聊”且单一（模式坍塌），其根本原因并非算法缺陷，而是人类标注数据中普遍存在的**典型性偏差（Typicality Bias）**——即人类倾向于认为“熟悉、流畅、可预测”的回答更好。为此，作者提出了一种无需训练的提示策略**Ver…
- **arXiv:** [2510.01171](https://arxiv.org/abs/2510.01171)
- **视频:** [BV1adNo6fEcE](https://www.bilibili.com/video/BV1adNo6fEcE)
- **发布:** 2026-07-18T00:48:55
- **精读:** [papers/2026/07/2510_01171/02_解析.md](papers/2026/07/2510_01171/02_解析.md) · [可以做什么](papers/2026/07/2510_01171/03_可以做什么.md)

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

### Choices Speak Louder than Questions

- **一句话:** 这篇论文揭示了一个反直觉的现象：大语言模型（LLM）在做选择题时，往往不是靠“读懂题目”，而是靠“猜选项”。模型可能仅仅因为某个选项的文本特征（如长度、特定词汇、句式）就选它，哪怕题目完全没看。为了解决这个问题，作者提出了**Choice Sensitivity（选项敏感度）**这一量化指标，并设计了一种新的评分方法…
- **arXiv:** [2502.18798](https://arxiv.org/abs/2502.18798)
- **视频:** [BV18vNH64EXu](https://www.bilibili.com/video/BV18vNH64EXu)
- **发布:** 2026-07-11T00:23:51
- **精读:** [papers/2026/07/2502_18798/02_解析.md](papers/2026/07/2502_18798/02_解析.md) · [可以做什么](papers/2026/07/2502_18798/03_可以做什么.md)

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

### ASI-Bench: At the Dawn of Artificial Superintelligence

- **一句话:** 这篇论文提出了 **ASI-Bench**，这是首个专门用于评估 AI 系统“科学自主性”的基准。它不再仅仅测试 AI 能否回答已知问题或执行给定步骤，而是通过在一个科研项目中逐步撤去人类的方法论指导（从完整步骤到仅给目标），来测量 AI 能否独立选择方法、构建流程并产出可验证的科研结果。
- **arXiv:** [2608.17271](https://arxiv.org/abs/2608.17271)
- **视频:** [BV1Wa8o6kEVN](https://www.bilibili.com/video/BV1Wa8o6kEVN)
- **发布:** 2026-08-27T08:30:03
- **精读:** [papers/2026/08/2608_17271/02_解析.md](papers/2026/08/2608_17271/02_解析.md) · [可以做什么](papers/2026/08/2608_17271/03_可以做什么.md)

### PiEvo: Principle-Evolvable Scientific Discovery via Uncertainty Minimization

- **一句话:** PiEvo 提出了一种让科学智能体“进化”其底层科学原理的框架，而非在固定的先验假设中盲目搜索。它通过识别实验中的“异常证据”（即现有理论无法解释的数据），动态扩充原理空间，从而打破智能体因固守错误先验而陷入的局部最优陷阱。
- **arXiv:** [2602.06448](https://arxiv.org/abs/2602.06448)
- **视频:** [BV1iMGP6qECz](https://www.bilibili.com/video/BV1iMGP6qECz)
- **发布:** 2026-07-31T23:30:29
- **精读:** [papers/2026/07/2602_06448/02_解析.md](papers/2026/07/2602_06448/02_解析.md) · [可以做什么](papers/2026/07/2602_06448/03_可以做什么.md)

### SciNet: Evaluating AI Agents in Relation-Aware Scientific Literature Retrieval

- **一句话:** 这篇论文提出了 **SciNet**，这是首个专门用于评估科研文献检索中“关系感知能力”的大规模数据集。它指出当前的科研 Agent（如 Deep Research）虽然能基于关键词或向量相似度找到“相关”论文，却完全不懂论文之间复杂的逻辑关系（如谁颠覆了谁、谁支持了谁、技术演化的路径是什么）。通过构建包含 2.69…
- **arXiv:** [2601.03260](https://arxiv.org/abs/2601.03260)
- **视频:** [BV14pK663EKJ](https://www.bilibili.com/video/BV14pK663EKJ)
- **发布:** 2026-07-19T19:00:21
- **精读:** [papers/2026/07/2601_03260/02_解析.md](papers/2026/07/2601_03260/02_解析.md) · [可以做什么](papers/2026/07/2601_03260/03_可以做什么.md)

## 评测 / Benchmark

### Huxley–Gödel Machine: Human-Level Coding Agent Development by an Approximation of the Optimal Self-Improving Machine

- **一句话:** 这篇论文提出了一种名为 Huxley–Gödel Machine (HGM) 的自进化编码智能体框架，旨在解决现有方法仅凭当前测试分数（Benchmark Score）来指导自我修改所导致的“元生产力 - 性能错配”问题。HGM 引入了一种基于“支系（Clade）”的长期潜力指标（CMP），通过聚合后代的表现来评估当…
- **arXiv:** [2510.21614](https://arxiv.org/abs/2510.21614)
- **视频:** [BV1nitH6KEQh](https://www.bilibili.com/video/BV1nitH6KEQh)
- **发布:** 2026-08-30T20:04:27
- **精读:** [papers/2026/08/2510_21614/02_解析.md](papers/2026/08/2510_21614/02_解析.md) · [可以做什么](papers/2026/08/2510_21614/03_可以做什么.md)

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
