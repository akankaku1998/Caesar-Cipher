alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
  new_text=""
  for letter in text:
    if letter in alphabet:
      index = alphabet.index(letter)
      if(direction == "encode"):
        letter = alphabet[index+shift]
      elif(direction == "decode"):
        letter = alphabet[index-shift]
    new_text += letter
  print(f"The {direction}d text is {new_text}")

from art import logo
print(logo)

choice = True 
while(choice):
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  shift = shift % 26

  caesar(text,shift,direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    choice = False
    print("Goodbye")