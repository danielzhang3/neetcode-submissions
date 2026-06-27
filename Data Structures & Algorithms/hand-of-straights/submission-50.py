class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = {}

        for card in hand: 
            count[card] = 1 + count.get(card, 0)
        
        for card in sorted(count): 
            cnt = count[card]
            if cnt > 0: 
                for i in range(groupSize): 
                    if count.get(card + i, 0) < cnt: 
                        return False
                    
                    count[card + i] -= cnt
        
        return True
        