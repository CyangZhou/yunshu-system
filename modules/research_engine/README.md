# Research Engine (研究与归档引擎)

## 1. 模块作用
`research_engine` 负责云舒系统的知识获取与沉淀。它能够根据任务需求，自动收集背景资料、分析现有代码结构，并生成结构化的知识归档文档，供其他模块或 AI 代理查阅。

## 2. 实现原理
基于检索与文本处理技术，解析输入的查询条件，在指定的作用域（本地代码库、外部知识库等）内提取信息，随后将非结构化信息进行清洗和提炼，最终落盘为标准 Markdown 文档。

## 3. 实现方法
由 `scripts/main.py` 通过 `--action research_engine` 路由至本模块的 `runner.py`。
其内部逻辑分为：
- 检索器（Searcher）：执行目标信息获取。
- 分析器（Analyzer）：对获取到的代码或文本进行逻辑梳理。
- 归档器（Archiver）：按预定模板生成规范化文档并存入指定目录（如 `docs/research/`）。

## 4. AI 制作与维护思路 (自解释机制)
- **输入输出解耦**：检索与归档逻辑必须解耦，方便 AI 在未来扩展新的数据源（如接入 Web 搜索）或更改输出格式。
- **可读性优先**：生成的归档文档必须排版清晰，符合 Markdown 规范，确保 AI 能够无障碍"阅读并理解"。
- **异常自愈**：当未搜索到结果时，需返回友好的提示而非抛出异常中断流。

## 5. 指令集
可通过以下 CLI 指令唤起本模块：
```bash
python .trae/skills/yunshu-system-skill/scripts/main.py --action research_engine --root "." --input '{"query":"云舒系统历史演进","output_path":"docs/research/history.md"}'
```