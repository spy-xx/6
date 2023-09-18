filename = input("Enter the filename: ")

try:
    with open(filename, "r") as file:
        lines = file.readlines()
        for i, line in enumerate(lines[:20]):
            print(i + 1, ":", line.strip())

        word = input("Enter a word: ")
        count = sum(line.count(word) for line in lines)

        print(f"The word {word} appears {count} times in the file.")
except FileNotFoundError:
    print(f"File {filename} doesn't exist.")