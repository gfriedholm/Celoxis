# Function to calculate the percentage
def calculate_percentage(hours, total_hours):
    percentage = (hours / total_hours) * 100
    return percentage

# Get user input for task name and hours
task_name = input("Enter the name of the task: ")
hours_worked = float(input("Enter the number of hours you will work on it: "))
total_hours_in_workweek = 40  # Assuming a 40-hour workweek

# Calculate the percentage
percentage = calculate_percentage(hours_worked, total_hours_in_workweek)

# Print the result
print(f"You will spend {percentage:.2f}% of your workweek on '{task_name}'.")