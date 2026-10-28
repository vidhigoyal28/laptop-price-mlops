
from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field

# Locate the model relative to this file
MODEL_PATH = Path(__file__).resolve().parent / "model.joblib"

model = joblib.load(MODEL_PATH)

app = FastAPI(
    title="Laptop Price Prediction API",
    description="Predict laptop prices using a trained ML model.",
    version="1.0.0",
)


class LaptopFeatures(BaseModel):
    Brand: str = Field(min_length=1)
    Processor_Speed: float = Field(gt=0)
    RAM_Size: int = Field(gt=0)
    Storage_Capacity: int = Field(gt=0)
    Screen_Size: float = Field(gt=0)
    Weight: float = Field(gt=0)


@app.get("/")
def home():
    return {
        "message": "Laptop Price Prediction API is running",
        "docs": "/docs",
    }


@app.get("/health")
def health():
    return {"status": "healthy", "model_loaded": True}


@app.post("/predict")
def predict_price(laptop: LaptopFeatures):
    # Convert request data to a DataFrame with the training column names
    input_data = pd.DataFrame([laptop.model_dump()])

    # Predict using the saved preprocessing + model pipeline
    prediction = model.predict(input_data)[0]

    return {
        "predicted_price": round(float(prediction), 2)
    }
