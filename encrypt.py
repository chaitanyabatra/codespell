# Function to convert Decimal to Hex
def convert_to_hex(num):
    temp = ""
    while num != 0:
        rem = num % 16
        c = rem + 48 if rem < 10 else rem + 87
        temp += chr(c)
        num //= 16
    return temp

# Function to encrypt the string
def encrypt_string(s):
    ans = ""
    i = 0

    # Iterate the characters of the string
    while i < len(s):
        ch = s[i]
        count = 0

        # Iterate until s[i] is equal to ch
        while i < len(s) and s[i] == ch:
            count += 1
            i += 1

        # Convert count to hexadecimal representation
        hex_count = convert_to_hex(count)

        # Append the character and its frequency in hexadecimal representation
        ans += ch
        ans += hex_count

    # Reverse the obtained answer
    ans = ans[::-1]

    # Return the required answer
    return ans
