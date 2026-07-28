list_of_scores = [45, 60, 75, 88, 92]

print("Full List:", list_of_scores)
print("Head of list", list_of_scores[0])
print("Tail of list", list_of_scores[1:])

def show_shrink(list_of_scores):
    print("Current list", list_of_scores)
    if len(list_of_scores) == 1:
        print("Base Case Reached:", list_of_scores)
        return
    show_shrink(list_of_scores[1:])
show_shrink(list_of_scores)

def is_sorted(list_of_scores):
    if len(list_of_scores)<=1:
        return True
    if list_of_scores[0] > list_of_scores[1]:
        return False
    return is_sorted(list_of_scores[1:])
print("Is The List Sorted?", is_sorted(list_of_scores))

not_sorted_list = [45, 75, 88, 92, 60]
print("Unsorted Scores:", not_sorted_list)
print("Is The List Sorted?", is_sorted(not_sorted_list))

def recursive_sum(list_of_scores):
    if len(list_of_scores) == 0:
        return 0
    return list_of_scores[0] + recursive_sum(list_of_scores[1:])
print("Total Score Of List Of Scores", recursive_sum(list_of_scores))

def largest_score(list_of_scores):
    if len(list_of_scores) == 1:
        return list_of_scores[0]
    largest_in_tail = largest_score(list_of_scores[1:])
    if list_of_scores[0]>largest_in_tail:
        return list_of_scores[0]
    return largest_in_tail
print("The Highest Score In The List Is:", largest_score(list_of_scores))
