def palindrome(word, index):
    left_index = index
    right_index = len(word) - 1 - index
    if left_index >= right_index:
        return f'{word} is a palindrome'
    else:
        if word[left_index] == word[right_index]:
            return palindrome(word, index+1)
        else:
            return f'{word} is not a palindrome'


print(palindrome("abcba", 0))
print(palindrome("peter", 0))