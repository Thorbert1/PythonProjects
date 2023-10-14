import re
import random

pattern = r'[\w]'
allowable_characters = [chr(i) for i in range(128) if re.match(pattern, chr(i))]
output: str = ""

def main():
    global output
    global allowable_characters

    print(allowable_characters)

    while True:
      try:
        pass_length = int(input("Input the length of the password you would want to generate"))
        break
      except ValueError:
        continue
    
    for _ in range(pass_length):
       if allowable_characters:
        output += allowable_characters[round(random.randint(0, len(allowable_characters)-1))]
    print(output)
if __name__ == "__main__":
    main()