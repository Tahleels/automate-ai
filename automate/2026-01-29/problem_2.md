Here's a unique DSA problem:

---

### 1. Title
**Even Frequency Substring**

### 2. Problem Statement
You are given a string `S` consisting of lowercase English letters. Your task is to find the length of the *shortest non-empty substring* of `S` such that every character present within that substring appears an *even* number of times. If no such substring exists, return -1.

### 3. Constraints
* `1 <= S.length <= 10^5`
* `S` consists only of lowercase English letters (`'a'` through `'z'`).

### 4. Example

**Input:**
`S = "banana"`

**Output:**
`4`

**Explanation:**
Let's analyze the substrings and their character counts:
- "b": 'b':1 (odd)
- "ba": 'b':1, 'a':1 (odd, odd)
- "ban": 'b':1, 'a':1, 'n':1 (odd, odd, odd)
- "bana": 'b':1, 'a':2, 'n':1 (odd, even, odd)
- "banan": 'b':1, 'a':2, 'n':2 (odd, even, even)
- "banana": 'b':1, 'a':3, 'n':2 (odd, odd, even)

Consider other substrings:
- "an": 'a':1, 'n':1 (odd, odd)
- **"anan"**: 'a':2, 'n':2 (even, even). This substring is valid and its length is 4.
- "nana": 'n':2, 'a':2 (even, even). This substring is also valid and its length is 4.

There is no valid substring with length less than 4. For example:
- "aa" (if `S` had it): 'a':2 (even). Length 2. This would be a valid candidate.
Since "anan" and "nana" are the shortest valid substrings, the answer is 4.