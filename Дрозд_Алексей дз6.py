#prostoe chislo
from math import sqrt


def is_prime(n):
  i = 2
  while i <= sqrt(n):
    if n % i == 0:
      return False
    i += 1
  if n > 1:
    return True


a = int(input())

if is_prime(a):
  print("True")
else:
  print("False")

#stroka
s = "1 9 3 4 -5"
"""nums = [int(n) for n in str.split()]
max(nums)
min(nums)
print(max(nums))
print(min(nums))"""

def nums(s):
  a = s.split(' ')
  max_number = max(a)
  min_number = min(a)
  return max_number, min_number
print(nums(s))

#"The sunset sets at twelve o' clock."
text = "The sunset sets at twelve o' clock."


def alphabet_position(text):
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  res = ''
  for j in text.lower():
    if j in alphabet:
      res += str(alphabet.index(j) + 1)
    else:
      res += ' '
  return res


print(alphabet_position("The sunset sets at twelve o' clock."))

