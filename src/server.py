## Mark(g) main server file 

# Imports
from flask import Flask, request
import json
import base64
import configparser
import html_generator as gen

# Preparations/Config
print("Markg server launched, remember to launch from the project folder and not the src folder if issues occur using the launch script")
config = configparser.ConfigParser()
config.read("dev/config.ini")
app_port = config["General"]["Port"]

app = Flask(__name__)

@app.route('/embed', methods=['GET'])
def embed():
    data_type = request.args.get("t", "json")
    request_data = request.args.get("d", "{}")
    try:
        data = json.loads(base64.b64decode(request_data).decode("utf-8")) if data_type == "base64" else json.loads(request_data)
    except json.JSONDecodeError as e:
        return f"Failed to parse JSON: {request_data}\n\nError: {e}", 400
    except base64.binascii.Error as e:
        return f"Improper base64 data, check for errors. If data is correct report as unknown error\nData:{request_data}\n\nError: {e}", 400
    except Exception as e:
        return f"Unknown error occured\nData:{request_data}\n\nError:", 500

    return gen.generate_html(data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=app_port)
