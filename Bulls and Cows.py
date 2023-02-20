from collections import defaultdict as dd

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        n = len(secret)
        bulls = cows = 0
        hash1 = dd(int)
        bull = dd(int)
        hash2 = dd(int)
        for x in range(n):
            if secret[x] == guess[x]:
                bulls += 1
                bull[guess[x]] = 1
            else:
                hash2[guess[x]] += 1
                hash1[secret[x]] += 1
        #print(hash2, hash1)
        for x in range(n):
            if secret[x] != guess[x] and hash1[guess[x]]:
                cows += min(hash2[guess[x]], hash1[guess[x]])
                hash1[guess[x]] = 0
        return str(bulls) + 'A' + str(cows) + 'B'
