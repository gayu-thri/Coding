class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        freq = sorted(freq, key = lambda x:x[1], reverse = True)
        return ''.join(f)