
#this function will return true for any palindrome string with 1 unknown element
defdef check(s):
    for i in range(len(s)):
        print(i)
        print(s[i])
        s1=s.replace(s[i],'',1)
        print(s1)
        if s1==s1[::-1] :
            return True
            
    return False
#here is the example it returns true however y is present    
s='madaym'  
print(check(s)
