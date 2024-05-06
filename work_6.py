class comx:
    def __init__(self, x, y):
        self.real=x
        self.imag=y

    def __add__(self, other):
        return comx(self.real+other.real, self.imag+other.imag)
    def __sub__(self, other):
        return comx(self.real-other.real, self.imag-other.imag)
    def __mul__(self, other):
        return comx(self.real*other.real-self.imag*other.imag, self.imag*other.real+self.real*other.imag)
    def __truediv__(self, other):
        return comx(self.real/other.real-self.imag/other.imag, self.imag/other.real+self.real/other.imag)
