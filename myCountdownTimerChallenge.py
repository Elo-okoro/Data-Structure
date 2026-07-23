print("My Countdown Timer Challenge! \n ")
def countdown(number):
    if number == 0:
        print("Time Is Up!")
        return
    print(number)
    countdown(number - 1)
countdown(10)

def build_unwind(n):
    if n == 0:
        print("Base Case Condition Met. Unwinding Starts: ")
        return
    print("Build", n)
    build_unwind(n - 1)
    print("Unwind", n)
build_unwind(4)

def counting(number):
    if number > 10:
        return
    print(number)
    counting(number+1)
print("Counting From 1 to 10:")
counting(1)

def factorails(i):
    if i == 1:
        return 1
    return i * factorails(i - 1)
print("Factorial is", factorails(6))
