from flask import Flask,render_template,request,redirect
import pickle
import numpy as np
from flask_mysqldb import MySQL

app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

app.config['MYSQL_HOST'] = 'Localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'dataset'
mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Type_form', methods=['GET', 'POST'])
def Type_form():
    return render_template('Type.html')

@app.route('/Health_form', methods=['GET', 'POST'])
def Health_form():
    return render_template('Health.html')

@app.route('/Visualization_form', methods=['GET', 'POST'])
def Visualization_form():
    return render_template('Visualization.html')

@app.route('/Qc_form', methods=['GET', 'POST'])
def Qc_form():
    if request.method=='POST':
        odor=int(request.values['odor'])
        spore_print_color=int(request.values['spore-print-color'])
        gill_color=int(request.values['gill-color'])
        ring_type=int(request.values['ring-type'])
        stalk_surface_above_ring=int(request.values['stalk-surface-above-ring'])
        stalk_surface_below_ring=int(request.values['stalk-surface-below-ring'])
        gill_size=int(request.values['gill-size'])
        stalk_color_above_ring=int(request.values['stalk-color-above-ring'])
        stalk_color_below_ring=int(request.values['stalk-color-below-ring'])
        bruises=int(request.values['bruises'])
        population=int(request.values['population'])
        habitat=int(request.values['habitat'])
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO mushroomsdb (odor, spore_print_color, gill_color, ring_type, stalk_surface_above_ring, stalk_surface_below_ring, gill_size, stalk_color_above_ring, stalk_color_below_ring, bruises, population, habitat) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",(odor, spore_print_color, gill_color, ring_type, stalk_surface_above_ring, stalk_surface_below_ring, gill_size, stalk_color_above_ring, stalk_color_below_ring, bruises, population, habitat))
        mysql.connection.commit()
        cur.close()
        return redirect ('/predict')
    return render_template('home.html')

@app.route('/values',methods=['GET','POST'])
def values():
    cur = mysql.connection.cursor() 
    cur.execute("SELECT * FROM mushroomsdb;")
    details = cur.fetchall()
    return render_template('values.html',details=details)


@app.route('/predict',methods=['GET','POST'])
def predict():
    cur = mysql.connection.cursor()
    
    cur.execute("SELECT odor, spore_print_color, gill_color, ring_type, stalk_surface_above_ring, stalk_surface_below_ring, gill_size, stalk_color_above_ring, stalk_color_below_ring, bruises, population, habitat FROM mushroomsdb WHERE id=(SELECT MAX(id) FROM mushroomsdb);")
    to_predict_list = cur.fetchall()
    result = model.predict(to_predict_list)
    return render_template('result.html',prediction_text="Mushroom is {}".format(result), x=to_predict_list)
    
if __name__ == "__main__":   
    app.run()