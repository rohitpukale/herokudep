from flask import Flask, render_template,request
import joblib  
# initalizing the object of class 
app = Flask(__name__) 

loaded_model = joblib.load('dib_75.pkl')

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/predict', methods=['POST'])
def predict():
    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')

    preg = int(preg)
    plas = int(plas)
    pres = int(pres)
    skin = int(skin)
    test = int(test)
    mass = int(mass)
    pedi = int(pedi)
    age = int(age)
    

    print(preg,plas,pres,skin,test,mass,pedi,age)

    prediction = loaded_model.predict([[preg,plas,pres,skin,test,mass,pedi,age]])

    if prediction[0] ==1:
        result = 'Diabetic'
    else:
        result='not diabetic'
    
    return render_template('result.html', value=result)
    
if __name__ == '__main__' :
     app.run(debug=True)