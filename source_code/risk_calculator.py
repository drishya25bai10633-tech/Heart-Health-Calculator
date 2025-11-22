# Module to calculate the health risk score

def calculate_risk(answers):
    """Calculates a weighted risk score based on user answers."""
    score = 0
    
    # Logic 1: Age (Index 0)
    try:
        age = int(answers[0])
        if age > 50: score += 3
        elif age > 30: score += 1
    except ValueError:
        # If the user input non-numeric age, treat it as a risk factor.
        score += 1 

    # Logic 2: Smoking is harmful (Index 1) - High Risk Factor
    if answers[1].lower() in ["yes", "y", "yep"]: score += 3

    # Logic 3: Lack of Exercise is unhealthy (Index 2) - Medium Risk Factor
    if answers[2].lower() in ["no", "n", "nope"]: score += 2

    # Logic 4: Family History matters (Index 3)
    if answers[3].lower() in ["yes", "y"]: score += 2

    # Logic 5: Good Diet is necessary (Index 4)
    if answers[4].lower() in ["yes", "y"]: score += 1
    
    return score
