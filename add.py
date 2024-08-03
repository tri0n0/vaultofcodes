task = []

limit = int(input("Enter the number of task you want to add: "))
for i in range(limit): 
    take = input(f"Enter the {i+1} task: ")
    task.append(take)
format_task = [f"{i+1}. {task}" for i, task in enumerate(task)]
print("\nList of task to be done are: ")
print("\n".join(format_task))

