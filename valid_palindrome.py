def is_palindrome(s):
  # Write your code here
  # Tip: You may use the code template provided
  # in the two_pointers.py file'
    left = 0
    right = len(s) - 1 
    print("\tThe element being pointed by the left index is", s[left], sep = " ")
    print("\tThe element being pointed by the right index is", s[right], sep = " ")
    while left < right:
        print("\tWe check if the two elements are indeed the same, in this case...")
        if s[left] != s[right]:  # If the elements at index l and index r are not equal,
            print("\tThe elements aren't the same, hence we return False")
            return False    # then the symmetry is broken, the string is not a palindrome
        print("\tThey are the same, thus we move the two pointers toward the middle to continue the \n\tverification process.\n")
        left = left + 1  # Heading towards the right
        right = right - 1  # Heading towards the left
        print("\tThe new element at the left pointer is", s[left], sep = " ")
        print("\tThe new element at the right pointer is", s[right], sep = " ")
    # We reached the middle of the string without finding a mismatch, so it is a palindrome.
    return True


def main():
    test_cases =  ["RACEACAR", "A", "ABCDEFGFEDCBA", "ABC", "ABCBA", "ABBA", "RACEACAR"]
    for i in test_cases:
        print(is_palindrome(i))
        print("-" * 100, end="\n\n")


if __name__ == '__main__':
    main()


# print(is_palindrome("kayak"))
# print(is_palindrome("hello"))
# print(is_palindrome("Hello"))
# print(is_palindrome("A"))
# print(is_palindrome("DCBAABCD"))

Solution summary
# We initialize two pointers and move them from opposite ends.
# The first pointer starts moving toward the middle from the start of our string, 
# while the second pointer starts moving toward the middle from the end of our string. 
# This allows us to compare these elements at every single instance to find a non-matching pair,
# and if they reach the middle of the string without encountering any non-matching pair, 
# that means we indeed traverse a palindrome.

Time Comlexity
# O(n) where n is number of characters in the string
Space Complexity 
# O(1) since we use cosntant space to store two indices 
