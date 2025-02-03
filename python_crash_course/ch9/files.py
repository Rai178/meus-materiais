# r = Read 
# a = Append
# w = Write
# x = Create

# Read - error if it doesn't exist

f = open("python_crash_course/ch9/names.text", "r")
# print(f.read(3))

# print(f.readline())
# print(f.readline())

for line in f:
    print(line)

f.close()

try:
    f = open("name_list.text")
    print(f.read())
except:
    print("The file you want to read doesn't exist")
finally:
    f.close()

# Append - creates the file if it doesn't exist
f = open("python_crash_course/ch9/names.text", "a")
f.write("Neil")
f.close()

f = open("python_crash_course/ch9/names.text")
print(f.read())
f.close()