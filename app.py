import numpy as np
import pickle
from flask import Flask, request, jsonify, render_template
import joblib  # For model loading

app = Flask(__name__)

# Load the trained model
model = pickle.load("Classifier.pkl")  # Replace with your model filename

@app.route("/predict", methods=["POST"])
def predict():
    # Get employee data from the request
    #data = request.get_json()   OPTIONAL

    # Preprocess the data (if necessary)
    # ... your preprocessing code ...

    # Make predictions
    #prediction = model.predict([data])[0]

    # Return the prediction as JSON
    #return jsonify({"promotion": prediction})

    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    final = ""
    #output = round(prediction[0], 2)
    output = prediction
    if output == 0:
      final = "Not Promoted"
    else:
      final = "Promoted"

    return render_template('index.html', prediction_text='Employee should be {}'.format(final))

if __name__ == "__main__":
    app.run(debug=True)  # Set debug=False for production