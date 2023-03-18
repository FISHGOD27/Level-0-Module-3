from tkinter import simpledialog, Tk
from playsound import playsound

can_play_sounds = False



def many_shiny_objects():
    # TODO 1) Call the method above to play Mister Zee
    # TODO 2) Ask the user how many shiny objects they want
    q=simpledialog.askinteger(title="e", prompt="how many shiny objects do you want?(lol)")
    # TODO 3) Play the sound that many times
    for i in range(q):
        playsound('shiny-objects.wav')
    pass


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    many_shiny_objects()
