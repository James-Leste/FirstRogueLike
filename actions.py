# Each action is represented by a subclass in actions.py

class Action:
    pass


# hitting ESC key
class EscapeAction(Action):
    pass


class MovementAction(Action):
    def __init__(self, dx: int, dy: int):
        super().__init__()

        self.dx = dx
        self.dy = dy

