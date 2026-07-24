print("STACK FRAME VISUALIZER")
def linear_recursion(n):
    if n == 0:
        return
    print("Linear call at level:", n)
    linear_recursion(n - 1)

print("Linear Recursion")
linear_recursion(5)

def tail_recursion(n):
    if n == 0:
        return
    print("Tail work before call:", n)
    tail_recursion(n - 1)

print("Tail Recursion")
tail_recursion(5)

def head_recursion(n):
    if n == 0:
        return
    head_recursion(n - 1)
    print("Head work after call:", n)

print("Head Recursion")
head_recursion(5)

def increasing_decreasing(n):
    if n == 0:
        return
    print("Going down:", n)
    increasing_decreasing(n - 1)
    print("Coming back:", n)

def tree_recursion(n):
    if n == 0:
        return
    print("Tree node:", n)
    tree_recursion(n - 1)
    tree_recursion(n - 1)

print("Tree Recursion")
tree_recursion(3)
