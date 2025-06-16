"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""


from collections import defaultdict

class Solution(object):

    def default_dict_groupAnagrams(self, strs):
        anagram_dict = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_dict[sorted_word].append(word)
        return list(anagram_dict.values())

    def groupAnagrams(self, strs):
        anagram_dict = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in anagram_dict:
                anagram_dict[sorted_word] = [word]
            else:
                anagram_dict[sorted_word].append(word)
        return list(anagram_dict.values())
    
if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    obj = Solution()
    print(obj.default_dict_groupAnagrams(strs))
    print(obj.groupAnagrams(strs))
