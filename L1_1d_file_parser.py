# File parsing - Character Count, word count, line count
# Date : 24-10-2025
# Author : Venkat

try:
    with open("sample.txt", "r") as file:
        line_count = 0
        word_count = 0
        char_count = 0

        all_lines = file.readlines() # list of lines
        line_count = len(all_lines)
        for line in all_lines:
            word_count+= len(line.rstrip("\n").split())
            char_count += len(line)
        
        print(f"Line Count: {line_count}")
        print(f"Word Count: {word_count}")
        print(f"Character Count: {char_count}")

except FileNotFoundError:
    print("File not found. Please check the file path.")
