
from DB import ShowAllStudentRecord
from flask import Flask, jsonify, request, render_template


app = Flask(__name__)

@app.route("/")
def Welcome():
    return render_template("index.html")

@app.route("/students")
def ShowAllStudents():
    students = ShowAllStudentRecord()
    for student in students:
        return jsonify(student)


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)