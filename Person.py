import re

class Person:
    ppl_count = 0

    def __init__(self, usr):
        """Initializes Person class with username."""
        while usr.strip() == "":
            print("Invalid username.")
            usr = input("Enter username: ")
        self.usr = usr
        Person.ppl_count += 1

        # if person not in database:
        self.make_acc()

        # else:
        # self.retrieve_acc()

    def make_acc(self):
        """Creates account details."""
        self._pwd = input("Enter password: ")
        self.first_name = input("Enter first name: ")
        self.last_name = input("Enter last name: ")

        valid_email = "^[A-Za-z]+@[A-Za-z]+[.][A-Za-z]+$"
        email = input("Enter email: ")
        while not re.match(valid_email, email):
            print("Invalid email.")
            email = input("Enter email: ")
        self.email = email

        self.schedule = None #Calendar() object?
        self.friends_list = []
        self._pending_reqs = []
        self._study_reqs = []
        self._updates = []   # list??
        self.private = True

    def retrieve_acc(self): #, database
        pass
        # self._pwd =
        # self.first_name =
        # self.last_name =
        # self.email = 
        # self.schedule =
        # self.friends_list =
        # self._pending_reqs =
        # self._study_reqs =
        # self._updates =
        # self.private = 


    def change_privacy(self, new=None):
        """Allows user to change privacy"""
        if new == "private":
            self.private = True
        elif new == "public":
            self.private = False

    def send_friend_req(self, student):
        """Send friend request to desired friend."""
        # TRUE: self.usr not in student.friends_list
        if student.private:
            student._pending_reqs.append(self.usr)
        else:
            self.friends_list.append(student.usr)


    def send_study_req(self, student):
        
        # student.private == False or student in self.friends_list
        # check if times are free
        # send study req to friend
        student.

    def view_mutuals(self, friend:"Person"):
        return self.friends_list & friend.friends_list
    

if __name__ == "__main__":

    user = input("Enter your username: ")
    user1 = Person(user)
    print(user1.ppl_count)
    # make private

    user2 = Person(user)

