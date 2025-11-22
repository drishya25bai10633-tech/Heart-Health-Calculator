# Heart Health Risk Calculator ❤️

### Submitted by: Drishya Prakash | [25BAI10633]

## 📖 Project Overview
This is a Python-based application developed for the [Your Course Name] course. It functions as a Rule-Based Expert System that assesses a user's risk of heart disease based on lifestyle and biological factors. This project demonstrates the use of structured programming, modular design, and conditional logic to solve a healthcare problem.

## ✨ Features
* **Modular Architecture:** Logic is split into valid input handling, processing, and reporting modules.
* **Input Validation:** Ensures users cannot enter empty or invalid data.
* **Risk Scoring Engine:** Applies weighted logic to Age, Smoking, Exercise, and Dietary habits.
* **Immediate Feedback:** Generates a categorized risk report (Low, Moderate, High).

## 📂 Project Structure
The project follows a modular design to ensure maintainability:
* `source_code/`
    * `main.py`: The entry point of the application.
    * `config.py`: Stores configuration data and questionnaire content.
    * `input_handler.py`: Manages user input validation and error handling.
    * `risk_calculator.py`: Contains the logic for processing health metrics.
    * `report_generator.py`: Handles the final output and advice generation.
* `assets/`: Contains project screenshots and recordings.
* `statement.md`: Detailed problem statement and scope.

## 🛠️ Technology Stack
* **Language:** Python 3
* **Concepts Used:** Modular Programming, Lists, Loops, Exception Handling.

## 🚀 Steps to Install & Run
1.  Clone the repository to your local machine.
2.  Navigate to the source code directory:
    ```bash
    cd source_code
    ```
3.  Run the application:
    ```bash
    python main.py
    ```
4.  Follow the on-screen prompts to enter your health details.

## ✔️ Instructions for Testing
To verify the logic, you can run the following test cases:
1.  **High Risk Test:** Enter Age > 50, Smoker = "yes", Exercise = "no". (Expected: High Risk)
2.  **Low Risk Test:** Enter Age < 30, Smoker = "no", Exercise = "yes". (Expected: Low Risk)
3.  **Validation Test:** Press "Enter" without typing anything to see the error handler.

## 📸 Screenshots
*(Screenshots are available in the /assets folder)*
