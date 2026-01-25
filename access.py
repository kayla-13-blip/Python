def update_student_record(filename, mode):
    """
    mode 'w' will overwrite the file.
    mode 'a' will add to the end of the file.
    """
    print(f"\n--- Recording Student Info (Mode: {mode}) ---")
    name = input("Enter Student Name: ")
    fav_subject = input("Enter Favorite Subject: ")
    
    # Using 'with' automatically closes the file after writing
    with open(filename, mode) as file:
        file.write(f"Student: {name} | Favorite Subject: {fav_subject}\n")
    print("Record updated successfully!")

def view_records(filename):
    print("\n--- Current Class Records ---")
    try:
        with open(filename, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("No records found yet. Please add a student first.")

# --- Roy's Command Center ---
filename = "class_8_records.txt"

# 1. Overwriting the file (Starting a new record for the term)
# update_student_record(filename, "w")

# 2. Adding more students (Appending to the list)
update_student_record(filename, "a")

# 3. Reading the records
view_records(filename)
