<h1 align="center">
  Credit Card Default Prediction System
</h1>

<h3 align="center">
    A System which is trained to lower the Frauds in Credit Cards. 
</h3>

# Project Title
Credit Card Defaulter classification

## ✨ Overview!

- A High Performing Credit Card Default Predicted with over 91.88975 score. 
- Extensively Fine tuned state of the art machine learning models. 
- Extensively done Data Processing, Ingestion, Feature Engineering 
- Built the state of the art models using StackNet, TabNet.

# About the Dataset
In recent years, the credit card issuers in Taiwan faced the cash and credit card debt crisis and the delinquency is expected to peak in the third quarter of 2006 (Chou,2006). In order to increase market share, card-issuing banks in Taiwan over-issued cash and credit cards to unqualified applicants. At the same time, most cardholders, irrespective of their repayment ability, overused credit card for consumption and accumulated heavy credit and cash–card debts. The crisis caused the blow to consumer finance confidence and it is a big challenge for both banks and cardholders



# Dataset
We used the [Credit Card Default payment in Taiwan] (https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients) to predict whether the credit card holders are defaulters or Non-defaulters. The Dataset and its attributes are described below


1. ID: ID of each client 
2. LIMIT_BAL: Amount of given credit in NT dollars (includes individual and family/supplementary credit
3. SEX: Gender (1=male, 2=female)
4. EDUCATION: (1=graduate school, 2=university, 3=high school, 4=others, 5=unknown, 6=unknown)
5. MARRIAGE: Marital status (1=married, 2=single, 3=others)
6. AGE: Age in years
7. PAY_0: Repayment status in September, 2005 (-1=pay duly, 1=payment delay for one month, 2=payment delay for two months,8=payment delay for eight months, 9=payment delay for nine months and above)
8. PAY_2: Repayment status in August, 2005 (scale same as above)
9. PAY_3: Repayment status in July, 2005 (scale same as above)
10. PAY_4: Repayment status in June, 2005 (scale same as above)
11. PAY_5: Repayment status in May, 2005 (scale same as above)
12. PAY_6: Repayment status in April, 2005 (scale same as above)
13. BILL_AMT1: Amount of bill statement in September, 2005 (NT dollar)
14. BILL_AMT2: Amount of bill statement in August, 2005 (NT dollar)
15. BILL_AMT3: Amount of bill statement in July, 2005 (NT dollar)
16. BILL_AMT4: Amount of bill statement in June, 2005 (NT dollar)
17. BILL_AMT5: Amount of bill statement in May, 2005 (NT dollar)
18. BILL_AMT6: Amount of bill statement in April, 2005 (NT dollar)
19. PAY_AMT1: Amount of previous payment in September, 2005 (NT dollar)
20. PAY_AMT2: Amount of previous payment in August, 2005 (NT dollar)
21. PAY_AMT3: Amount of previous payment in July, 2005 (NT dollar)
22. PAY_AMT4: Amount of previous payment in June, 2005 (NT dollar)
23. PAY_AMT5: Amount of previous payment in May, 2005 (NT dollar)
24. PAY_AMT6: Amount of previous payment in April, 2005 (NT dollar)
25. default.payment.next.month: Default payment (1=yes, 0=no)


## Requirements

- Python [3.7 or above] - https://www.python.org/downloads/
- Git - https://git-scm.com/download/
- Pipenv [Python package for virtual envs] - Install it using `pip install pipenv` 
- sklearn 
- pandas 
- numpy 
- pytorch-tabnet
- stacknet

## Project and code structure information

- src 
   - data_ingestion :- Ingestion of the data and some data utilities classes. 
   - validate_data:- Dataset development and outlier detection classes.
   - process_data:- data_cleaning, handling imbalanced_data, imputation of missing values, scaling numerical features and etc. 
   - feature_engineering:- Feature addition, interaction terms, mean encoding of the categorical features.
   - model_dev:- developed high performing models, trained on gpu's, hyperparametric optimization using optuna. 
   - evaluate_models:- evaluation of models on various metric such as precision, recall, AUC and ROC Curve and etc. 
   - TabNet, Autoencoder:- Deep Learning Models 

## 🙌 Show your support

Be sure to leave a ⭐️ if you like the project!

<div align="center">Made by Kritika Banerjee with ❤</div>
