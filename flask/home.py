import sqlite3

from flask import Flask,request,render_template,url_for,redirect




app=Flask(__name__)


@app.route('/')
def home():



    return render_template('home.html') 



@app.route('/submit', methods=['POST','GET'])
def submit():
    email = request.form['email']
    try :
        with sqlite3.connect('washwash.db') as data:
            cur = data.cursor()

            create = "CREATE TABLE IF NOT EXISTS MAILS (E_MAIL VARCHAR(30))"

            cur.execute(create)
            add= f"INSERT INTO DETAILS VALUES('{email}')"
            cur.execute(add)
            data.commit()
            cur.close()
            print("data added successfully")
    except:
        print("*************there is an error in the database connectivity*********************")


    return "Its Done"




if __name__ =="__main__":
    app.run(host="localhost",port=5000,debug=True)