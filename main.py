from flask import Flask, request, jsonify
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/v0.1/highlight', methods=['GET'])
def highlight():
    data = request.args 
    print(data['filename'], data['code'])
    return "<p>success</p>"

if __name__ == "__main__":
    app.run(debug=True)
