from datetime import datetime

def generate_password(name):
    # Get current time (hours and minutes)
    current_time = datetime.now().strftime("%H%M")

    # Get current date
    current_date = datetime.now().strftime("%Y%m%d")

    # Concatenate time, name, and date
    password = current_time + name + current_date
    
    return password

if __name__ == "__main__":
    # Get user's name as input
    user_name = input("Enter your name: ")

    # Generate and display the password
    generated_password = generate_password(user_name)
    print(f"Generated Password: {generated_password}")
