from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    double_result = ""
    convert_result = ""

    if request.method == "POST":
        # Double a Number
        if "double_number" in request.form:
            try:
                num = float(request.form.get("double_number"))
                double_result = f"{num} doubled is {num * 2}"
            except ValueError:
                double_result = "Please enter a valid number."

        # CM ↔ Inch Converter
        elif "convert_value" in request.form:
            try:
                value = float(request.form.get("convert_value"))
                direction = request.form.get("direction")
                if direction == "cm_to_inch":
                    convert_result = f"{value} cm = {value / 2.54:.2f} inches"
                elif direction == "inch_to_cm":
                    convert_result = f"{value} inches = {value * 2.54:.2f} cm"
                else:
                    convert_result = "Invalid conversion direction."
            except ValueError:
                convert_result = "Please enter a valid number."

    return render_template("index.html",
                           double_result=double_result,
                           convert_result=convert_result)

if __name__ == "__main__":
    app.run(debug=True)
