hex_value = 0x5c2f94ba2180
print(hex_value)  # prints as a decimal
print(bytes.fromhex(hex(hex_value)[2:]).decode('utf-8', 'ignore'))  # Try to convert it to text
