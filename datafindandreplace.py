file_read= open("data.txt", "r")
file_write= open("data3.txt", "w")

for line in file_read:
	for ch in line:
		if ch=="a":
			print("*", end="",file=file_write)
		else:
			print(ch, end="", file=file_write)