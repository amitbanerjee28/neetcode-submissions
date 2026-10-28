class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map : defaultdict[str,list[str]] = defaultdict(list)
        for word in strs:
            canonical_key = "".join(sorted(word))
            anagram_map[canonical_key].append(word)
        return list(anagram_map.values())