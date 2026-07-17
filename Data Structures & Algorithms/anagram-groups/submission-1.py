class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_map = [[0 for _ in range(26)] for _ in range(len(strs))]
        for word_idx in range(0, len(strs)):
            current_freq_map = freq_map[word_idx]
            word = strs[word_idx]
            for char in word:
                current_freq_map[int(ord(char)-ord("a"))]+=1
        # LOGIC JUST TO SUPPORT PYTHON
        # CONVERT EACH LIST TO A STRING OF FREQUENCIES
        for idx in range(0, len(freq_map)):
            freq_map[idx] = tuple(freq_map[idx])
        result = {}
        for map_idx in range(0, len(freq_map)):
            result[freq_map[map_idx]] = result.get(freq_map[map_idx], [])
            result[freq_map[map_idx]].append(strs[map_idx])
        return list(result.values())