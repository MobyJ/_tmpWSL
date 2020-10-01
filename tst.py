import os, sys

print("HelloWorld")

for i in range(32, 126):
    print( i, chr(i) )


words = ['apple', 'banana', 'peach', '42']
if 'apple' in words:
    print('found apple')

if 'a' in words:
    print('found a')
else:
    print('NOT found a')

if 42 in words:
    print('found 42')
else:
    print('NOT found 42')