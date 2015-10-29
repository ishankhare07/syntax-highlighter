from pygments import highlight
from pygments.formatters import HtmlFormatter
import pygments.lexers
import os

class Highlighter:
    def __init__(self, filename, code):
        self.lexer = pygments.lexers.get_lexer_for_filename(filename)
        self.highlighted_code = highlight(code, self.lexer, HtmlFormatter(linnenos=True))

    def get_highlighted_code(self):
        return self.highlighted_code

    def get_stylesheet_content(self):
        css_content = HtmlFormatter(linnenos=True).get_style_defs('.highlight')
        css_filename = 'static/css/' + self.lexer.__class__.__name__
        if not os.path.exists(css_filename):
            open('static/css/' + self.lexer.__class__.__name__, 'w').write(css_content)
        return 'static/css/'+ self.lexer.__class__.__name__

