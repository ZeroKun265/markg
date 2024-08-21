## Mark(g) main server file 
from flask import Flask, request
import json
import base64
import html_generator as gen

app = Flask(__name__)

@app.route('/embed', methods=['GET'])
def embed():
    data_type = request.args.get("t", "json")
    request_data = request.args.get("d", "")
    try:
        data = json.loads(base64.b64decode(request_data).decode("utf-8")) if data_type == "base64" else json.loads(data)
    except base64.binascii.Error as e:
        return "Improper base64 data, check for errors. If data is correct report as unknown error"

    return gen.generate_html(data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
