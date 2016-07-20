import os

my_string = "Hello, friends."

print(my_string[0:3])

print(my_string)

filepath = "new_file"


out_file = open(filepath, "ab")

print(out_file.mode)
print(out_file.name)

out_file.write(bytes("yo\n", "UTF-8"))

out_file.close()

os.remove(filepath)

# print(os.urandom(24))
