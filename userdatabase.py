import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from Person import Person

cred = credentials.Certificate("./firebase1.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# def checkServer(p: Person):
#     doc_ref = db.collection(u'users').document(p.email).get()
#     doc_dict = doc_ref.to_dict()
#     print(doc_dict)
#     if p.email in doc_dict:
#         return True
#     else:
#         return False

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

def retrieveSchedule(p: Person):
    users_ref = db.collection(u'users').document(p.email)#.document(u'schedule')
    user = users_ref.get()
    user_dict = user.to_dict()
    print(user_dict['schedule'])

if __name__ == "__main__":
    p1 = Person("user1@gmail.com")
    p2 = Person("user2@gmail.com")

    addUser(p1)
    addUser(p2)

    #assert checkServer(p1), "p1 not found"

    print(f'{p1.email} checks the schedule of {p2.email}')
    

    retrieveSchedule(p1)
    retrieveSchedule(p2)
    
