#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Output files formatted as 'letter_for_[name].txt'

with open(file='Input/Names/invited_names.txt', mode='r') as file:
    names = file.readlines()
for i in range(len(names)):
    names[i] = names[i].strip('\n')


with open(file='Input/Letters/starting_letter.txt', mode='r') as file:
    original_letter = file.read()
    for name in names:
        new_letter = original_letter.replace('[name]', name)
        filename = f'Output/ReadyToSend/letter_for_{name}.txt'
        with open(file=filename, mode='w') as file:
            file.write(new_letter)
