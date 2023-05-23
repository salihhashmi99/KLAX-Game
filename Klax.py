import random

# Alphabet dictionary
alphabet_dict = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1,
    'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1,
    'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
}

def generate_random_letter():
    """Generates a random letter from the alphabet dictionary."""
    return random.choice(list(alphabet_dict.keys()))

def calculate_score(word):
    """Calculates the score for a given word."""
    score = 0
    for letter in word:
        score += alphabet_dict.get(letter.upper(), 0)
    return score

def main():
    score = 0

    while True:
        letter = generate_random_letter()
        print("New letter:", letter)

        # Prompt user for input
        word = input("Enter a word or press 'Enter' to skip: ").strip().upper()
                if word == "":
            continue  # Skip if the user presses 'Enter'

        if letter in word:
            print("The letter is used!")
            if word in alphabet_dict:
                print("Valid word!")
                score += 10
            else:
                print("Invalid word!")
        else:
            print("The letter is not used!")

        print("Current score:", score)
        print()

if __name__ == "__main__":
    main()
