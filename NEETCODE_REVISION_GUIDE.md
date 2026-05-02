# NeetCode Problems Revision Guide

## Table of Contents
- [Arrays & Hashing](#arrays--hashing)
- [Two Pointers](#two-pointers)
- [Sliding Window](#sliding-window)
- [Stack](#stack)
- [Binary Search](#binary-search)
- [Linked List](#linked-list)
- [Trees](#trees)
- [Tries](#tries)
- [Heap / Priority Queue](#heap--priority-queue)
- [Backtracking](#backtracking)
- [Graphs](#graphs)
- [Advanced Graphs](#advanced-graphs)
- [1-D Dynamic Programming](#1-d-dynamic-programming)
- [2-D Dynamic Programming](#2-d-dynamic-programming)
- [Greedy](#greedy)
- [Intervals](#intervals)
- [Math & Geometry](#math--geometry)
- [Bit Manipulation](#bit-manipulation)

---

## Arrays & Hashing

### Two Integer Sum
- Use hashmap to store `target - current_number` as key and index as value
- Check if current number exists in hashmap before adding complement
- Return indices when complement is found
- Time: O(n), Space: O(n)

### Anagram Groups
- Sort each string to create a key for grouping anagrams
- Use hashmap where key is sorted string, value is list of original strings
- All anagrams will have the same sorted representation
- Return list of all grouped values
- Time: O(n * m log m), Space: O(n * m)

### Top K Elements in List
- Use Counter to count frequency of each element
- Use heap to maintain k most frequent elements
- Can also use bucket sort approach for O(n) solution
- Return the k most frequent elements
- Time: O(n log k), Space: O(n)

### Products of Array Discluding Self
- Calculate prefix products from left to right
- Calculate suffix products from right to left while building result
- Multiply prefix and suffix products for each position
- Avoid division to handle zeros correctly
- Time: O(n), Space: O(1) excluding output array

### Valid Sudoku
- Use sets to track seen numbers in rows, columns, and 3x3 boxes
- For each cell, check if number already exists in corresponding row/col/box
- Box index calculated as `(row//3)*3 + col//3`
- Return false if any duplicate found
- Time: O(1) since 9x9 grid, Space: O(1)

### Longest Consecutive Sequence
- Use set for O(1) lookup of numbers
- For each number, check if it's start of sequence (no n-1 exists)
- If start, count consecutive numbers by incrementing
- Track maximum sequence length found
- Time: O(n), Space: O(n)

### Duplicate Integer
- Use set to track seen numbers
- Return true immediately when duplicate found
- Alternative: sort array and check adjacent elements
- Time: O(n), Space: O(n) for set approach

### Is Anagram
- Sort both strings and compare, or use character frequency count
- Two strings are anagrams if they have same character frequencies
- Can use array of size 26 for lowercase letters
- Time: O(n log n) for sorting, O(n) for counting

### Concatenation of Array
- Create result array of size 2*n
- Fill both halves with original array elements
- Use single loop with modulo operation for efficiency
- Time: O(n), Space: O(n)

---

## Two Pointers

### Two Integer Sum II
- Use two pointers from start and end of sorted array
- Move left pointer right if sum too small, right pointer left if sum too large
- Return indices when target sum found
- Works because array is sorted
- Time: O(n), Space: O(1)

### Three Integer Sum
- Sort array first to enable two-pointer technique
- Fix first element, use two pointers for remaining two elements
- Skip duplicates to avoid duplicate triplets
- For each fixed element, find pairs that sum to negative of fixed element
- Time: O(n²), Space: O(1)

### Max Water Container
- Use two pointers from both ends of array
- Calculate area with current pointers, update maximum
- Move pointer with smaller height inward (moving larger height won't improve area)
- Continue until pointers meet
- Time: O(n), Space: O(1)

### Trapping Rain Water
- Use two pointers with left_max and right_max tracking
- Move pointer with smaller max value inward
- Add trapped water based on difference between max and current height
- Water trapped depends on minimum of left and right boundaries
- Time: O(n), Space: O(1)

### Boats to Save People
- Sort people by weight, use two pointers
- Try to pair lightest and heaviest person in each boat
- If both can fit (weight ≤ limit), move both pointers
- Otherwise, only take heavier person and move right pointer
- Time: O(n log n), Space: O(1)

---

## Sliding Window

### Longest Substring Without Duplicates
- Use sliding window with set to track characters in current window
- Expand right pointer and add characters to set
- When duplicate found, shrink left pointer until duplicate removed
- Track maximum window size seen
- Time: O(n), Space: O(min(m,n)) where m is charset size

### Longest Repeating Substring with Replacement
- Use sliding window with character frequency map
- Track most frequent character in current window
- If window_size - max_frequency > k, shrink window from left
- Update maximum valid window size
- Time: O(n), Space: O(1) for fixed alphabet

### Minimum Window with Characters
- Use two hashmaps: one for target characters, one for window
- Expand window until all target characters included
- Then shrink from left while maintaining validity
- Track minimum valid window found
- Time: O(n), Space: O(m) where m is target string length

### Sliding Window Maximum
- Use deque to maintain indices of potential maximum elements
- Remove indices outside current window from front
- Remove smaller elements from back before adding new element
- Front of deque always contains index of maximum in current window
- Time: O(n), Space: O(k)

---

## Stack

### Valid Parentheses
- Use stack to track opening brackets
- Push opening brackets onto stack
- For closing brackets, check if stack top matches
- Stack should be empty at end for valid parentheses
- Time: O(n), Space: O(n)

### Minimum Stack
- Use two stacks: one for values, one for minimums
- Push current minimum onto min stack with each value
- Pop from both stacks together
- Top of min stack always gives current minimum
- Time: O(1) for all operations, Space: O(n)

### Evaluate Reverse Polish Notation
- Use stack to store operands
- For numbers, push onto stack
- For operators, pop two operands, compute result, push back
- Handle division carefully for negative numbers
- Time: O(n), Space: O(n)

### Daily Temperatures
- Use stack to store indices of temperatures
- For each temperature, pop indices with smaller temperatures
- Calculate days difference for popped indices
- Push current index onto stack
- Time: O(n), Space: O(n)

### Car Fleet
- Pair positions with speeds, sort by position (descending)
- Calculate time to reach target for each car
- Use stack to track fleet formation
- Cars with longer time will form separate fleets
- Time: O(n log n), Space: O(n)

### Asteroid Collision
- Use stack to simulate asteroid movements
- Positive asteroids (moving right) go on stack
- Negative asteroids (moving left) may collide with stack top
- Handle collision cases: destruction, survival, mutual destruction
- Time: O(n), Space: O(n)

---

## Binary Search

### Binary Search
- Use two pointers (left, right) to define search space
- Calculate mid point, compare with target
- Adjust search space based on comparison
- Continue until target found or search space exhausted
- Time: O(log n), Space: O(1)

### Search 2D Matrix
- Treat 2D matrix as 1D sorted array
- Use binary search with index conversion: `row = mid // cols, col = mid % cols`
- Compare matrix[row][col] with target
- Adjust search space accordingly
- Time: O(log(m*n)), Space: O(1)

### Eating Bananas
- Binary search on eating speed (1 to max pile size)
- For each speed, calculate total hours needed
- If hours ≤ h, try smaller speed; otherwise try larger speed
- Find minimum speed that allows finishing within h hours
- Time: O(n log m), Space: O(1)

### Find Minimum in Rotated Sorted Array
- Use binary search to find rotation point
- Compare mid with right element to determine which half is sorted
- Minimum is either at mid or in unsorted half
- Handle edge cases where array is not rotated
- Time: O(log n), Space: O(1)

### Find Target in Rotated Sorted Array
- First determine which half of array is properly sorted
- Check if target lies in sorted half, otherwise search other half
- Use standard binary search logic within sorted portions
- Handle rotation by comparing mid with left/right boundaries
- Time: O(log n), Space: O(1)

---

## Linked List

### Reverse a Linked List
- Use three pointers: prev, current, next
- Iteratively reverse links between nodes
- Update pointers: next = curr.next, curr.next = prev, prev = curr, curr = next
- Return prev as new head
- Time: O(n), Space: O(1)

### Merge Two Sorted Linked Lists
- Use dummy node to simplify edge cases
- Compare values of both list heads, attach smaller one
- Move pointer of chosen list forward
- Attach remaining list when one becomes null
- Time: O(n+m), Space: O(1)

### Linked List Cycle Detection
- Use Floyd's cycle detection (tortoise and hare)
- Slow pointer moves one step, fast pointer moves two steps
- If cycle exists, fast will eventually meet slow
- If fast reaches null, no cycle exists
- Time: O(n), Space: O(1)

### Remove Node from End of Linked List
- Use two pointers with n+1 gap between them
- Move both pointers until second reaches end
- First pointer will be at node before target
- Remove target node by updating links
- Time: O(n), Space: O(1)

### Merge K Sorted Linked Lists
- Use divide and conquer approach
- Recursively merge pairs of lists
- Reduce k lists to k/2, then k/4, until one list remains
- Use merge two sorted lists as helper function
- Time: O(n log k), Space: O(log k)

### Add Two Numbers
- Traverse both lists simultaneously, handling carry
- Create new nodes for sum digits
- Handle different length lists by treating missing nodes as 0
- Don't forget final carry if it exists
- Time: O(max(n,m)), Space: O(max(n,m))

### Copy Linked List with Random Pointer
- First pass: create copy nodes and map original to copy
- Second pass: set next and random pointers using the map
- Use hashmap to maintain original to copy node mapping
- Handle null pointers carefully
- Time: O(n), Space: O(n)

---

## Trees

### Invert a Binary Tree
- Recursively swap left and right children of each node
- Base case: return null for null nodes
- Swap children, then recursively invert subtrees
- Can be done iteratively using queue/stack
- Time: O(n), Space: O(h) where h is height

### Depth of Binary Tree
- Recursively calculate depth of left and right subtrees
- Return 1 + maximum of left and right depths
- Base case: return 0 for null nodes
- Can be done iteratively using level-order traversal
- Time: O(n), Space: O(h)

### Same Binary Tree
- Recursively compare corresponding nodes
- Check if both nodes are null (equal) or one is null (not equal)
- Compare values and recursively check left and right subtrees
- All comparisons must be true for trees to be same
- Time: O(n), Space: O(h)

### Subtree of a Binary Tree
- For each node in main tree, check if subtree rooted there matches given subtree
- Use same tree function to check if two trees are identical
- Recursively check left and right subtrees if current root doesn't match
- Time: O(m*n), Space: O(h)

### Lowest Common Ancestor in BST
- Use BST property: LCA is first node where paths diverge
- If both nodes are smaller, LCA is in left subtree
- If both nodes are larger, LCA is in right subtree
- Otherwise, current node is LCA
- Time: O(h), Space: O(1) iterative

### Binary Tree Level Order Traversal
- Use queue for breadth-first traversal
- Process nodes level by level
- Track level size to group nodes by level
- Add children to queue for next level
- Time: O(n), Space: O(w) where w is maximum width

### Binary Tree Right Side View
- Use level-order traversal or DFS with level tracking
- For each level, record the rightmost node
- In DFS, visit right subtree before left
- Track maximum level seen to avoid duplicates
- Time: O(n), Space: O(h)

### Valid Binary Search Tree
- Use inorder traversal to check if values are in ascending order
- Or recursively check with min/max bounds for each subtree
- Left subtree values must be less than root
- Right subtree values must be greater than root
- Time: O(n), Space: O(h)

### Kth Smallest Integer in BST
- Use inorder traversal (gives sorted order in BST)
- Count nodes during traversal, return when count reaches k
- Can optimize with iterative inorder using stack
- Time: O(h + k), Space: O(h)

### Binary Tree Diameter
- For each node, calculate longest path through that node
- Path through node = left height + right height
- Recursively calculate heights and update global maximum
- Use global variable to track maximum diameter seen
- Time: O(n), Space: O(h)

---

## Backtracking

### Subsets
- Use backtracking to generate all possible subsets
- For each element, choose to include or exclude it
- Build subset incrementally and backtrack
- Add current subset to result at each recursive call
- Time: O(2^n), Space: O(n)

### Combination Target Sum
- Use backtracking with remaining target sum
- For each candidate, subtract from target and recurse
- Allow reusing same candidate (start index doesn't change)
- Backtrack by removing last added candidate
- Time: O(2^t) where t is target, Space: O(t)

### Permutations
- Use backtracking with visited array or by swapping
- Build permutation one element at a time
- Mark elements as used, backtrack by unmarking
- Add complete permutation to result
- Time: O(n!), Space: O(n)

### Subsets II
- Sort array first to handle duplicates
- Use backtracking similar to subsets
- Skip duplicate elements at same recursion level
- Only process duplicate if previous same element was included
- Time: O(2^n), Space: O(n)

### Combination Target Sum II
- Sort candidates to handle duplicates
- Use backtracking with start index to avoid reusing elements
- Skip duplicates at same recursion level
- Each element can only be used once
- Time: O(2^n), Space: O(n)

### Word Break
- Use backtracking or dynamic programming
- For each position, try all possible words that start there
- Recursively solve for remaining string
- Use memoization to avoid recomputing subproblems
- Time: O(n^2), Space: O(n)

### Palindrome Partitioning
- Use backtracking to try all possible partitions
- For each position, try all substrings starting there
- Check if substring is palindrome before recursing
- Build partition incrementally and backtrack
- Time: O(2^n), Space: O(n)

---

## Graphs

### Count Number of Islands
- Use DFS or BFS to explore connected components
- For each unvisited land cell, start DFS and mark all connected land
- Increment island count for each DFS start
- Mark visited cells to avoid recounting
- Time: O(m*n), Space: O(m*n)

### Clone Graph
- Use DFS with hashmap to track original to clone mapping
- For each node, create clone and recursively clone neighbors
- Use hashmap to avoid infinite loops and duplicate clones
- Return clone of starting node
- Time: O(V+E), Space: O(V)

### Pacific Atlantic Water Flow
- Use DFS from ocean borders inward
- Track cells reachable from each ocean separately
- Water flows from higher to lower or equal elevation
- Return cells reachable from both oceans
- Time: O(m*n), Space: O(m*n)

### Course Schedule
- Model as directed graph, detect cycles using DFS
- Use three states: unvisited, visiting, visited
- If we reach a visiting node, cycle detected
- Mark nodes as visited after processing all neighbors
- Time: O(V+E), Space: O(V)

### Count Connected Components
- Use DFS or Union-Find to count components
- For each unvisited node, start DFS and mark all reachable nodes
- Increment component count for each DFS start
- Use adjacency list for graph representation
- Time: O(V+E), Space: O(V+E)

### Rotting Fruit
- Use BFS to simulate simultaneous rotting process
- Start BFS from all initially rotten oranges
- Track time using level-by-level BFS
- Check if any fresh oranges remain unreachable
- Time: O(m*n), Space: O(m*n)

---

## Dynamic Programming

### Climbing Stairs
- Each step can be reached from previous step or step before that
- dp[i] = dp[i-1] + dp[i-2]
- Base cases: dp[1] = 1, dp[2] = 2
- Can optimize space to O(1) using two variables
- Time: O(n), Space: O(1)

### House Robber
- For each house, choose to rob or not rob
- If rob current, can't rob previous: dp[i] = nums[i] + dp[i-2]
- If don't rob current: dp[i] = dp[i-1]
- Take maximum of both choices
- Time: O(n), Space: O(1)

### House Robber II
- Houses arranged in circle, so first and last can't both be robbed
- Solve two subproblems: rob houses 0 to n-2, and houses 1 to n-1
- Return maximum of both solutions
- Use House Robber I solution for each subproblem
- Time: O(n), Space: O(1)

### Longest Increasing Subsequence
- dp[i] = length of LIS ending at index i
- For each element, check all previous smaller elements
- dp[i] = max(dp[j] + 1) for all j < i where nums[j] < nums[i]
- Return maximum value in dp array
- Time: O(n²), Space: O(n)

### Coin Change
- dp[i] = minimum coins needed to make amount i
- For each amount, try all coin denominations
- dp[i] = min(dp[i], 1 + dp[i - coin]) for each valid coin
- Return dp[amount] or -1 if impossible
- Time: O(amount * coins), Space: O(amount)

### Maximum Product Subarray
- Track both maximum and minimum products ending at each position
- Negative numbers can make minimum become maximum
- For each element: new_max = max(num, max_prod * num, min_prod * num)
- Update global maximum at each step
- Time: O(n), Space: O(1)

### Word Break
- dp[i] = true if string[0:i] can be segmented
- For each position, check all possible words ending there
- dp[i] = true if any dp[j] is true and string[j:i] is in dictionary
- Time: O(n²), Space: O(n)

### Longest Common Subsequence
- dp[i][j] = LCS length for text1[0:i] and text2[0:j]
- If characters match: dp[i][j] = 1 + dp[i-1][j-1]
- If don't match: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
- Build table bottom-up or use memoization
- Time: O(m*n), Space: O(m*n)

### Unique Paths
- dp[i][j] = number of paths to reach cell (i,j)
- Can only move right or down
- dp[i][j] = dp[i-1][j] + dp[i][j-1]
- Initialize first row and column to 1
- Time: O(m*n), Space: O(m*n)

---

## Greedy

### Jump Game
- Track the farthest position reachable so far
- For each position, update farthest if current position is reachable
- If farthest reaches or exceeds last index, return true
- If current position > farthest, return false
- Time: O(n), Space: O(1)

### Jump Game II
- Use greedy approach to find minimum jumps
- Track current jump's reach and farthest possible reach
- When current reach is exhausted, make another jump
- Count number of jumps needed
- Time: O(n), Space: O(1)

### Gas Station
- Calculate net gas at each station (gas[i] - cost[i])
- If total net gas is negative, no solution exists
- Use greedy approach: start from station where we can complete circuit
- Reset starting point when running out of gas
- Time: O(n), Space: O(1)

### Hand of Straights
- Use hashmap to count card frequencies
- Sort unique cards and try to form consecutive groups
- For each card, try to form group starting with that card
- Decrease count for each card used in group
- Time: O(n log n), Space: O(n)

### Merge Intervals
- Sort intervals by start time
- Merge overlapping intervals by comparing end times
- If current start ≤ previous end, merge by updating end time
- Otherwise, add current interval to result
- Time: O(n log n), Space: O(n)

### Non-overlapping Intervals
- Sort intervals by end time (greedy choice)
- Keep track of last selected interval's end time
- Select interval only if its start ≥ last selected end
- Count intervals that need to be removed
- Time: O(n log n), Space: O(1)

---

## Math & Geometry

### Rotate Matrix
- Transpose matrix (swap rows and columns)
- Reverse each row to complete 90-degree clockwise rotation
- Can be done in-place for space optimization
- Alternative: rotate layer by layer from outside to inside
- Time: O(n²), Space: O(1)

### Spiral Matrix
- Use four boundaries: top, bottom, left, right
- Traverse right, down, left, up in spiral pattern
- Update boundaries after each direction
- Continue until all elements processed
- Time: O(m*n), Space: O(1)

### Set Matrix Zeroes
- Use first row and column as markers for zero positions
- First pass: mark rows and columns that should be zero
- Second pass: set elements to zero based on markers
- Handle first row and column separately
- Time: O(m*n), Space: O(1)

### Happy Number
- Use Floyd's cycle detection to find loops
- Calculate sum of squares of digits repeatedly
- If reaches 1, number is happy
- If enters cycle, number is not happy
- Time: O(log n), Space: O(1)

### Plus One
- Start from least significant digit (rightmost)
- Add 1 and handle carry propagation
- If carry remains after processing all digits, prepend 1
- Handle edge case where all digits are 9
- Time: O(n), Space: O(1) or O(n) if new array needed

---

## Bit Manipulation

### Single Number
- Use XOR operation: a ⊕ a = 0, a ⊕ 0 = a
- XOR all numbers together
- Duplicate numbers cancel out, leaving only single number
- Works because XOR is commutative and associative
- Time: O(n), Space: O(1)

### Number of One Bits
- Use bit manipulation to count set bits
- Method 1: Check each bit using n & 1, then right shift
- Method 2: Use n & (n-1) to clear rightmost set bit
- Continue until n becomes 0
- Time: O(log n), Space: O(1)

### Counting Bits
- Use dynamic programming with bit manipulation
- dp[i] = dp[i >> 1] + (i & 1)
- Right shift removes last bit, i & 1 checks if last bit is set
- Build up from smaller numbers
- Time: O(n), Space: O(n)

### Reverse Bits
- Process each bit from right to left
- Extract bit using n & 1, add to result
- Shift result left and n right for next iteration
- Continue for all 32 bits
- Time: O(1), Space: O(1)

### Missing Number
- Use XOR or sum formula approach
- XOR: XOR all numbers 0 to n with all array elements
- Sum: expected_sum - actual_sum = missing number
- Both handle overflow differently
- Time: O(n), Space: O(1)

### Sum of Two Integers
- Use bit manipulation to simulate addition
- XOR gives sum without carry, AND gives carry positions
- Shift carry left and repeat until no carry
- Handle negative numbers carefully
- Time: O(1), Space: O(1)

---

## Heap / Priority Queue

### Kth Largest Element in Stream
- Use min heap of size k to track k largest elements
- If heap size < k, add element
- If new element > heap top, remove top and add new element
- Heap top always gives kth largest element
- Time: O(log k) per operation, Space: O(k)

### Last Stone Weight
- Use max heap to always get two heaviest stones
- Simulate stone collision process
- If stones have different weights, put difference back in heap
- Continue until at most one stone remains
- Time: O(n log n), Space: O(n)

### K Closest Points to Origin
- Use max heap of size k to track closest points
- Calculate distance using Euclidean formula
- Maintain heap of k closest points seen so far
- Can also use quickselect for O(n) average time
- Time: O(n log k), Space: O(k)

### Task Scheduling
- Use max heap to prioritize tasks with highest frequency
- Use queue to track tasks in cooldown period
- Process most frequent available task at each time unit
- Add completed tasks back to heap after cooldown
- Time: O(n), Space: O(1) for fixed alphabet

### Design Twitter Feed
- Use max heap to merge timelines from multiple users
- Store tweets with timestamp for ordering
- Maintain follow relationships using hashmap
- Efficiently retrieve top 10 tweets from merged timeline
- Time: O(k log k) for getNewsFeed, Space: O(n)

---

## Advanced Topics

### Median from Data Stream
- Use two heaps: max heap for smaller half, min heap for larger half
- Balance heaps so size difference is at most 1
- Median is top of larger heap or average of both tops
- Add elements to appropriate heap and rebalance
- Time: O(log n) per operation, Space: O(n)

### Serialize and Deserialize Binary Tree
- Use preorder traversal with null markers for serialization
- Use queue or index pointer for deserialization
- Handle null nodes explicitly in serialized string
- Reconstruct tree using same traversal order
- Time: O(n), Space: O(n)

### Design LRU Cache
- Use hashmap + doubly linked list combination
- Hashmap provides O(1) access, linked list maintains order
- Move accessed nodes to front, remove from back when capacity exceeded
- Dummy head and tail nodes simplify edge cases
- Time: O(1) for all operations, Space: O(capacity)

### Find Median in Data Stream
- Use two heaps to maintain sorted order
- Max heap stores smaller half, min heap stores larger half
- Keep heaps balanced in size
- Median is either heap top or average of both tops
- Time: O(log n) insert, O(1) median, Space: O(n)

### Alien Dictionary
- Build directed graph from character ordering in words
- Use topological sort to find valid character ordering
- Compare adjacent words to determine character precedence
- Detect cycles which indicate invalid ordering
- Time: O(C) where C is total characters, Space: O(1) for fixed alphabet

This revision guide covers the key concepts, approaches, and complexities for each problem. Use these bullet points to quickly review the essential solution strategies before coding interviews or practice sessions.