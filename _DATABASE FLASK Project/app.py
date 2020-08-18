from flask import Flask,render_template,request,redirect,url_for
from flask_mysqldb import MySQL

app=Flask(__name__) #referencing

#configure db
app.config['MYSQL_HOST']='localhost'            
app.config['MYSQL_USER']='root'                
app.config['MYSQL_PASSWORD']='Yuvan 27112000'   
app.config['MYSQL_DB']='dentalproject'          

mysql=MySQL(app)#instantiation

@app.route('/',methods=('GET','POST'))
def login():
    error=None
    if request.method=='POST':        
        if 'register' in request.form:
            return redirect(url_for('first'))
        elif request.form['login']!='admin' or request.form['password']!='admin':
            return redirect(url_for('invalid'))
        elif request.form['login']=='admin' and request.form['password']=='admin':
            return redirect(url_for('allvalues'))
    return render_template('Login.html')

 

@app.route('/invalid',methods=('GET','POST'))
def invalid():
    if request.method=='POST':
        return redirect(url_for('login'))
    return render_template('Invalid.html')

@app.route('/allvalues',methods=('GET','POST'))
def allvalues():
    cur=mysql.connection.cursor()
    result=cur.execute("SELECT * FROM dental")
    if result>0:
        userDetails=cur.fetchall()
    if "signin" in request.form:
        return redirect(url_for('login'))
    return render_template('users.html',userDetails=userDetails)
    

@app.route('/first',methods=('GET','POST'))
def first():
    if request.method=='POST':
        #first
        usersDetails=request.form
        pname=usersDetails['pname']
        birthdate=usersDetails['birthdate']
        age=usersDetails['age']
        gender=usersDetails['Gender']
        occupation=usersDetails['occupation']
        mobile=usersDetails['mobile']
        raddress=usersDetails['raddress']
        e_name=usersDetails['e_name']
        e_mobile=usersDetails['e_mobile']
        relation=usersDetails['relation']
        #second
        care=usersDetails['med1_']
        drugs=usersDetails['med2_']
        surgery=usersDetails['med3_']
        chest=usersDetails['med4_']
        #third
        bleed=usersDetails['med5']
        bldis=usersDetails['med6']
        odrugs=usersDetails['med7']
        smoke=usersDetails['smoke']
        ocondn=usersDetails['ocondn']
        #womenonly
        pregnant=usersDetails['women1']
        period=usersDetails['women2']
        pills=usersDetails['women3']
        #inserit"""
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO dental(pname,birthdate,age,gender,occupation,mobile,raddress,e_name,e_mobile,relation,care,drugs,surgery,chest,bleed,bldis,odrugs,smoke,ocondn,pregnant,period,pills) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(pname,birthdate,age,gender,occupation,mobile,raddress,e_name,e_mobile,relation,care,drugs,surgery,chest,bleed,bldis,odrugs,smoke,ocondn,pregnant,period,pills))
        #cur.execute("INSERT INTO firstpage(pname,birthdate) VALUES(%s,%s)",(pname,birthdate))
        mysql.connection.commit()                                                                                                                                                                                                                                   
        cur.close()
        return redirect(url_for('success'))
    return render_template('index.html')


@app.route('/success',methods=('GET','POST'))
def success():
    if request.method=='POST':
        if "home" in request.form:
            return redirect(url_for('login'))
        else:
            return redirect(url_for('first'))
    return render_template('Success.html')
    



if __name__=="__main__":
    app.run(debug=True)#if any errors they'll pop on the web page
     
     


"""
If you looking at this code, 
You must be either my teacher, my friend or a developer
Welcome to my easter egg


"Hello darkness, my old friend
I've come to talk with you again
Because a vision softly creeping
Left its seeds while I was sleeping
And the vision that was planted in my brain
Still remains
Within the sound of silence"
            -The Sound of Silence by Simon & Garfunkel, 1964

Subscribe me @7UV4N youtube


@app.route('/users')
def users():
    cur=mysql.connection.cursor()
    result=cur.execute("SELECT * FROM users")
    if result>0:
        userDetails=cur.fetchall()
        return render_template('users.html',userDetails=userDetails)
"""