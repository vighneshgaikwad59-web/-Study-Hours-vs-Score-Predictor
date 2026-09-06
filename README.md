# 📚 Study Hours vs Score Predictor

A simple **Linear Regression** project that predicts a student's exam score based on the number of hours they studied.

## 🧠 What it does

- Loads student study-hours and score data from `student.csv`
- Trains a `LinearRegression` model from scikit-learn on `Hours → Score`
- Predicts scores for the existing dataset and evaluates the model
- Takes a new "hours studied" input from the user and predicts their score

## 📊 Evaluation Metrics

| Metric | Description |
|--------|-------------|
| **MAE** (Mean Absolute Error) | Average absolute difference between actual and predicted scores |
| **MSE** (Mean Squared Error) | Average squared difference — penalizes larger errors more |
| **RMSE** (Root Mean Squared Error) | Square root of MSE — back in the original score units |

## 🗂️ Project Structure

```
study-hours-score-predictor/
├── predictor.py
├── student.csv
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Setup & Run

```bash
# clone the repo
git clone https://github.com/vighneshgaikwad59-web/study-hours-score-predictor.git
cd study-hours-score-predictor

# install dependencies
pip install -r requirements.txt

# run the script
python predictor.py
```

## 📄 Dataset Format (`student.csv`)

| Hours | Score |
|-------|-------|
| 2.5   | 21    |
| 5.1   | 47    |
| ...   | ...   |

## 🚀 Example Output

```
Predicted Scores: [...]
Mean Absolute Error: ...
Mean Squared Error: ...
Root Mean Squared Error: ...
Enter the number of hours studied: 6
Prediction for 6.0 hours of study is [[...]]
```

## 🔧 Tech Stack

- Python
- pandas
- scikit-learn
- NumPy

---
Built as part of a bioinformatics-to-data-science portfolio 🧬📈
