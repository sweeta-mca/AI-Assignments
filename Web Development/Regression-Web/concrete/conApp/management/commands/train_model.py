import pandas as pd
from django.conf import settings
from sklearn.linear_model import LinearRegression
import joblib
import os


MODEL_PATH = os.path.join(settings.BASE_DIR, "conApp", "ml_models", "concrete_model.pkl")

# Example dummy dataset
data = {
    'cement':[540,540,332],
    'slag':[0,0,142],
    'flyash':[0,0,0],
    'water':[162,162,228],
    'superplasticizer':[2.5,2.5,0],
    'coarseaggregate':[1040,1055,932],
    'fineaggregate':[676,676,594],
    'age':[28,28,270],
    'strength':[79.99,61.89,40.27]
}

df = pd.DataFrame(data)

X = df.drop("strength", axis=1)
y = df["strength"]

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, MODEL_PATH)
