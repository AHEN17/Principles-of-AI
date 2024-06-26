# Define the fuzzy sets A and B
A = {"a": 0.1, "b": 0.2, "c": 0.4, "d": 0.6}
B = {"a": 0.2, "b": 0.3, "c": 0.7, "d": 0.5}

# Print the fuzzy sets A and B
print('The First Fuzzy Set is :', A)
print('The Second Fuzzy Set is :', B)

# Initialize an empty dictionary Y to store the results
Y = {}

# Calculate the fuzzy set union
for A_key, B_key in zip(A, B):
    A_value = A[A_key]  # Get the value of A corresponding to the current key
    B_value = B[B_key]  # Get the value of B corresponding to the current key

    if A_value > B_value:
        Y[A_key] = A_value  # Choose the larger value for the union
    else:
        Y[B_key] = B_value  # Choose the larger value for the union

# Print the fuzzy set union
print('Fuzzy Set Union is :', Y)

# Initialize Y again to clear the previous results for intersection
Y = {}

# Calculate the fuzzy set intersection
for A_key, B_key in zip(A, B):
    A_value = A[A_key]  # Get the value of A corresponding to the current key
    B_value = B[B_key]  # Get the value of B corresponding to the current key

    if A_value < B_value:
        Y[A_key] = A_value  # Choose the smaller value for the intersection
    else:
        Y[B_key] = B_value  # Choose the smaller value for the intersection

# Print the fuzzy set intersection
print('Fuzzy Set Intersection is :', Y)
