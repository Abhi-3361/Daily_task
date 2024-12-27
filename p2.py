# Sample Dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Method 1: Using the update() method
result_dict = dic1.copy()  # Create a copy of dic1 to avoid modifying the original
result_dict.update(dic2)  # Add dic2 to result_dict
result_dict.update(dic3)  # Add dic3 to result_dict

print("Concatenated Dictionary:", result_dict)
