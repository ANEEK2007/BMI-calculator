# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Function to categorize BMI
def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Main function to get input from the user and display the result
def main():
    # Get user input for weight and height
    try:
        weight = float(input("Enter your weight (in kg): "))
        height = float(input("Enter your height (in meters): "))
        
        # Check for valid input ranges
        if weight <= 0 or height <= 0:
            print("Please enter valid positive values for weight and height.")
            return

        # Calculate BMI
        bmi = calculate_bmi(weight, height)
        
        # Get the BMI category
        category = categorize_bmi(bmi)
        
        # Display the result
        print(f"Your BMI is {bmi:.2f}. You are classified as {category}.")
    
    except ValueError:
        print("Please enter valid numerical values for weight and height.")

# Run the main function
if __name__ == "__main__":
    main()
