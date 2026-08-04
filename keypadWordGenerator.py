#tower of hanoi
def tower_of_hanoi(disks, source, helper, destination):
    if disks == 1:
        print("Move Disks 1 From", source, "to", destination)
        return
    tower_of_hanoi(disks - 1, source, destination, helper)
    print("Mover Disk", disks, "from", source, "to", destination)
    tower_of_hanoi(disks - 1, helper, source, destination)
print("TOWER OF HANOI WITH 3 DISKS")
tower_of_hanoi(3, "A", "B", "C")

keypad = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}

def generate_words(digits, current_word):
    if len(digits) == 0:
        print(current_word)
        return
    first_digit = digits[0]
    remaining_digits = digits[1:]
    for letter in keypad[first_digit]:
        generate_words(remaining_digits, current_word + letter)
print("The combos for 45 are")
num = "45"
generate_words(num, "")

def show_recursion_tree(digits, current_word, level):
    indent = " " * level
    if len(digits) == 0:
        print(indent + "Word completed: "+ current_word)
        return
    first_digit = digits[0]
    remaining_digits = digits[1:]
    print(indent + "Current word: " + current_word + " | Next digit: " + first_digit)
    for letter in keypad[first_digit]:
        show_recursion_tree(remaining_digits, current_word + letter, level + 1)

print("Recursion Tree")
show_recursion_tree("23", "", 0)
