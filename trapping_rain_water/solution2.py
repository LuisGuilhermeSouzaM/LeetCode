from sys import maxsize
class Solution:

    def trap(self, height):
            max_h = get_max_height_index(height)
            return trapping_rain_water(height, 0, max_h, 1) + trapping_rain_water(height, len(height) - 1, max_h, -1)

def trapping_rain_water(height,  begin, end, step):
            sum = 0
            highest_seen = -maxsize-1
            for i in range(begin, end, step):
                if(height[i] >= highest_seen):
                    highest_seen = height[i]
                else:
                    sum += highest_seen - height[i]
            return sum;

def get_max_height_index(height):
        max_height_index = 0
        max_height = height[0]
        for i in range(len(height)):
            if(height[i] > max_height):
                max_height = height[i]
                max_height_index = i
        return max_height_index