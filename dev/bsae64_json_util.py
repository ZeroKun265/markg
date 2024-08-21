import json
import base64

def json_to_base64(json_data):
    # Convert the dictionary to a JSON string
    json_str = json.dumps(json_data)
    
    # Encode the JSON string to bytes and then to a Base64 string
    base64_bytes = base64.b64encode(json_str.encode('utf-8'))
    
    # Return the Base64 string
    return base64_bytes.decode('utf-8')

def base64_to_json(base64_str):
    # Decode the Base64 string to bytes
    json_bytes = base64.b64decode(base64_str)
    
    # Convert bytes back to a JSON string
    json_str = json_bytes.decode('utf-8')
    
    # Load the JSON string into a dictionary and return
    return json.loads(json_str)

print(json_to_base64({"test": 1}))