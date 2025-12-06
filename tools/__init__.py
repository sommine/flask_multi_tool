from flask import Blueprint, render_template
import time
import csv
import requests
from io import StringIO

# Define Blueprint first
tools_bp = Blueprint('tools', __name__)

# Import submodules after blueprint
from . import atomic, converter, double



# Homepage route
@tools_bp.route("/", methods=["GET"])
def home():
    epoch_time = int(time.time())
    co2_data = get_latest_co2()
    co2_value = co2_data['co2']
    #co2_value = 420.5  # temporary tes
    print("CO2 data:", co2_data)  # temporary debug
    return render_template("home.html", epoch=epoch_time, co2=co2_value)





def get_latest_co2():
    url = "https://datahub.io/core/co2-ppm/r/co2-mm-mlo.csv"
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        f = StringIO(resp.text)
        reader = csv.DictReader(f)
        
        # Filter out rows where 'Date' or 'Average' is empty
        valid_rows = [row for row in reader if row["Date"] and row["Average"]]
        if not valid_rows:
            raise ValueError("No valid rows in CSV")

        latest = valid_rows[-1]
        print(latest)

        # Extract CO2 value
        co2 = float(latest["Average"])

        # Extract year and month from Date safely
        date_parts = latest["Date"].split("-")
        if len(date_parts) >= 2:
            year, month = int(date_parts[0]), int(date_parts[1])
        else:
            year, month = None, None

        return {"co2": co2, "year": year, "month": month}

    except Exception as e:
        print("Error fetching CO2:", e)
        return {"co2": None, "year": None, "month": None}