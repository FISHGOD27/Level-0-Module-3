from tkinter import simpledialog, messagebox, Tk
import webbrowser


# Use this function to play a video from the internet
def play_video(url):
    webbrowser.open(url)

# =================== DO NOT MODIFY THE CODE ABOVE ===========================


if __name__ == '__main__':
    # TODO 1) Make a new window variable, window = Tk()
    window = Tk()
    #      2) Hide the window using the window's .withdraw() method
    window.withdraw()
    #      3) Ask the user how many cats they have
    j=simpledialog.askinteger(title="meow?", prompt="meow? (how many cats do you own?")
    #      4) If they have 3 or more cats, tell them they are a crazy cat lady
    if j >= 100:
        messagebox.showinfo(message="3853 Rosecrans Street San Diego. Go Now.")
    elif j >= 3:
        messagebox.showinfo(message="yu r crosy crt lqdy")
    elif j == 3:
        play_video("https://www.youtube.com/watch?v=YSHDBB6id4A2")
    elif j == 2:
        play_video("https://www.youtube.com/watch?v=YSHDBB6id4A2")
    elif j == 1:
        play_video("https://www.youtube.com/watch?v=YSHDBB6id4A2")
    elif j == 0:
        play_video("https://www.youtube.com/watch?v=cozpr4me3eo")

    #      5) If they have less than 3 cats AND more than 0 cats, call the
    #         play_video function below to show them a cat video
    #      6) If they have 0 cats, show them a video of A Frog Sitting on a
    #         Bench Like a Human

    pass
