# Heart Health Risk Calculator
# Submitted by: Drishya Prakash[25BAI10633]
# Project: Rule-Based Expert System using Python Lists and Loops

print("*******************************************")
print("   HEART HEALTH RISK CALCULATOR SYSTEM     ")
print("*******************************************")
print("Please answer the following questions to assess your risk.\n")

# STEP A: Setup the ListS
# We keep questions and answers in parallel lists.
questions = [
    "1. Enter your Age (e.g., 25, 50): ",
    "2. Do you smoke? (yes/no): ",
    "3. Do you exercise daily? (yes/no): ",
    "4. Do you have a family history of heart disease? (yes/no): ",
    "5. Do you often eat fast food / high sugar diet? (yes/no): "
]

answers = [] # This list starts empty

# STEP B: The Input Loop
# We loop through the questions list so we don't have to write input() 5 times.
for q in questions:
    user_input = input(q)
    answers.append(user_input) 

# STEP C: The Risk Calculation (The "Brain")
# Now we analyze the data stored in the 'answers' list.
# answers[0] is Age, answers[1] is Smoking, etc.

risk_score = 0

# Logic 1: Age Check (Convert text to number first)
age = int(answers[0]) 
if age > 50:
    risk_score = risk_score + 2
elif age > 30:
    risk_score = risk_score + 1

# Logic 2: Smoking Check (We use .lower() to handle "Yes" or "yes")
if answers[1].lower() == "yes":
    risk_score = risk_score + 3

# Logic 3: Exercise Check (Lack of exercise increases risk)
if answers[2].lower() == "no":
    risk_score = risk_score + 2

# Logic 4: Family History
if answers[3].lower() == "yes":
    risk_score = risk_score + 2

# Logic 5: Diet
if answers[4].lower() == "yes":
    risk_score = risk_score + 1

# STEP D: The Report (Output)
print("\n===========================================")
print("           FINAL ANALYSIS REPORT           ")
print("===========================================")

print(f"Calculated Risk Score: {risk_score}/10")

if risk_score >= 6:
    print("Result: HIGH RISK ⚠️")
    print("Advice: You have multiple risk factors. Please consult a doctor soon.")
elif risk_score >= 3:
    print("Result: MODERATE RISK ⚠️")
    print("Advice: Consider improving your lifestyle (diet/exercise).")
else:
    print("Result: LOW RISK ✅")
    print("Advice: Great job! Keep maintaining your healthy habits.")

print("===========================================")
