class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if N == 1:
            return True
        dict = {}
        for pairs in dislikes:
            if pairs[0] in dict:
                dict[pairs[0]].add(pairs[1])
            else:
                dict[pairs[0]] = set([pairs[1]])
                
            if pairs[1] in dict:
                dict[pairs[1]].add(pairs[0])
            else:
                dict[pairs[1]] = set([pairs[0]])
                
        #print(dict)
        room = {}
        for i in range(1, N+1):
            if i not in room:
                room[i] = 0
                stack = [i]
                while stack:
                    a = stack.pop()
                    if a in dict:
                        for b in dict[a]:
                            if b in room:
                                if room[a] == room[b]:
                                    return False
                            else:
                                room[b] = (room[a] + 1)%2
                                stack.append(b)
        return True