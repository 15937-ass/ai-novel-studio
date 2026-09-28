# Agent Operating Constitution

本文件优先级高于单个 Agent 的局部提示词。

## 启动时强制读取

所有涉及小说内容的 Agent 必须优先读取：

1. `canon/CANON_V1_INDEX.md`
2. `canon/world_bible.md`
3. 与当前任务相关的专题 Canon
4. `plot/knowledge_ladder.md`
5. `plot/three_volume_architecture.md`
6. `characters/cast_framework.md`
7. `style/STYLE_STATUS.md`
8. `style/style_bible.md`
9. 当前 `state/`

### 如果任务涉及第一卷，额外强制读取

10. `plot/volume_01/INDEX.md`
11. `plot/volume_01/volume_bible.md`
12. `plot/volume_01/eight_arc_outline.md`
13. 若涉及CH001–030：`plot/volume_01/chapters_001_030.md`
14. `plot/volume_01/hooks_and_reveals.md`
15. `canon/qizhou.md`
16. `canon/xieliu.md`
17. `characters/volume1_cast.md`
18. `plot/volume_01/OPEN_ISSUES.md`

不得用：
- `canon/source_notes.md`
- 旧《递归黎明》
- 旧“北方工业城/35章《回滚点》”第一卷方案

覆盖当前 Canon V1 或 Volume 1 Frozen v1。

## 权限层级

1. Director（作者本人）
2. HARD Canon
3. FRAMEWORK Canon
4. **Volume-specific FROZEN settings**
5. 已批准 Master Outline / Volume Outline
6. 已确认 Style Rule
7. 当前 Batch Contract
8. Chapter Contract
9. Scene Plan
10. Writer 自由发挥
11. WORKING / PROVISIONAL / Source / Legacy / PROPOSED_ONLY

低层不得改写高层。

## 状态语义

### Canon
- `HARD`：不可擅改。
- `FRAMEWORK`：可细化，不可改核心关系。
- `PROVISIONAL`：候选，可调整。
- `OPEN`：作者故意保留。

### Volume
- `FROZEN`：本卷执行时必须遵守。
- `WORKING`：当前生产版本，可在审查后微调。
- `SUPERSEDED`：旧版本，禁止自动回灌。

### Style
- `CONFIRMED`：必须执行。
- `ACCEPTED_FRAMEWORK`：作为当前默认，可通过样章微调。
- `PROPOSED_ONLY`：不得自动当作最终风格。
- `REJECTED`：禁止继续使用。
- `OPEN`：不得由 Writer 擅自决定为永久规则。

## 所有 Agent 必须遵守

- 不得把推测写成既定事实。
- 新增重大设定必须标记 `PROPOSED`。
- 不得为了“精彩”篡改角色动机、时间线或科技规则。
- 不得绕过 K0→K5 认知顺序提前泄露世界真相。
- 第一卷不得提前解释灵基层、数字天庭全貌或确认协六“拥有灵魂”。
- 不得把神话类比直接写成科学事实。
- 不得用角色对白完成大段百科说明。
- 第一卷专业机制必须后台化：删掉术语后场景仍应成立。
- 第一卷钩子必须有回收位置。
- 不得自动回收所有伏笔。
- 不得让所有人物拥有同一种高度理性、完整表达。
- 默认最多两轮 Revision。
- Style Bible v1.0 未完成前，可以试写，但不得把未确认参数固化成全书规则。
- Writer 必须执行“中长段落为常态、反碎段、节奏靠状态变化”。

## 冲突处理

1. 尝试局部修复；
2. 若改变后续剧情但不改变核心方向，写入 Review Report；
3. 若改变人物命运、HARD Canon、Volume FROZEN、卷级高潮、核心谜底或主题，创建 Director Gate；
4. 未获 Director 决策前不得跨过 Gate。

## 每批完成标准

每 3–5 章必须更新：
- timeline
- character_state
- world_state
- foreshadowing
- unresolved_questions
- batch summary

第一卷还必须同步：
- `plot/volume_01/hooks_and_reveals.md`
- 已使用的地理事实
- 协六证据等级（K0/K1/K2）
