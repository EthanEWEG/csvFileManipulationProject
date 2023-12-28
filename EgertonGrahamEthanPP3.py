import csv
import threading

# Define a Record class to represent data records
class Record:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Age: {self.age}"

# Function to read data from a CSV file and store it in a list of records
class read:
    @staticmethod
    def read_data_from_csv(filename, num_records, records):
        try:
            with open(filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header row (assuming the first row is a header)
                for i, row in enumerate(reader):
                    if i >= num_records:
                        break
                    id, name, age = row  # Extract data from the CSV row
                    record = Record(id, name, age)  # Create a Record object
                    records.append(record)  # Add the record to the list
        except FileNotFoundError:
            print("Error: The file is missing or not available.")

# Function to write data from a list of records to a CSV file
class write:
    @staticmethod
    def write_data_to_csv(filename, records):
        try:
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Name", "Age"])  # Write the header row
                for record in records:
                    writer.writerow([record.id, record.name, record.age])  # Write record data
            print("Data saved to the file.")
        except FileNotFoundError:
            print("Error: The file is missing or not available.")

# Function to display records, either all records or a specific record by ID
class display:
    def display_records(records, record_id):
        found = False  # Initialize a flag to track if the record is found
        for record in records:
            if record.id == record_id:
                print("Record found: ")
                print(record)
                found = True
                break
        if not found:  # If the flag is not set, no record was found
            for record in records:
                print(record)

# Function to create a new record by taking user input
class create:
    def create_record():
        id = input("Enter ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        return Record(id, name, age)  # Create and return a new Record object

# Function to edit a record based on its ID
class edit:
    def edit_record(records, record_id):
        found = False  # Initialize a flag to track if the record is found
        for record in records:
            if record.id == record_id:
                print("Editing Record:")
                print(record)
                record.name = input("Enter new Name: ")  # Update the name
                record.age = input("Enter new Age: ")  # Update the age
                print("Record updated.")
                found = True
                break
        if not found:
            print("Record not found.")

# Function to delete a record based on its ID
class delete:
    def delete_record(records, record_id):
        found = False  # Initialize a flag to track if the record is found
        for record in records:
            if record.id == record_id:
                records.remove(record)  # Remove the record from the list
                print("Record deleted.")
                found = True
                break
        if not found:
            print("Record not found.")

# Main program
def main():
    #File name
    filename = 'data.csv'
    num_records = 100  # Limit to 100 records

    #records = read.read_data_from_csv(filename, num_records)
    records = []
    
    # Use threading for reading data from the CSV file
    read_thread = threading.Thread(target=read.read_data_from_csv, args=(filename, num_records, records))
    read_thread.start()
    # Wait for the read thread to complete
    read_thread.join() 
    
    full_name = "Ethan Egerton-Graham 04108894"  # Programmer credentials

    #Display all options to user
    while True:
        print(f"\nProgram by, {full_name}")
        print("1. Reload data from the dataset")
        print("2. Persist data to a new file")
        print("3. Display records")
        print("4. Create a new record")
        print("5. Edit a record")
        print("6. Delete a record")
        print("7. Exit")

        #Takes user input for the option
        choice = input("Enter your choice: ")

        #implementation of options for the user
        if choice == '1':
            1# Create a new list for reloaded data
            reloaded_records = []
            # Use a new thread for reading data from the CSV file
            read_thread = threading.Thread(target=read.read_data_from_csv, args=(filename, num_records, reloaded_records))
            read_thread.start()
            # Wait for the read thread to complete
            read_thread.join() 
            # Update the main records list with the reloaded data
            records = reloaded_records
            print("Dataset Reloaded")
        elif choice == '2':
            write.write_data_to_csv('new_data.csv', records)
        elif choice == '3':
            record_id = input("Hit enter for full list or input the ID of the record to display: ")
            display.display_records(records, record_id)
        elif choice == '4':
            record = create.create_record()
            records.append(record)
            print("Record added.")
        elif choice == '5':
            record_id = input("Enter the ID of the record to edit: ")
            edit.edit_record(records, record_id)
        elif choice == '6':
            record_id = input("Enter the ID of the record to delete: ")
            delete.delete_record(records, record_id)
        elif choice == '7':
            print("Bye! :)")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

# launch point
if __name__ == "__main__":
    main()