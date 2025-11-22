# Module to handle user input and validation

def get_user_responses(questions_list):
    """Gathers responses from the user, ensuring input is not empty."""
    answers = []
    print("\nPlease answer the following questions:")
    
    for q in questions_list:
        valid = False
        while not valid:
            ans = input(q).strip() # .strip() removes whitespace
            if ans != "":
                answers.append(ans)
                valid = True
            else:
                print("⚠️ Error: Input cannot be empty. Please try again.")
    return answers
