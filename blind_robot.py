"""
// Time Complexity : O(n)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No

// Your code here along with comments explaining your approach
Algorithm Explanation
Given below
"""

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        """
        directions = G, L, R
        
        
        |
        0,0 
        
        
        eg GGLLGG 
        
        
         |
      |  |
      |  S-|
        
        
        Cases
        - Only one direction - false
        
        directions array represented in x-y form(considering origin as starting point) - {(0,1) - N,(-1,0) - W,(0,-1) - S,(1,0) - E} ->anticlockwise movement ( do any one movement only)
        N
        |
     W-   -E
        |
        S
        
        So the main detecting scenario is 
        a) If the new position is at origin after executing the instructions
        b) OR if the new position doesn't point towards north -> direction_ptr = 0
        
        Iterator updates for L,R,G
        L = direction_ptr -> (direction_ptr + 1 ) % 4 -> to cover all the direction in a cycle
        R = direction_ptr -> (direction_ptr + 3) % 4 ->  reverse direction so need to cover all three directions before coming to w for right and anticlockwise sense -> N ->"R" > E(3)
        G = update the x and y coordinate of original position based on current direction ptr
        """
        
        #direction array in anticlockwise sense
        dirs = [[0,1],[-1,0],[0,-1],[1,0]]
        
        origin_x,origin_y = 0,0
        
        direction_ptr = 0
        for instruction in instructions:
            if instruction == "L":
                direction_ptr = (direction_ptr + 1) % 4
            elif instruction == "R":
                direction_ptr = (direction_ptr + 3) % 4
            else:
                origin_x += dirs[direction_ptr][0]
                origin_y += dirs[direction_ptr][1]
        
        
        return origin_x == origin_y == 0 or direction_ptr !=0