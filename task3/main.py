import threading
from authenticator import Authenticator

class ExtendedAuthenticator(Authenticator):
    pass

def create_instance(thread_name: str):
    instance = Authenticator()
    print(f"{thread_name} (Authenticator): {id(instance)}")

def create_instance_extended(thread_name: str):
    instance = ExtendedAuthenticator()
    print(f"{thread_name} (ExtendedAuthenticator): {id(instance)}")

def main():
    threads = []

    for i in range(3):
        t = threading.Thread(target=create_instance, args=(f"Thread-A-{i}",))
        threads.append(t)
        t.start()

    for i in range(3):
        t = threading.Thread(target=create_instance_extended, args=(f"Thread-B-{i}",))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    auth = Authenticator()
    print("\nПеревірка аутентифікації:")
    print("admin/secret ->", auth.authenticate("admin", "secret"))
    print("user/pass ->", auth.authenticate("user", "pass"))

if __name__ == "__main__":
    main()
