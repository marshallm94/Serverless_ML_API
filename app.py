import os
import json
import pandas as pd
import numpy as np
from pickle import load

from flask import Flask, request, jsonify

app = Flask(__name__)
model_file = 'prod_model.joblib'
prod_model = load(open( model_file, 'rb' ))

@app.route('/')
def index():
    return 'you suck'

@app.route('/get_predictions/', methods=['POST'])
def predict(model=prod_model):
    if request.method == 'POST':
        data = json.loads( request.data )
        X = pd.read_json(data)
        predictions = np.array2string( model.predict(X) )
        return jsonify( predictions )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
    #app.run(debug=True)

