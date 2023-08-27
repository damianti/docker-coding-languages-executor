# router.py
from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'tmp/code_files'
# Docker container names instead of local paths
python_executor_url = 'http://python-executor:5001/python-executor'
java_executor_url = 'http://java-executor:5002/'
dart_executor_url = 'http://dart-executor:5003/dart-executor'


# BASE_URL = 'http://127.0.0.1:5000'


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file received'}), 400

    file = request.files['file']

    if file:
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return jsonify({'message': 'File saved successfully'}), 200


@app.route('/execute', methods=['GET'])
def execute_code():
    responses = []
    for filename in os.listdir(app.config['UPLOAD_FOLDER']):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        with open(file_path, 'r') as file:
            code = file.read()
            print(f"Executing code from file: {filename}")
            print(f"Code content:\n{code}")
            executor = identify_executor(file_path)
            if executor:
                print(f"Sending code to URL: {executor}")
                response = requests.post(executor, data=code)
                responses.append({
                    'file': filename,
                    'response': response.content.decode()
                })
            else:
                responses.append({
                    'file': filename,
                    'response': 'No executor found for this file type'
                })

            # os.remove(file_path)
    return {'responses': responses}


def identify_executor(file_name):
    if file_name.endswith('.py'):
        return python_executor_url
    elif file_name.endswith('.java'):
        return java_executor_url
    elif file_name.endswith('.dart'):
        return dart_executor_url
    else:
        return None


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5005)
