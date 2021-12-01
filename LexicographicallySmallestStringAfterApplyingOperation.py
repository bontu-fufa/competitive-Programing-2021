class Solution(object):
    
    def add_odd(self,nums,a):
        for i , num in enumerate(nums):
            if not i % 2 == 0 :
                nums[i] = str( (int(num) + a) % 10)
        return "".join(nums)
    def move_right(self,nums,b):
            return ''.join(nums[b:] + nums[:b])
    def generate(self,s,a,b,visited,min_s):
            if s in visited: return 
            visited.add(s)
            
            added = self.add_odd(list(s),a)
            shifted = self.move_right(list(s),b)
            
            min_s[0] = min(min_s[0],(min(added,shifted)))
            
            self.generate(added,a,b,visited,min_s)
            self.generate(shifted,a,b,visited,min_s)
            
            
    def findLexSmallestString(self, s, a, b):
        """
        :type s: str
        :type a: int
        :type b: int
        :rtype: str
        """ 
        visited = set()
        min_s = ['9'*len(s)]
        print(s)
        self.generate(s,a,b,visited,min_s)
        return min_s[0]
        
