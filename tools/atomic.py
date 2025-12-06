from flask import Blueprint, render_template, request
from collections import defaultdict

atomic_bp = Blueprint('atomic', __name__)


atomic_masses = {
    "H": 1.008,            # Hydrogen
    "He": 4.0026,          # Helium
    "Li": 6.94,            # Lithium
    "Be": 9.0122,          # Beryllium
    "B": 10.81,            # Boron
    "C": 12.011,           # Carbon
    "N": 14.007,           # Nitrogen
    "O": 15.999,           # Oxygen
    "F": 18.998,           # Fluorine
    "Ne": 20.180,          # Neon
    "Na": 22.98976928,     # Sodium
    "Mg": 24.305,          # Magnesium
    "Al": 26.9815385,      # Aluminium
    "Si": 28.085,          # Silicon
    "P": 30.973761998,     # Phosphorus
    "S": 32.06,            # Sulfur
    "Cl": 35.45,           # Chlorine
    "Ar": 39.948,          # Argon
    "K": 39.0983,          # Potassium
    "Ca": 40.078,          # Calcium
    "Sc": 44.955908,       # Scandium
    "Ti": 47.867,          # Titanium
    "V": 50.9415,          # Vanadium
    "Cr": 51.9961,         # Chromium
    "Mn": 54.938044,       # Manganese
    "Fe": 55.845,          # Iron
    "Co": 58.933194,       # Cobalt
    "Ni": 58.6934,         # Nickel
    "Cu": 63.546,          # Copper
    "Zn": 65.38,           # Zinc
    "Ga": 69.723,          # Gallium
    "Ge": 72.630,          # Germanium
    "As": 74.921595,       # Arsenic
    "Se": 78.971,          # Selenium
    "Br": 79.904,          # Bromine
    "Kr": 83.798,          # Krypton
    "Rb": 85.4678,         # Rubidium
    "Sr": 87.62,           # Strontium
    "Y": 88.90584,         # Yttrium
    "Zr": 91.224,          # Zirconium
    "Nb": 92.90637,        # Niobium
    "Mo": 95.95,           # Molybdenum
    "Tc": 98,              # Technetium
    "Ru": 101.07,          # Ruthenium
    "Rh": 102.90550,       # Rhodium
    "Pd": 106.42,          # Palladium
    "Ag": 107.8682,        # Silver
    "Cd": 112.414,         # Cadmium
    "In": 114.818,         # Indium
    "Sn": 118.710,         # Tin
    "Sb": 121.760,         # Antimony
    "Te": 127.60,          # Tellurium
    "I": 126.90447,        # Iodine
    "Xe": 131.293,         # Xenon
    "Cs": 132.90545196,    # Cesium
    "Ba": 137.327,         # Barium
    "La": 138.90547,       # Lanthanum
    "Ce": 140.116,         # Cerium
    "Pr": 140.90766,       # Praseodymium
    "Nd": 144.242,         # Neodymium
    "Pm": 145,             # Promethium
    "Sm": 150.36,          # Samarium
    "Eu": 151.964,         # Europium
    "Gd": 157.25,          # Gadolinium
    "Tb": 158.92535,       # Terbium
    "Dy": 162.500,         # Dysprosium
    "Ho": 164.93033,       # Holmium
    "Er": 167.259,         # Erbium
    "Tm": 168.93422,       # Thulium
    "Yb": 173.045,         # Ytterbium
    "Lu": 174.9668,        # Lutetium
    "Hf": 178.49,          # Hafnium
    "Ta": 180.94788,       # Tantalum
    "W": 183.84,           # Tungsten
    "Re": 186.207,         # Rhenium
    "Os": 190.23,          # Osmium
    "Ir": 192.217,         # Iridium
    "Pt": 195.084,         # Platinum
    "Au": 196.96657,       # Gold
    "Hg": 200.592,         # Mercury
    "Tl": 204.38,          # Thallium
    "Pb": 207.2,           # Lead
    "Bi": 208.98040,       # Bismuth
    "Po": 209,             # Polonium
    "At": 210,             # Astatine
    "Rn": 222,             # Radon
    "Fr": 223,             # Francium
    "Ra": 226,             # Radium
    "Ac": 227,             # Actinium
    "Th": 232.0377,        # Thorium
    "Pa": 231.03588,       # Protactinium
    "U": 238.02891,        # Uranium
    "Np": 237,             # Neptunium
    "Pu": 244,             # Plutonium
    "Am": 243,             # Americium
    "Cm": 247,             # Curium
    "Bk": 247,             # Berkelium
    "Cf": 251,             # Californium
    "Es": 252,             # Einsteinium
    "Fm": 257,             # Fermium
    "Md": 258,             # Mendelevium
    "No": 259,             # Nobelium
    "Lr": 266,             # Lawrencium
    "Rf": 267,             # Rutherfordium
    "Db": 268,             # Dubnium
    "Sg": 269,             # Seaborgium
    "Bh": 270,             # Bohrium
    "Hs": 270,             # Hassium
    "Mt": 278,             # Meitnerium
    "Ds": 281,             # Darmstadtium
    "Rg": 282,             # Roentgenium
    "Cn": 285,             # Copernicium
    "Nh": 286,             # Nihonium
    "Fl": 289,             # Flerovium
    "Mc": 290,             # Moscovium
    "Lv": 293,             # Livermorium
    "Ts": 294,             # Tennessine
    "Og": 294              # Oganesson
}



molecule_formula = defaultdict(int)

@atomic_bp.route("/atomic", methods=["GET", "POST"])
def atomic():
    message = ""
    if request.method == "POST":
        action = request.form.get("action")

        if action == "add_element":
            element = request.form.get("element")
            num_atoms = request.form.get("num_atoms")
            try:
                num_atoms = int(num_atoms)
                if element in atomic_masses and num_atoms > 0:
                    molecule_formula[element] += num_atoms
                    message = f"Added {num_atoms} {element}(s)."
                else:
                    message = "Invalid element or count!"
            except:
                message = "Enter a valid number of atoms!"

        elif action == "calculate_mass":
            if molecule_formula:
                total_mass = sum(atomic_masses[el] * count for el, count in molecule_formula.items())
                message = f"Molecular Mass: {total_mass:.4f} u"
            else:
                message = "Add at least one element first!"

        elif action == "clear_formula":
            molecule_formula.clear()
            message = "Formula cleared."

    return render_template(
        "atomic.html",
        atomic_masses=atomic_masses,
        molecule=dict(molecule_formula),
        message=message
    )