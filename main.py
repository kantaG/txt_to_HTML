from generater import *
import re

f = open(r"txt_to_HTML\generater.py",encoding="utf-8")

print("<html><head><title>...</title><head></body>")

title = True
for block in blocks(f):
    if title:
        print("<h1>")
        print(block)
        print("</h1>")
        title = False
    else:
        print("<p>")
        print(block)
        print("</p>")



print("</body></html>")
