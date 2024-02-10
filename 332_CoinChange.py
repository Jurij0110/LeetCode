class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        result = -1
        temp = 0
        coins.sort()
        while (len(coins) > 0 and amount > 0):
            if amount > coins[-1]:
                temp += int(amount / coins[-1])
                amount = int(amount % coins[-1])
                coins.pop()
                print(("amount > coins[-1]: result =%s, amount=%s,coins= %s")%(temp,amount,coins))
            elif amount == coins[-1]:
                temp += 1
                amount = int(amount % coins[-1])
                coins.pop()
                print(("amount == coins[-1]: result =%s, amount=%s,coins= %s")%(temp,amount,coins))
            else:
                coins.pop()
                print(("amount < coins[-1]: result =%s, amount=%s,coins= %s")%(temp,amount,coins))
        if amount > 0:
            return result
        else:
            return temp

coins=[186,419,83,408]
amount=6249
s1 = Solution()
print(s1.coinChange(coins, amount))