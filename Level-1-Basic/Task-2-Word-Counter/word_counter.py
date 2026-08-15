def count_words(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

        words = content.split()
        return len(words)

    except FileNotFoundError:
        print("Error: File not found.")
        return None


print("==============================")
print("        WORD COUNTER")
print("==============================")

filename = input("Enter the text file name: ")

word_count = count_words(filename)

if word_count is not None:
    print("Total number of words:", word_count)