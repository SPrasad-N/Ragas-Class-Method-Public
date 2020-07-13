
# Program for getting info about Ragas and play the audio related to it

import playsound

Raga_input = input("Enter the name of Raag : \n")

class Raga:
    def __init__(self,name,aaroh,avroha):
        self.name = name
        self.aaroh = aaroh
        self.avroha = avroha

    def print_raga(self):
        print(f"Raga {self.name} - \n Aaroh : {self.aaroh} \n Avroha : {self.avroha}")

Dict = {
        "Yaman": Raga("Yaman", " 'Ni Re Ga Ma Dha Ni Sa' ", "Sa' Ni Dha Pa Ma Ga Re Sa"),
        "Kedar": Raga("Kedar", "Ma Ga", "Ni Re"),
        }

if Raga_input.capitalize() in Dict:
    Raga.print_raga(self=Dict[Raga_input.capitalize()])
    print("Do you want to play the audio?\nIf yes type y otherwise n.")
    play_audio = input(" Play? : ")
    if play_audio == "y":
        playsound.playsound(f"Raga/{Raga_input.capitalize()}.mp3")

        exit()
    else:
        print("Exited Successfully!")
        exit()
else:
    print("Wrong input or Raga unavailable")

