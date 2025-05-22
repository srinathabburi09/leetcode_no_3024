class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        a, b, c = nums   #these are the sides of a triangle:a,b,c = nums that is a = nums[0], b = nums[1], c = nums[2]!

        if a + b <= c:   #from properties of a triangle sum of two sides should be greater than the otherside so if it is false we return none
            return "none"
        if a == b and b == c:  #if all three sides are equal -- equilateral
            return "equilateral"
        elif a == b or b == c or c == a:  #if any two sides are equal -- isosceles
            return "isosceles"
        else:                         #if there is no equal sides -- scalene
            return "scalene"        
