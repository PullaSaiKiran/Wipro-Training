import json
import os


def write_json(filename):
    data = {
        "people": [
            {"name": "Jon Doe", "age": 30},
            {"name": "Jane Smith", "age": 25}
        ]
    }

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)  # corrected 'index' → 'indent'
    print(f"Wrote {filename} successfully")


def read_json(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            data = json.load(file)
            for person in data["people"]:
                print(f"Name: {person['name']}, Age: {person['age']}")
    else:
        print(f"{filename} does not exist.")


def delete_json(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Deleted {filename} successfully")
    else:
        print(f"{filename} not found")


# Example usage:
write_json("people.json")
read_json("people.json")
# delete_json("people.json")
