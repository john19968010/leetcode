
## Leetcode description
https://leetcode.com/problems/average-of-levels-in-binary-tree/

### Intro:
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.

### Example
Example 1:  
    Input: root = [3,9,20,null,null,15,7]
    Output: [3.00000,14.50000,11.00000]

 
## My idea

### First Try (Correct)
Intro: BFS problem, and get the level's average

Outcome: Correct, Running time 44ms(62.24%), Memory usage 18.50MB(59.54%), not good enough.

code: [here](1.py)


### Second Try (Correct)
Intro: Maybe it is not necessary to create a temp_queues, so use range() feature to run the max times of process in queue.

Outcome: Correct, Running time 40ms(82.24%),  Memory usage 18.62MB(7.28%), 
    Due to python list characteristic(Dynamic size increase) so the memory usage increase.
code: [here](2.py)
