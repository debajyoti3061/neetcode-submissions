#!/usr/bin/env python3
import os

def add_comment_to_file(filepath, problem_name):
    """Add revision comment to a specific file"""
    
    # Define revision notes for key problems
    notes = {
        "two-integer-sum": [
            "Use hashmap to store target - current_number as key and index as value",
            "Check if current number exists in hashmap before adding complement", 
            "Return indices when complement is found",
            "Time: O(n), Space: O(n)"
        ],
        "binary-search": [
            "Use two pointers (left, right) to define search space",
            "Calculate mid point, compare with target",
            "Adjust search space based on comparison", 
            "Continue until target found or search space exhausted",
            "Time: O(log n), Space: O(1)"
        ],
        "anagram-groups": [
            "Sort each string to create a key for grouping anagrams",
            "Use hashmap where key is sorted string, value is list of original strings",
            "All anagrams will have the same sorted representation",
            "Return list of all grouped values",
            "Time: O(n * m log m), Space: O(n * m)"
        ],
        "climbing-stairs": [
            "Each step can be reached from previous step or step before that",
            "dp[i] = dp[i-1] + dp[i-2]",
            "Base cases: dp[1] = 1, dp[2] = 2", 
            "Can optimize space to O(1) using two variables",
            "Time: O(n), Space: O(1)"
        ],
        "coin-change": [
            "dp[i] = minimum coins needed to make amount i",
            "For each amount, try all coin denominations",
            "dp[i] = min(dp[i], 1 + dp[i - coin]) for each valid coin",
            "Return dp[amount] or -1 if impossible",
            "Time: O(amount * coins), Space: O(amount)"
        ],
        "count-number-of-islands": [
            "Use DFS or BFS to explore connected components",
            "For each unvisited land cell, start DFS and mark all connected land",
            "Increment island count for each DFS start",
            "Mark visited cells to avoid recounting",
            "Time: O(m*n), Space: O(m*n)"
        ],
        "longest-substring-without-duplicates": [
            "Use sliding window with set to track characters in current window",
            "Expand right pointer and add characters to set",
            "When duplicate found, shrink left pointer until duplicate removed",
            "Track maximum window size seen",
            "Time: O(n), Space: O(min(m,n)) where m is charset size"
        ],
        "trapping-rain-water": [
            "Use two pointers with left_max and right_max tracking",
            "Move pointer with smaller max value inward",
            "Add trapped water based on difference between max and current height",
            "Water trapped depends on minimum of left and right boundaries",
            "Time: O(n), Space: O(1)"
        ]
    }
    
    if problem_name not in notes:
        return False
        
    try:
        with open(filepath, 'r') as f:
            content = f.read()
            
        if 'REVISION NOTES' in content:
            return False
            
        # Create comment
        title = problem_name.replace("-", " ").title()
        comment_lines = ['REVISION NOTES - ' + title + ':']
        for note in notes[problem_name]:
            comment_lines.append('- ' + note)
            
        comment = '"""\n' + '\n'.join(comment_lines) + '\n"""\n\n'
        
        # Add comment to file
        new_content = comment + content
        
        with open(filepath, 'w') as f:
            f.write(new_content)
            
        print("Added comment to: " + filepath)
        return True
        
    except Exception as e:
        print("Error: " + str(e))
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