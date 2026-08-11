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


#Reomve duplicate from sorted array

#brute force approach using a set
#time:O(n log n)
#space:O(n)
@app.post("/remove_duplicates_brute_force")
def remove_duplicates_brute_force(nums: list[int]):

   unique = list(set(nums))
   unique.sort()

   for i in range(len(unique)):
        nums[i] = unique[i]
        return len(unique)


@app.post("/remove_duplicates_optimal_approach")
def remove_duplicates_optimal_approach(nums: list[int]):
    # """
    # Optimal approach to remove duplicates from a sorted array.
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # """
    if not nums:
        return 0

    left=0
    for right in range(1, len(nums)):
        if nums[right] != nums[left]:
            left += 1
            nums[left] = nums[right]

    return left + 1
