class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # base case
        if n < k or n < 1:
            return []
        if k == 0:
            return [[]]
        if n == k:
            return [[i for i in range(1, n+1)]]
        # 拆分子问题，从剩下n-1个数中去k个数和k-1个数
        ans1 = self.combine(n-1, k-1)
        ans2 = self.combine(n-1, k)
        #对于第一个子问题，补齐当前的第n个数
        if ans1:
            for i in ans1:
                i.append(n)
        return ans1+ans2