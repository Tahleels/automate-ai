Here is a unique DSA problem:

---

### 1. Title: Balanced Numeric Parentheses Subarrays

### 2. Problem Statement:
You are given an array of non-zero integers `arr`. In this array, a positive integer `X` acts as an "opening parenthesis" and its absolute negative counterpart `-X` acts as a "closing parenthesis". For example, `1` opens and `-1` closes, `5` opens and `-5` closes.

Your task is to count the total number of subarrays `arr[i...j]` (where `0 <= i <= j < arr.length`) that are "balanced". A subarray is considered balanced if, when processed from left to right, all its elements form properly matched and nested pairs.

Specifically, the rules for checking a subarray `arr_sub` for balance are:
1. Initialize an empty stack.
2. Iterate through each element `val` in `arr_sub`:
   - If `val > 0` (an opening parenthesis), push `val` onto the stack.
   - If `val < 0` (a closing parenthesis), let `expected_open = -val`.
     - If the stack is empty or its top element is not `expected_open`, the subarray `arr_sub` is immediately **unbalanced**. You can stop processing this subarray.
     - Otherwise (stack is not empty and `stack.top() == expected_open`), pop the top element from the stack.
3. After processing all elements in `arr_sub`:
   - If the stack is empty, the subarray `arr_sub` is **balanced**.
   - If the stack is not empty, the subarray `arr_sub` is **unbalanced** (due to unmatched opening parentheses).

Return the total count of such balanced subarrays.

### 3. Constraints:
- `1 <= arr.length <= 2000`
- `-1000 <= arr[i] <= 1000`
- `arr[i] != 0` for all `i`.

### 4. Example:
Input: `arr = [1, 2, -2, -1, 3, -3]`

Output: `4`

Explanation:
Let's analyze the subarrays for balance:

1.  **`[2, -2]`** (from index 1 to 2):
    - Process `2`: Push `2`. Stack: `[2]`
    - Process `-2`: `expected_open = 2`. Stack top is `2`. Pop `2`. Stack: `[]`
    - End of subarray. Stack is empty. **Balanced!** (Count = 1)

2.  **`[3, -3]`** (from index 4 to 5):
    - Process `3`: Push `3`. Stack: `[3]`
    - Process `-3`: `expected_open = 3`. Stack top is `3`. Pop `3`. Stack: `[]`
    - End of subarray. Stack is empty. **Balanced!** (Count = 2)

3.  **`[1, 2, -2, -1]`** (from index 0 to 3):
    - Process `1`: Push `1`. Stack: `[1]`
    - Process `2`: Push `2`. Stack: `[1, 2]`
    - Process `-2`: `expected_open = 2`. Stack top is `2`. Pop `2`. Stack: `[1]`
    - Process `-1`: `expected_open = 1`. Stack top is `1`. Pop `1`. Stack: `[]`
    - End of subarray. Stack is empty. **Balanced!** (Count = 3)

4.  **`[1, 2, -2, -1, 3, -3]`** (from index 0 to 5):
    - Process `1`: Push `1`. Stack: `[1]`
    - Process `2`: Push `2`. Stack: `[1, 2]`
    - Process `-2`: `expected_open = 2`. Stack top is `2`. Pop `2`. Stack: `[1]`
    - Process `-1`: `expected_open = 1`. Stack top is `1`. Pop `1`. Stack: `[]`
    - Process `3`: Push `3`. Stack: `[3]`
    - Process `-3`: `expected_open = 3`. Stack top is `3`. Pop `3`. Stack: `[]`
    - End of subarray. Stack is empty. **Balanced!** (Count = 4)

All other subarrays are unbalanced. For instance:
- `[1]` : Stack `[1]` at end. Not balanced.
- `[-2]` : Stack is empty when `-2` is encountered. Not balanced.
- `[1, -1, 2]` : Stack `[2]` at end. Not balanced.
- `[1, 2, -1]` : `expected_open = 1`. Stack top `2` != `1`. Not balanced.