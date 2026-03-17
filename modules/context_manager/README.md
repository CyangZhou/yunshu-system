# Context Manager (断点恢复与上下文管理)

## 1. 模块作用
`context_manager` 致力于解决长周期任务执行过程中的状态丢失问题。它允许云舒系统在执行中途保存当前进度、环境变量及任务状态，并在需要时重新加载，实现跨 Agent 会话和跨时间段的上下文连续性。

## 2. 实现原理
基于状态快照（State Snapshot）理念。将系统运行时的关键数据（如已完成的任务 ID、当前分析结果、暂存区变量）序列化为 JSON 格式并落盘到本地隐藏目录（如 `.context/`）。在重新启动时，反序列化这些数据以恢复上下文。

## 3. 实现方法
通过全局路由 `scripts/main.py` 的 `--action context_manager` 触发。
核心实现位于 `runner.py`，包括：
- `save_state`：提取当前运行环境关键指标，压缩并写入磁盘。
- `load_state`：读取指定的历史快照，并在内存中重建上下文结构。
- `clear_state`：清理过期或已完成的任务上下文。

## 4. AI 制作与维护思路 (自解释机制)
- **原子化操作**：状态的保存与读取必须是原子级的，防止写了一半导致文件损坏，需加入临时文件替换机制（写 tmp 后 rename）。
- **兼容性设计**：如果数据结构发生版本迭代，应能兼容老版本状态文件的读取，或者提供平滑升级策略，以免导致 AI 在新旧版本切换时崩溃。
- **透明的快照**：保存的状态文件内容必须是高可读的 JSON 或 YAML，让 AI 在无代码干预的情况下也能通过读取文件直接了解断点位置。

## 5. 指令集
可通过以下 CLI 指令唤起本模块：
```bash
# 保存当前上下文状态
python .trae/skills/yunshu-system-skill/scripts/main.py --action context_manager --root "." --input '{"operation":"save","state_id":"session_01","data":{"current_step": 3}}'

# 恢复指定的上下文状态
python .trae/skills/yunshu-system-skill/scripts/main.py --action context_manager --root "." --input '{"operation":"load","state_id":"session_01"}'
```