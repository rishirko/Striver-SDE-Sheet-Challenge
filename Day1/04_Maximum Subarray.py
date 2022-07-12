class Solution:
    def maxSubArray(self, arr: List[int]) -> int:
        sum=0
        maximum=arr[0]
        for i in arr:
            sum+=i
            if maximum<sum:
                maximum=sum
            if sum<0:
                sum=0
        return maximum
        
