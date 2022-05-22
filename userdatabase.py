import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from Person import Person

cred = credentials.Certificate("./firebase1.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

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

    retrieveSchedule(p1)
    retrieveSchedule(p2)
    
