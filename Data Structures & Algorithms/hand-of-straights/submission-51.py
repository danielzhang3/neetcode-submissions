class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        groupMap = {}

        for card in hand: 
            groupMap[card] = 1 + groupMap.get(card, 0)
        
        for card in sorted(groupMap): 
            cnt = groupMap[card]

            if cnt > 0: 
                for i in range(groupSize): 
                    if groupMap.get(card + i, 0) < cnt: 
                        return False

                    groupMap[card + i] -= cnt
        
        return True
        