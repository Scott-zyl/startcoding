class Solution(object):
    def find132pattern(self, nums):
	ak = float('-inf')
	st = []
	for i in reversed(range(len(nums))):
	    if num[i] < ak:
		return True
	    else:
		while st and num[i] > st[-1]
		    ak = st.pop()
	    st.append(num[i])
	return False
