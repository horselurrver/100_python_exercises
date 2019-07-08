import zlib
"""
Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".


Hints:
Use zlib.compress() and zlib.decompress() to compress and decompress a string.
"""
#use python 2
string = "hello world!hello world!hello world!hello world!"
compress = zlib.compress(string)
print(compress)
print(zlib.decompress(compress))
