class ShortTermMemory:

    def __init__(self, max_messages=10):

        self.max_messages = max_messages
        self.messages = []

    def add_message(self, role, content):

        self.messages.append({
            "role": role,
            "content": content
        })

        if len(self.messages) > self.max_messages:
            self.messages.pop(0)

    def get_context(self):

        context = ""

        for message in self.messages:
            context += (
                f"{message['role']}: "
                f"{message['content']}\n"
            )

        return context

    def clear(self):
        self.messages = []