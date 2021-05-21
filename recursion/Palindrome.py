
def reverse(string)->str:
    """[summary]

    Args:
        string ([type]): [description]

    Returns:
        str: [description]
    """    
    len_string= len(string)
    if len_string==1:
        return string[0]
    else:
        return string[len_string-1]+ reverse(string[:len_string-1])
        
def is_palindrome(string)->bool:
   return True if string == reverse(string) else False

def is_palindrome2(string):
    if len(string) == 0:
        return True
    if string[0] != string[len(string)-1]:
        return False
    return is_palindrome2(string[1:-1])


print(is_palindrome('awesome'))
print(is_palindrome('tacocat'))


print(is_palindrome2('awesome'))
print(is_palindrome2('tacocat'))