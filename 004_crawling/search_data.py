import csv
import datetime

# 20250508_143507_AI.csv
data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"],
    ["Charlie", 35, "Chicago"],
]


def save_data_to_csv(data):
    # Generate filename with specific format
    current_time = datetime.datetime.now()
    timestamp = current_time.strftime("%Y%m%d_%H%M%S")
    filename = f"{timestamp}_AI.csv"

    # Write data to CSV file
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print(f"Data saved to {filename}")


# Call the function
save_data_to_csv(data)
