import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://project-ffc76-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "12305531":
        {
            "name": "Reena",
            "major": "ML",
            "starting_year": 2023,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "12305566":
        {
            "name": "Nikita Bisht",
            "major": "AI",
            "starting_year": 2023,
            "total_attendance": 12,
            "standing": "B",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "12313382":
        {
            "name": "Kishan Gangwar",
            "major": "Physics",
            "starting_year": 2023,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
        "12313402":
        {
            "name": "Anshika Kumari",
            "major": "DSA",
            "starting_year": 2023,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
        "12313937":
        {
            "name": "Priyanka Panigrahi",
            "major": "Data Science",
            "starting_year": 2023,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)