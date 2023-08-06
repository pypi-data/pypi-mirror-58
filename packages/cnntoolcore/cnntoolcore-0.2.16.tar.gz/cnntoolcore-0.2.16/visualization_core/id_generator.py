
class IdGenerator():
    _instance = None

    def __init__(self) -> None:
        super().__init__()
        self.current_id = 10

    def reset(self):
        self.current_id = 0

    def get_id(self):
        self.current_id += 1
        return self.current_id

def get_id_generator():
    if IdGenerator._instance is None:
        IdGenerator._instance = IdGenerator()
    return IdGenerator._instance



