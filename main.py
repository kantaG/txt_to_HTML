from generater import *
import re

f = open(r"txt_to_HTML\test_input.txt",encoding="utf-8")
html = open(r"txt_to_HTML\text_out.html", "w")

print("<html><head><title>...</title><head></body>", file=html)

title = True
for block in blocks(f):
    block = re.sub(r"\*(.+?)\*",r"<em>\1</em>", block)
    if title:
        print("<h1>", file=html)
        print(block, file=html)
        print("</h1>", file=html)
        title = False
    else:
        print("<p>", file=html)
        print(block, file=html)
        print("</p>", file=html)



print("</body></html>", file=html)
