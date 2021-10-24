class Gene:

    def __init__(self, code):
        self._code = code

    def get_code(self):
        return self._code

    def to_string(self):
        return str(self._code)

    def is_smoothable_code(self):
        return True
