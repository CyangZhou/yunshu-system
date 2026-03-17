# 云舒系统 (Yunshu System)

> **基于纯脚本与AI可读文档的工程自动化增幅流水线**

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-green.svg)](https://www.python.org/)

---

## 🌟 核心定位

云舒系统是一套**"纯脚本 + AI可读文档"**驱动的工程自动化增幅流水线，核心目标是：

1. **统一的系统增幅执行** - 依托核心放大器 (`amplifier_core`) 提供标准的业务调度与生成流
2. **深度研究与归档** - 依托研究引擎 (`research_engine`) 实现智能检索、资料清洗及结构化知识沉淀
3. **闭环的回归与验证** - 依托回归测试系统 (`regression_tester`) 保证每一次迭代不破坏既有功能
4. **稳定的上下文管理** - 依托断点恢复与上下文管理 (`context_manager`) 确保长周期任务的前后一致性与中断可恢复性
5. **AI 友好型维护** - 通过高自解释性文档与标准化脚本接口，让 AI 能够"读懂并自维护"此系统

---

## ⚡ 核心哲学：Pure Script + AI-Readable Docs

在这个架构里，我们追求 **Zero-Friction（零摩擦）** 的认知流。

### 纯脚本主义 (Pure Script)
代码必须是**"哑巴"**。它不应该包含复杂的 Prompt 逻辑，也不应该试图去"理解"用户。
- 脚本只接收 JSON 参数，执行原子操作，返回结构化数据

### AI 可读文档 (AI-Readable Docs)
这是技能的**大脑**。我们将业务逻辑、决策树、错误处理机制全部写在 Markdown 文档里。
- AI 读取文档 → 理解当前上下文 → 决定调用哪个脚本 → 分析脚本输出 → 修正行为

> 💡 **Insight**: 代码变更是昂贵的（需要测试、部署），但文档变更是廉价的（实时生效）。让 AI 阅读文档来调整行为，就是最极致的**热更新**。

---

## 🏗️ 系统架构

```text
yunshu-system/
├── 📄 SKILL.md                    # [灵魂] 技能说明书、Prompt 注入源
├── 📄 README.md                   # [皮囊] 给人类看的简要介绍
├── 📂 guides/                     # [知识库] 构建指南与维护手册
│   ├── 云舒系统技能构建指南.md
│   └── 真实模块维护手册.md
├── 📂 modules/                    # [器官] 核心功能模块
│   ├── amplifier_core/            # 云舒增幅器主流程
│   ├── research_engine/           # 研究与归档引擎
│   ├── regression_tester/         # 回归与验证系统
│   └── context_manager/           # 断点恢复与上下文管理
├── 📂 schemas/                    # [神经] JSON Schema 定义
│   └── actions_contracts.json
└── 📄 requirements.txt            # 依赖清单
```

---

## 🚀 快速开始

### 安装依赖

```bash
pip install -r requirements.txt
```

### 命令入口

统一入口：通过各模块的 `runner.py` 执行

#### 1) 云舒增幅器主流程 (amplifier_core)

```bash
python modules/amplifier_core/runner.py --goal "你的任务目标"
```

#### 2) 研究与归档引擎 (research_engine)

```bash
python modules/research_engine/runner.py --url "https://example.com"
```

#### 3) 回归与验证系统 (regression_tester)

```bash
python modules/regression_tester/runner.py --cases all
```

#### 4) 断点恢复与上下文管理 (context_manager)

```bash
python modules/context_manager/runner.py --sub-action list-context
```

---

## 🧠 自主学习协议 (Autonomous Learning Protocol)

这是云舒系统最性感的部分。当 `amplifier_core` 返回"未找到直连技能"或"no_command_requested"时，**严禁**直接返回询问用户。系统会自动执行以下闭环：

1. **Search & Learn** - 立即调用 `research_engine` 搜索该任务的实现方案
2. **Try & Fix** - 根据研究结果构造命令并尝试，失败则读取错误日志修正
3. **Crystallize** - 任务成功后，将验证通过的流程整理成新的 Skill

这就是**自进化**。

---

## 📦 模块详解

### Amplifier Core (云舒增幅器主流程)
核心中枢，负责接收上层任务请求，调度并统筹代码生成、文档编写等增幅工作流。

### Research Engine (研究与归档引擎)
负责知识获取与沉淀，自动收集背景资料、分析现有代码结构，并生成结构化的知识归档文档。

### Regression Tester (回归与验证系统)
保障系统更新不破坏原有功能，自动运行预设的测试用例集，对比当前结果与历史基线。

### Context Manager (断点恢复与上下文管理)
解决长周期任务执行过程中的状态丢失问题，允许保存当前进度并在需要时重新加载。

---

## 🛡️ 最佳实践

### 1. JSON 参数是唯一真理
永远不要让 AI 生成非结构化的文本作为参数。
- ❌ `run.py --target "那个红色的文件"`
- ✅ `run.py --args '{"target_file": "red.txt", "mode": "overwrite"}'`

### 2. 关注点分离
- **脚本**只管：文件 I/O、API 调用、数学计算
- **文档**只管：意图识别、参数提取、结果摘要、情感安抚

### 3. AI 维护手册
在 `guides/` 目录下放维护手册，告诉 AI 常见故障的修复代码片段。当脚本崩了，AI 可以**自己读取手册，自己写代码修复脚本**。

---

## 📄 License

MIT License

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

---

**LCS Protocol: STANDBY.** 😈