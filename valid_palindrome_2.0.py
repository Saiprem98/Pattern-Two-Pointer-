# Write a function that takes a string as input 
# and checks whether it can be a valid palindrome 
# by removing at most one character from it.
def is_palindrome(s):
  left = 0
  right = len(s) - 1
  skipLeft = False
  skipRight = False
  while left < right:
    if s[left] == s[right]:
      left += 1
      right -= 1
    else: 
    # so now we have a mistmatch 
    # we need to skip one on the left and see if it works
    # then skip one on the right and see if it works 

      currLeft = left
      currRight = right 
      skipLeft = False
      skipRight = False
    #   first lets skip left 
      currLeft += 1
      while currLeft < currRight:
        if s[currLeft] == s[currRight]:
          currLeft += 1
          currRight -= 1
        else: 
          skipLeft = True 
          break 
        # if it enters here that means skipping left did not work 
      
    #   so we need to restart, skip right and check 
      currLeft = left
      currRight = right 

      currRight -= 1
      while currLeft < currRight:
        if s[currLeft] == s[currRight]:
          currLeft += 1
          currRight -= 1
        else: 
            # if it enters here that means skip right did not work 
          skipRight = True 
          break 
    # now check the boolean values
    # if both skipright and left are true then fail 
    # but if at least one stays false than it is good 
      if(skipRight == False or skipLeft == False):
        return True
      else:
        return False

  return True

Time Complexity:
    # we technically don't have any nested loops
    # just running the same loop from different points
    #  so O(n)
Space Complexity:
    # not really using any data besides varaibles to store index
    # constant space so O(1)