class EventManager:
    def __init__(self):
        self.listeners = []
        self.messages = []  # тут будемо зберігати всі повідомлення

    def subscribe(self, listener):
        self.listeners.append(listener)

    def notify(self, message):
        self.messages.append(message)  # зберігаємо повідомлення
        for listener in self.listeners:
            listener.update(message)

    def get_messages(self):
        return self.messages

class Logger:
    def update(self, message):
        print(f"[Logger] {message}")

class EmailNotifier:
    def update(self, message):
        print(f"[Email] Notification: {message}")

class SMSNotifier:
    def update(self, message):
        print(f"[SMS] Alert: {message}")
