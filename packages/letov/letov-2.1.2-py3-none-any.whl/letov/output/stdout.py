class Stdout:
    def send(self, message):
        print(message)
        return True

    def close(self):
        pass
