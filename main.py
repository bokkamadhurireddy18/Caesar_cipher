alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#ART
import art
print(art.logo)

def cesar(direction, text, shift):
  new_text=""
  if (direction=="decode"):
    shift*= -1
  for i in range(0,len(text)):
    if text[i] in alphabet:
      pos = alphabet.index(text[i])
      new_text+= alphabet[pos+shift]
    else:
      new_text+= text[i]
    
  print(f"The {direction}d text is "+ new_text)
  
'''
def encrypt(text, shift):
  cipher_text=""
  for i in range(0,len(text)):
    pos = alphabet.index(text[i])
    cipher_text+= alphabet[pos+shift]
  print("The encoded text is "+ cipher_text)
    
def decrypt(text, shift):
  original_text=""
  for i in range(0,len(text)):
    pos = alphabet.index(text[i])
    original_text+= alphabet[pos-shift]
  print("The decoded text is "+ original_text)
  '''

generate= True
while generate:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift=shift % 26
  cesar(direction, text, shift)

  result = input("Do you want to continue? yes or no?")
  if result=="no":
    generate= False
    print("Thank you")