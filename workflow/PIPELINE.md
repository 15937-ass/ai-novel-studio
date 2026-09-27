# Novel Production Pipeline v0.1

## 输入
Director 给出一条阶段级指令。

## Phase 1 — Context Load
Orchestrator 读取：
- Canon
- Master Outline
- 当前世界状态
- 人物状态
- 时间线
- 未解问题
- 伏笔表
- Style Bible
- 最近 2–5 章摘要

## Phase 2 — Batch Contract
Architect 规划 3–5 章。
Canon Keeper 审查。
若出现重大冲突 → Director Gate。

## Phase 3 — Chapter Loop
每章：

1. Architect 生成 Chapter Contract
2. Canon Keeper 预审
3. Scene Planner 生成 Scene Plan
4. Writer 初稿
5. Style Director 检查
6. Review Board 联合审查
7. Anti-AI Reviewer 检查
8. Reality Anchor 给低成本现实增强建议
9. Revision Editor 修改
10. Canon Keeper 终审
11. State Manager 写回状态

默认最多两轮 Revision。

## Phase 4 — Batch Close
生成：
- batch summary
- 人物变化
- 新增/推进/回收伏笔
- 世界状态变化
- 技术新增
- 风险清单
- 是否需要 Director 决策

## Git 规则
建议一个 batch 一个分支：

`batch/001-ch001-ch005`

完成后发 PR 到 `main`。

PR 合并代表该 batch 正式成为 Canon 历史。
