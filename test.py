from main import app
from highlighter import Highlighter

if __name__ == "__main__":
    h = Highlighter('hello.py', "print('hello world')")
    h.get_highlighted_code()
    h.get_stylesheet_content()
    h.get_css_id_name()

    print('successfully finished all tests')
