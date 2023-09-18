"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:
       return x
   else:
       return(foo(x-1) + foo(x-2))

    pass

def longest_run(mylist, key):
    longKey = 0
    currContiKey = 0
    for i in mylist:
        if i == key:
            currContiKey += 1
        else:
            longKey = max(longKey, currContiKey)
            currContiKey = 0
    return max(longKey, currContiKey)


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_recursive(mylist, key):
    if not mylist or len(mylist) == 1:
        return mylist[0] == key
    
    midPart = len(mylist) // 2
    leftPart = mylist[:midPart]
    rightPart = mylist[midPart:]
    
    left_longest = longest_run_recursive(left, key)
    right_longest = longest_run_recursive(right, key)
    
    mid_longest = 0
    leftLongCount = 0
    rightLongCount = 0
    for i in range(midPart-1, -1, -1):
        if mylist[i] == key:
            leftLongCount += 1
        else:
            break
    for i in range(mid, len(mylist)):
        if mylist[i] == key:
            rightLongCount += 1
        else:
            break
    mid_longest = leftLongCount + rightLongCount
    
    return max(leftLongCount, rightLongCount, mid_longest)

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3


