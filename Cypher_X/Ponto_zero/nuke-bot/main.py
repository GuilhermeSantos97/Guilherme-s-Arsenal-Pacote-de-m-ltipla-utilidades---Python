import subprocess
import sys
import re
from colorama import init, Fore

# Initialize colorama
init()

# Set the URL for redirection
redirect_url = "https://github.com/GuilhermeSantos97"

# Print colored text with redirection URL
print(Fore.MAGENTA + "Made by " + Fore.BLUE + "GuilhermeSantos97")
print(Fore.YELLOW + f"Clique aqui para visitar o meu perfil: {redirect_url}")

command = ['node', '--version']

process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
stdout, _ = process.communicate()

node_version = stdout.decode('utf-8').strip()

match = re.match(r"v(\d+)", node_version)
if match:
    node_major_version = int(match.group(1))
else:
    print(Fore.RED + "Error: Failed to extract Node.js version.")
    sys.exit(1)

if node_major_version < 18:
    print(Fore.RED + "Error: Node.js version 18 or higher is required to run this script.")
    sys.exit(1)

print(Fore.GREEN + "Starting Nuke Bot...")
command_run = ['node', 'nuke-bot/index.js']
process = subprocess.Popen(command_run, shell=False)
process.communicate()
