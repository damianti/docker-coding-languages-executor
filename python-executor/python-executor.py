# python-executor.py
from flask import Flask, request
import subprocess

app = Flask(__name__)


@app.route('/python-executor', methods=['POST'])
def execute_code():
    code = request.get_data().decode()
    try:
        output = subprocess.check_output(
            ["python3", "-c", code], stderr=subprocess.STDOUT
        )
    except subprocess.CalledProcessError as e:
        output = e.output

    return output.decode()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)


