# Renata Guadalupe Ruiz de la Cruz
# 2630424
# IM1-1

# executive summary
# In Python, the string data type represents text strings and is characterized by its immutability, preventing direct changes.
# It allows basic operations like concatenating (+), getting its length (len()), extracting substrings ([]), searching for patterns (find or in), and replacing text (replace()).
# Validating and normalizing input text in emails, names, and passwords is crucial to ensure security and data cleanliness.
# The document will cover a detailed description of each problem posed and its respective design of inputs and outputs.
# It will also include the validations applied and the use of string methods.
# Finally, the corresponding test cases will be included along with the executable code.

# 7.1 Problem 1: Full name formatter (name + initials)
# Description: Given a person's full name in a single string (e.g., "juan carlos tovar"):
# 1) Normalize the text (strip, extra space removal, uppercase/lowercase adjustment).
# 2) Display the formatted name in Title Case and the initials (e.g., J.C.T.).

# Inputs
full_name = input("Enter your full name: ").strip() # Read the full name as a string and remove leading/trailing spaces with strip

# Check if the input string is empty after stripping whitespace
if not full_name:
    # Outputs
    print("Error: invalid input") # Show error if the user entered nothing

else:
    name_parts = full_name.split() # Split the full name string into a list of words using space as delimiter

    # Validate that the user entered at least two words
    if len(name_parts) < 2: # Check if the number of words in the list is less than two
        # Outputs
        print("Error: invalid input") # Show error if there is only one word

    else:
        formatted_name = full_name.title() # Convert the full name to Title Case (first letter of each word capitalized)

        # Extract the first letter of each part, convert to uppercase, and concatenate with dots
        initials = name_parts[0][0].upper() + "." + name_parts[1][0].upper() + "."
        
        # Outputs
        print("Formatted name:", formatted_name) # Display the nicely formatted name
        print("Initials:", initials) # Display the generated initials
# CASE NORMAL
"""
Enter your full name: cesar enriquq garcia
Formatted name: Cesar Enrique Gacia
Initials: C.E.G
"""

# CASE BORDE
"""
Enter your full name: renata ruiz
Formatted name: Renata Ruiz
Initials: R.R
"""

# CASE ERROR
"""
Enter your full name:   
Error: invalid input ≽^- ˕ -^≼
"""

# 7.2 Problem 2: Simple email validator (structure + domain)
# Description: Validates if an email address has a basic correct format:
# - Contains exactly one '@'.
# - After the '@', there must be at least one '.'.
# - Contains no whitespace characters.
# If the email is valid, it also displays the domain (the part after the '@').

# Inputs
email_text = input("Enter your email: ").strip() # Read email input and remove unwanted spaces

# Check if the email string is empty
if not email_text:
    # Outputs
    print("Error: invalid input")

# Verify that the email contains exactly one '@' symbol using count()
elif email_text.count("@") != 1: # Check if count of '@' is different from 1
    # Outputs
    print("Error: invalid input")

# Verify that there are no empty spaces anywhere inside the email string
elif " " in email_text: # Check for whitespace characters
    # Outputs
    print("Error: invalid input")

else:
    at_position = email_text.find("@") # Locate the exact index position of the '@' character
    domain_part = email_text[at_position + 1:] # Slice the string to extract everything after the '@' symbol

    # Check if there is at least one dot '.' present in the domain part
    if "." not in domain_part: # Validate domain structure
        # Outputs
        print("Error: invalid input")
    else:
        # Outputs
        print("Valid email: true") # Confirm email validity
        print("Result:", domain_part) # Display extracted domain name
# CASE NORMAL
"""
Enter your email: test@example.com
Valid email: true
Result: example.com
"""

# CASE BORDE
"""
Enter your email: user@domain
Error: invalid input
"""

# CASE ERROR
"""
Enter your email: user@@domain.com
Error: invalid input
"""
# 7.3 Problem 3: Palindrome checker (ignoring spaces and case)
# Description: Determines whether a phrase is a palindrome (reads the same from
# left to right as from right to left), ignoring spaces and case sensitivity.

