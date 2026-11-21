HOUSE PRICE PREDICTION WEB APP

Files:
- app.py
- templates/index.html
- requirements.txt

IMPORTANT:
Place your original Housing.csv dataset in the same folder as app.py.
The app needs this dataset to train the models and calculate real predictions/metrics.
The dataset was not included with the uploaded Python script.

Run:
1. Install Python.
2. Open a terminal in this folder.
3. Run: pip install -r requirements.txt
4. Run: python app.py
5. Open the local address shown in the terminal (usually http://127.0.0.1:5000).

The website follows the uploaded script:
- Drops the Address column.
- Uses Price as the target and the five remaining features as inputs.
- Uses train_test_split(test_size=0.2, random_state=42).
- Trains Linear Regression, Decision Tree and Random Forest.
- Uses Linear Regression for the interactive prediction, as in the original script.
- Displays MAE, RMSE and R2 for all three models.

Note: The original dataset is required; no sample or invented prediction values are used.