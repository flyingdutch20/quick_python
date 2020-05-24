class HTML:
    def __init__(self, str):
        self.str = str
    def output(self):
        return "<html>" + Body.output(str) + "</html>"

class Body:
    def __init__(self, str, sub):
        self.str = str
        self.sub = sub
    def output(self):
        output = "<body>" + self.str
        for para in self.sub:
            output = output + P.output(para)
        output = output + "</body>"
        return output

class P:
    def __init__(self, str):
        self.str = str
    def output(self):
        return "<p>" + self.str + "</p>"
