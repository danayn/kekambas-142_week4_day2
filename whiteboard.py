# Pair of gloves
# Winter is coming, you must prepare your ski holidays. The objective of this kata is to determine the number of pair of gloves you can constitute from the gloves you have in your drawer.

# Given an array describing the color of each glove, return the number of pairs you can constitute, assuming that only gloves of the same color can form pairs.

# Examples:
# input = ["red", "green", "red", "blue", "blue"]
# result = 2 (1 red pair + 1 blue pair)

# input = ["red", "red", "red", "red", "red", "red"]
# result = 3 (3 red pairs)

def solution(gloves):
    color_count = {}
    for color in gloves:
        color_count[color] = color_count.get(color, 0) + 1
    pairs = 0
    for color, count in color_count.items():
        pairs_of_color = count // 2
        pairs += pairs_of_color
        print(f"We can make {pairs_of_color} pair{'' if pairs_of_color == 1 else 's'} of {color}")
    return pairs

print(solution(["red", "green", "red", "blue", "blue", "green", 'green', 'red', 'blue', 'blue', 'yellow']))

# def solution(gloves):
#     pairs = 0
#     for color in set(gloves):
#         pairs += gloves.count(color) // 2
#     return pairs

# from collections import Counter
# def solution(arr):    
#     glove_dict = Counter(arr)
#     total_pairs = 0
    
#     for key, value in glove_dict.items():
#         pairs = value // 2
#         total_pairs += pairs
    
#     return total_pairs

def solution(gloves):
    output = 0
    while len(gloves) > 0:
        if gloves.count(gloves[0]) > 1:
            output += 1
            pair = gloves[0]
            gloves.remove(pair)
            gloves.remove(pair)
        else:
            single = gloves[0]
            gloves.remove(single)
    return output