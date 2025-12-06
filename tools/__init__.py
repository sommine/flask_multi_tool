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


# def get_latest_co2():
#     url = "https://datahub.io/core/co2-ppm/r/co2-mm-mlo.csv"
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         df = pd.read_csv(StringIO(response.text))

#         # Drop rows with missing CO2 value
#         df = df.dropna(subset=['Average'])
#         latest = df.iloc[-1]

#         # Use Decimal Date to approximate year and month
#         decimal_date = latest['Decimal Date']
#         year = int(decimal_date)
#         month = int((decimal_date - year) * 12) + 1

#         return {
#             "co2": latest['Average'],
#             "year": year,
#             "month": month
#         }
#     except Exception as e:
#         print("Error fetching CO2:", e)
#         return {"co2": None, "year": None, "month": None}
    




def get_latest_co2():
    url = "https://datahub.io/core/co2-ppm/r/co2-mm-mlo.csv"
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        f = StringIO(resp.text)
        reader = csv.DictReader(f)
        rows = list(reader)
        latest = rows[-1]
        return {"co2": float(latest["Average"]), "year": int(latest["Year"]), "month": int(latest["Month"])}
    except Exception as e:
        print("Error fetching CO2:", e)
        return {"co2": None, "year": None, "month": None}