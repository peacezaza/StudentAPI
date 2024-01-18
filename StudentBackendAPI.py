

from DB import ShowAllStudentRecord, AddStudentRecord, FindStudentRecord, UpdateStudentRecord, DeleteStudentRecord
from flask import Flask, jsonify, request, render_template
from flask_basicauth import BasicAuth


app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME']='username'
app.config['BASIC_AUTH_PASSWORD']='password'
basic_auth = BasicAuth(app)

@app.route("/")
def Welcome():
    return render_template("index.html")


@app.route("/students")
@basic_auth.required
def ShowAllStudents():
    students = ShowAllStudentRecord()
    studentsList = []
    for student in students:
        studentsList.append(student)

    return jsonify({"studentsList": studentsList})


@app.route("/students/<std_id>")
@basic_auth.required
def ShowStudent(std_id):
    if FindStudentRecord(std_id) == None:
        return jsonify({"error": "Student not found"}), 404
    else:
        return jsonify(FindStudentRecord(std_id))


@app.route("/students", methods=["POST"])
@basic_auth.required
def AddStudent():
    data = request.get_json()
    ID = data.get('_id')
    name = data.get('fullname')
    major = data.get('major')
    GPA = data.get('gpa')


    if FindStudentRecord(ID) == None:
        AddStudentRecord(ID, name, major, GPA)
        return jsonify(FindStudentRecord(ID))
    else:
        return jsonify({"error": "Cannot create new student"}, 500)

@app.route("/students/<std_id>", methods=["DELETE"])
@basic_auth.required
def DeleteStudent(std_id):
    if FindStudentRecord(std_id) == None:
        return jsonify({"error": "Student not found"}), 404
    else:
        DeleteStudentRecord(std_id)
        return jsonify({"message":"Student deleted successfully"}), 200


@app.route("/students/<std_id>", methods=["PUT"])
@basic_auth.required
def UpdateStudent(std_id):
    data = request.get_json()
    name = data.get('fullname')
    major = data.get('major')
    GPA = data.get('gpa')

    if FindStudentRecord(std_id) == None:
        return jsonify({"error": "Cannot update student"}), 404
    else:
        UpdateStudentRecord(std_id, name, major, GPA)
        return jsonify(FindStudentRecord(std_id))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
