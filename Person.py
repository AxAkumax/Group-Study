import re

class Person:
    num_ppl = 0

    def __init__(self, usr:str):
        """Initializes Person class."""
        while usr.strip() == "":
            print("Invalid username.")
            usr = input("Enter username: ")
        self.usr = usr
        Person.num_ppl += 1

        # Setup default account information
        self.schedule = None # <--- Calendar() object?
        self.friends_list = []
        self.study_list = []
        self._incoming_reqs = {"Friends": [], "Study Rooms": []}
        self._outgoing_reqs = {"Friends": [], "Study Rooms": []}
        self.private = True

        # if person not in database:
        self.make_acc()

        # else:
        # self.load_acc()

    def make_acc(self):
        """Creates account details."""
        # Create password
        pwd = input("Enter password (8-24 chars): ")
        while not len(pwd) in range(8,25) or " " in pwd:
            print("Invalid password.")
            pwd = input("Enter password (8-24 chars): ")
        self._pwd = pwd

        # Create first name
        valid_name = "^(([A-Za-z]+)|[A-Za-z]+[-| ][A-za-z]+)$"
        first_name = input("Enter first name: ")
        while not re.match(valid_name, first_name):
            print("Invalid first name.")
            first_name = input("Enter first name: ")
        self.first_name = first_name

        # Create last name
        last_name = input("Enter last name: ")
        while not re.match(valid_name, last_name):
            print("Invalid last name.")
            first_name = input("Enter last name: ")
        self.last_name = last_name

        # Create email address
        valid_email = "^[A-Za-z]+@[A-Za-z]+[.][A-Za-z]+$"
        email = input("Enter email: ")
        while not re.match(valid_email, email):
            print("Invalid email.")
            email = input("Enter email: ")
        self.email = email

        # TO DO: Add information to the larger database

    def load_acc(self): #, database
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

    def change_privacy(self, private=None):
        """Allows user to change account privacy."""
        if private != None:
            self.private = private
        

    def add_friend(self, student:"Person"):
        """Allows user to add another student as friend or send them a friend request."""
        if student.private:
            self._outgoing_reqs["Friends"].append(student)
            student._incoming_reqs["Friends"].append(self)
        else:
            self.friends_list.append(student)
            student.friends_list.append(self)

    def acc_or_rej(self, student:"Person", accept:bool):
        """Allows private user to accept or reject another student as friend."""
        self._incoming_reqs["Friends"].remove(student)
        student._outgoing_reqs["Friends"].remove(student)
        
        if accept == True:
            self.friends_list.append(student)
            student.friends_list.append(self)
        elif accept == False:
            self._outgoing_reqs["Friends"].remove(student)
    

    def send_study_req(self, student:"Person"):
        """Allows user to send another student a study request."""
        if student.private and student not in self.friends_list:
            print(f"{student.usr} is a private account.")
            return

        else:
            # if times are free:
            self._outgoing_reqs["Study Rooms"].append(student)
            student._incoming_reqs["Study Rooms"].append(self)
            # else:
            # print(f"{student.usr} is not available the same time that you are."}
            # return


    def view_mutuals(self, friend:"Person"):
        mutuals = set(self.friends_list) & set(friend.friends_list)
        return list(mutuals)
    

if __name__ == "__main__":

    def show_info(user):
        print(f"INFO ABOUT {user.usr}")
        print("PRIVACY", user.private)
        print("FRIENDS", user.friends_list)
        print("STUDY LIST", user.study_list)
        print("INCOMING REQS")
        for i in user._incoming_reqs:
            print(i, user._incoming_reqs[i])
        print("OUTGOING REQS")
        for i in user._outgoing_reqs:
            print(i, user._outgoing_reqs[i])

    
    user_1 = input("Enter your username: ")
    user1 = Person(user_1)
    
    print(f"{user1.usr} becomes public.")
    user1.change_privacy(private=False)

    user_2 = input("Enter your username: ")
    user2 = Person(user_2) # user2 is private

    show_info(user1)
    print()
    show_info(user2)
    print()

    print(f"{user1.usr} wants to be friends with {user2.usr}")
    if user1 not in user2.friends_list:
        user1.add_friend(user2)
    print("USER1", user1._outgoing_reqs)
    print()
    print("USER2", user2._incoming_reqs)
    print()

    print(f"{user2.usr} accepts {user1.usr}'s friend request.")
    user2.acc_or_rej(user1, True)

    print("USER1", user1._incoming_reqs, user1._outgoing_reqs)
    print()
    print("USER2", user2._incoming_reqs, user2._outgoing_reqs, )
    print()

    print("USER1", user1.friends_list)
    print()
    print("USER2", user2.friends_list)
    print()







