#Dictionary Creation:

#To create a dictionary, you enclose key-value pairs within curly braces { }, separating each pair with a colon :. Here's an example:

student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science"
}
#Dictionary Access:

#You can access the values in a dictionary by referring to their corresponding keys. Keys provide a way to uniquely identify and retrieve values. Here's an example:

print(student["name"])   # Output: "Alice"
print(student["age"])    # Output: 20
#Dictionary Modification:

#Dictionaries are mutable, which means you can modify their values by assigning new values to specific keys. Here's an example:

student["age"] = 21       # Modifying a value
student["city"] = "London"    # Adding a new key-value pair
#Dictionary Operations:

#Python provides various operations that can be performed on dictionaries. Some common operations include:

#Length: The len() function returns the number of key-value pairs in a dictionary.
#Iteration: You can iterate over the keys, values, or key-value pairs of a dictionary using loops.
#Deletion: You can remove a key-value pair from a dictionary using the del keyword.
#Here are some examples:

student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science"
}


print(len(student))          # Output: 3


for key in student:
    print(key, student[key])  # Output: "name Alice", "age 20", "major Computer Science"


del student["age"]           # Deleting a key-value pair