import pygame
from pygame import mixer
import os

musics_dir = os.path.join(os.getcwd(), "musics")
music_files = os.listdir(musics_dir)
current_music_index = 0
mixer.init()
pygame.display.init()
mixer.music.set_volume(0.5)

# create a clock object to control the timing
clock = pygame.time.Clock()


def play_music():
    global current_music_index
    while True:
        next_music_index = (current_music_index + 1) % len(music_files)
        file_name = music_files[next_music_index]
        file_path = os.path.join(musics_dir, file_name)
        mixer.music.load(file_path)
        mixer.music.play()
        current_music_index = next_music_index
        # wait for the music to finish playing before loading the next one
        while mixer.music.get_busy():
            clock.tick(30)  # set the frame rate to 30 fps


while True:
    print("Press 'P' to pause!")
    print("Press 'R' to resume!")
    print("Press 'C' to change music!")
    print("Press 'V' to set volume!")
    print("Press 'E' to exit!")
    event = pygame.event.wait()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_p:
            mixer.music.pause()
        elif event.key == pygame.K_r:
            mixer.music.unpause()
        elif event.key == pygame.K_v:
            try:
                v = float(input("Enter volume (0 to 1): "))
                if 0 <= v <= 1:
                    mixer.music.set_volume(v)
                else:
                    print("Invalid volume value!")
            except ValueError:
                print("Invalid input!")
        elif event.key == pygame.K_c:
            input_file_name = input(
                "Enter the name of the song (without .mp3 extension). \nNOTE: the song *MUST* be in the 'musics' folder.\n")
            file_path = os.path.join(musics_dir, f"{input_file_name}.mp3")
            if os.path.exists(file_path):
                mixer.music.load(file_path)
            else:
                print("Invalid song name!")
        elif event.key == pygame.K_e:
            break
