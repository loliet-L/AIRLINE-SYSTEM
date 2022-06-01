
from flask import Flask , render_template , request
from  flask_mysqldb import MySQLdb

# mysql = MySQL()

app = Flask(__name__)
conn = MySQLdb.connect(host="localhost" , user = "root" , password = "Gaurav@2002" , db="airline_reservation_system")

# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'Gaurav@2002'
# app.config['MYSQL_DATABASE_DB'] = 'airline_reservation_system'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# mysql.init_app(app)

@app.route("/")
def signUpLogin():
    return render_template('signUpLogin.html')

@app.route("/",methods=['POST','GET'])
def register(): 
    
    name = str(request.form['name']) 
    email = str(request.form['email'])
    username = str(request.form['S_uname'])
    upass = str(request.form['S_pass'])
    uCpass = str(request.form['Cpass'])
    phone = str(request.form['phone'])
    
    cursor = conn.cursor()

    if ( (upass == uCpass) and (len(phone) == 10) ):        

        cursor.execute("INSERT INTO user_info (user_name, name ,email , password ,ph_no) VALUES (%s,%s,%s,%s,%s)" , (username,name , email , upass , phone))
        conn.commit()
        return "USER REGISTERED"
        
    else :
        return "PLEASE ENTER CORRECT DETAILS"

@app.route("/",methods=['POST','GET'])
def authentication():
    username = str(request.form['uname'])
    upass = str(request.form['pass'])

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM user_info WHERE user_name = '"+username+"' and password = '"+upass+"'")
    
    return "LOGIN SUCCESSFULL"
        


app.run(debug=True)  