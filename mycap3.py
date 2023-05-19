def most_frequent(string):
    # Create an empty dictionary to store the frequency of each letter
    freq_dict = {}

    # Count the frequency of each letter in the string
    for letter in string:
        if letter.isalpha():
            freq_dict[letter] = freq_dict.get(letter, 0) + 1

    # Sort the dictionary by values in descending order
    sorted_dict = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)

    # Print the letters in decreasing order of frequency
    for item in sorted_dict:
        print(item[0], ":", item[1])

# Prompt the user for input
input_string = input("Enter a string: ")

# Call the function to print the letters in decreasing order of frequency
most_frequent(input_string)
