class Logger:
    def Log(self, message):
        print("\033[32m" + message + "\033[0m")

    def Error(self, message):
        print("\033[31m" + message + "\033[0m")

    def Warn(self, message):
        print("\033[38;5;208m" + message + "\033[0m")
