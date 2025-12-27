
def chaiCode(num):
    def actual(x):
        return x ** num
    return actual


f = chaiCode(1)
g = chaiCode(2)

print(f)
print(g)

print(f(5))
print(g(5))