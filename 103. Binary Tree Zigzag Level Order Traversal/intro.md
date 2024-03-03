
## Leetcode description
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

### Intro:
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

### Example
Example 1:  
    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[20,9],[15,7]]
Example 2:
    Input: root = [1]
    Output: [[1]]
Example 3:
    Input: root = []
    Output: []
 
## My idea

### Frist Try (Wrong)
Intro: At the beginning, i do not know the different between `Breadth-First Tree Traversal` and `Depth-First Tree Traversal`, 
the only thing i know is BT can has  `root` -> `left` ->`right` this order(actually this is `preorder` in DFT).
So my idea is writing a function using DFT's preorder then using the position(1 is first level, 2~3 is sec, 4~7 is third....) to get the answer. 

Outcome: Definitely wrong !!!!! `DFT-preorder` traverses the nodes from left to right, not level by level.

code: [here](1.py)
