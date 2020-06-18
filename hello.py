from flask import Flask
import pymysql
import os

host = os.environ["MYSQL_TEST_HOST"]
user = os.environ["MYSQL_TEST_USER"]
password = os.environ["MYSQL_TEST_PASSWORD"]
database = os.environ.get("MYSQL_TEST_DATABASE", "mysql")

db = pymysql.connect(host, user, password, database)

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World"


@app.route("/test_db/")
def show_db():
    cursor = db.cursor()
    cursor.execute("select * from db")
    db_result = cursor.fetchall()

    result = []
    for row in db_result:
        result.extend(list(row))

    return ",".join(result)


if __name__ == "__main__":
    app.run(port=5000, debug=True, host="0.0.0.0")
