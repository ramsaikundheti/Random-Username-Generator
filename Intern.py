import random

# Lists of adjectives and nouns
adjectives = ["Cool", "Happy", "Fast", "Lucky", "Brave", "Charming", "Funny", "Sneaky", "Bright", "Wise"]
nouns = ["Tiger", "Dragon", "Eagle", "Wizard", "Phoenix", "Knight", "Warrior", "Hawk", "Panther", "Lion"]

# Function to generate a username by combining random adjective and noun
def generate_username(adjectives, nouns):
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    return adjective + noun

# Function to add customizations to the username
def customize_username(base_username, add_number=False, add_special_char=False):
    if add_number:
        base_username += str(random.randint(10, 99))  # Add a random two-digit number
    if add_special_char:
        special_chars = "!@#$%^&*"
        base_username += random.choice(special_chars)  # Add a random special character
    return base_username

# Function to save generated usernames to a file
def save_usernames_to_file(usernames, filename="usernames.txt"):
    with open(filename, "w") as file:
        for username in usernames:
            file.write(username + "\n")
    print(f"Usernames saved to {filename}")

# Main program
def main():
    print("Welcome to the Random Username Generator!")
    
    generated_usernames = []  # List to store generated usernames
    
    while True:
        print("\nOptions:")
        print("1. Generate a username")
        print("2. Save generated usernames to a file")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == "1":
            # User preferences for customization
            add_number = input("Include numbers? (yes/no): ").lower() == "yes"
            add_special_char = input("Include special characters? (yes/no): ").lower() == "yes"
            
            # Generate and customize the username
            username = generate_username(adjectives, nouns)
            username = customize_username(username, add_number, add_special_char)
            
            print(f"Generated Username: {username}")
            generated_usernames.append(username)  # Add to the list of generated usernames
        
        elif choice == "2":
            if not generated_usernames:
                print("No usernames have been generated yet!")
            else:
                # Save usernames to file
                save_usernames_to_file(generated_usernames)
        
        elif choice == "3":
            print("Thank you for using the Random Username Generator! Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")
