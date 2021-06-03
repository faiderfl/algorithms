def capitalize_words(arr):
    if len(arr)==1:
        return [arr[0].upper()]
    else:
        return [arr[0].upper()]+ capitalize_words(arr[1:])


def capitalize_words2(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0].upper())
    return result + capitalize_words2(arr[1:])

words=['i','am','learning','recursion']
print(capitalize_words(words))