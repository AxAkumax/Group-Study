import re
import userdatabase as user_db

class Person:
    num_users = 0

    def __init__(self, usr: str, create_acc:bool) -> None: # usr:str) -> None:
        """Initializes student's account information. Email functions as username."""
        # Setup default account information
        self.private = True # acc is private by default
        self._schedule = None # <--- Calendar() object? visible to others if public
        self.friends_list = []
        self.study_list = [] # ???

        if create_acc:
            self._make_acc()
        else:
            self._load_acc()
        
        # while usr.strip() == "":
            # print("Invalid username.")
            # usr = input("Enter username: ")
        # self._usr = usr

        Person.num_users += 1

        # move to database . . . ?
        self._incoming_reqs = {"Friends": [], "Study Rooms": []}
        self._outgoing_reqs = {"Friends": [], "Study Rooms": []}

    def _make_acc(self) -> None:
        """Creates account details."""
        # Create email address
        valid_email = "^[A-Za-z]+@[A-Za-z]+[.][A-Za-z]+$"
        email = input("Enter email: ")
        while not re.match(valid_email, email):
            print("Invalid email.")
            email = input("Enter email: ")
        
        # Verify email is not already in server
            # if email in server:
                # print(f"{email} is already in use.")
        self.email = email

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

        # Add student account to the larger database


    def _load_acc(self) -> None: #, database):
        pass
        # if email not in database:
        # print("Email not found.")

        # else:
            # pwd = input("Enter password: ")
            # while input pwd != pwd in database:
                # print("Incorrect password.")
                # pwd = input("Enter password: ")
            
            # self.email = 
            # self._pwd = 
            # self.first_name =
            # self.last_name =

            # self.private = 
            # self._schedule =
            # self.friends_list =
            # self.study_list =

            # self._incoming_reqs = 
            # self._outgoing_reqs =
    
    def get_email(self) -> str:
        """Returns student's email address."""
        return self.email
    
    def get_schedule(self) -> str:
        """Returns student's schedule."""
        return self._schedule

    def get_friends_list(self) -> list:
        return self.friends_list

    def get_incoming(self) -> dict:
        """Returns student's incoming requests."""
        return self._incoming_reqs

    def get_outgoing(self) -> dict:
        """Returns student's outgoing requests."""
        return self._outgoing_reqs

    def change_privacy(self, private=None) -> None:
        """Allows user to change account privacy."""
        if private != None:
            self.private = private
        
    def add_friend(self, student:"Person") -> None:
        """Allows user to add another student as friend or send them a friend request."""
        if student.private:
            self._outgoing_reqs["Friends"].append(student)
            student._incoming_reqs["Friends"].append(self)
        else:
            self.friends_list.append(student)
            student.friends_list.append(self)

    def acc_or_rej(self, student:"Person", accept:bool) -> None:
        """Allows private user to accept or reject another student as friend."""
        self._incoming_reqs["Friends"].remove(student)
        student._outgoing_reqs["Friends"].remove(student)

        if accept == True:
            self.friends_list.append(student)
            student.friends_list.append(self)
        elif accept == False:
            self._outgoing_reqs["Friends"].remove(student)
    

    def send_study_req(self, student:"Person") -> None:
        """Allows user to send another student a study request."""
        if student.private and student not in self.friends_list:
            print(f"{student.get_email()} is a private account.")
            return

        else:
            # if times are free:
            self._outgoing_reqs["Study Rooms"].append(student)
            student._incoming_reqs["Study Rooms"].append(self)
            # else:
                # print(f"{student.usr} is not available the same time that you are."}
                # return


    def view_mutuals(self, friend:"Person") -> list: # shows automatically if user is private
        """Displays the same """
        if not friend.private:
            return list(set(self.friends_list) & set(friend.friends_list))
        # else:
        # print(f"{student.usr} is private."}
        # return
    

if __name__ == "__main__":

    def show_info(user:Person) -> None:
        print(f"INFO ABOUT {user.get_email()}")
        print("PRIVACY", user.private)
        print("FRIENDS", user.get_friends_list())
        print("STUDY LIST", user.study_list)
        print("INCOMING REQS")
        for i in user.get_incoming():
            print(i, user.get_incoming()[i])
        print("OUTGOING REQS")
        for i in user.get_outgoing():
            print(i, user.get_outgoing()[i])
    
    user_1 = input("Enter your username: ")
    user1 = Person(user_1)
    
    print(f"{user1.get_email()} becomes public.")
    user1.change_privacy(private=False)

    user_2 = input("Enter your username: ")
    user2 = Person(user_2) # user2 is private

    show_info(user1)
    print()
    show_info(user2)
    print()

    print(f"{user1.get_email()} wants to be friends with {user2.get_email()}")
    if user1 not in user2.get_friends_list():
        user1.add_friend(user2)
    print("USER1", user1.get_incoming(), user2.get_outgoing())
    print()
    print("USER2", user2.get_incoming(), user2.get_outgoing())
    print()

    print(f"{user2.get_email()} accepts {user1.get_email()}'s friend request.")
    user2.acc_or_rej(user1, True)

    print("USER1", user1.get_incoming(), user1.get_outgoing())
    print()
    print("USER1", user2.get_incoming(), user2.get_outgoing())
    print()

    print("USER1", user1.get_friends_list())
    print()
    print("USER2", user2.get_friends_list())
    print()