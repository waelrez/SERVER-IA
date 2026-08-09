class Memory:

    def __init__(self):
        self.messages = []

    def add(self, user_message, ai_response):

        self.messages.append({
            "user": user_message,
            "assistant": ai_response
        })

    def get_all(self):
        return self.messages

    def clear(self):
        self.messages = []
