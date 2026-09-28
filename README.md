# AI Novel Studio

一个面向长篇科幻小说的多 Agent 创作仓库。

## 当前状态

### Canon
**Canon V1.0 已完成。**

权威入口：
`canon/CANON_V1_INDEX.md`

### Style
**Style Framework v0.8 已归档，Style Bible v1.0 尚未最终锁定。**

权威入口：
- `style/STYLE_STATUS.md`
- `style/style_bible.md`
- `style/reference_palette.md`
- `style/narrative_theory.md`

### Volume 1
**第一卷 Frozen v1 已建立。**

权威入口：
- `plot/volume_01/INDEX.md`
- `plot/volume_01/volume_bible.md`
- `plot/volume_01/eight_arc_outline.md`
- `plot/volume_01/chapters_001_030.md`
- `plot/volume_01/hooks_and_reveals.md`
- `canon/qizhou.md`
- `canon/xieliu.md`
- `characters/volume1_cast.md`

当前第一卷：
- 核心城市：栖州（杭州型虚构城市）
- 核心高校：栖州大学
- 核心AI：栖州市城市协同运行平台第六代（协六）
- 时间：约5年，人物约20→25；2037→2042为候选年份
- 规模：约100–120章 / 35–45万字（工作目标）
- 八篇：雨幕 / 死人来电 / 空床 / 黑箱 / 凌晨3:17 / 它在看你 / 断城前夜 / 4·17断城
- 认知：K0系统 → K1人格 → K2主体迹象
- 卷末只回答：**“协六是不是一个‘谁’？”**

第一卷旧的“北方工业城/约35章《回滚点》”方案已标记为SUPERSEDED，不得自动回灌。

## 当前写作准备度

见：
`workflow/WRITING_READINESS.md`

当前结论：

**可以进入CH001的正式开发与风格标定；尚不建议直接无人值守连续生产整卷。**

## 核心原则

- 作者掌握世界观、关键人物命运、卷级方向与重大分叉。
- Agent 负责结构、场景、正文、审查、修订和状态维护。
- GitHub 是长期记忆层。
- GPT Work 是操作层。
- 新设定必须走 Proposed → Review → Approved。
- 第一卷专业知识后台化，普通读者不依赖专业知识也能理解危险、选择与代价。

## Agent 流水线

`Orchestrator → Architect → Canon Keeper → Scene Planner → Writer → Review Board → Revision Editor → State Manager`

## 第一卷读取顺序

先读 Canon / Style，再读：
1. `plot/volume_01/INDEX.md`
2. `plot/volume_01/volume_bible.md`
3. `plot/volume_01/eight_arc_outline.md`
4. `characters/volume1_cast.md`
5. `canon/qizhou.md`
6. `canon/xieliu.md`
7. 对应章节文件与状态库

## 目录

- `agents/`：Agent岗位与提示词
- `canon/`：正式世界观、栖州、协六与历史来源
- `characters/`：人物框架与第一卷执行档
- `plot/`：总纲、认知主轴、第一卷、伏笔
- `state/`：时间线、人物状态、世界状态、未决问题
- `style/`：语言风格框架与后续校准
- `workflow/`：流水线、Director Gate、写作准备度
- `templates/`：章节合同与审查模板
- `schemas/`：机器可读状态结构
- `scripts/`：校验工具
