# 📦 supply-chain-demand-forecasting

Predicting weekly product demand using machine learning models and historical retail supply chain data.

---

## 🔍 Overview

This project applies machine learning to forecast product demand using historical supply chain data. Using publicly available inventory data, the objective of the project is to build predictive models that improve demand precision, leading to more informed decision making.
---

## Data Source

[Grupo Bimbo Inventory Demand](https://www.kaggle.com/competitions/grupo-bimbo-inventory-demand)

Due to the size of the datatset, 10,000 random rows were pulled from the dataset and used for this project.

## 📊 Modeling Results

| Metric         | Linear Regression | Random Forest Regressor | Gradient Boosting Regressor | Notes |
|----------------|--------------------|--------------------------|------------------------------|-------|
| **R² Score**   | 0.9662             | 0.9603                   | 0.9658                       | All models performed very well, but Linear Regression slightly outperformed the others |
| **MAE**        | $0.12              | $0.10                    | $0.11                        | Random Forest had the lowest average error, but difference is marginal |
| **RMSE**       | $2.33              | $2.53                    | $2.34                        | Gradient Boosting had slightly higher RMSE than Linear Regression |

## Virtual Environment Setup and Pushing to Github

#### I opened the project in VS Code

#### I added a .gitignore file

#### I added a requirements.txt file

#### I created a virtual environment using the code below

```shell
py -m venv .venv
.venv\Scripts\Activate

```

## Install packages in Virtual Envvironment

#### The code below installs pandas in the requirements.txt file
```shell

pip install pandas
python -m pip freeze > requirements.txt

```

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