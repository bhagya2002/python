# def mygenerator():
#     yield 1
#     yield 2
#     yield 3

# g = mygenerator()

# print(sum(g))

# sorted(g)

def countdown(num):
    print("Starting")
    while num > 0:
        yield num
        num -= 1
        
cd = countdown(4)