import json
import urllib.request
import urllib.error

class LN:
    def __init__(self: "LN", value: object, next: "LN" = None):
        self.value = value
        self.next = next
class Notification:
    def __init__(self) -> None:
        self._stack = LN()
    def add_message(self, msg: str) -> None:
        #adds the new notification to the top of the stack
        temp = self._stack
        self._stack = LN(msg,temp)
    def get_recent_message(self) -> str:
        #return the most recent message (message at top of the stack)
        return self._stack.value
    def get_last_message(self) -> str:
        #return the notification at the bottom of the stack
        msg = ""
        head = self._stack
        while(head != None):
            msg = self._stack.value
            head = head.next
        return msg
    def send_message(self, message: str):
        #sends notification of friend request to person
        pass
    def delete_notification(self, message: None):
        if message != None:
            temp = self._stack
            while(temp.value != None and temp.value != message):
                temp = temp.next
                



    