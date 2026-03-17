import subprocess
import sys
import os
from pathlib import Path

def run(root_dir: str, input_data: dict):
    print("🔍 唤醒 Research Engine (研究与归档引擎) ...")
    
    root_path = Path(root_dir).resolve() if root_dir else Path.cwd().resolve()
    src_path = root_path / "云舒增幅器" / "src"
    cli_path = src_path / "云舒增幅器" / "命令行.py"
    
    if not cli_path.exists():
        print(f"❌ 致命错误: 找不到真实引擎入口 {cli_path}")
        return

    urls = input_data.get("url", [])
    if not urls:
        print("❌ 错误: 必须提供至少一个 'url' 参数")
        return
        
    cmd = [sys.executable, str(cli_path), "research"]
    for u in urls:
        cmd.extend(["--url", u])
        
    env = os.environ.copy()
    env["PYTHONPATH"] = str(src_path)
    
    print(f"😈 执行底层命令: {' '.join(cmd)}")
    result = subprocess.run(cmd, env=env, capture_output=True, text=True, encoding="utf-8")
    
    print(result.stdout)
    if result.returncode != 0:
        print(f"❌ 引擎执行异常 (Exit Code: {result.returncode}):\n{result.stderr}")