from typing import *

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        position = [0, 0]
        direction = "up"

        for v in instructions:
            if direction == "up":
                if v == "G":
                    position[1] += 1
                elif v == "L":
                    direction = "left"
                elif v == "R":
                    direction = "right"
            elif direction == "left":
                if v == "G":
                    position[0] -= 1
                elif v == "L":
                    direction = "down"
                elif v == "R":
                    direction = "up"
            elif direction == "right":
                if v == "G":
                    position[0] += 1
                elif v == "L":
                    direction = "up"
                elif v == "R":
                    direction = "down"
            elif direction == "down":
                if v == "G":
                    position[1] -= 1
                elif v == "L":
                    direction = "right"
                elif v == "R":
                    direction = "left"

        if position != [0, 0] and direction == "up":
            return False
        else:
            return True