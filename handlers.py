class HTMLrender:
    def start_paragraph(self):
        print("<p>")
    def end_paragraph(self):
        print("</p>")
    def emphsis(self, line):
        return f'<em>{line.group(1)}</em>'
    def feed(self, data):
        print(data)
    