from flask import Flask, request, jsonify
from flask import render_template
from highlighter import Highlighter


app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('html/index.html')

@app.route('/api/v0.1/highlight', methods=['POST'])
def highlight():
    data = request.get_json()
    highlight = Highlighter(data['filename'], data['code'])
    return_dict = {
        'highlighted_code': highlight.get_highlighted_code(),
        'css_class': highlight.get_stylesheet_content(),
        'id_name': highlight.get_css_id_name(),
        'success': True,
            }
    return jsonify(return_dict)

if __name__ == "__main__":
    app.run(debug=True)
