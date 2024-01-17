from pymongo.mongo_client import MongoClient

def LoginDB():
    url = "mongodb+srv://kanisorn:1234@cluster0.4swyaig.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(url)
    client.admin.command('ping')
    db = client["students"]
    collection = db["std_info"]
    return db,collection

def ShowAllStudentRecord():
    db, collection = LoginDB()
    all_students = collection.find()
    return all_students

def AddStudentRecord(id, name, major, gpa):
    db, collection = LoginDB()
    try:
        collection.insert_one({"_id": id,
                               "fullname": name,
                               "major": major,
                               "gpa": gpa
                               })
    except Exception as e:
        print(e)

def UpdateStudentRecord(oldID, newID, newFullName, newMajor, newGPA):
    db, collection = LoginDB()
    try:
        collection.update_one(
            {"_id": oldID},
            {"$set": {
                "fullname": newFullName,
                "major": newMajor,
                "gpa": newGPA}}
        )
    except Exception as e:
        print(e)

def DeleteStudentRecord(id):
    db, collection = LoginDB()
    try:
        collection.delete_one(
            {"_id": id}
        )
    except Exception as e:
        print(e)

all_student = ShowAllStudentRecord()
