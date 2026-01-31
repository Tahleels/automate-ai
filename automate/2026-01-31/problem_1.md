Here's a unique DSA problem:

---

### 1. Title
**Balanced Alternating Subarray**

### 2. Problem Statement
You are given an array of positive integers `nums`.

A subarray is considered **alternating** if no two adjacent elements within it are equal (i.e., `nums[i] != nums[i+1]` for all `i` in the subarray's range). For example, `[1, 2, 1]` is alternating, but `[1, 2, 2]` is not. A single-element subarray is always alternating.

A subarray is considered **balanced** if the count of even numbers within it is equal to the count of odd numbers within it.

Your task is to find the **length of the longest subarray** that is both **alternating** and **balanced**. If no such subarray exists (e.g., if no single-element subarray can ever be balanced, which can't happen as odd/even counts would be 1/0 or 0/1), or if `nums` is empty, return 0.

### 3. Constraints
*   `1 <= nums.length <= 10^5`
*   `1 <= nums[i] <= 10^9`

### 4. Example

**Example 1:**
`nums = [1, 2, 3, 2, 1, 4]`

**Explanation:**
Let's analyze some subarrays:
*   `[1]` - Alternating. Not balanced (1 odd, 0 even).
*   `[1, 2]` - Alternating (`1 != 2`). Balanced (1 odd, 1 even). Length = 2.
*   `[1, 2, 3]` - Alternating (`1 != 2`, `2 != 3`). Not balanced (2 odd, 1 even).
*   `[1, 2, 3, 2]` - Alternating (`1!=2`, `2!=3`, `3!=2`). Balanced (2 odd, 2 even). Length = 4.
*   `[1, 2, 3, 2, 1]` - Alternating. Not balanced (3 odd, 2 even).
*   `[1, 2, 3, 2, 1, 4]` - Alternating (`1!=2`, `2!=3`, `3!=2`, `2!=1`, `1!=4`). Balanced (3 odd, 3 even). Length = 6.

*   `[2, 3]` - Alternating (`2 != 3`). Balanced (1 even, 1 odd). Length = 2.

The longest subarray that is both alternating and balanced is `[1, 2, 3, 2, 1, 4]`, with a length of 6.

**Output:** `6`

---

**Example 2:**
`nums = [1, 2, 2, 3, 4]`

**Explanation:**
*   `[1, 2]` - Alternating. Balanced. Length = 2.
*   When we reach `nums[2]` (which is `2`), `nums[2] == nums[1]`. The alternating property is broken for any subarray ending at `2` and starting before `2`.
*   We then consider new alternating subarrays starting from `nums[2]`.
*   `[2]` - Alternating. Not balanced.
*   `[2, 3]` - Alternating. Balanced. Length = 2.
*   `[2, 3, 4]` - Alternating. Not balanced (1 odd, 2 even).

The longest subarray is `[1, 2]` or `[2, 3]`, both with a length of 2.

**Output:** `2`