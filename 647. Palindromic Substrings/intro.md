
## Leetcode description
https://leetcode.com/problems/palindromic-substrings/

### Intro:
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

### Example
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

 
## My idea

### First Try (Wrong)
Intro: BFS problem, Find the Substring, and calculate by divided to 2 e.g 'abcba' -> 5 // 2 = 2, it has 2 answers (abcba, bcb)

Outcome: Wrong, calculated part is wrong, e.g aabaa is more that 2 answers (aabaa, aa, aa, aba)

code: [here](1.py)


### Second Try (Correct)
Intro: Find the formula, and using the formula + DP to get the answer

Outcome: Correct, Running time 246ms Beats 32.38%,  Memory usage 24.49MB Beats 22.35%
    Seem there is still a room to improve.
code: [here](2.py)
