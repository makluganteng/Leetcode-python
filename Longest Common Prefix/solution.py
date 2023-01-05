def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        short = min(strs, key=len) # short = "flow"
        print(short)
        for item in strs: # When item = "flight"
            while len(short) > 0:
                if item.startswith(short):
                    print(item)# during loop 1 condition fails, during loop 2 condition fails, during loop 3 "flight" startswith fl is True
                    break
                else:
                    short = short[:-1]
                    print(short)# during loop 1 short = flo, during loop 2 short = fl
        return short
                
                    
        
        
        
        
case1 = ["flower","flow","flight"]
case2 = ["dog","racecar","car"]

print(longestCommonPrefix(case1))