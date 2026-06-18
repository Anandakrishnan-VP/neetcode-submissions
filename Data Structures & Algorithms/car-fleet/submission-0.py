class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = [] #pos and speed
        cars = sorted(zip(position,speed), reverse = True)
        #at = target - position / speed

        for c in cars:
            at = (target - c[0]) / c[1]
            if stack and stack[-1] >= at:
                continue
            stack.append(at)
        return len(stack)
        