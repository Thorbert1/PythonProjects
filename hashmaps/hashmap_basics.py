class Solution:
  def main(self):
    result = self.twoNum(nums = [2,4,6,8,8], target = 8)
    print(result)

  def twoNum(self, nums: list[int], target: int) -> list[int]:
    numMap = {} #creates a hashmap to search from (hashmap = a data type that stores key-value pairs)
    n = len(nums) #creates a counter variable to store number of iterations
    for i in range(n):
      if nums[i] not in numMap: #if the i-th element is not in the hash table,
        numMap[nums[i]] = i     #assign the element who's index is the i-th element a value of i
    return numMap


if __name__ == "__main__":
  solution = Solution()
  solution.main()