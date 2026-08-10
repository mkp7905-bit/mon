from fastapi import FastAPI

app = FastAPI()

@app.post("/two_sum")
def two_sum_brute_force(nums: list[int], target: int) -> list[int]:
    # """
    # Brute force approach to find two indices such that nums[i] + nums[j] == target.
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    # """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


@app.post("/two_sum_optimal_approach")
def two_sum_optimal_approach( nums: list[int], target: int) -> list[int]:
    # """
    # Optimal approach to find two indices such that nums[i] + nums[j] == target.
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # """
     preMap = {}
     for i, num in enumerate(nums):
      diff = target - num
      if diff in preMap:
        return [preMap[diff], i]
     preMap[num] = i
     return []
      