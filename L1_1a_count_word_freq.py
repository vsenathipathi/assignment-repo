# Write a script to read a text file and count the frequency of each word in the file.
# Date : 24-10-2025
# Author : Venkat

filename='sample.txt'
try:
    wordcount=0
    with open(filename, 'r') as file:
        # print(file.read())
        all_lines=file.readlines() # give list of strings, easy to iterate
        word_list=[]
        for line in all_lines:
            word_list.extend(line.lower().split())
        print(word_list)
    
    for word in set(word_list):
        count=word_list.count(word)
        print(f'"{word}" - occurs {count} times in the file.')

except FileNotFoundError:
    print(f"The file {filename} does not exist.")
    exit()


