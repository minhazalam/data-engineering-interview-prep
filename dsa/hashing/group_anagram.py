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

"""
Problem: Group Anagrams — Frequency Counting Approach

Given a list of strings, group anagrams together.

Approach:
    1. Create a frequency array of 26 integers for each word.
    2. Count the occurrences of each lowercase English character.
    3. Convert the frequency array into a tuple.
    4. Use the tuple as a dictionary key to group anagrams.

Assumption:
    Input contains only lowercase English letters (a-z).

Complexity:
    Time: O(n * k), where n is the number of words
          and k is the maximum word length.
    Auxiliary Space: O(n), excluding the output.
"""


def group_anagrams(words: list[str]) -> list[list[str]]:
    groups = {}
    for word in words:
        frequency = [0] * 26
        for char in word:
            index = ord(char) - ord("a")
            frequency[index] += 1
        signature = tuple(frequency)
        if signature in groups:
            groups[signature].append(word)
        else:
            groups[signature] = [word]
    return list(groups.values())


print(group_anagrams(["eat", "tea", "ate", "tan", "nat", "bat"]))
