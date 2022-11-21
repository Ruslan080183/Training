# list
sequence = input("Enter a sequence of numbers to create a list :")
sequence_list = list(sequence)
del sequence_list[1::2]
print(sequence_list)
# tuple
sequence_tuple = input("Enter a sequence of numbers to create a tuple :")
sequence_tuple1 = tuple(sequence_tuple)
sequence_tuple_end = sequence_tuple1[::2]
print(sequence_tuple_end)
