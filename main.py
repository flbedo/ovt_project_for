from datetime import datetime
import os
from flask import Flask
import easydata3 as ed
import bb

app = Flask(__name__)
FILE_NAME = "logs.txt"
if not os.path.exists('data.db'):
    ed.create_database('data')
    ed.give_item_data('data', 'system', 'status', 'off')

def write_status(status):
    ed.give_item_data('data', 'system', 'status', status)
    bb.add('System', f'Changed status to {status}')

def get_status():
    return ed.get_item_data('data', 'system', 'status')


@app.route("/")
def home():
    return "Список команд: /on, /off или /status в строке браузера."


@app.route("/on")
def turn_on():
    write_status("on")
    return "Статус ON."


@app.route("/off")
def turn_off():
    write_status("off")
    return "Статус OFF."


@app.route("/status")
def show_status():
    current_status = get_status()
    html_page = f"""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Текущий статус</title>
        <style>
            :root {{
                --bg-color: #f8fafc;
                --card-bg: #ffffff;
                --text-on: #10b981;
                --text-off: #ef4444;
                --shadow-on: 0 0 40px rgba(16, 185, 129, 0.25);
                --shadow-off: 0 0 40px rgba(239, 68, 68, 0.25);
                --text-secondary: #64748b;
            }}
            body {{
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
                background-color: var(--bg-color);
                color: #334155;
            }}
            .status-container {{
                text-align: center;
                padding: 3rem 4rem;
                border-radius: 1.5rem;
                background: var(--card-bg);
                box-shadow: 0 20px 40px rgba(0, 0, 0, 0.04);
                animation: fadeIn 0.8s cubic-bezier(0.16, 1, 0.3, 1);
            }}
            .label {{
                font-size: 0.875rem;
                text-transform: uppercase;
                letter-spacing: 0.15em;
                color: var(--text-secondary);
                margin-bottom: 1.5rem;
                font-weight: 600;
            }}
            h1 {{
                font-size: clamp(3rem, 12vw, 10rem);
                font-weight: 800;
                text-transform: uppercase;
                letter-spacing: 0.02em;
                margin: 0;
                line-height: 1;
                color: {"var(--text-on)" if current_status == "on" else "var(--text-off)"};
                text-shadow: {"var(--shadow-on)" if current_status == "on" else "var(--shadow-off)"};
                transition: color 0.4s ease, text-shadow 0.4s ease;
            }}
            @keyframes fadeIn {{
                from {{ opacity: 0; transform: translateY(20px) scale(0.98); }}
                to {{ opacity: 1; transform: translateY(0) scale(1); }}
            }}
        </style>
    </head>
    <body>
        <div class="status-container">
            <div class="label">Системный статус</div>
            <h1>{current_status}</h1>
        </div>
    </body>
    </html>
    """
    return html_page


@app.route("/api/status")
def api_status():

    return get_status()

if __name__ == "__main__":
    app.run(debug=True, port=3000)