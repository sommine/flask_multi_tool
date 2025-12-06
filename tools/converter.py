from flask import Blueprint, render_template, request
from . import tools_bp

converter_bp = Blueprint('converter', __name__)

@tools_bp.route("/converter", methods=["GET", "POST"])
#@converter_bp.route("/converter", methods=["GET", "POST"])
def converter():
    result = ""
    if request.method == "POST":
        try:
            value = float(request.form.get("convert_value"))
            direction = request.form.get("direction")
            if direction == "cm_to_inch":
                result = f"{value} cm = {value / 2.54:.2f} inches"
            elif direction == "inch_to_cm":
                result = f"{value} inches = {value * 2.54:.2f} cm"
            else:
                result = "Invalid conversion!"
        except:
            result = "Enter a valid number!"
    return render_template("converter.html", result=result)
