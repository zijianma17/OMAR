import yaml
import subprocess
import sys

def load_debug_config(yaml_path):
    with open(yaml_path, 'r') as file:
        return yaml.safe_load(file)

def run_debugger(config):
    script = config["debug"]["script"]
    args = config["debug"].get("args", [])
    
    # 拼接命令
    command = [sys.executable, script] + args

    print(f"Running: {' '.join(command)}")
    subprocess.run(command)

if __name__ == "__main__":
    yaml_file = "debug_config.yaml"
    suffix = "debug_yamls/"

    config = load_debug_config(f"{suffix}{yaml_file}")
    run_debugger(config)