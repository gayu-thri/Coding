s = input('Enter encoded string')
stack_strs = [] # chars stack
stack_nums = [] # num stack
num = "" # to keep track of digits
str_t = "" # to keep track of characters
i = 1
for ch in s:
    print("-- ITERATION ",i)
    if ch.isdigit():
        num += ch
        print(num)
    elif ch =="[":
        stack_strs.append(str_t)
        print("--- elif ch ==[: ----")
        print("Stack strs appended",str_t)
        stack_nums.append(int(num))
        print("Stack nums appended",num)
        num, str_t = "", "" # reset so that we don't push what we have already pushed again
    elif ch =="]":
        print("---- elif ch ==]: ----")
        n = stack_nums.pop() # get the last number we pushed
        print("Popped from stack nums", n)
        t = stack_strs.pop() # get the last charcter(s) we pushed
        print("Popped from stack strs", t)
        str_t = t + str_t * n # str_t has already a value from the previous loop that hasn't been pushed, so we need to pop characters and concatenate at the begining of the current string, so that we will have the same order, pushing at the end e.g. str_t * n + t will end up having the string in a reverse order 
        print("Multiplied n times", str_t)
    else: # it's a char
        print("--- else: ----")
        str_t +=ch
        print("str_t += ch ; str_t -->", str_t)
    i = i+1
        
print("Decoded: ",str_t)
"""
Time Complexity: O(N) where N is the length of the string, push or pop only require O(1)
Space Complexity: O(N) - we need space for the two stacks, but both of them (together) 
require N (length of the string), space for num and str_t <N
"""
'''
class Solution:
    def decodeString(self, s) -> str:
        """
        :type s: str
        :retype: str
        """
        
        stack_str = list()
        stack_nums = list()
        
        n, st = "", ""
        
        for ch in s:
            
            if ch.isdigit():
                n = n + ch
            
            elif ch == '[':
                stack_str.append(st)
                stack_nums.append(int(n))
                n, st = "", "" # reset so that we don't push what we have already pushed again
                
            elif ch == ']':
                s_pop = stack_str.pop()
                n_pop = stack_nums.pop()
                st = s_pop + st * n_pop
            
            else:
                st = st + ch
        
        return st              
'''
