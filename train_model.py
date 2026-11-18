import pandas as pd
import joblib
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import numpy as np

DATA_PATH = Path("data/Housing.csv")
MODEL_DIR = Path("models")
MODEL_DIR.mkdir(exist_ok=True)

FEATURES = [
    "Avg. Area Income",
    "Avg. Area House Age",
    "Avg. Area Number of Rooms",
    "Avg. Area Number of Bedrooms",
    "Area Population",
]
TARGET = "Price"

if not DATA_PATH.exists():
    raise SystemExit(
        "Housing.csv nahi mili. Apni existing Housing.csv file ko project ke data folder mein rakho: data/Housing.csv"
    )

df = pd.read_csv(DATA_PATH)
missing = [c for c in FEATURES + [TARGET] if c not in df.columns]
if missing:
    raise SystemExit(f"CSV mein required columns missing hain: {missing}")

df = df[FEATURES + [TARGET]].apply(pd.to_numeric, errors="coerce").dropna()
if len(df) < 10:
    raise SystemExit("Dataset mein kam se kam 10 valid rows honi chahiye.")

X = df[FEATURES]
y = df[TARGET]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

r2 = r2_score(y_test, predictions)
mae = mean_absolute_error(y_test, predictions)
rmse = np.sqrt(mean_squared_error(y_test, predictions))

joblib.dump(model, MODEL_DIR / "house_price_model.pkl")

print("\nMODEL TRAINING COMPLETE!")
print(f"Total records: {len(df)}")
print(f"R2 Score: {r2:.4f}")
print(f"MAE: {mae:,.2f}")
print(f"RMSE: {rmse:,.2f}")
print("\nModel saved at: models/house_price_model.pkl")
print("Ab website start karne ke liye: python app.py")
