Here is a unique DSA problem:

---

### 1. Title: Balanced Parentheses with Even Digit Sum

### 2. Problem Statement:

Given a string `s` consisting of opening parentheses `(`, closing parentheses `)`, and digits `0-9`. Your task is to find the length of the longest substring of `s` that satisfies two conditions:

1.  **Valid Parentheses Sequence:** The substring must be a "valid parentheses sequence". This means:
    *   Every opening parenthesis has a corresponding closing parenthesis.
    *   Parentheses are correctly nested.
    *   Digits are ignored for the purpose of parenthesis validation. For example, `(12)` is a valid sequence, as is `(1(2))`.
    *   An empty string is not considered a valid parentheses sequence. A single digit or a sequence of digits without any parentheses is also not a valid parentheses sequence.

2.  **Even Digit Sum:** The sum of all digits present within that valid parentheses substring must be an even number. For example, `(12)` has digit sum `1 + 2 = 3` (odd), while `(13)` has digit sum `1 + 3 = 4` (even). Note that 0 is an even number, so a valid parentheses sequence with no digits (e.g., `()`) would have a digit sum of 0, satisfying this condition.

Return the length of the longest such substring. If no such substring exists, return 0.

### 3. Constraints:

*   `1 <= s.length <= 5000`
*   `s` consists only of characters `(`, `)`, and `0-9`.

### 4. Example:

**Example 1:**

Input: `s = "((12)3)4)"`

Output: `9`

Explanation:
Let's consider relevant substrings and check the conditions:

*   `"(12)"` (from index 1 to 4):
    *   Valid Parentheses: Yes.
    *   Digit Sum: `1 + 2 = 3` (odd).
    *   Not a candidate.

*   `"((12)3)"` (from index 0 to 6):
    *   Valid Parentheses: Yes.
    *   Digit Sum: `1 + 2 + 3 = 6` (even).
    *   Length: `7`. This is a candidate.

*   `"((12)3)4)"` (from index 0 to 8):
    *   Valid Parentheses: Yes.
    *   Digit Sum: `1 + 2 + 3 + 4 = 10` (even).
    *   Length: `9`. This is a candidate.

The longest substring satisfying both conditions is `((12)3)4)`, with a length of `9`.

---

**Example 2:**

Input: `s = "()1(2)"`

Output: `3`

Explanation:
Let's consider relevant substrings and check the conditions:

*   `()` (from index 0 to 1):
    *   Valid Parentheses: Yes.
    *   Digit Sum: `0` (even).
    *   Length: `2`. This is a candidate.

*   `(2)` (from index 3 to 4):
    *   Valid Parentheses: Yes.
    *   Digit Sum: `2` (even).
    *   Length: `3`. This is a candidate.

The longest substring satisfying both conditions is `(2)`, with a length of `3`.