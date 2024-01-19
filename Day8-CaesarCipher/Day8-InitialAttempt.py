# The cipher shifts letters by a certain amount to encode a message.

'''
Requirements:
    - Ask the user if they would like to encode or decode a message
    - Ask for the message
    - Ask for the shift number
    - Show the encoded or decoded message
    - Ask the user if they would like to go again
'''
def shift(character, number, minus):
    max = ord('z')
    min = ord('a')
    c_ascii = character
    n = number
    return_c = ''
    if minus:
        n *= -1
    if c_ascii + n > max:
        diff = max - c_ascii
        n = n - diff
        new_ascii = min + n
        return_c = chr(new_ascii)
    elif c_ascii + n < min:
        diff = c_ascii - min
        n = n + diff
        new_ascii = max + n
        return_c = chr(new_ascii)
    else:
        return_c = chr(n + c_ascii)
    return return_c


def cipher(code, message, number):
    m = []
    # Create list of ASCII values for each char in message
    for c in list(message):
        m.append(ord(c))
    
    new_c = []
    new_msg = ''
    if code.lower() == 'encode':
        # Add number to each ASCII value and create new message
        for a in m:
            c = shift(a, number, False)
            new_c.append(c)
            new_msg = f'Here\'s the encoded result: {"".join(new_c)}'
    elif code.lower() == 'decode':
        # Subtract number to each ASCII value and create new message
        for a in m:
            c = shift(a, number, True)
            new_c.append(c)
            new_msg = f'Here\'s the decoded result: {"".join(new_c)}'
    else:
        return 'Not a valid decrypt code'
    return new_msg


running = True

while running:
    code = input('Type "encode" to encrypt, type "decode" to decrypt:\n')

    msg = input('Type your message:\n')
    n = int(input('Type the shift number:\n'))

    new_msg = cipher(code, msg, n)
    print(new_msg)

    again = input('Type "yes" if you want to go again. Otherwise type "no"\n').lower() == 'yes'
    if not again:
        running = False
