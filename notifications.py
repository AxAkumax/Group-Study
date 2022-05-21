import json
import urllib.request
import urllib.error


class Notifications:
    def __init__(self) -> None:
        self._url = "https://gmail.googleapis.com"
        self._data = ""
    def get_request(self) -> bool:
        response = None 
        try:
            req = urllib.request.Request(self._url)
            response = urllib.request.urlopen(req)
            self._data = response.read().decode(encoding = 'utf-8')
            self._data = json.loads(self._data)
        except:
            #exception handling
            pass
        finally:
            if response != None:
                response.close()
                return True
            return False
    def send_message(self, message: str):
        pass


