
from DB import ShowAllStudentRecord
from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route("/")
def hello_world():
    all_students = ShowAllStudentRecord()
    for std in all_students:
        print(std)
    return "Hello World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)