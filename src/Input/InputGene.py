from src.GA.Gene import Gene


class InputGene(Gene):

    CODE_WAIT = 0
    CODE_ARROW_LEFT = 1
    CODE_ARROW_RIGHT = 2
    CODE_ARROW_UP = 3
    CODE_ARROW_DOWN = 4
    CODE_CLICK_CENTER = 5
    CODE_CLICK_RIGHT_CORNER = 6

    def is_smoothable_code(self):
        if self._code in [
            InputGene.CODE_ARROW_LEFT,
            InputGene.CODE_ARROW_RIGHT,
            InputGene.CODE_ARROW_UP,
            InputGene.CODE_ARROW_DOWN,
        ]:
            return True
        return False
