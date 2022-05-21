import re

class Person:
    # ppl_count = 0 <-- move somewhere else

    def __init__(self, usr):
        """Initializes Person class with username."""
        while usr.strip() == "":
            print("Invalid username.")
            usr = input("Enter username: ")
        
        self.usr = usr
        # self.ppl_count += 1 <-- move somewhere else
        self.make_acc()

    def make_acc(self):
        """Creates account details."""
        self.pwd = input("Enter password: ")
        self.first_name = input("Enter first name: ")
        self.last_name = input("Enter last name: ")

        valid_email = "^[A-Za-z]+@[A-Za-z]+[.][A-Za-z]+$"
        email = input("Enter email: ")
        while not re.match(valid_email, email):
            print("Invalid email.")
            email = input("Enter email: ")
        self.email = email

        self._schedule = None #Calendar() object?
        self._friend_list = set()
        self._pending_reqs = []
        self._study_reqs = []
        self._updates = []   # list??
        self._private = True

    def view_friends(self):
        """Displays current friends."""
        return self._friend_list
    
    def view_friend_reqs(self):
        """Displays pending friend requests."""
        return self._pending_reqs

    def view_study_reqs(self):
        return self._study_reqs

    def view_updates(self):
        """Displays all new updates (all requests)."""
        return self._updates
    
    def get_privacy(self):
        return self._private

    def change_privacy(self, new=None):
        if new == "private":
            self._private = True
        elif new == "public":
            self._private = False

    def send_friend_req(self, friend):
        # send request to friend 
        pass

    def send_study_req(self, friend):
        # friend.get_privacy == False
        # check if times are free
        # send study req to friend
        pass

    def view_mutuals(self, friend:"Person"):
        return self._friend_list & friend._friend_list
    

if __name__ == "__main__":

    user = input("Enter your username: ")
    p  = Person(user)
    z = Person("heee")

    print(p.__dict__)

