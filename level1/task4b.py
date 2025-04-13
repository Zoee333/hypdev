# Request a sentence from the user, assigned to "str_manip"
str_manip = input("Please enter a sentence: ")
# Print the length of the string
str_len = len(str_manip)
print("String length is {}".format(str_len))
# Find the last letter of the string and replace it with "@", then print it
last_ch = str_manip[-1]
print(str_manip.replace(last_ch, "@"))
# Print the last three characters backwards
print(str_manip[str_len:(str_len-4):-1])
# Print a new string with the first three characters and last two of the user string
new_str = str_manip[0:3] + str_manip[(str_len-2):]
print(new_str)