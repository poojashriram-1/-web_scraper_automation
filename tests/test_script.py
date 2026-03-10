import subprocess

result = subprocess.run(["python", "main.py"], capture_output=True)

print(result.stdout)