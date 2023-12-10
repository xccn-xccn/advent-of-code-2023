def gcd(a, b):
    if a == 0 or b == 0:
        return a + b
    
    print(a, b)
    return gcd(b, a%b)

def lcm(a, b):
    print(a, b, "lcm")
    print(a, b, gcd(a, b), "lcm")
    return a * b / gcd(a, b)

def lcmm(*nums):
    if len(nums) == 1:
        return nums
    
    return lcmm(lcm(nums[0], nums[1]) , *nums[2:])

# print(gcd(23948, 100))
print(lcm(12, 15))
print(lcmm(12, 15, 75, 182930, 229292990))