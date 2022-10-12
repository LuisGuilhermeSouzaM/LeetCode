class Solution(object):
    def maxProfit(self, prices):
        answer = 0
        left = 0
        for right in range(1, len(prices)):
            if prices[right] < prices[left]:
                left = right
            answer = max(answer, prices[right] - prices[left])
        return answer