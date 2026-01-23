The problem "Adjacent Sum Purge" asks us to repeatedly remove pairs of adjacent digits from a string if their sum is an even number. This process continues until no more such pairs can be removed.

### Understanding the Core Rule

The key condition is "if any two adjacent digits `x` and `y` have an *even sum*". Let's analyze when `x + y` is even:
*   `Even + Even = Even` (e.g., `2 + 4 = 6`)
*   `Odd + Odd = Even` (e.g., `1 + 3 = 4`)
*   `Even + Odd = Odd` (e.g., `2 + 3 = 5`)
*   `Odd + Even = Odd` (e.g., `1 + 2 = 3`)

From this, we can conclude that `x + y` is even if and only if `x` and `y` have the *same parity* (both even or both odd). If they have different parities, their sum is odd.

So, the rule simplifies to: **Remove two adjacent digits if they have the same parity.**

The repeated removal and concatenation nature of the problem, where removals can trigger new adjacencies that need to be checked, is a classic indicator for a **stack-based approach**.

### Approach: Using a Stack

We can process the input string `s` from left to right using a stack to build our result. The stack will effectively maintain the current "unpurged" sequence of digits.

Here's how the stack logic works:

1.  **Initialization:** Create an empty list, `stack`, which will function as our stack. It will store digits (as characters) that have not been removed.

2.  **Iterate through the input string `s`:** For each `char_digit` in `s`:
    *   **Convert to Integer:** Convert `char_digit` to an integer `current_digit_val` to easily check its parity.
    *   **Check Stack:**
        *   **If the stack is NOT empty:** This means there's a previous digit to form an adjacent pair with.
            *   Get the `last_char_on_stack` (the top element of the stack, `stack[-1]`).
            *   Convert `last_char_on_stack` to an integer `last_digit_val`.
            *   **Compare Parities:** Check if `(current_digit_val % 2)` is equal to `(last_digit_val % 2)`.
                *   **If parities are the same (even sum condition met):** Both digits are removed. We simulate removing `last_digit_val` by `pop()`ing it from the stack. We simulate removing `current_digit_val` by simply *not* pushing it onto the stack.
                *   **If parities are different (odd sum):** No removal occurs. We push `char_digit` onto the stack, as it becomes part of the current result.
        *   **If the stack IS empty:** There's no preceding digit to form a pair with. In this case, the `current_digit_val` simply gets pushed onto the stack.

3.  **Final Result:** After processing all characters in `s`, the `stack` contains the characters that remain. Join these characters together to form the final string.

### Example Walkthrough (`s = "1221"`)

1.  `stack = []`
2.  `char_digit = '1'`, `current_digit_val = 1`. Stack is empty. Push '1'.
    `stack = ['1']`
3.  `char_digit = '2'`, `current_digit_val = 2`.
    Stack is `['1']`. `last_digit_val = 1`.
    `1` (odd) and `2` (even) have different parities. Push '2'.
    `stack = ['1', '2']`
4.  `char_digit = '2'`, `current_digit_val = 2`.
    Stack is `['1', '2']`. `last_digit_val = 2`.
    `2` (even) and `2` (even) have the same parity. Pop from stack. Don't push current '2'.
    `stack = ['1']`
5.  `char_digit = '1'`, `current_digit_val = 1`.
    Stack is `['1']`. `last_digit_val = 1`.
    `1` (odd) and `1` (odd) have the same parity. Pop from stack. Don't push current '1'.
    `stack = []`
6.  End of string. Join stack elements: `"".join([])` which is `""`.

### Note on Problem Example Discrepancy

The problem statement's example for `s = "1357"` gives `output = "1357"` with the explanation "All sums are odd." However, based on our derived rule (same parity means even sum):
*   `1` (odd) and `3` (odd) have the same parity (`1+3=4`, even).
*   `3` (odd) and `5` (odd) have the same parity (`3+5=8`, even).
*   `5` (odd) and `7` (odd) have the same parity (`5+7=12`, even).

Following the stack logic for `s = "1357"`:
1. `stack = []`
2. `char='1'`. Push '1'. `stack=['1']`.
3. `char='3'`. `last='1'`. Same parity. Pop. `stack=[]`.
4. `char='5'`. Stack empty. Push '5'. `stack=['5']`.
5. `char='7'`. `last='5'`. Same parity. Pop. `stack=[]`.
Final output: `""`.

My solution follows the rule strictly, leading to `""` for `"1357"`. This suggests the example table might have an error for `"1357"`.

### Complexity Analysis

*   **Time Complexity: O(N)**
    *   We iterate through the input string `s` once, where `N` is the length of `s`.
    *   For each character, we perform a few constant-time operations: integer conversion, parity check, and stack operations (`append`, `pop`, accessing `[-1]`).
    *   Python's list `append` and `pop` from the end are amortized O(1) operations.
    *   Therefore, the total time complexity is linear with the length of the string.

*   **Space Complexity: O(N)**
    *   In the worst case (e.g., `s = "121212"`), no pairs have the same parity, so no elements are ever removed from the stack. The stack will grow to store all `N` characters of the input string.
    *   Thus, the space complexity is proportional to the length of the input string.