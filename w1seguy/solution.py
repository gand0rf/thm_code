# text is for the string that the server gives you.
text = '302e2722245507063720211e1e182010520932372508186a35082a1331011612136921161e252b29'

# temp will hold the dehexed value of text
temp = ''

# key is going to store the key value that was used to encrypt the flag
key = ''

# key length given by the box
key_len = 5

# flag format specified by the answer format of the questions
flag_k = 'THM{}'

# variable to hold the unencrypted flag_1
flag_1 = ''

# The loop will go through and unhex the text string from the server
for x in range(0,len(text),2):
    temp += bytearray.fromhex(text[x:x+2]).decode()

# This loop will go through the first four characters of temp and the last one
# and, using flag_k value, find the key that was used to encrypt the flag.
for y in range(0,len(flag_k)):
    if y != 4:
        key += chr(ord(flag_k[y]) ^ ord(temp[y%key_len]))
    else:
        key += chr(ord(flag_k[y]) ^ ord(temp[-1]))

# This last loop will go through temp using the key to get flag_1
for z in range(0,len(temp)):
    flag_1 += chr(ord(temp[z]) ^ ord(key[z%key_len]))

# Print foudn values
print(f'KEY: {key}')
print(f'FLAG_1: {flag_1}')
