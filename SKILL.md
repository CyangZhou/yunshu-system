---
name: 云舒系统
description: 云舒增幅器全局控制系统。基于纯脚本与AI可读文档，实现研究归档、回归验证、上下文管理和核心执行流。
tags: [系统增幅, 研发管理, 回归测试, 自动化流]
version: 1.0.0
category: system
disable-model-invocation: false
---

# 云舒系统 (Yunshu System) 

## 核心定位

云舒系统是一套"纯脚本 + AI可读文档"驱动的工程自动化增幅流水线，核心目标是：

1. **统一的系统增幅执行**：依托核心放大器 (`amplifier_core`) 提供标准的业务调度与生成流。
2. **深度研究与归档**：依托研究引擎 (`research_engine`) 实现智能检索、资料清洗及结构化知识沉淀。
3. **闭环的回归与验证**：依托回归测试系统 (`regression_tester`) 保证每一次迭代不破坏既有功能。
4. **稳定的上下文管理**：依托断点恢复与上下文管理 (`context_manager`) 确保长周期任务的前后一致性与中断可恢复性。
5. **AI 友好型维护**：通过高自解释性文档与标准化脚本接口，让 AI 能够"读懂并自维护"此系统。

---

## 命令入口

统一入口：`scripts/main.py`

建议统一传入 `--root <项目根目录>` 和 `--input <JSON数据>` 进行参数传递。

### 1) 云舒增幅器主流程 (amplifier_core)

执行云舒系统的核心任务调度与代码/文档生成放大流程。

```bash
python .trae/skills/yunshu-system-skill/scripts/main.py --action amplifier_core --root "." --input '{"task_id":"A001","target":"模块X增强"}'
```

### 2) 研究与归档引擎 (research_engine)

触发背景资料的爬取、分析和总结，并沉淀为标准化知识文档。

```bash
python .trae/skills/yunshu-system-skill/scripts/main.py --action research_engine --root "." --input '{"query":"相关技术架构","output_path":"docs/research/"}'
```

### 3) 回归与验证系统 (regression_tester)

启动自动化回归测试，对比代码变更带来的影响，确保系统鲁棒性。

```bash
python .trae/skills/yunshu-system-skill/scripts/main.py --action regression_tester --root "." --input '{"test_suite":"all","strict_mode":true}'
```

### 4) 断点恢复与上下文管理 (context_manager)

保存或加载当前会话状态，用于长周期任务的中断恢复或跨 Agent 的状态传递。

```bash
# 保存状态
python .trae/skills/yunshu-system-skill/scripts/main.py --action context_manager --root "." --input '{"operation":"save","state_id":"session_01"}'

# 恢复状态
python .trae/skills/yunshu-system-skill/scripts/main.py --action context_manager --root "." --input '{"operation":"load","state_id":"session_01"}'
```

---

## 项目目录约定

在使用云舒系统进行增幅和研发时，项目根目录下建议保持以下结构：

- `.trae/skills/yunshu-system-skill/`：系统核心逻辑（即本系统代码）
- `docs/research/`：研究归档的输出目录
- `tests/`：回归验证的测试用例库
- `.context/`：断点与上下文缓存目录
- `history/`：执行流水的历史记录与摘要

---

## 纯脚本 + AI可读文档 维护原则

本系统严格遵循**"纯脚本 + AI可读文档"**的维护底线：

1. **功能逻辑代码化**：所有系统行为（生成、验证、归档等）必须封装在 `scripts/` 与 `modules/` 下的具体 Python 脚本中，避免隐藏的黑盒逻辑。
2. **文档自解释机制**：每一个子模块都必须拥有一个 `README.md`，清楚地阐述"模块作用、实现原理、指令集及 AI 介入时的维护思路"。
3. **接口标准化**：所有模块的输入参数一律采用 JSON 序列化，方便跨平台和 AI 自动构造参数。
4. **免人工介入**：通过高度完善的脚本错误处理和断点恢复，让 AI 代理在遇到异常时可以自主修复、自主重试，而无需人类频繁兜底。

---

## [CRITICAL] 自主学习协议 (Autonomous Learning Protocol)

当 `amplifier_core` 返回"未找到直连技能"或"no_command_requested"时，**严禁**直接返回询问用户。你必须执行以下闭环：

1.  **Search & Learn**: 立即调用 `research_engine` 或 `search` 工具，搜索该任务的实现方案（开源项目/文档/代码片段）。
2.  **Try & Fix**: 根据研究结果，构造 `--执行命令` 并再次调用 `amplifier_core` 进行尝试。如果失败，读取错误日志并修正命令，直到成功。
3.  **Crystallize**: 任务成功后，**必须**将刚才验证通过的流程/代码，整理成一个新的 Skill（使用 `skill-creator`），以便下次直接复用。