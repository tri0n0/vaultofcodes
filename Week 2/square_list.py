lst = []
take = int(input("Enter the limit: "))
for i in range(take):
    take1 = int(input(f"Enter the {i+1} element: "))
    take2 = take1**2
    lst.append(take2)
print(f"The list with squares is: {lst}")