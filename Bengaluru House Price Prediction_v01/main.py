from flask import Flask,render_template,request
from flask.wrappers import Request
import pandas as pd
import pickle


app=Flask(__name__)

data=pd.read_csv('Cleaned_data.csv')

pipe= pickle.load(open("model.pkl",'rb'))
@app.route('/')
def index():
    locations=sorted(data['location'].unique())
    return render_template('index.html',locations=locations)


@app.route('/predictioning',methods=['POST'])
def predict():
    location=request.form.get('location')
    bhk=request.form.get('bhk')
    bath=float(request.form.get('bath'))
    sqft=float(request.form.get('total_sqft'))
    
    print(location,bhk,bath,sqft)
    
    input =pd.DataFrame([[location,sqft,bath,bhk]],columns=['location','total_sqft','bath','bhk'])
    prediction=pipe.predict(input)[0]
    
    
    return str(prediction)

if __name__=="__main__":
    app.run(debug=True,port=5001)