stringToReverse = "pleaseReverseMe"

#  please write a function without using inbuilt reverse or slicing system in python to reverse the given stringToReverse

def reverse_the_string(s, l, r):
  if l == r:
    return s
  mid = l + (r - l) // 2
  left_part = reverse_the_string(s[l:mid+1], l, mid)
  right_part = reverse_the_string(s[mid+1:r+1], 0, r - mid - 1)
  return right_part + left_part
  


def strRev(string: str):
  l, r = 0, len(string) - 1
  rev_str = reverse_the_string(string, l, r)
  print(rev_str)
  return rev_str
  
  # str_rev = ""
  # for i in range(len_str-1, -1, -1):
  #   str_rev += string[i]
  # return str_rev
  

# Test Case

assert strRev(stringToReverse) == "eMesreveResaelp"