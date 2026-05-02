#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

# Simple revision notes for remaining problems
REVISION_NOTES = {
    "excel-sheet-column-title": [
        "Convert number to Excel column title (base 26 with A-Z)",
        "Use modulo and division to extract digits",
        "Handle 1-indexed system (subtract 1 before modulo)",
        "Build result string from right to left",
        "Time: O(log n), Space: O(log n)"
    ],
    "find-duplicate-integer": [
        "Use Floyd's cycle detection algorithm",
        "Treat array as linked list where nums[i] points to nums[nums[i]]",
        "Find intersection point, then find start of cycle",
        "Duplicate number is the start of the cycle",
        "Time: O(n), Space: O(1)"
    ],
    "find-minimum-in-rotated-sorted-array": [
        "Use binary search to find rotation point",
        "Compare mid with right element to determine which half is sorted",
        "Minimum is either at mid or in unsorted half",
        "Handle edge cases where array is not rotated",
        "Time: O(log n), Space: O(1)"
    ],
    "find-target-in-rotated-sorted-array": [
        "First determine which half of array is properly sorted",
        "Check if target lies in sorted half, otherwise search other half",
        "Use standard binary search logic within sorted portions",
        "Handle rotation by comparing mid with left/right boundaries",
        "Time: O(log n), Space: O(1)"
    ],
    "gas-station": [
        "Calculate net gas at each station (gas[i] - cost[i])",
        "If total net gas is negative, no solution exists",
        "Use greedy approach: start from station where we can complete circuit",
        "Reset starting point when running out of gas",
        "Time: O(n), Space: O(1)"
    ],
    "generate-parentheses": [
        "Use backtracking to generate valid combinations",
        "Track count of open and close parentheses",
        "Add open parenthesis if count < n",
        "Add close parenthesis if close_count < open_count",
        "Time: O(4^n / sqrt(n)), Space: O(n)"
    ],
    "house-robber": [
        "For each house, choose to rob or not rob",
        "If rob current, can't rob previous: dp[i] = nums[i] + dp[i-2]",
        "If don't rob current: dp[i] = dp[i-1]",
        "Take maximum of both choices",
        "Time: O(n), Space: O(1)"
    ],
    "house-robber-ii": [
        "Houses arranged in circle, so first and last can't both be robbed",
        "Solve two subproblems: rob houses 0 to n-2, and houses 1 to n-1",
        "Return maximum of both solutions",
        "Use House Robber I solution for each subproblem",
        "Time: O(n), Space: O(1)"
    ],
    "invert-a-binary-tree": [
        "Recursively swap left and right children of each node",
        "Base case: return null for null nodes",
        "Swap children, then recursively invert subtrees",
        "Can be done iteratively using queue/stack",
        "Time: O(n), Space: O(h)"
    ],
    "is-anagram": [
        "Sort both strings and compare, or use character frequency count",
        "Two strings are anagrams if they have same character frequencies",
        "Can use array of size 26 for lowercase letters",
        "Time: O(n log n) for sorting, O(n) for counting"
    ],
    "jump-game": [
        "Track the farthest position reachable so far",
        "For each position, update farthest if current position is reachable",
        "If farthest reaches or exceeds last index, return true",
        "If current position > farthest, return false",
        "Time: O(n), Space: O(1)"
    ],
    "jump-game-ii": [
        "Use greedy approach to find minimum jumps",
        "Track current jump's reach and farthest possible reach",
        "When current reach is exhausted, make another jump",
        "Count number of jumps needed",
        "Time: O(n), Space: O(1)"
    ],
    "linked-list-cycle-detection": [
        "Use Floyd's cycle detection (tortoise and hare)",
        "Slow pointer moves one step, fast pointer moves two steps",
        "If cycle exists, fast will eventually meet slow",
        "If fast reaches null, no cycle exists",
        "Time: O(n), Space: O(1)"
    ],
    "longest-common-subsequence": [
        "dp[i][j] = LCS length for text1[0:i] and text2[0:j]",
        "If characters match: dp[i][j] = 1 + dp[i-1][j-1]",
        "If don't match: dp[i][j] = max(dp[i-1][j], dp[i][j-1])",
        "Build table bottom-up or use memoization",
        "Time: O(m*n), Space: O(m*n)"
    ],
    "longest-increasing-subsequence": [
        "dp[i] = length of LIS ending at index i",
        "For each element, check all previous smaller elements",
        "dp[i] = max(dp[j] + 1) for all j < i where nums[j] < nums[i]",
        "Return maximum value in dp array",
        "Time: O(n^2), Space: O(n)"
    ],
    "longest-palindromic-substring": [
        "Expand around centers approach (odd and even length palindromes)",
        "For each position, expand outward while characters match",
        "Track longest palindrome found so far",
        "Handle both odd-length and even-length palindromes",
        "Time: O(n^2), Space: O(1)"
    ],
    "max-water-container": [
        "Use two pointers from both ends of array",
        "Calculate area with current pointers, update maximum",
        "Move pointer with smaller height inward",
        "Continue until pointers meet",
        "Time: O(n), Space: O(1)"
    ],
    "maximum-product-subarray": [
        "Track both maximum and minimum products ending at each position",
        "Negative numbers can make minimum become maximum",
        "For each element: new_max = max(num, max_prod * num, min_prod * num)",
        "Update global maximum at each step",
        "Time: O(n), Space: O(1)"
    ],
    "merge-intervals": [
        "Sort intervals by start time",
        "Merge overlapping intervals by comparing end times",
        "If current start <= previous end, merge by updating end time",
        "Otherwise, add current interval to result",
        "Time: O(n log n), Space: O(n)"
    ],
    "merge-k-sorted-linked-lists": [
        "Use divide and conquer approach",
        "Recursively merge pairs of lists",
        "Reduce k lists to k/2, then k/4, until one list remains",
        "Use merge two sorted lists as helper function",
        "Time: O(n log k), Space: O(log k)"
    ],
    "minimum-window-with-characters": [
        "Use two hashmaps: one for target characters, one for window",
        "Expand window until all target characters included",
        "Then shrink from left while maintaining validity",
        "Track minimum valid window found",
        "Time: O(n), Space: O(m) where m is target string length"
    ],
    "missing-number": [
        "Use XOR or sum formula approach",
        "XOR: XOR all numbers 0 to n with all array elements",
        "Sum: expected_sum - actual_sum = missing number",
        "Both handle overflow differently",
        "Time: O(n), Space: O(1)"
    ],
    "number-of-one-bits": [
        "Use bit manipulation to count set bits",
        "Method 1: Check each bit using n & 1, then right shift",
        "Method 2: Use n & (n-1) to clear rightmost set bit",
        "Continue until n becomes 0",
        "Time: O(log n), Space: O(1)"
    ],
    "permutations": [
        "Use backtracking with visited array or by swapping",
        "Build permutation one element at a time",
        "Mark elements as used, backtrack by unmarking",
        "Add complete permutation to result",
        "Time: O(n!), Space: O(n)"
    ],
    "products-of-array-discluding-self": [
        "Calculate prefix products from left to right",
        "Calculate suffix products from right to left while building result",
        "Multiply prefix and suffix products for each position",
        "Avoid division to handle zeros correctly",
        "Time: O(n), Space: O(1) excluding output array"
    ],
    "remove-node-from-end-of-linked-list": [
        "Use two pointers with n+1 gap between them",
        "Move both pointers until second reaches end",
        "First pointer will be at node before target",
        "Remove target node by updating links",
        "Time: O(n), Space: O(1)"
    ],
    "reverse-a-linked-list": [
        "Use three pointers: prev, current, next",
        "Iteratively reverse links between nodes",
        "Update pointers: next = curr.next, curr.next = prev, prev = curr, curr = next",
        "Return prev as new head",
        "Time: O(n), Space: O(1)"
    ],
    "reverse-bits": [
        "Process each bit from right to left",
        "Extract bit using n & 1, add to result",
        "Shift result left and n right for next iteration",
        "Continue for all 32 bits",
        "Time: O(1), Space: O(1)"
    ],
    "same-binary-tree": [
        "Recursively compare corresponding nodes",
        "Check if both nodes are null (equal) or one is null (not equal)",
        "Compare values and recursively check left and right subtrees",
        "All comparisons must be true for trees to be same",
        "Time: O(n), Space: O(h)"
    ],
    "single-number": [
        "Use XOR operation: a XOR a = 0, a XOR 0 = a",
        "XOR all numbers together",
        "Duplicate numbers cancel out, leaving only single number",
        "Works because XOR is commutative and associative",
        "Time: O(n), Space: O(1)"
    ],
    "sliding-window-maximum": [
        "Use deque to maintain indices of potential maximum elements",
        "Remove indices outside current window from front",
        "Remove smaller elements from back before adding new element",
        "Front of deque always contains index of maximum in current window",
        "Time: O(n), Space: O(k)"
    ],
    "subsets": [
        "Use backtracking to generate all possible subsets",
        "For each element, choose to include or exclude it",
        "Build subset incrementally and backtrack",
        "Add current subset to result at each recursive call",
        "Time: O(2^n), Space: O(n)"
    ],
    "subsets-ii": [
        "Sort array first to handle duplicates",
        "Use backtracking similar to subsets",
        "Skip duplicate elements at same recursion level",
        "Only process duplicate if previous same element was included",
        "Time: O(2^n), Space: O(n)"
    ],
    "three-integer-sum": [
        "Sort array first to enable two-pointer technique",
        "Fix first element, use two pointers for remaining two elements",
        "Skip duplicates to avoid duplicate triplets",
        "For each fixed element, find pairs that sum to negative of fixed element",
        "Time: O(n^2), Space: O(1)"
    ],
    "two-integer-sum-ii": [
        "Use two pointers from start and end of sorted array",
        "Move left pointer right if sum too small, right pointer left if sum too large",
        "Return indices when target sum found",
        "Works because array is sorted",
        "Time: O(n), Space: O(1)"
    ],
    "valid-binary-search-tree": [
        "Use inorder traversal to check if values are in ascending order",
        "Or recursively check with min/max bounds for each subtree",
        "Left subtree values must be less than root",
        "Right subtree values must be greater than root",
        "Time: O(n), Space: O(h)"
    ],
    "validate-parentheses": [
        "Use stack to track opening brackets",
        "Push opening brackets onto stack",
        "For closing brackets, check if stack top matches",
        "Stack should be empty at end for valid parentheses",
        "Time: O(n), Space: O(n)"
    ],
    "word-break": [
        "Use backtracking or dynamic programming",
        "For each position, try all possible words that start there",
        "Recursively solve for remaining string",
        "Use memoization to avoid recomputing subproblems",
        "Time: O(n^2), Space: O(n)"
    ]
}

def add_comment_to_file(filepath, problem_name):
    """Add revision comment to a specific file"""
    
    if problem_name not in REVISION_NOTES:
        return False
        
    try:
        with open(filepath, 'r') as f:
            content = f.read()
            
        if 'REVISION NOTES' in content:
            return False
            
        # Create comment
        title = problem_name.replace("-", " ").title()
        comment_lines = ['REVISION NOTES - ' + title + ':']
        for note in REVISION_NOTES[problem_name]:
            comment_lines.append('- ' + note)
            
        comment = '"""\n' + '\n'.join(comment_lines) + '\n"""\n\n'
        
        # Add comment to file
        new_content = comment + content
        
        with open(filepath, 'w') as f:
            f.write(new_content)
            
        print("Added comment to: " + problem_name)
        return True
        
    except Exception as e:
        print("Error with " + problem_name + ": " + str(e))
        return False

def main():
    base_dir = "Data Structures & Algorithms"
    count = 0
    
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.py'):
                filepath = os.path.join(root, file)
                problem_name = os.path.basename(root)
                
                if add_comment_to_file(filepath, problem_name):
                    count += 1
                    
    print("Added comments to " + str(count) + " files")

if __name__ == "__main__":
    main()