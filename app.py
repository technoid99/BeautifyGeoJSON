from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/beautify', methods=['POST'])
def beautify():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file:
        data = file.read()
        try:
            json_data = json.loads(data)
            beautified_json = json.dumps(json_data, indent=4)
            return beautified_json
        except json.JSONDecodeError:
            return "Invalid JSON file"

if __name__ == '__main__':
    app.run(debug=True)
