def reverse(string)-> str:
    """Funtion whitch accepts a string and returns and new string in reverse

    Args:
        string (str): Input string

    Returns:
        [str]: string in reverse
    """    
    if len(string)==1:
        return string[0]
    else:
        return string[len(string)-1] + reverse(string[:len(string)-1])
        
print(reverse('Python'))