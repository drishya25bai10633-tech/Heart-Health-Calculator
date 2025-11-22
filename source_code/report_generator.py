# Module to generate the final output report

def print_report(score):
    """Prints the final categorized risk report and advice."""
    
    print("\n" + "=" * 40)
    print(f"       Calculated Risk Score: {score}/11") # Max score is 11 now
    print("=" * 40)

    if score >= 7:
        print("Result: 🔴 HIGH RISK")
        print("Advice: You have significant risk factors. Please consult a doctor for a full check-up soon.")
    elif score >= 4:
        print("Result: 🟠 MODERATE RISK")
        print("Advice: Implement major lifestyle changes (diet, exercise) to lower your risk.")
    else:
        print("Result: 🟢 LOW RISK")
        print("Advice: Your current lifestyle is good. Maintain healthy habits!")
