message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))

new_message = ""
for ch in message:
  if ch >= "a" and ch <= "z":
    pos = ord(ch) - ord("a")  # The ord function converts a character to its integer position within the ASCII table.
    
    # Process a lowercase letter by determining its
    #position in the alphabet(0-25), computing its new 
    #position, and adding it to new message

    pos = (pos + shift) % 26 
    new_char = chr(pos + ord("a")) # The chr function returns the character from ASCII table in the position
    new_message += new_char
  elif ch >= "A" and ch <= "Z":
    pos = ord(ch) - ord("A")
    pos = (pos + shift) % 26 
    new_char = chr(pos + ord("A"))
    new_message += new_char
  else:
    new_message += ch 

print(f"The shifted message is {new_message}")

