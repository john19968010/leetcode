
## Leetcode description
not on Leetcode, just curious what BFS can do, and ask ChatGPT to give me a real word question

### Intro:
Assume that there is at least one solution of a maze, the start position is (0,0), and the end position is (rows-1, cols-1), 
and 1 is wall, 0 is path, find the way out path.

### Example
Example 1:  
    Input: root = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
    ]
    Output: [[(0, 0), (1, 0), (2, 1), (2, 2), (2, 3), (3, 4), (4, 4)]]

 
## My idea

### First Try (Correct)
Intro: BFS problem, but needs to record the path down, so the content in queue would be like [(x, y), [the way path]]

Outcome: Correct. but it take a while to find the content structure in queue.

code: [here](1.py)


