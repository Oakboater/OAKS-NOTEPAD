import json
from datetime import datetime
from time import sleep
while True:
    print("Welcome back User:")
    with open('notes.json', 'a') as file: # FILE LOADING
        note = input("Add ur note :3 ")
        futurenote = input("Anything for the future? ")
        if note == "READ.":
            for letters in "BOOTING UP ˢⁿᵒᵘᵗᶦʷᵃʳᵉ¹ᵒʷᵒ", "( *}w{ *)":
                print(letters) #This will print all of the letters one by one!!!!
                sleep(0.15)
            file.close()
            with open('notes.json', 'r') as read_file:
                try:
                    for line in read_file:
                        if line.strip():
                            print(json.loads(line))
                except json.JSONDecodeError:
                    print("No valid JSON data found.")
        else:
            data = {
                'Time': datetime.now().isoformat(),
                'Note': note,
                'Future note': futurenote
            }
            json.dump(data, file) # DUMP DATA INTO JSON