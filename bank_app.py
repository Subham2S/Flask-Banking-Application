"""
This is a Banking Application to predict wherether any new person
seeking loans will default or NOT. This app takes the following
inputs to predict the result:
'income', 'debtinc', 'othdebt', 'employ', 'creddebt'
"""

import pickle
import pandas as pd
from flask import Flask, render_template, request

with open("RF_model_Banking_Application.pkl", "rb") as source:
    model = pickle.load(source)

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Defining the actions based on the "GET" and "POST" requests
    in the index.html
    """
    if request.method == "GET":
        return render_template("index.html")

    else:
        form_inputs = pd.DataFrame(request.form.to_dict(), index=[0])
        prediction = model.predict(form_inputs.astype(float))
        return str(prediction)  # form_inputs.to_html(),


if __name__ == "__main__":
    app.run(debug=True)
