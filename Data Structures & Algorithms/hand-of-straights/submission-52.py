class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: 
            return False
        
        count = Counter(hand)
        hand.sort()

        for card in hand: 
            cnt = count[card]
            if cnt > 0: 
                for i in range(groupSize): 
                    if count.get(card + i, 0) < cnt: 
                        return False
                    
                    count[card + i] -= cnt
        
        return True
        



        