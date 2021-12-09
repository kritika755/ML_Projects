from flask import Flask,render_template,request
import iris_model


app=Flask(__name__)


@app.route('/',methods=['GET','POST'])

def basic():
    
    if(request.method=='POST'): # get all the four attributes from our source
        sepal_length = request.form['sepallength']
        sepal_width = request.form['petalwidth']
        petal_length = request.form['petallength']
        petal_width = request.form['petalwidth']
        y_pred=[[sepal_length,sepal_width,petal_length,petal_width]]  #this variable act as the predicted value for input features.
        trained_model=iris_model.training_model()
        prediction_value= trained_model.predict(y_pred)
        
        
        setosa='setosa'
        versicolor='versicolor'
        virginica='virginica'
        
        if prediction_value==0:
            return render_template('index.html',setosa=setosa)
        elif prediction_value==1:
            return render_template('index.html',versicolor=versicolor)
        else : 
            return render_template('index.html',virginica=virginica)
        
        #return render_template('index.html',prediction_value=prediction_value) #prediction value is passed in jinja2 template for displaying
    return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True)
    