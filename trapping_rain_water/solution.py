def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    n = len(height)
    water = 0
    leftmax = rightmax = 0
    left = 0
    right = n - 1
    while left <= right:
        if height[left] <= height[right]:
            water += max(0, leftmax - height[left])
            leftmax = max(leftmax, height[left])
            left += 1
        else:
            water += max(0,rightmax - height[right])
            rightmax = max(rightmax, height[right])
            right -= 1
    return water

    