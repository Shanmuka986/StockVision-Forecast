import joblib

model = joblib.load("models/best_model.pkl")

print("=" * 60)
print("Model Type")
print("=" * 60)
print(type(model))

print()

print("=" * 60)
print("Features Used During Training")
print("=" * 60)

print(model.feature_names_in_)