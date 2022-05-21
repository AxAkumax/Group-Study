import re

class Person:
    ppl_count = 0

    def __init__(self, usr):
        """Initializes Person class with username."""
        while usr.strip() == "":
            print("Invalid username.")
            usr = input("Enter username: ")
        
        self.usr = usr
        self.ppl_count += 1
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

        # self._schedule = Calendar() object?
        self._friend_list = []
        self._pending_reqs = []
        self._study_reqs = []
        self._updates = []   # list??

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
    
    def send_friend_reqs(self):
        pass

    #def send_
    

if __name__ == "__main__":
    user = input("Enter your email: ")
    p  = Person(user)


