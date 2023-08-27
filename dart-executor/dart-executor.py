# dart-executor.py
from flask import Flask, request
import subprocess

app = Flask(__name__)


@app.route('/dart-executor', methods=['POST'])
def execute_code():
    code = request.get_data().decode()

    with open('main.dart', 'w') as f:
        f.write(code)

    try:
        run_output = subprocess.run(['dart', 'main.dart'], capture_output=True, text=True)

        return run_output.stdout

    except subprocess.CalledProcessError as e:
        return e.stderr


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5003)
