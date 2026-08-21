binary_scores = [1, 1, 1, 0, 1, 0, 1, 1, 1, 1]
print("This Only Contains 0s and 1s: \n", binary_scores)
streak = 0
for score in binary_scores:
    if score == 1:
        streak += 1
    else:
        streak = 0
print("Score:", score, "Streak:", streak)
best_streak = 0
for score in binary_scores:
    if score == 1:
        streak += 1
        best_streak = max(best_streak, streak)
    else:
        streak = 0
print("Longest Streak Of 1s:", best_streak)
numbers = [0, 0, 2, 4, 5, 6, 2, 1, 0, 0]
print("These Are The Numbers:", numbers)
write = 0
for read in range(len(numbers)):
    if numbers[read] != 0:
        numbers[write] = numbers[read]
        write += 1
print("After Same Direction Two Pointer", numbers)
while write < len(numbers):
    numbers[write] = 0
    write += 1
print("Final Array After Moving Zeros To The End:", numbers)
