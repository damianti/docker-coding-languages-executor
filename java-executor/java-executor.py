# java-executor.py
from flask import Flask, request
import subprocess
import os
import re

app = Flask(__name__)


@app.route('/', methods=['POST'])
def execute_code():
    code = request.get_data().decode()

    # Extract class name from the Java code
    class_name_match = re.search(r'class (\w+)', code)
    if class_name_match is None:
        return "Invalid code: Could not find a class declaration"

    class_name = class_name_match.group(1)

    with open(f"/tmp/{class_name}.java", "w") as file:
        file.write(code)

    try:
        compile_output = subprocess.check_output(
            ["javac", f"/tmp/{class_name}.java"], stderr=subprocess.STDOUT
        )

        run_output = subprocess.check_output(
            ["java", "-cp", "/tmp", class_name], stderr=subprocess.STDOUT
        )

        os.remove(f"/tmp/{class_name}.java")
        os.remove(f"/tmp/{class_name}.class")

    except subprocess.CalledProcessError as e:
        return e.output.decode()

    return run_output.decode()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5002)
