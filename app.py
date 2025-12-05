from flask import Flask, request, render_template
from collections import defaultdict

app = Flask(__name__)

# Atomic masses
atomic_masses = {
    'H': 1.008, 'He': 4.0026, 'Li': 6.94, 'Be': 9.0122, 'B': 10.81,
    'C': 12.011, 'N': 14.007, 'O': 15.999, 'F': 18.998, 'Ne': 20.180,
    'Na': 22.990, 'Mg': 24.305, 'Al': 26.982, 'Si': 28.085, 'P': 30.974,
    'S': 32.06, 'Cl': 35.45, 'K': 39.098, 'Ca': 40.078, 'Fe': 55.845,
    'Ni': 58.6934, 'Cu': 63.546, 'Zn': 65.38, 'Ag': 107.8682, 'I': 126.90447,
    'Au': 196.96657, 'Pb': 207.2
}

# Store atomic mass formula
molecule_formula = defaultdict(int)

@app.route("/", methods=["GET", "POST"])
def index():
    global molecule_formula
    results = {
        "double_result": "",
        "convert_result": "",
        "atomic_mass_message": ""
    }

    if request.method == "POST":
        # Double a number
        if "double_number" in request.form:
            try:
                num = float(request.form.get("double_number"))
                results["double_result"] = f"{num} doubled is {num * 2}"
            except ValueError:
                results["double_result"] = "Enter a valid number!"

        # CM ↔ Inch converter
        elif "convert_value" in request.form:
            try:
                value = float(request.form.get("convert_value"))
                direction = request.form.get("direction")
                if direction == "cm_to_inch":
                    results["convert_result"] = f"{value} cm = {value / 2.54:.2f} inches"
                elif direction == "inch_to_cm":
                    results["convert_result"] = f"{value} inches = {value * 2.54:.2f} cm"
                else:
                    results["convert_result"] = "Invalid conversion!"
            except ValueError:
                results["convert_result"] = "Enter a valid number!"

        # Atomic Mass Calculator
        elif "add_element" in request.form:
            element = request.form.get("element")
            num_atoms = request.form.get("num_atoms")
            try:
                num_atoms = int(num_atoms)
                if element in atomic_masses and num_atoms > 0:
                    molecule_formula[element] += num_atoms
                else:
                    results["atomic_mass_message"] = "Invalid element or count!"
            except ValueError:
                results["atomic_mass_message"] = "Enter a valid number of atoms!"

        elif "calculate_mass" in request.form:
            total_mass = sum(atomic_masses[el] * count for el, count in molecule_formula.items())
            results["atomic_mass_message"] = f"Molecular Mass: {total_mass:.4f} u"

        elif "clear_formula" in request.form:
            molecule_formula.clear()

    return render_template("index.html", 
                           atomic_masses=atomic_masses, 
                           molecule_formula=dict(molecule_formula),
                           results=results)

if __name__ == "__main__":
    app.run(debug=True)
