import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from Person import Person

cred = credentials.Certificate("./firebase1.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def checkServer(email:str):
    doc_ref = db.collection(u'users').document(email).get()
    return doc_ref.exists

def addUser(p: Person):
    doc_ref = db.collection(u'users').document(p.email)
    doc_ref.set({
            u'email': p.email,
            u'password': p._pwd,
            u'first name': p.first_name,
            u'last name': p.last_name,
            u'private': p.private,
            u'schedule': p.schedule,
            #u'friends list': p.friends_list,
            u'study list': p.study_list,
            #u'incoming reqs': p.get_incoming(),
            #u'outgoing reqs': p.get_outgoing(),
        })

def retrieveSchedule(email:str):
    users_ref = db.collection(u'users').document(email)#.document(u'schedule')
    user = users_ref.get()
    user_dict = user.to_dict()
    print(user_dict['schedule'])

if __name__ == "__main__":
    p1 = Person("user1@gmail.com")
    p2 = Person("user2@gmail.com")

    addUser(p1)
    addUser(p2)

    print(f'{p1.email} checks the schedule of {p2.email}')
    
    friend = input("Enter the email of the student you'd like to study with: ")
    if checkServer(friend):
        retrieveSchedule(friend)
    else:
        print(f"Error: student with email {friend} not found")
    
