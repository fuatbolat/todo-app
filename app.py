from flask import Flask, render_template_string

app = Flask(__name__)

todos = ["DevOps", "Steps", "Monitoring"]

@app.route("/")
def home():
    html = """
    <h1>ToDo Listem</h1>
    <ul>
        {% for item in todos %}
            <li>{{ item }}</li>
        {% endfor %}
    </ul>
    """
    return render_template_string(html, todos=todos)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
