import subprocess
import sys
import os
from pathlib import Path

def run(root_dir: str, input_data: dict):
    print("💾 唤醒 Context Manager (断点恢复与上下文管理) ...")
    
    root_path = Path(root_dir).resolve() if root_dir else Path.cwd().resolve()
    src_path = root_path / "云舒增幅器" / "src"
    cli_path = src_path / "云舒增幅器" / "命令行.py"
    
    if not cli_path.exists():
        print(f"❌ 致命错误: 找不到真实引擎入口 {cli_path}")
        return

    sub_action = input_data.get("sub_action", "list-context")
    cmd = [sys.executable, str(cli_path), sub_action]
    
    if sub_action == "list-context":
        if "session_id" in input_data:
            cmd.extend(["--session-id", input_data["session_id"]])
        if "limit" in input_data:
            cmd.extend(["--limit", str(input_data["limit"])])
    elif sub_action == "resume":
        if "checkpoint" in input_data:
            cmd.extend(["--checkpoint", input_data["checkpoint"]])
        if "session_id" in input_data:
            cmd.extend(["--session-id", input_data["session_id"]])
        if "context_checkpoint_id" in input_data:
            cmd.extend(["--context-checkpoint-id", input_data["context_checkpoint_id"]])
    elif sub_action == "read-artifact":
        for key in ["path", "checkpoint_id", "session_id", "max_chars"]:
            if key in input_data:
                cmd.extend([f"--{key.replace('_', '-')}", str(input_data[key])])
        for flag in ["latest_phase0_report", "latest_context", "include_full", "context_bundle"]:
            if input_data.get(flag):
                cmd.append(f"--{flag.replace('_', '-')}")
    else:
        print(f"❌ 未知的上下文子动作: {sub_action}")
        return
        
    env = os.environ.copy()
    env["PYTHONPATH"] = str(src_path)
    
    print(f"😈 执行底层命令: {' '.join(cmd)}")
    result = subprocess.run(cmd, env=env, capture_output=True, text=True, encoding="utf-8")
    
    print(result.stdout)
    if result.returncode != 0:
        print(f"❌ 引擎执行异常 (Exit Code: {result.returncode}):\n{result.stderr}")