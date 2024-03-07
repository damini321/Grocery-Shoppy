import subprocess


def commit_to_git_in_the_past(date, message):
    """Commits to Git with a past date.

    Args:
      date: The date to commit with.
      message: The commit message.
    """

    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "--date", date, "-m", message])
    subprocess.run(["git", "push"])

from datetime import datetime, timedelta


def get_dates_until_today(start_date_str):
    # Convert the start date string to a datetime object
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')

    # Get today's date as a datetime object
    today = datetime.now()

    # Initialize a list to store the dates
    dates = []

    # Loop from the start date until today's date, inclusive
    current_date = start_date
    while current_date <= today:
        # Append the date in the desired format
        dates.append(current_date.strftime('%Y-%m-%d'))
        current_date += timedelta(days=1)
       # print(current_date)
    return dates


# Example usage
start_date_str = '2024-03-07'
dates_until_today = get_dates_until_today(start_date_str)

for i in dates_until_today:
    print(i, "commenting for date")
    import uuid
    with open(str(uuid.uuid4()), "w") as file:
        # Write some content to the file
        file.write("Hello, this is some content written to the file.\n")
    commit_to_git_in_the_past(i, "My commit message")
    commit_to_git_in_the_past(i, "My commit message")
    commit_to_git_in_the_past(i, "My commit message")
    commit_to_git_in_the_past(i, "My commit message")
    commit_to_git_in_the_past(i, "My commit message")
