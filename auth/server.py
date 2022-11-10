import os
from flask import Flask, request
from flask_mysqldb import MySQL
from helpers import createJWT, decodeJWT


app = Flask(__name__)
mysql = MySQL(app)

# set configuration
app.config["MYSQL_HOST"] = os.environ.get("MYSQL_HOST")
app.config["MYSQL_USER"] = os.environ.get("MYSQL_USER")
app.config["MYSQL_PASSWORD"] = os.environ.get("MYSQL_HOST")
app.config["MYSQL_DB"] = os.environ.get("MYSQL_DB")
app.config["MYSQL_PORT"] = os.environ.get("MYSQL_PORT")


# create api route

@app.route("/login", methods = "POST")
def login():
    auth = request.authorization
    if not auth:
        return "missing credentials", 401
    
    cur = mysql.connection.cursor()
    res = cur.execute("SELECT email, password FROM users WHERE email =%s",(auth.username))

    if res > 0:
        user_row = res.fetchone
        email = user_row[0]
        password = user_row[1]

        if email != auth.username or password != auth.password:
            return "invalid creadentials", 401
        return createJWT(auth.username, os.environ.get('JWT_SECRET'), True)
    else:
        return "invalid credentials",401

@app.route('/validate-jwtoken', methods='POST')
def validateJWT():
    encodeJWT = request.headers['Authorization']

    if not encodeJWT:
        return "missing credentials", 401
    
    encodeJWT = encodeJWT.split(" ")[1]
    decoded = decodeJWT(encodeJWT, os.environ.get('JWT_SECRET'))

    return decoded, 200

# start web server

if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 5000)

