from flask import Flask, request
from flask_mysqldb import MySQL



app = Flask(__name__)

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'tiger'
app.config['MYSQL_DB'] = 'HoloST'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


# init MySQL
mysql = MySQL(app)


@app.route('/qrcode',methods=['GET','POST'])
def qrcode():
    JSO = request.get_json() or request.args
    qrcode = JSO['qrcode']
    cur = mysql.connection.cursor()

    # Execute query
    cur.execute('INSERT INTO qrcode(qrcode) VALUES(%s)',[qrcode])

    # Commit DB
    mysql.connection.commit()

     # Close connection
    cur.close()

    return 'success'



if __name__ == ('__main__'):
    app.secret_key = 'secret1234'
    app.run(debug=True, host='0.0.0.0', port=8000)
