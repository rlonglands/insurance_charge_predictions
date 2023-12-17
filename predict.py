import pickle
from flask import Flask
from flask import request
from flask import jsonify
import numpy as np

model_file = 'model.pkl'
dv_file = 'dv.bin'
with open (model_file, 'rb') as f_in:
    model = pickle.load(f_in)
with open (dv_file, 'rb') as f_in:
   dv = pickle.load(f_in) 

app = Flask('predict')

@app.route('/predict', methods=['POST'])

def predict():
    customer = request.get_json()
    X = dv.transform([customer])
    y_pred = model.predict(X)
    charge  = np.expm1(y_pred)

    result = {
        'predicted_charges': float(charge)
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug = True, host = '0.0.0.0', port=1234)



