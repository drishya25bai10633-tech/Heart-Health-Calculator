# Main Entry Point of the Heart Health Risk Calculator

# Import the necessary modules/libraries
import config
import input_handler
import risk_calculator
import report_generator

def main():
    """
    Orchestrates the program flow: Input -> Process -> Output.
    """
    # 1. Display the system title from config.py
    print("=" * 40)
    print(config.SYSTEM_TITLE)
    print("=" * 40)
    
    # 2. Get Input (calls the input_handler module)
    # The input_handler asks the questions defined in config.py
    responses = input_handler.get_user_responses(config.QUESTIONS)
    
    # 3. Process Data (calls the risk_calculator module)
    # The calculator returns the final score based on the responses
    final_score = risk_calculator.calculate_risk(responses)
    
    # 4. Generate Report (calls the report_generator module)
    # The generator prints the result and advice
    report_generator.print_report(final_score)

if __name__ == "__main__":
    main()