# Constante
MIN_LENGTH = 3

# Inputs
phrase = input("Enter your phrase: ").strip() # Read input phrase from user

# Check if the entered phrase is empty
if not phrase:
    # Outputs
    print("Error: invalid input")

else:
    # Remove all spaces and convert the entire phrase to lowercase for uniform comparison
    cleaned_phrase = phrase.replace(" ", "").lower() # Normalize string by removing spaces and casing

    # Check if the cleaned phrase meets the minimum length requirement
    if len(cleaned_phrase) < MIN_LENGTH: # Validate against MIN_LENGTH constant
        # Outputs
        print("Error: invalid input") 

    else:
        reversed_phrase = cleaned_phrase[::-1] # Reverse the normalized string using slicing with step -1

        # Compare the normalized string with its reversed version
        if cleaned_phrase == reversed_phrase:
            # Outputs
            print("Result: true") # True if it reads the same forwards and backwards
        else:
            # Outputs
            print("Result: false") # False otherwise

# CASE NORMAL
"""
Enter your phrase: oso
Result: true
"""

# CASE BORDE
"""
Enter your phrase: La ruta natural
Result: true
"""

# CASE ERROR
"""
Enter your phrase: no como eso
Error: invalid input
"""

# 7.4 Problem 4: Sentence word stats (lengths and first/last word)
# Description: Given a sentence, the program must:
# 1) Normalize spaces (remove leading and trailing spaces).
# 2) Split words by spaces.
# 3) Display:
#    - Total number of words.
#    - First and last word.
#    - Shortest and longest word (by length).

# Inputs
sentence = input("Enter your sentence: ").strip() # Read sentence and remove edge spaces

# Check if sentence is empty
if not sentence:
    # Outputs
    print("Error: invalid input")

else:
    word_list = sentence.split() # Split the sentence into a list of individual words by spaces
    
    word_count = len(word_list) # Get the total number of words using len()
    
    first_word = word_list[0] # Access the very first element of the list
    last_word = word_list[-1] # Access the very last element of the list using negative indexing

    shortest_word = min(word_list, key=len) # Find the shortest word in the list using length as key
    longest_word = max(word_list, key=len) # Find the longest word in the list using length as key

    # Outputs
    print("Length:", word_count) # Display total word count
    print("Result first word:", first_word) # Display first word
    print("Result last word:", last_word) # Display last word
    print("Result shortest word:", shortest_word) # Display shortest word
    print("Result longest word:", longest_word) # Display longest word

# CASE NORMAL
"""
Enter your sentence: python is amazing
Length: 3
Result first word: python
Result last word: amazing
Result shortest word: is
Result longest word: amazing
"""

# CASE BORDE
"""
Enter your sentence: code
Length: 1
Result first word: code
Result last word: code
Result shortest word: code
Result longest word: code
"""

# CASE ERROR
"""
Enter your sentence:   
Error: invalid input
"""

# 7.5 Problem 5: Password strength classifier
# Description: Classifies a password as "weak", "medium", or "strong" based on
# minimum rules documented in internal validations.

# Inputs
password_input = input("Enter a password: ").strip() # Read password string and trim whitespace

# Check if password input is empty
if not password_input:  
    # Outputs
    print("Error: invalid input")  

else:
    has_upper = False  # Initialize boolean flag for uppercase letters
    has_lower = False  # Initialize boolean flag for lowercase letters
    has_digit = False  # Initialize boolean flag for numeric digits
    has_symbol = False # Initialize boolean flag for non-alphanumeric symbols

    for character in password_input:  # Iterate through each character in the password string
        if character.isupper():  # Check if current character is an uppercase letter
            has_upper = True
        elif character.islower():  # Check if current character is a lowercase letter
            has_lower = True
        elif character.isdigit():  # Check if current character is a number digit
            has_digit = True
        else:
            has_symbol = True  # If none of the above, mark it as a special symbol

    # Evaluate password strength based on length and character composition rules
    if len(password_input) < 8:  # Check if password length is less than 8 characters
        strength = "weak"  # Classify short passwords as weak
    elif has_upper and has_lower and has_digit and has_symbol:  # Check if all four character types are present
        strength = "strong"  # Classify complex passwords as strong
    else:
        strength = "medium"  # Classify intermediate passwords as medium

    # Outputs
    print("Result:", strength)  # Display final security classification level

