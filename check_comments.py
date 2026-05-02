#!/usr/bin/env python3
import os

def check_files_for_comments():
    """Check which files have revision comments and which don't"""
    base_dir = "Data Structures & Algorithms"
    
    files_with_comments = []
    files_without_comments = []
    
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.py'):
                filepath = os.path.join(root, file)
                problem_name = os.path.basename(root)
                
                try:
                    with open(filepath, 'r') as f:
                        content = f.read()
                    
                    if 'REVISION NOTES' in content:
                        files_with_comments.append((problem_name, filepath))
                    else:
                        files_without_comments.append((problem_name, filepath))
                        
                except Exception as e:
                    print("Error reading " + filepath + ": " + str(e))
    
    print("Files WITH revision comments (" + str(len(files_with_comments)) + "):")
    for problem, filepath in sorted(files_with_comments):
        print("  + " + problem)
    
    print("\nFiles WITHOUT revision comments (" + str(len(files_without_comments)) + "):")
    for problem, filepath in sorted(files_without_comments):
        print("  - " + problem)
    
    print("\nSummary: " + str(len(files_with_comments)) + " with comments, " + str(len(files_without_comments)) + " without comments")
    return files_without_comments

if __name__ == "__main__":
    check_files_for_comments()