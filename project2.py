students = []

def add_student():
   
    roll = input("Enter Roll Number: ")
   
    name = input("Enter Name: ")
   
    age = input("Enter Age: ")
   
    course = input("Enter Course: ")
   
    students.append({"roll": roll, "name": name, "age": age, "course": course})
   
    print("Student added successfully.\n")

def view_students():
   
    if not students:
   
        print("No students found.")
    
    for s in students:
        print(f"Roll: {s['roll']}, Name: {s['name']}, Age: {s['age']}, Course: {s['course']}")

def search_student():
    
    roll = input("Enter Roll Number to search: ")
    
    for s in students:
        if s["roll"] == roll:
            print(f"Found: {s}")
            return
    
    print("Student not found.")

def delete_student():
    
    roll = input("Enter Roll Number to delete: ")
    
    for s in students:
       
        if s["roll"] == roll:
            students.remove(s)
            print("Student deleted.")
            return
    print("Student not found.")

def update_student():
    
    roll = input("Enter Roll Number to update: ")
    
    for s in students:
       
        if s["roll"] == roll:
            
            s["name"] = input("Enter New Name: ")
            
            s["age"] = input("Enter New Age: ")
            
            s["course"] = input("Enter New Course: ")
            
            print("Student updated.")
            
            return
    print("Student not found.")

def menu():
    while True:
        
        print("\n--- Student Management System ---")
        
        print("1. Add Student")
        
        print("2. View All Students")
        
        print("3. Search Student")
        
        print("4. Delete Student")
        
        print("5. Update Student")
        
        print("6. Exit")

        choice = input("Enter choice: ")

       
        if choice == "1":
       
            add_student()
       
        elif choice == "2":
       
            view_students()
       
        elif choice == "3":
       
            search_student()
       
        elif choice == "4":
       
            delete_student()
       
        elif choice == "5":
       
            update_student()
       
        elif choice == "6":
       
            print("Exiting...")
       
            break
       
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
