Here is a unique DSA problem:

---

### 1. Title
Balanced Unique Split

### 2. Problem Statement
You are given an array of integers `nums`. Your task is to find the number of ways to split the array into two non-empty contiguous subarrays, `left` and `right`, such that the number of distinct elements in `left` is equal to the number of distinct elements in `right`.

A split point `i` (0-indexed) means:
- The `left` subarray consists of elements `nums[0]` through `nums[i]`.
- The `right` subarray consists of elements `nums[i+1]` through `nums[n-1]`, where `n` is the length of `nums`.

You need to return the total count of such valid split points.

### 3. Constraints
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^9`

### 4. Example

**Input:**
`nums = [1, 2, 1, 3, 2]`

**Output:**
`1`

**Explanation:**

Let's denote `distinct(subarray)` as the number of unique elements in that subarray.

1. **Split at `i = 0`:**
   - `left` = `[1]` (distinct: 1)
   - `right` = `[2, 1, 3, 2]` (distinct: 3, which are {1, 2, 3})
   - `1 != 3`. Not a valid split.

2. **Split at `i = 1`:**
   - `left` = `[1, 2]` (distinct: 2, which are {1, 2})
   - `right` = `[1, 3, 2]` (distinct: 3, which are {1, 2, 3})
   - `2 != 3`. Not a valid split.

3. **Split at `i = 2`:**
   - `left` = `[1, 2, 1]` (distinct: 2, which are {1, 2})
   - `right` = `[3, 2]` (distinct: 2, which are {2, 3})
   - `2 == 2`. This is a valid split. Count = 1.

4. **Split at `i = 3`:**
   - `left` = `[1, 2, 1, 3]` (distinct: 3, which are {1, 2, 3})
   - `right` = `[2]` (distinct: 1, which is {2})
   - `3 != 1`. Not a valid split.

There is only one valid split point (`i=2`), so the total count is `1`.