from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    name = ""

    if request.method == "POST":
        name = request.form.get("name", "")

    template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>SSTI Challenge</title>

        <style>
            body {
                margin: 0;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: #0f172a;
                color: #e2e8f0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }

            .container {
                background: #1e293b;
                padding: 40px;
                border-radius: 16px;
                box-shadow: 0 0 25px rgba(0,0,0,0.6);
                width: 400px;
                text-align: center;
            }

            h1 {
                margin-bottom: 10px;
                color: #38bdf8;
            }

            p {
                color: #94a3b8;
                font-size: 14px;
                margin-bottom: 25px;
            }

            input {
                width: 100%;
                padding: 12px;
                border-radius: 8px;
                border: none;
                outline: none;
                margin-bottom: 15px;
                background: #0f172a;
                color: #e2e8f0;
            }

            button {
                width: 100%;
                padding: 12px;
                border: none;
                border-radius: 8px;
                background: #38bdf8;
                color: #0f172a;
                font-weight: bold;
                cursor: pointer;
            }

            .output {
                margin-top: 20px;
                padding: 15px;
                background: #020617;
                border-radius: 8px;
                border: 1px solid #334155;
            }

            .hint {
                margin-top: 20px;
                font-size: 12px;
                color: #475569;
            }
        </style>
    </head>

    <body>
        <div class="container">
            <h1>CSEC CYBER DIVISION</h1>
            <h2>🧪 These unsanitized codes are getting on my nerves</h2>
            <p>what language did I use to make the server I wonder 🤔</p>

            <form method="POST">
                <input type="text" name="name" placeholder="Enter your input...">
                <button type="submit">Execute</button>
            </form>

            {% if name %}
            <div class="output">
                Hello """ + name + """
            </div>
            {% endif %}

            <div class="hint">
                Hint: people call it ssti
            </div>
        </div>
    </body>
    </html>
    """

    return render_template_string(template, name=name)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
