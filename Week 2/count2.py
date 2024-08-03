test_str = "Computer Science is a liberal art, it teaches you how to think."
print(f"The original string is: {test_str}")

res = {key: test_str.count(key) for key in test_str.split()}
print("The words frequency: " + str(res))