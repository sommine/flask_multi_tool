from flask import Flask
from tools import tools_bp
import os

app = Flask(__name__)

# Register the main blueprint that includes all tool blueprints & homepage
app.register_blueprint(tools_bp)




if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
