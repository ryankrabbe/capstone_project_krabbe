# 📦 supply-chain-demand-forecasting

Predicting weekly product demand using machine learning models and historical retail supply chain data.

---

## 🔍 Overview

This project applies machine learning to forecast product demand using historical supply chain data. Using publicly available inventory data, the objective of the project is to build predictive models that improve demand precision, leading to more informed decision making.
---

## 📁 Project Structure

```
supply-chain-demand-forecasting/
├── data/ # Sample of cleaned dataset (if shared)
├── figures/ # Visualizations (e.g., actual vs predicted, residuals)
├── modeling.ipynb # Jupyter notebook with modeling pipeline
├── README.md # Project documentation
├── requirements.txt # Python dependencies
└── .gitignore # Files excluded from version control
```

---

## 📊 Modeling Summary

Three models were trained and evaluated:
- **Linear Regression**
- **Random Forest**
- **Gradient Boosting**

**Evaluation Metrics:**

| Metric         | Linear Regression | Random Forest Regressor | Gradient Boosting Regressor | Notes |
|----------------|--------------------|--------------------------|------------------------------|-------|
| **R² Score**   | 0.9662             | 0.9603                   | 0.9658                       | Linear Regression slightly outperformed the other models |
| **MAE**        | $0.12              | $0.10                    | $0.11                        | Random Forest had the lowest average error between the models |
| **RMSE**       | $2.33              | $2.53                    | $2.34                        | Gradient Boosting performed similiary to Linear Regression, but had slightly higher RMSE |

---

## 📂 Data Source

Dataset: [Grupo Bimbo Inventory Demand](https://www.kaggle.com/competitions/grupo-bimbo-inventory-demand)  
Due to file size, a random sample of 10,000 rows was used for modeling.

---

## 📈 Key Visualizations

- Feature Importance
- Actual vs. Predicted (Gradient Boosting)
- Residual Distribution Plot
- Bar Charts Comparing Model Metrics (R², MAE, RMSE)

All visualizations are available in the final report.

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/ryankrabbe/supply-chain-demand-forecasting.git
cd supply-chain-demand-forecasting

```

### 2. Create and Activate Virtual Environment

```shell
py -m venv .venv
.venv\Scripts\Activate

```

### 3. Install Dependencies

```shell

pip install pandas
python -m pip freeze > requirements.txt

```

### 4. Push Changes to Github

## Git add my recent changes to my github
```shell

Git add .

```

## Git commit my recent changes to my github

```shell

git commit -m "Start New Project"

```

## Push recent changes to my github

```shell

git push origin main

```

🧠 Technologies Used
Python (Pandas, Scikit-learn, Matplotlib, Seaborn)

Jupyter Notebook

Git & GitHub

Overleaf (LaTeX)

📄 Final Report
The full modeling process and conclusions are documented in the final report:
📘 [Overleaf Report](https://www.overleaf.com/read/wkkcscvjcjfb#fc399e)