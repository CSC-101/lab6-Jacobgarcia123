import data
from typing import Optional

# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp


# Part 1
def selection_sort_books(books:list[data.Book]):
    n = len(books)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if books[j].title < books[min_idx].title:
                min_idx = j
        books[i],books[min_idx] = books[min_idx], books[i]

    return [book.title for book in books]


# Part 2
def swap_case(word:str)->str:
    new_word = []
    for character in word:
        if character.islower():
            new_word.append(character.upper())
        elif character.isupper():
            new_word.append(character.lower())
        else:
            new_word.append(character)
    return ''.join(new_word)



# Part 3
def str_translate(word:str,old:str,new:str) -> str:
    new_word = []

    for character in word:
        if character == old:
            new_word.append(new)
        else:
            new_word.append(character)
    return ''.join(new_word)

# Part 4
def histogram(word:str) -> dict:
    word_count = {}
    words = word.split()
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

