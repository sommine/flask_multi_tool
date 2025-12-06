from flask import Blueprint, render_template, request
from . import tools_bp
double_bp = Blueprint('double', __name__)

@tools_bp.route("/double", methods=["GET", "POST"])

#@double_bp.route("/double", methods=["GET", "POST"])
def double():
    result = ""
    if request.method == "POST":
        try:
            num = float(request.form.get("double_number"))
            result = f"{num} doubled is {num * 2}"
        except:
            result = "Enter a valid number!"
    return render_template("double.html", result=result)
