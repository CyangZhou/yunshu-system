# Regression Tester (回归与验证系统)

## 1. 模块作用
`regression_tester` 是保障云舒系统更新不破坏原有功能的关键。在每次代码变更或逻辑迭代后，自动运行预设的测试用例集，对比当前结果与历史基线，生成可被 AI 快速识别的验证报告。

## 2. 实现原理
采用基于基线（Baseline）对比的自动化测试框架思想。通过执行特定的测试脚本或代码分析工具，捕获标准输出和返回码，并与历史预期结果进行 Diff 比较，从而判定系统是否发生退化（Regression）。

## 3. 实现方法
通过 `scripts/main.py` 以 `--action regression_tester` 参数启动，加载本目录下的 `runner.py`。
内部机制包含：
- 测试套件加载：读取 `tests/` 目录下的用例。
- 隔离执行：在隔离环境中运行测试（或采用模拟输入）。
- 结果断言：对比实际输出与预期基线。
- 报告生成：输出带有 Diff 高亮和失败堆栈的 Markdown 验证报告。

## 4. AI 制作与维护思路 (自解释机制)
- **零依赖性**：测试脚本应尽量减少外部依赖，使用纯 Python 标准库或项目已有组件，降低 AI 重构或配置的难度。
- **报告的 AI 友好度**：错误报告需清晰指出失败的行号、预期值和实际值，以便 AI 可以直接基于报告修正代码。
- **严格模式切换**：提供灵活的参数（如 `strict_mode`），让 AI 在调试初期能忽略非致命警告。

## 5. 指令集
可通过以下 CLI 指令唤起本模块：
```bash
python .trae/skills/yunshu-system-skill/scripts/main.py --action regression_tester --root "." --input '{"test_suite":"all","strict_mode":true}'
```