def sequence(sequence):
    words = sequence.split("-")
    words.sort()
    sorted_sequence = "-".join(words)
    print(sorted_sequence)

sequence = input("Enter a hyphen-separated sequence of words: ")
sequence(sequence)