from flask import Flask, render_template
from tools.atomic import atomic_bp
from tools.double import double_bp
from tools.converter import converter_bp
import os

app = Flask(__name__)

# Register blueprints
app.register_blueprint(atomic_bp)
app.register_blueprint(double_bp)
app.register_blueprint(converter_bp)

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

