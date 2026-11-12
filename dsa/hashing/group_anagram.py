"""
Problem: Group Anagrams

Given a list of strings, group the anagrams together.
Strings that contain the same characters with the same frequencies
belong to the same group.

Example:
Input:
    ["eat", "tea", "tan", "ate", "nat", "bat"]

Output:
    [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

Approach:
    Use a dictionary to group words by a common signature.
    The initial solution uses sorted characters as the dictionary key.

Complexity:
    Let n = number of words and k = maximum word length.
    Time: O(n * k log k)
    Space: O(n * k)
"""


def brute_force_group_anagrams(words: list[str]) -> list[list[str]]:
    groups = {}

    for word in words:
        signature = "".join(sorted(word))
        # print(signature)
        if signature in groups:
            groups[signature].append(word)
        else:
            groups[signature] = [word]

    return list(groups.values())


print(brute_force_group_anagrams(words=["eat", "tea", "tan", "ate", "nat", "bat"]))
