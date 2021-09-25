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
            result = self.callback('sub_', name, match)
            if result is None:
                match.group(0)
            return result
        return subtituation
    


class HTMLrender(Handler):
    def start_document(self):
        print('<!DOCTYPE html><html lang="ja"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>...</title></head><body>')
    def end_documenmt(self):
        print("</body></html>")
    def start_paragraph(self):
        print("<p>")
    def end_paragraph(self):
        print("</p>")
    def start_title(self):
        print("<h1>")
    def end_title(self):
        print("</h1>")
    def start_heading(self):
        print("<h2>")
    def end_heading(self):
        print("</h2>")
    def start_list(self):
        print("<ul>")
    def end_list(self):
        print("</ul>")
    def start_listitem(self):
        print("<li>")
    def end_listitem(self):
        print("</li>")
    def sub_emphasis(self, match):
        return f'<em>{match.group(1)}</em>'
    def sub_url(self, match):
        return f'<a href="{match.group(1)}">{match.group(1)}</a>'
    def sub_mail(self, match):
        return f'<a href="mailto:{match.group(1)}">{match.group(1)}</a>'
    def feed(self, data):
        print(data)