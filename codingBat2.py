#Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.

def count_evens(nums):
  count = 0
  for num in nums:
      if num % 2 == 0:
          count += 1
  return count


#Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.


def has22(nums):
  for i in range(len(nums) - 1):
    if nums[i] == 2 and nums[i + 1] == 2:
       return True
  return False


#When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.

def cigar_party(cigars, is_weekend):
  if is_weekend:
    return cigars >= 40
  else:
    return 40 <= cigars <= 60

