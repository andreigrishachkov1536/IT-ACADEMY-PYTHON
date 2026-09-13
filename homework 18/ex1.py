class History:
    def __init__(self, actions):
        self.actions = actions

    def __iter__(self):
        return HistoryIterator(self.actions)

class HistoryIterator:
    def __init__(self, actions):
        self.actions = actions
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.actions):
            raise StopIteration

        action = self.actions[self.index]
        self.index += 1

        return action

history = History([
    "login",
    "open_profile",
    "edit_profile",
    "logout"
])

for action in history:
    print(action)

print("-----------")

for action in history:
    print(action)