
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


<!-- ### Second Try (Correct)
Intro: Maybe it is not necessary to create a temp_queues, so use range() feature to run the max times of process in queue.

Outcome: Correct, Running time 40ms(82.24%),  Memory usage 18.62MB(7.28%), 
    Due to python list characteristic(Dynamic size increase) so the memory usage increase.
code: [here](2.py) -->
