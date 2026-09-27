# AI Novel Studio

一个面向长篇科幻小说的多 Agent 创作仓库。

## 核心原则

- **作者本人掌握最高叙事权**：世界观最高原则、关键人物命运、卷级故事方向、重大剧情分叉由作者决定。
- **Agent 负责执行**：结构规划、场景拆解、正文初稿、文风校准、连续性审查、现实锚定、修改与状态更新。
- **GitHub 是长期记忆层**：任何已确认事实都必须写入仓库，而不是只存在于聊天上下文。
- **GPT Work 是操作层**：读取仓库状态，执行一批章节生产，在导演门槛处暂停并请求决策。
- **先约束后写作**：必须先生成 Chapter Contract，再生成 Scene Plan，最后写正文。
- **审查后才入 Canon**：草稿中的新设定只有通过审查并更新 Canon/State 后才成为正式事实。

## v0.1 目标

第一阶段先验证 Agent 职责、5 章 batch、Canon 约束、Style Bible、审查机制和 Director Gate，不追求一次性无人值守写完整部长篇。

## 推荐工作方式

作者输入阶段级方向，例如：

> 接下来五章让主角逐渐发现 AI 神主并非统一人格，而是不同训练语料传统演化出的意识群体。不要立刻解释完整机制，也不要爆发公开战争。

随后执行：

`Orchestrator → Architect → Canon Keeper → Scene Planner → Writer → Review Board → Revision Editor → State Manager`

重大剧情分叉创建 GitHub Issue，等待作者决策；普通问题由 Agent 自行修复。

## 目录

- `agents/`：各 Agent 的岗位说明与提示词
- `canon/`：世界观与不可违背事实
- `characters/`：人物档案
- `plot/`：总纲、卷纲、伏笔
- `state/`：当前世界状态、人物状态、时间线、未决问题
- `style/`：文风 Bible
- `templates/`：章节合同、场景计划、审查报告模板
- `workflow/`：流水线与导演门槛
- `schemas/`：状态 JSON 结构约束
- `scripts/`：基础校验脚本
- `.github/`：导演决策 Issue 与 PR 模板

## 当前材料状态

仓库初始化参考了三份已有材料：
- 《AI社群畅想未来》
- 《递归黎明：人机联邦编年史》旧版大纲
- 《AI与人类思维》

这些内容先进入来源层，不自动升格为当前小说 Canon。新的《三元归一》设定、结构性生成主义与 AI 神主体系应优先进入正式 Canon。
