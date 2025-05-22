import threading

class Authenticator:
    _singleton_instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if Authenticator._singleton_instance is None:
            with Authenticator._lock:
                if Authenticator._singleton_instance is None:
                    Authenticator._singleton_instance = super().__new__(cls)
        return Authenticator._singleton_instance

    def __init__(self):
        pass

    def authenticate(self, username: str, password: str) -> bool:
        return username == "admin" and password == "secret"
