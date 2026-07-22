def count(n):
    if n == 11:
        return
    print(n)
    count(n + 1)
count(1)

def two_phases(n):
    if n == 0:
        return
    print("Build", n)
    two_phases(n - 1)
    print("Unwind", n)
two_phases(5)

def factorails(n):
    if n == 1:
        return 1
    return n * factorails(n - 1)
print(factorails(6))
