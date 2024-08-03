#main function(add,delete,display the list of task, function to mark if the task is complete or not)
print("\n")
print(":::::::::::Choose one of the options::::::::::")
print("1. Add")
print("2. Delete")
print("3. Display")
print("4. Mark")

take = input("Enter your choice: ")
if take == '1': 
    data = input("Enter: ")
    print(f"The data is: {data}")
    if data == 'done': 
        break
elif take == '2':
    print("2")
elif take == '3':
    print("3")
else: 
    print("4")
