Here is a unique DSA problem:

---

1.  **Title:** Even Character Parentheses Substring

2.  **Problem Statement:**
    You are given a string `S` consisting of lowercase English letters and parentheses `'('` and `')'`.
    Your task is to find the length of the longest substring of `S` that satisfies two conditions:
    1.  The substring is a **valid parenthesis string**. A string is a valid parenthesis string if:
        *   It is empty.
        *   It is `(A)`, where `A` is a valid parenthesis string.
        *   It is `AB`, where `A` and `B` are valid parenthesis strings.
    2.  The substring is **character-balanced**. A substring is character-balanced if, for every lowercase English letter (from 'a' to 'z'), its total count within the substring is an even number. If a letter does not appear, its count is 0, which is an even number. Parentheses themselves do not count towards character balance.

    Return the maximum length of such a substring. If no such substring exists, return 0.

3.  **Constraints:**
    *   `1 <= S.length <= 10^5`
    *   `S` consists only of lowercase English letters `('a'-'z')`, `'('`, and `')'`.

4.  **Examples:**

    *   **Input:** `S = "a(b)(ba)"`
    *   **Output:** `0`
    *   **Explanation:**
        *   Valid parenthesis substrings and their character counts:
            *   `"(b)"` (indices 1 to 3): Contains 'b' once. Count of 'b' is 1 (odd). Not character-balanced.
            *   `"(ba)"` (indices 4 to 7): Contains 'b' once, 'a' once. Counts are 1 for both (odd). Not character-balanced.
            *   `"(b)(ba)"` (indices 1 to 7): Contains 'b' twice, 'a' once. Count of 'b' is 2 (even), count of 'a' is 1 (odd). Not character-balanced.
        *   No valid parenthesis substring is character-balanced. Hence, the answer is 0.

    *   **Input:** `S = "(aa)(a)"`
    *   **Output:** `4`
    *   **Explanation:**
        *   `"(aa)"` (indices 0 to 3): Valid parenthesis string. Contains 'a' twice. Count of 'a' is 2 (even). This substring is character-balanced. Its length is 4.
        *   `"(a)"` (indices 4 to 6): Valid parenthesis string. Contains 'a' once. Count of 'a' is 1 (odd). Not character-balanced.
        *   `"(aa)(a)"` (indices 0 to 6): Valid parenthesis string. Contains 'a' three times. Count of 'a' is 3 (odd). Not character-balanced.
        *   The longest valid and character-balanced substring is `"(aa)"` with length 4.

    *   **Input:** `S = "((()))"`
    *   **Output:** `6`
    *   **Explanation:**
        *   The entire string `((()))` is a valid parenthesis string.
        *   It contains no lowercase letters. Thus, all character counts are 0, which is an even number. It is character-balanced.
        *   The length is 6.

    *   **Input:** `S = "a()b"`
    *   **Output:** `2`
    *   **Explanation:**
        *   `"()"` (indices 1 to 2): Valid parenthesis string. Contains no lowercase letters. Character counts are all 0 (even). This substring is character-balanced. Its length is 2.
        *   No longer valid parenthesis substring is character-balanced. For example, `a()b` is not a valid parenthesis string.