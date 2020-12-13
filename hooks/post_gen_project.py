import subprocess
import json
from pathlib import Path

# initialize git repo
print('initializing git repo')
subprocess.run('git init', shell=True)

# create conda env
subprocess.run('conda env create -f ./env.yml', shell=True)

# update VS Code settings python path with new conda env
print("updating VS Code settings with new python conda env")
r = subprocess.run('conda info -e', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
line = [x for x in r.stdout.decode().splitlines() if x.split(' ')[0] == '{{ cookiecutter.package_name }}'][0]
env_path = line.split()[-1]
config = json.loads(Path('./.vscode/settings.json').read_text())
config["python.pythonPath"] = env_path
Path('./.vscode/settings.json').write_text(json.dumps(config, indent=2))
