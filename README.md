# Insurance Charge Predictions

Machine learning project to predict health insurance costs based on customer data  

### Problem
The objective is to predict insurance charges based on customer demographic data.  The dataset contains the following fields 

    age: age of primary beneficiary

    sex: insurance contractor gender, female, male

    bmi: Body mass index, providing an understanding of body, weights that are relatively high or low relative to height, objective index of body weight (kg / m ^ 2) using the ratio of height to weight, ideally 18.5 to 24.9

    children: Number of children covered by health insurance / Number of dependents

    smoker: Smoking

    region: the beneficiary's residential area in the US, northeast, southeast, southwest, northwest

The target variable is 'charges'.  

There are obvious real world advantages to being able to predict this kind of cost.  Medical charges and insurance costs can be hugely variable and predicting costs can be beneficial to company profits and customer charges.   

### Project Contents
- insurance.csv - dataset.  The original dataset comes from Kaggle and can be viewed here https://www.kaggle.com/code/mariapushkareva/medical-insurance-cost-with-linear-regression
- notebook.ipynb for EDA, training models and feature engineering.  I used several different models - Linear Regression, Lasso Regression, Ridge Regression, Decision Tree Regressor, Random Forest Regressor and XGBoost Regressor.  I selected the Decision Tree Regressor model for deployment as it produced the lowest RSME.
- train.py - python file for training the final model
- predict.py - deployment file for running the model as a web service
- Dockerfile - to run web service in a container
- Pipfile and Pipfile.lock to install dependencies to run predict service
- model.pkl and dv.bin - model and DictVectorizer files
- customer files with example customer data for testing the service

Running the web service in a virtual environment or docker container requires access to files in the repo.  To achieve this clone the repo first and run commands from insurance_charge_predictions directory. 

### Running notebook and train.py
The following libraries are required - pandas, numpy, matplotlib, scikit-learn==1.3.2, seaborn
```pip install pandas numpy matplotlib scikit-learn==1.3.2 seaborn```

Notebook can be viewed using nbviewer https://nbviewer.org/github/rlonglands/insurance_charge_predictions/blob/main/notebook.ipynb

### Running prediction locally as web service:
Use pipenv to create virtual environment and install dependencies - run commands inside insurance_charge_predictions directory.
1. If you don't have pipenv first run ```pip install pipenv```
2. To install dependencies ```pipenv install```
3. Run the service ```pipenv run waitress-serve --listen=0.0.0.0:9696 predict:app```
4. To use the service run the customer files from a new terminal while the service is running ```python customer1.py``` ```python customer2.py``` ```python customer3.py```

### Run web service in a docker container:
1. Docker needs to be installed and running.  Then run commands inside insurance_charge_predictions directory.
2. Build container ```docker build -t insurance_charge_predictions .```
3. Run container ```docker run -it -p 9696:9696 insurance_charge_predictions:latest```
4. To use the service run the customer files again.

### 




