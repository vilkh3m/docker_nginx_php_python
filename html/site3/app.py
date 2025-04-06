from flask import Flask
import sys
import platform
import os
import pkg_resources

app = Flask(__name__)


@app.route("/")
def python_info():
    # Zbieranie informacji
    info = {
        "Python Version": sys.version,
        "Python Executable": sys.executable,
        "Platform": platform.platform(),
        "OS": os.name,
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "System": platform.system(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Current Working Directory": os.getcwd(),
        "Environment Variables": dict(os.environ),
        "Installed Packages": {
            d.project_name: d.version for d in pkg_resources.working_set
        },
    }

    # Formatowanie odpowiedzi jako HTML
    html = "<h1>Python Info</h1><pre>"
    for key, value in info.items():
        html += f"{key}: {value}\n"
    html += "</pre>"
    return html


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
