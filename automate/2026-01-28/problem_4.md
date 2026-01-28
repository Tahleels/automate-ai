Here's a unique DSA problem:

---

### 1. Title
**Alternating Parity Subarray Count**

### 2. Problem Statement
You are given an array of integers `nums` and an integer `k`. Your task is to find the number of subarrays of `nums` of length exactly `k` such that if we consider the elements within the subarray using 0-based *relative indices*, the sum of elements at **even** relative indices equals the sum of elements at **odd** relative indices.

**Definition of relative indices:**
For a subarray `[a, b, c, d, e]`:
- `a` is at relative index 0 (even)
- `b` is at relative index 1 (odd)
- `c` is at relative index 2 (even)
- `d` is at relative index 3 (odd)
- `e` is at relative index 4 (even)

The condition for the subarray `[a, b, c, d, e]` would be `a + c + e == b + d`.

### 3. Constraints
*   `1 <= nums.length <= 10^5`
*   `1 <= k <= nums.length`
*   `-10^9 <= nums[i] <= 10^9`

### 4. Example

**Input:**
`nums = [0, 1, 2, 1, 3]`
`k = 3`

**Output:**
`1`

**Explanation:**

Let's analyze all subarrays of length `k = 3`:

1.  **Subarray: `[0, 1, 2]`** (from `nums[0]` to `nums[2]`)
    *   Elements at even relative indices: `nums[0]=0` (relative index 0), `nums[2]=2` (relative index 2). Sum = `0 + 2 = 2`.
    *   Elements at odd relative indices: `nums[1]=1` (relative index 1). Sum = `1`.
    *   `2 != 1`. This subarray does not satisfy the condition.

2.  **Subarray: `[1, 2, 1]`** (from `nums[1]` to `nums[3]`)
    *   Elements at even relative indices: `nums[1]=1` (relative index 0), `nums[3]=1` (relative index 2). Sum = `1 + 1 = 2`.
    *   Elements at odd relative indices: `nums[2]=2` (relative index 1). Sum = `2`.
    *   `2 == 2`. This subarray **satisfies** the condition. Count = 1.

3.  **Subarray: `[2, 1, 3]`** (from `nums[2]` to `nums[4]`)
    *   Elements at even relative indices: `nums[2]=2` (relative index 0), `nums[4]=3` (relative index 2). Sum = `2 + 3 = 5`.
    *   Elements at odd relative indices: `nums[3]=1` (relative index 1). Sum = `1`.
    *   `5 != 1`. This subarray does not satisfy the condition.

Since only one subarray `[1, 2, 1]` satisfies the condition, the output is `1`.