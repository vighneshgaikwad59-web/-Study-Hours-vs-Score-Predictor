import tkinter as tk
from tkinter import messagebox
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

# ---------- load data & train model (runs once at startup) ----------
try:
    data = pd.read_csv("student.csv")
    x = data[["Hours"]]
    y = data[["Score"]]

    model = LinearRegression()
    model.fit(x, y)

    predicted_score = model.predict(x)
    mae = mean_absolute_error(y, predicted_score)
    mse = mean_squared_error(y, predicted_score)
    rmse = np.sqrt(mse)
except Exception as e:
    model = None
    mae = mse = rmse = None
    load_error = str(e)


# ---------- GUI logic ----------
def predict_score():
    if model is None:
        messagebox.showerror("Error", f"Could not load student.csv:\n{load_error}")
        return
    try:
        hours = float(hours_entry.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number of hours.")
        return

    prediction = model.predict([[hours]])[0][0]
    result_label.config(text=f"Predicted Score: {prediction:.2f}")


# ---------- build window ----------
root = tk.Tk()
root.title("Study Hours vs Score Predictor")
root.geometry("380x280")
root.resizable(False, False)

title_label = tk.Label(root, text="📚 Study Hours → Score Predictor", font=("Arial", 14, "bold"))
title_label.pack(pady=15)

input_frame = tk.Frame(root)
input_frame.pack(pady=5)

tk.Label(input_frame, text="Hours studied:", font=("Arial", 11)).grid(row=0, column=0, padx=5)
hours_entry = tk.Entry(input_frame, width=10, font=("Arial", 11))
hours_entry.grid(row=0, column=1, padx=5)

predict_btn = tk.Button(root, text="Predict Score", command=predict_score,
                         bg="#4CAF50", fg="white", font=("Arial", 11), padx=10, pady=5)
predict_btn.pack(pady=15)

result_label = tk.Label(root, text="Predicted Score: --", font=("Arial", 12, "bold"))
result_label.pack(pady=5)

if model is not None:
    metrics_text = f"MAE: {mae:.2f}   MSE: {mse:.2f}   RMSE: {rmse:.2f}"
else:
    metrics_text = "student.csv not found — predictions disabled"
metrics_label = tk.Label(root, text=metrics_text, font=("Arial", 9), fg="gray")
metrics_label.pack(pady=10)

root.mainloop()