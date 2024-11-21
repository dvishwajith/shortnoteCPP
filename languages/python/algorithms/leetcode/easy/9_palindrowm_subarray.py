def isPalindrome(x: int) -> bool:

    ## works but bad mathod. No need of recrusive if converted to string ####
    # if x < 0:
    #     return False
    # def isPalindromeStr(s):
    #     if len(s) <= 1:
    #         return True
    #     else:
    #         return (s[0] == s[-1]) and isPalindromeStr(s[1:len(s)-1])

    # return isPalindromeStr(str(x))

    # ## Method 2 ##
    # if x < 0 :
    #     return False
    # x_s = str(x)
    # return x_s[:] == x_s[::-1]
    
    # ## Method 3. Without converting to string ##
    # if x < 0 :
    #     return False
    # digit_list = []
    # while x:
    #     digit_list.append(x%10)
    #     x = x//10
    # return digit_list[:] == digit_list[::-1]

    ## Method 4. Without converting to string. And without list ##
    if x < 0 :
        return False
    reverse_num = 0
    x_orig = x
    while x:
        lsb = x%10
        reverse_num = reverse_num*10 + lsb
        x = x//10
    return x_orig == reverse_num

print(isPalindrome(1000021))