# mrebuilder - a small and dirty script to help you with building MRE projects
# By giangvinhloc610 (giangvinhloc610@gmail.com)
# Licensed under MIT license. See LICENSE file in the repo

# Check the current environment
import sys

if sys.version_info.major < 3:
    raise Exception("You are using Python " + sys.version.major + "." + sys.version.minor + "." + sys.version.micro + ". mrebuider will only work with Python 3. Please consider upgrading your python. Note that this script *might* works on Python 2 with some modifications")
    exit(1)

if sys.platform != "win32":
    print("This script only works on Windows. Please consider switching to Windows, or using Wine")
    exit(1)

# Import needed modules
import winreg

# Help string
help_string = '''
mrebuilder - a small and dirty script to help you with building MRE projects
By giangvinhloc610 (giangvinhloc610@gmail.com)
\nUsage: mrebuilder.py <command> [options]
Build commands:
  create         - create a new project
  update         - update an the file list
  build          - build a project
  build_modis    - build a project for MODIS
  run            - run a project with a ARM MRE emulator (not supported yet, in development)
  run_modis      - run built x86 vxp with MODIS
  clean          - clean a project

Config commands:
  newconfig      - create a new config
  selectconfig   - select the config to use
  delconfig      - delete a config
  config         - configure the settings

Fix commands:
  problems       - show all detected problems in a project
  fix            - fix all detected problems in a project
  fixpath        - fix the paths when copying project from other computers
  fixlib         - automatically add the libraries needed to the build command line
  fixpermission  - automatically add the needed permissions to the app
  fixinclude     - automatically add the needed header files

Info commands:
  info           - show info about a project
  infovxp        - show info about a built vxp
  infoenv        - show info about the development environment

Sign commands:
  sign           - sign a built vxp
  unsign         - unsign a signed vxp
  signinfo       - show info about a signed vxp (and probably steal the IMSI :D)

Reverse engineering commands:
  fixheader      - fix the header of a vxp (for loading into IDA)
  unpack         - unpack a zlib compressed vxp

Help commands:
  version        - show the version of mrebuilder
  help           - show this help

For help of a command, please run mrebuilder.py <command> -h or mrebuilder.py help <command>
'''

# Parse the arguments
if len(sys.argv) == 1:
    print(help_string)
    exit(1)

# Redirect the commands
# Hopefully no one will use this for bad purpose

command_list = []

for i in help_string.split("\n"):
    if i.startswith("  "):
        command_list.append(i.split("  ")[1])

if sys.argv[1] in command_list:
    exec(sys.argv[1] + "()") # Execute the function with the same name as the command
else:
    print("Unknown command: " + sys.argv[1])
    print(help_string)
    exit(1)

