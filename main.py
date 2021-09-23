import re, sys
from utils import *
from handlers import *
from rules import *

class Parser:
    def __init__(self, handler):
        self.handler = handler
        self.rules = []
        self.filters = []
    def addRule(self, rule):
        self.rules.append(rule)
    def addFilter(self, pattern, name):
        def filter(block, handler):
            return re.sub(pattern, handler.sub(name), block)
        self.filters.append(filter)
    
    def parse(self, file):
        self.handler.start("docment")
        for block in blocks(file):
            for filter in self.filters:
                block = filter(block, self.handler)
            for rule in self.rules:
                if rule.condition(block):
                    last = rule.action(block, self.handler)
                    if last:
                        break
        self.handler.end('docment')

class BasicTextParser(Parser):
    def __init__(self, handler):
        Parser.__init__(self, handler)
        self.addRule(ListRule)
        self.addRule(ListItemRule)
        self.addRule(TitleRule)
        self.addRule(HeadingRule)
        self.addRule(ParagraphRule)

        self.addFilter(r'\*(.+?)\*', "emphasis")
        self.addFilter(r'(https://[\.a-zA-Z/]+)', "url")
        self.addFilter(r'([\.a-zA-Z/]+@[\.a-zA-Z/]+)', "mail")

handler = HTMLrender()
parser = BasicTextParser(handler)

parser.parse(sys.stdin)