# CASE NORMAL
"""
Enter a password: Margarita569!
Result: strong
"""

# CASE BORDE
"""
Enter a password: pastelito1
Result: medium
"""

# CASE ERROR
"""
Enter a password: 
Error: invalid input
"""


# 7.6 Problem 6: Product label formatter (fixed-width text)
# Description: Given a product name and its price, generates a single-line label
# with the format: Product: <NAME> | Price: $<PRICE>
# The complete string must be exactly 30 characters long (padded with trailing
# spaces if shorter, or truncated if longer).

# Inputs
product_name = input("Enter the product name: ").strip() # Read product name string

# Validate product name is not empty
if not product_name:
    # Outputs
    print("Error: invalid input")

else:
    product_price = input("Enter the product price: ").strip() # Read price as string
    
    # Validate product price is not empty
    if not product_price:
        # Outputs
        print("Error: invalid input")
    else:
        product_value = float(product_price) # Convert price string to float for calculations

        # Validate that price is greater than zero
        if product_value <= 0:
            # Outputs
            print("Error: invalid input")
            
        else:
            # Format the label string using an f-string interpolating name and price with 2 decimals
            label = f"Product: {product_name} | Price: ${product_value:.2f}"  # Construct base product label

            # Adjust label length to exactly 30 characters
            if len(label) < 30:  # Check if label length is shorter than 30
                label = label + " " * (30 - len(label))  # Append necessary spaces to reach 30 characters
            else:
                label = label[:30]  # Slice the label to keep strictly the first 30 characters if too long

            # Outputs
            print("Result:", label)  # Display the formatted label string
            print("Length:", len(label))  # Verify and display final string length


# CASE NORMAL
"""
Enter the product name: grapes
Enter the product price: 12.50
Result: Product: grapes | Price: $12.50
Length: 30
"""

# CASE BORDE
"""
Enter the product name: pencil
Enter the product price: 1.5
Result: Product: pencil | Price: $1.50
Length: 30
"""

# CASE ERROR
"""
Enter the product name: 
Error: invalid input
"""
# 8. CONCLUSIONS
# Strings are a bridge between the program and the user, so handling them is crucial for inputs and outputs.
# Methods like lower() make text lowercase, strip() removes spaces, split() divides strings, and join() combines elements.
# Normalizing text before comparing it improves the accuracy of the evaluation process.
# Good validation design acts as a quality filter, preventing errors and junk data.
# Strings don't change once created, but slicing allows you to extract parts of them.
"""
Rreferences:
1.De la Cruz, R. (2026). Python Class Repository and Notes. GitHub.
   https://github.com/Renata-2630424/Python_class
2. Python Software Foundation. (2026). Python standard library: 
string — Common string operations (Version 3.15.0) [Documentation]. Python Software Foundation. 
https://docs.python.org/3/library/string.html
3. CharlyMercury. (2026). Programming-methodologies [Repositorio de GitHub]. 
GitHub. https://github.com/CharlyMercury/programming-methodologies-.git
4. Visually Explained. (2025, 31 de diciembre). Python Strings - Visually Explained [Video]. 
YouTube. https://www.youtube.com/watch?v=vheAwWSyEC8
5. Info-Prof. (2026, 23 de julio). Python String-Funktionen einfach erklärt | Die wichtigsten Methoden für Anfänger [Video]. 
YouTube. https://www.youtube.com/watch?v=JCiFomQiovw
"""