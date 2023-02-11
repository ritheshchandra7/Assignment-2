dict_keys = {}
 
for i in range(97, 97+26):
    
    dict_keys[chr(i)] = i

print('The dictionary of alphabets to correspondng ASCII values:')
print(dict_keys)