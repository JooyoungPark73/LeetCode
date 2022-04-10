class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort(reverse=True)
        while len(stones) > 1:
            stones.sort(reverse=True)
            stones = self.collide(stones)
            while stones.count(0) != 0:
                stones.pop()

        stones.sort(reverse=True)
        if len(stones) == 1:
            return stones[0]
        elif len(stones) == 0:
            return 0
        else:
            assert len(stones) > 1

    def collide(self, stones: list[int]):
        tmp = stones[0]
        stones[0] = stones[0] - stones[1]
        stones[1] = stones[1] - tmp

        if stones[0] < 0:
            stones[0] = 0
        if stones[1] < 0:
            stones[1] = 0

        stones.sort(reverse = True)

        return stones