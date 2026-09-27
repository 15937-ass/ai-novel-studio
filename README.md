# AI Novel Studio

一个面向长篇科幻小说的多 Agent 创作仓库。

## 当前状态

### Canon
**Canon V1.0 已完成。**

权威入口：
`canon/CANON_V1_INDEX.md`

### Style
**Style Framework v0.8 已完成归档，Style Bible v1.0 尚未最终锁定。**

权威入口：
- `style/STYLE_STATUS.md`
- `style/style_bible.md`
- `style/reference_palette.md`
- `style/narrative_theory.md`

当前已经确认：
- 可读性第一；
- 思辨通过冲突、选择和后果完成；
- 近身现实型科幻叙事；
- 主要有限第三人称；
- 单场景意识中心；
- 中长段落、连续流动叙述；
- 反碎段；
- 节奏靠有效状态变化；
- 科学/高概念事件化；
- 生活与制度细节承担世界感。

仍未锁定：
- narrator voice 的温度/幽默/讽刺；
- 心理距离；
- POV正式切换规则；
- 句法与段落样章校准；
- 核心人物语言指纹；
- 抒情/哲思与爱情/暴力/身体书写尺度；
- 正例与反例样章。

当前写作准备度：
`workflow/WRITING_READINESS.md`

结论：**可开始试写，不建议直接进行整卷连续生产。**

## 核心原则

- **作者本人掌握最高叙事权**：世界观最高原则、关键人物命运、卷级方向与重大剧情分叉由 Director 决定。
- **Agent 负责执行**：结构规划、场景拆解、正文、审查、修订与状态更新。
- **GitHub 是长期记忆层**：已确认事实必须入库。
- **GPT Work 是操作层**：读取 Canon/Style/State，执行章节生产，在 Director Gate 暂停。
- **先约束后写作**：Chapter Contract → Scene Plan → Draft。
- **审查后才入 Canon**：新设定必须走 Proposed → Review → Approved。

## Agent 流水线

`Orchestrator → Architect → Canon Keeper → Scene Planner → Writer → Review Board → Revision Editor → State Manager`

## Agent 阅读顺序

1. `canon/CANON_V1_INDEX.md`
2. `canon/world_bible.md`
3. 与任务相关的专题 Canon
4. `plot/knowledge_ladder.md`
5. `plot/three_volume_architecture.md`
6. `characters/cast_framework.md`
7. `style/STYLE_STATUS.md`
8. `style/style_bible.md`
9. 当前 `state/`

旧材料只作为 Source/Legacy，不能覆盖以上文件。

## 目录

- `agents/`：Agent岗位与提示词
- `canon/`：正式世界观与历史来源
- `characters/`：人物框架与档案
- `plot/`：认知主轴、三卷架构、伏笔
- `state/`：时间线、人物状态、世界状态、未决问题
- `style/`：语言风格框架与后续校准
- `templates/`：章节合同、场景计划、审查模板
- `workflow/`：流水线、Director Gate、写作准备度
- `schemas/`：机器可读状态结构
- `scripts/`：校验工具

## Legacy

以下均不得自动回灌：
- 旧《递归黎明》具体剧情与人物；
- 旧AI社群中的固定派系比例；
- 旧递归宇宙终极答案；
- 未经 Canon V1 再确认的旧世界观细节。
