import joblib
import xgboost as xgb

# Assuming model is the trained XGBoost model
model_path = 'final_xgboost_model.pkl'
joblib.dump(model, model_path)
print(f"Model saved to {model_path}")
