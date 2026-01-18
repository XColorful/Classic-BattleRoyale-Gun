import os
import json

def remove_double_slash_comments(directory_path):
    """
    Removes lines containing double-slash comments from JSON files in a directory and its subdirectories.

    Args:
        directory_path (str): The path to the directory containing the JSON files.
    """
    if not os.path.isdir(directory_path):
        print(f"Error: Directory not found at '{directory_path}'.")
        return

    print(f"Starting to process JSON files in '{directory_path}'...")
    
    for root, dirs, files in os.walk(directory_path):
        for filename in files:
            if filename.endswith(".json"):
                file_path = os.path.join(root, filename)
                
                try:
                    # Read the file content
                    with open(file_path, 'r', encoding='utf-8') as file:
                        lines = file.readlines()
                    
                    # Check for the presence of "//"
                    has_comments = any("//" in line for line in lines)
                    
                    if has_comments:
                        print(f"  - Processing file: '{filename}'")
                        new_lines = []
                        # Filter out lines with "//"
                        for line in lines:
                            if "//" not in line:
                                new_lines.append(line)
                        
                        # Write the new content back to the file
                        with open(file_path, 'w', encoding='utf-8') as file:
                            file.writelines(new_lines)
                        print(f"    - Removed comments and saved the updated file.")
                    else:
                        print(f"  - Skipping file: '{filename}' (no double-slash comments found).")
                
                except json.JSONDecodeError:
                    print(f"  - Warning: Skipping '{filename}' as it is not a valid JSON file.")
                except Exception as e:
                    print(f"  - Error processing file '{filename}': {e}")
                
    print("\nProcess finished.")

target_directory = input("目录：")
remove_double_slash_comments(target_directory)