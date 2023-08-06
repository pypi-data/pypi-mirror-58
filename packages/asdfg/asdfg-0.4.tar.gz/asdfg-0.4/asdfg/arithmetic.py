
class Arithmetic:
    def __init__(self, first_term, common_diff):
        self.first_term= first_term
        self.common_diff= common_diff

    def nth_term(self, nth_pos):
        return self.first_term+1+ (nth_pos-1)*self.common_diff
