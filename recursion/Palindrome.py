
def reverse(string)->str:
    """[summary]

    Args:
        string ([type]): [description]

    Returns:
        str: [description]
    """    
    len_string= len(string)
    if len(string)==1:
        return string[0]
    else:
        return string[len_string-1]+ reverse(string[:len_string-1])
        
def is_palindrome(string)->bool:
   return True if string == reverse(string) else False


print(is_palindrome('awesome'))
print(is_palindrome('tacocat'))
