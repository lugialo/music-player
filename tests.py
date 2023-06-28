import contextlib
with contextlib.redirect_stdout(None):
    import pygame
    from pygame import mixer
import os
from os import system

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

musics_dir = os.path.join(os.getcwd(), "musics")

music_files = os.listdir(musics_dir)
current_music_index = 0

pygame.mixer.init()
pygame.display.init()


def play_next_music():
    global current_music_index
    current_music_index = (current_music_index + 1) % len(music_files)
    file_name = music_files[current_music_index]
    file_path = os.path.join(musics_dir, file_name)
    mixer.music.load(file_path)
    mixer.music.play()


file_name = "001nao-ha-ferrolhos.mp3"
file_path = os.path.join(musics_dir, file_name)
mixer.music.load(file_path)
mixer.music.set_volume(0.5)
mixer.music.play()

while True:
    if mixer.music.get_busy():
        print("Press 'P' to pause!")
    else:
        print("Press 'R' to resume!")
    print("Press 'C' to change music!")
    print("Press 'V' to set volume!")
    print("Press 'E' to exit!")

    ch = input("['p', 'r', 'v', 'c', 'e']>>> ")
    system("cls")
    if ch == "p":
        mixer.music.pause()
    elif ch == "r":
        mixer.music.unpause()
    elif ch == "v":
        v = float(input("Enter volume (0 to 1): "))
        mixer.music.set_volume(v)
        system("cls")
    elif ch == "c":
        input_file_name = input(
            "Enter the name of the song (without .mp3 extension).\n"
            "NOTE: the song *MUST* be in the 'musics' folder.\n"
        )
        file_path = os.path.join(musics_dir, input_file_name + ".mp3")
        mixer.music.load(file_path)
        mixer.music.play()
        system("cls")
    elif ch == "e":
        exit()

    # Check if music has ended
    if not mixer.music.get_busy():
        play_next_music()
