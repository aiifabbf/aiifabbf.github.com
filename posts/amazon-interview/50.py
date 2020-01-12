class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            if n == 0:
                return float("nan")
            else:
                return 0
        else:
            if n == 0:
                return 1
            elif n < 0:
                return 1 / self.myPow(x, -n)
            elif n % 2 == 0:
                return self.myPow(x * x, n // 2) # 很奇怪，我也不知道为什么这里用x * x就不会overflow，但是用x ** 2就会overflow
            else:
                return x * self.myPow(x, n - 1)