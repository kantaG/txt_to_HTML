class Handler:
    def callback(self, prefix, name, *args):
        method = getattr(self, prefix + name, None)
        if callable(method):
            return method(*args)
    def start(self, name):
        self.callback('start_', name)
    def end(self, name):
        self.callback('end_', name)
    def sub(self, name):
        def subtituation(match):
            result = self.callback('sub_', name)
            if result is None:
                match.group(0)
            return result
        return subtituation
    


class HTMLrender(Handler):
    def start_paragraph(self):
        print("<p>")
    def end_paragraph(self):
        print("</p>")
    def sub_emphsis(self, line):
        return f'<em>{line.group(1)}</em>'
    def feed(self, data):
        print(data)