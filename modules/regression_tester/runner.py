import subprocess
import sys
import os
from pathlib import Path

def run(root_dir: str, input_data: dict):
    print("✅ 唤醒 Regression Tester (回归与验证系统) ...")
    
    root_path = Path(root_dir).resolve() if root_dir else Path.cwd().resolve()
    src_path = root_path / "云舒增幅器" / "src"
    cli_path = src_path / "云舒增幅器" / "命令行.py"
    
    if not cli_path.exists():
        print(f"❌ 致命错误: 找不到真实引擎入口 {cli_path}")
        return

    sub_action = input_data.get("sub_action", "regress")
    cmd = [sys.executable, str(cli_path), sub_action]
    
    if sub_action == "regress":
        if "cases" in input_data:
            cmd.extend(["--cases", input_data["cases"]])
        if "report_out" in input_data:
            cmd.extend(["--report-out", input_data["report_out"]])
    elif sub_action == "compare-reports":
        if "baseline" not in input_data or "candidate" not in input_data:
            print("❌ compare-reports 必须提供 baseline 和 candidate 参数")
            return
        cmd.extend(["--baseline", input_data["baseline"], "--candidate", input_data["candidate"]])
        if "report_out" in input_data:
            cmd.extend(["--report-out", input_data["report_out"]])
        if input_data.get("json"):
            cmd.append("--json")
    elif sub_action == "regress-experiment":
        if "baseline_report" not in input_data:
            print("❌ regress-experiment 必须提供 baseline_report 参数")
            return
        cmd.extend(["--baseline-report", input_data["baseline_report"]])
        for key in ["cases", "candidate_report_out", "compare_out", "experiment_out", "baseline_label", "candidate_label", "baseline_notes", "candidate_notes"]:
            if key in input_data:
                cmd.extend([f"--{key.replace('_', '-')}", str(input_data[key])])
        if input_data.get("require_same_case_set"):
            cmd.append("--require-same-case-set")
        if input_data.get("json"):
            cmd.append("--json")
    else:
        print(f"❌ 未知的回归子动作: {sub_action}")
        return
        
    env = os.environ.copy()
    env["PYTHONPATH"] = str(src_path)
    
    print(f"😈 执行底层命令: {' '.join(cmd)}")
    result = subprocess.run(cmd, env=env, capture_output=True, text=True, encoding="utf-8")
    
    print(result.stdout)
    if result.returncode != 0:
        print(f"❌ 引擎执行异常 (Exit Code: {result.returncode}):\n{result.stderr}")