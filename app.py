from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

app = Flask(__name__)

# Keep Housing.csv in the same folder as app.py
df = pd.read_csv("Housing.csv")
df = df.drop("Address", axis=1)

X = df.drop("Price", axis=1)
y = df["Price"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

lr = LinearRegression()
lr.fit(X_train, y_train)

dt = DecisionTreeRegressor(random_state=42)
dt.fit(X_train, y_train)

rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

models = {"Linear Regression": (lr, lr.predict(X_test)),
          "Decision Tree": (dt, dt.predict(X_test)),
          "Random Forest": (rf, rf.predict(X_test))}

metrics = {}
for name, (_, pred) in models.items():
    metrics[name] = {
        "mae": mean_absolute_error(y_test, pred),
        "rmse": np.sqrt(mean_squared_error(y_test, pred)),
        "r2": r2_score(y_test, pred)
    }

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    error = None
    values = {}
    if request.method == "POST":
        try:
            fields = ["income", "house_age", "rooms", "bedrooms", "population"]
            values = {key: float(request.form[key]) for key in fields}
            if any(v < 0 for v in values.values()):
                raise ValueError("Please enter values that are zero or greater.")
            row = pd.DataFrame([[
                values["income"], values["house_age"], values["rooms"],
                values["bedrooms"], values["population"]
            ]], columns=X.columns)
            prediction = float(lr.predict(row)[0])
        except (ValueError, KeyError):
            error = "Please enter valid numeric values (zero or greater) in every field."
    return render_template("index.html", prediction=prediction, error=error,
                           values=values, metrics=metrics, rows=len(df))

if __name__ == "__main__":
    app.run(debug=True)
