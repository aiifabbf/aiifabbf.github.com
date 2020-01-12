class Solution:
    def numberToWords(self, num: int) -> str:
        string = str(num)
        units = string[-3: ]
        thousands = string[-6: -3]
        