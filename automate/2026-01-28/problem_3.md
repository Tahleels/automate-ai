Here is a unique DSA problem:

---

### 1. Title: Balanced Parity Halves Subarrays

### 2. Problem Statement:
You are given an array of positive integers `nums`. Your task is to find the number of subarrays `[i, j]` (where `0 <= i <= j < N`, and `N` is the length of `nums`) that satisfy a specific "balanced parity" condition.

The condition is as follows:
If a subarray `nums[i...j]` is conceptually divided into two parts:
1.  **Left Part**: `nums[i]` to `nums[mid]` (inclusive)
2.  **Right Part**: `nums[mid+1]` to `nums[j]` (inclusive)
where `mid` is calculated as `i + (j - i) / 2` using integer division.

Then, the subarray `nums[i...j]` is considered "balanced" if and only if both of the following two conditions are met:
*   The count of even numbers in the **Left Part** is equal to the count of odd numbers in the **Right Part**.
*   The count of odd numbers in the **Left Part** is equal to the count of even numbers in the **Right Part**.

**Note:**
*   If the **Right Part** is empty (i.e., `mid+1 > j`), then its count of even numbers and count of odd numbers are both considered to be zero.
*   Subarrays of length 1 (where `i == j`) will always result in an empty Right Part. As a consequence, they can never satisfy the balanced parity conditions (e.g., if `nums[i]` is even, then `1 == 0` for the first condition is false).

Return the total count of such balanced subarrays.

### 3. Constraints:
*   `1 <= N <= 2000`
*   `1 <= nums[k] <= 10^9` for all `0 <= k < N`

### 4. Example:

**Input:** `nums = [1, 2, 3, 4]`

**Output:** `4`

**Explanation:**
Let's analyze all possible subarrays and their balanced parity:

*   **Subarray `[1]` (i=0, j=0):**
    *   `mid = 0 + (0-0)/2 = 0`.
    *   Left Part: `[1]`. Counts: Even=0, Odd=1.
    *   Right Part: Empty. Counts: Even=0, Odd=0.
    *   Conditions: `0 == 0` (True), `1 == 0` (False). Not balanced.

*   **Subarray `[1, 2]` (i=0, j=1):**
    *   `mid = 0 + (1-0)/2 = 0`.
    *   Left Part: `[1]`. Counts: Even=0, Odd=1.
    *   Right Part: `[2]`. Counts: Even=1, Odd=0.
    *   Conditions: `0 == 0` (True), `1 == 1` (True). **Balanced!**

*   **Subarray `[1, 2, 3]` (i=0, j=2):**
    *   `mid = 0 + (2-0)/2 = 1`.
    *   Left Part: `[1, 2]`. Counts: Even=1, Odd=1.
    *   Right Part: `[3]`. Counts: Even=0, Odd=1.
    *   Conditions: `1 == 1` (True), `1 == 0` (False). Not balanced.

*   **Subarray `[1, 2, 3, 4]` (i=0, j=3):**
    *   `mid = 0 + (3-0)/2 = 1`.
    *   Left Part: `[1, 2]`. Counts: Even=1, Odd=1.
    *   Right Part: `[3, 4]`. Counts: Even=1, Odd=1.
    *   Conditions: `1 == 1` (True), `1 == 1` (True). **Balanced!**

*   **Subarray `[2]` (i=1, j=1):** Not balanced (similar to `[1]`).

*   **Subarray `[2, 3]` (i=1, j=2):**
    *   `mid = 1 + (2-1)/2 = 1`.
    *   Left Part: `[2]`. Counts: Even=1, Odd=0.
    *   Right Part: `[3]`. Counts: Even=0, Odd=1.
    *   Conditions: `1 == 1` (True), `0 == 0` (True). **Balanced!**

*   **Subarray `[2, 3, 4]` (i=1, j=3):**
    *   `mid = 1 + (3-1)/2 = 2`.
    *   Left Part: `[2, 3]`. Counts: Even=1, Odd=1.
    *   Right Part: `[4]`. Counts: Even=1, Odd=0.
    *   Conditions: `1 == 0` (False), `1 == 1` (True). Not balanced.

*   **Subarray `[3]` (i=2, j=2):** Not balanced.

*   **Subarray `[3, 4]` (i=2, j=3):**
    *   `mid = 2 + (3-2)/2 = 2`.
    *   Left Part: `[3]`. Counts: Even=0, Odd=1.
    *   Right Part: `[4]`. Counts: Even=1, Odd=0.
    *   Conditions: `0 == 0` (True), `1 == 1` (True). **Balanced!**

*   **Subarray `[4]` (i=3, j=3):** Not balanced.

The total count of balanced subarrays is 4.