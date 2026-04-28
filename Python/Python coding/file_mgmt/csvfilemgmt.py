import csv
import os

def write_csv(filename):
    data = [
        {'name': 'Sai', 'age': 22},
        {'name': 'Kiran', 'age': 25}
    ]
    # Write header and rows
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "age"])
        writer.writeheader()
        writer.writerows(data)
    print(f"Wrote {filename} successfully")

def read_csv(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(f"Name: {row['name']}, Age: {row['age']}")
    else:
        print(f"{filename} does not exist.")

def delete_csv(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Deleted {filename} successfully")
    else:
        print(f"{filename} not found")

# Example usage
filename = "data.csv"
write_csv(filename)
print("Data read from CSV file:")
read_csv(filename)
# delete_csv(filename)
