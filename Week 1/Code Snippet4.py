def update_record(records, name, score): 
	if name in records: 
		records[name].append(score)
	else:
		records[name] = [score]


student_records = {"Alice": [88,92], "Bob": [70,85]}
update_record(student_records, "Charlie", 91)
update_record(student_records, "Alice", 95)

print(student_records)
