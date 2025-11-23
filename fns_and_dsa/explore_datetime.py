from datetime import datetime


def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    print("Current Date and Time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))


def calculate_future_date():
    """Prompt for a number of days, calculate and print the future date.

    The future date is stored in `future_date` and printed in YYYY-MM-DD format.
    """
    from datetime import timedelta

    while True:
        try:
            days_str = input("Enter the number of days to add to the current date: ")
            days = int(days_str)
            break
        except ValueError:
            print("Please enter a valid integer number of days.")

    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    print("Future date:", future_date.strftime("%Y-%m-%d"))
    return future_date


if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()



