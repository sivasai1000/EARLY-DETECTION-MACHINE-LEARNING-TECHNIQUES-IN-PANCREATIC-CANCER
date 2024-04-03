from flask import Flask, render_template, request
import numpy as np
import pickle
model = pickle.load(open(r"C:\Users\sivas\OneDrive\Desktop\New folder\panreatic cancer detection\flask\panc.pkl", 'rb'))
app = Flask(__name__)
@app.route("/")
def about():
    return render_template('home.html')
@app.route("/home")
def about1():
    return render_template('home.html')
@app.route("/predict")
def home1():
    return render_template('predict.html')

@app.route("/performance_analysis")
def performance_analysis():
    return render_template('Performance_analysis.html')
@app.route("/Abouting")
def aboutuss():
    return render_template('aboutuss.html')
@app.route("/pred", methods=['POST', 'GET'])
def predict():
    x = [[x for x in request.form.values()]]
    print(x)

    x = np.array(x)
    print(x.shape)

    print(x)
    pred = model.predict(x)
    if pred == 0:
        pred = 'Healthy'
    elif pred == 1:
        pred = 'Healthy'
    else:
        pred = 'Pancreas Cancer Detected'
    return render_template('submit.html', prediction_text=str(pred))
if __name__ == "__main__":
    app.run(debug=True)
