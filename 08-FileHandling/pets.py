###
# Reads the entire contents of a file
#
def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content

# reads the entire file and splits lines into array
file_lines = read_from_file('pets.txt').splitlines()

# calculates the total number of cars parked
totalc = 0
for line in file_lines:
   totalc += len(line)

print('Total characters:', totalc)