
## Leetcode description
https://leetcode.com/problems/sum-root-to-leaf-numbers/

### Intro:
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.


### Example
Example 1:  
    Input: root = [4,9,0,5,1]
    Output: 1026
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
 
## My idea

### Frist Try (Correct)
Intro: Calculating the sum of all leaf numbers from the root, using DFS pre-order traversal to solve this problem.

Outcome: Correct, create an variable(ans) in class `__init__` is faster than, use a list to record all leaf and put it in travel helper function

code: [here](1.py)




