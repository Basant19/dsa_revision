class Solution:
    def isPalindrome(self, x: int) -> bool:
        #0 is Plaindrome
        if x ==0 :
            return True 
        #negative numbers are not palindrome 
        if x<0:
            return False 
        #ending with zero are not palindrome (10,500)
        if x%10==0:
            return False 
        
        reversenumber=0
        original=x
        while x>0:
            lastdigit=x%10
            reversenumber=(reversenumber*10)+lastdigit
            x=x//10
        return original == reversenumber


             

        