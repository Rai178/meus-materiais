# import os


# # # r = Read 
# # # a = Append
# # # w = Write
# # # x = Create

# # # Read - error if it doesn't exist

# # f = open("python_crash_course/ch9/names.txt", "r")
# # # print(f.read())
# # # print(f.read(4))

# # # print(f.readline())
# # # print(f.readline())

# # for line in f:
# #     print(line)

# # f.close()

# # try:
# #     f = open("name_list.txt")
# #     print(f.read())
# # except:
# #     print("The file you want to read doesn't exist")
# # finally:
# #     f.close()

# # Append - creates the file if it doesn't exist
# f = open("python_crash_course/ch9/names.txt", "a")
# f.write("\nNeil")
# f.close()

# f = open("python_crash_course/ch9/names.txt")
# print(f.read())
# f.close()

# # Write (overwrite)
# f = open("python_crash_course/ch9/names.txt", "w")
# f.write("I delete all of the context")
# f.close()

# f = open("python_crash_course/ch9/names.txt")
# print(f.read())
# f.close()

# # Two ways to create a new file

# # Opens a file for writing, creates the file if it does not exist
# f = open("name_list.txt", "w")
# f.close()

# # Creates the specified file, but returns an error if the file exists
# if not os.path.exists("dave.txt"):
#     f = open("dave.txt", "x")
#     f.close()

# # avoid an error if it doesn't exist
# if os.path.exists("dave.txt"):
#     os.remove("dave.txt")
# else:
#     print("The file you with to delete does not exist")

# with open("more_names.txt") as f:
#     content = f.read()

# with open("names.txt", "w") as f:
#     f.write(content)

filename = 'example.txt'

# Step 1: Read the file and replace text
with open(filename, 'r',encoding='utf-8') as file:
    content = file.read()

# Perform text replacement
new_content = content.replace('old', 'new')

# Step 2: Overwrite the original file with the modified content
with open(filename, 'w', enconding='utf-8') as file:
    file.write(new_content) # Write the new content

print(f"The occurrences of 'old' have been replaces with 'new' in '{filename}'.")