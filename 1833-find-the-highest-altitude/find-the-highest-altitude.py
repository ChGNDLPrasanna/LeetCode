class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current = 0
        highest = 0

        for value in gain:
            current = current + value

            if current > highest:
                highest = current

        return highest