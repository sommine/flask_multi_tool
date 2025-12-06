from flask import Flask, render_template
from tools.atomic import atomic_bp
from tools.double import double_bp
from tools.converter import converter_bp
import os
import time


from tools import tools_bp  # this now works

app = Flask(__name__)
app.register_blueprint(tools_bp)






# Register blueprints
app.register_blueprint(atomic_bp)
app.register_blueprint(double_bp)
app.register_blueprint(converter_bp)

@app.route("/")
def home():
    return render_template("home.html")

def index():
    epoch_time = int(time.time())
    co2_value = 420.12  # placeholder, later live API
    return render_template("index.html", epoch=epoch_time, co2=co2_value)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

