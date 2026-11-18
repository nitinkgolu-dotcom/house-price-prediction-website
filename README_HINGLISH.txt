HOUSE PRICE PREDICTION WEBSITE - START KARNE KA TARIKA
======================================================

IMPORTANT:
1. Is ZIP ko extract karo.
2. Apni original Housing.csv file ko is project ke "data" folder ke andar copy karo.
   Final path aisa hona chahiye: data/Housing.csv
3. VS Code mein "House_Price_Prediction_Website" folder open karo.

VS CODE TERMINAL:
Terminal > New Terminal

STEP 1 - Virtual environment (optional but recommended):
py -m venv .venv

STEP 2 - Activate:
Windows PowerShell:
.venv\Scripts\Activate.ps1

Agar activation permission error aaye:
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.venv\Scripts\Activate.ps1

STEP 3 - Install libraries:
py -m pip install -r requirements.txt

STEP 4 - Train actual ML model:
py train_model.py

Training complete hone par models folder mein house_price_model.pkl banega.
Terminal mein R2 Score, MAE aur RMSE bhi dikhenge.

STEP 5 - Website start:
py app.py

Browser mein kholo:
http://127.0.0.1:5000

IMPORTANT NOTES:
- Website ko Live Server se mat chalao. Flask server ke liye terminal mein "py app.py" chalao.
- Housing.csv ke columns hone chahiye:
  Avg. Area Income
  Avg. Area House Age
  Avg. Area Number of Rooms
  Avg. Area Number of Bedrooms
  Area Population
  Price
- Address column optional hai; training mein use nahi hota.
- Currency display INR format mein hai, lekin model ka output dataset ki original Price units mein hota hai.
  Agar dataset prices USD mein hain, toh result ko INR samajhna sahi nahi hoga.
- Estimate sirf model prediction hai, guaranteed market price nahi.
