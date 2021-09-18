from generater import *

f = open(r"C:\Users\kanta\Documents\programming\python\txt_to_HTML\test_input.txt",encoding="utf-8")

for line in blocks(f):
    print(line)