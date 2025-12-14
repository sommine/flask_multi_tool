from flask import Blueprint, render_template, request
from .electron_config import electron_configuration
from .elements import ELEMENTS  # import the centralized elements

orbitals_bp = Blueprint("orbitals", __name__, url_prefix="/orbitals")

@orbitals_bp.route("/", methods=["GET", "POST"])
def orbitals_page():
    config = None
    element = None
    atomic_data = None

    if request.method == "POST":
        element = request.form.get("element")
        if element in ELEMENTS:
            atomic_data = ELEMENTS[element]
            z = atomic_data["Z"]
            
            config = electron_configuration(z)

    return render_template(
        "orbitals.html",
        elements=ELEMENTS,
        config=config,
        element=element,
        atomic_data=atomic_data
    )