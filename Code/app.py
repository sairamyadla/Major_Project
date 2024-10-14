from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('Kidney.pkl', 'rb'))

@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        age = float(request.form['age'])
        bp = float(request.form['bp'])
        sg = float(request.form['sg'])
        al = float(request.form['al'])
        su = float(request.form['su'])
        rbc = float(request.form['rbc'])
        pc = float(request.form['pc'])
        pcc = float(request.form['pcc'])
        ba = float(request.form['ba'])
        bgr = float(request.form['bgr'])
        bu = float(request.form['bu'])
        sc = float(request.form['sc'])
        sod = float(request.form['sod'])
        pot = float(request.form['pot'])
        hemo = float(request.form['hemo'])
        wc = float(request.form['wc'])
        rc = float(request.form['rc'])
        htn = float(request.form['htn'])
        dm = float(request.form['dm'])
        cad = float(request.form['cad'])
        appet = float(request.form['appet'])
        pe = float(request.form['pe'])
        ane = float(request.form['ane'])

        values = np.array([[age, bp, sg, al, su, rbc, pc, pcc, ba, bgr, bu, sc, sod, pot, hemo, wc, rc, htn, dm, cad, appet, pe, ane]])
        prediction = model.predict(values)

        return render_template('result.html', prediction=prediction)

@app.route('/ckd_stage_calculator')
def ckd_stage_calculator():
    return render_template('ckd_stage_calculator.html')

if __name__ == "__main__":
    app.run(debug=True)
