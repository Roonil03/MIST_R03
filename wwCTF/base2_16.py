def process_string(input_str):
    # Step 1: Convert each character to its Unicode binary representation and store in a string array
    binary_strings = [format(ord(char), '08b') for char in input_str]

    # Step 2: Reverse the binary string for each string in the array
    reversed_binaries = [binary[::-1] for binary in binary_strings]

    # Step 3: Process the reversed binary strings
    result = ""
    for binary in reversed_binaries:
        # Extract the first 8 characters and convert to an ASCII character
        char1 = chr(int(binary[:8], 2))
        # Extract the next 8 characters (if available) and convert to an ASCII character
        if len(binary) > 8:
            char2 = chr(int(binary[8:], 2))
            # Concatenate both characters
            result += char1 + char2
        else:
            # If only one character is available, add it to the result
            result += char1

    # Print the final result
    print(result)

# Input string
input_string = "MkpIbmdFcWs4MzVjR3BHRXFVVnZtZWJUQWtSTlNNamE1dGZYQTdwR25ac203SnJQV2FyTUdHQnA3Uk1XZDNZVFlTNTJjemVya1BCN0dBY2NBNkN4U1VBS29TalVBOU1tR1EyYUF0UVlHZTFYOXp1TThWS2o1OHdKRFJaVXhzTGRaZUpaTGV6NUFWc2JHdm5CbTdjV28yNTRyWGpzQURYdEhkSmJmWmtGREVEQWZWeEhFeDNYanNNODZMZVo2cnM2NExGbU5QeG1mUXBqQ3BoY3pCczlRa3kySnFZb1JzSnFtUnk0cW02WFgyOU50N1g2Vg"

# Call the function
process_string(input_string)
