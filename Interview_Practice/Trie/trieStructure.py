"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Input: strs = ["flower","flow","flight"]
Output: "fl"
"""


def createTrie(strings):
    trie = {}

    for s in strings:
        node = trie
        for char in s:
            if char not in node:
                node[char] = {}
            node = node[char]
        node["#"] = True

    return trie


def longestPrefix(s):
    node = createTrie(s)
    prefix = ""
    while True:
        keys = list(node.keys())

        if len(keys) != 1 and "#" not in keys:
            break
        ch = keys[0]
        prefix += ch
        node = node[ch]
    return prefix


if __name__ == "__main__":
    s = ["cat", "cap", "car"]
    si = ["flower","flow","flight"]
    # print(createTrie(si))
    print(longestPrefix(s))