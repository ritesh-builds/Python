class calculator():
    def __init__(self, n): # This is a constructor.
        self.n = n  

    def square(self):
        print(f"The square of number {self.n} is {self.n*self.n}.")

    def sqrt(self):
        print(f"The square root of number {self.n} is {self.n**1/2}.")

    
    def cubrt(self):
        print(f"The squcubeare root of number {self.n} is {self.n**1/3}.")

    
a = calculator(64)
a.square()
a.sqrt()
a.cubrt()