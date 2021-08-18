class Tile:
    def __init__(self, value = None) -> None:
        self._value = value
        # self._move_state = False

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value
       
    # def update_state(self, state):
       #  self.move_state = state

    # def get_state(self):
       #  return self.move_state

    def update_value(self):
        self._value *= 2

    
