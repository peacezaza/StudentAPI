
from DB import ShowAllStudentRecord
from flask import Flask, jsonify, request, render_template


app = Flask(__name__)

@app.route("/")
def Welcome():
    return render_template("index.html")

@app.route("/students")
def ShowAllStudents():
    students = ShowAllStudentRecord()
    studentsList = []
    for student in students:
        studentsList.append(student)

    return jsonify({"studentsList": studentsList})

@app.route("/students/<std_id>")
def ShowStudent(std_id):
    students = ShowAllStudentRecord()
    for student in students:
        stdID = student.get('_id')
        if stdID == std_id:
            return jsonify(student)



if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)