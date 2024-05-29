
def isPalindrome(s):
	return s == s[::-1]

s = "mom"
ans = isPalindrome(s)

if ans:
	print("Yes,its a pallindrome")
else:
	print("No")
