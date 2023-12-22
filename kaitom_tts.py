import iapp_ai
import pygame

def generate_and_play_audio(text):
    # You can request an API key at https://ai.iapp.co.th
    apikey = '...'

    api = iapp_ai.api(apikey)

    output_file = "output.mp3"
    response = api.thai_thaitts_kaitom(text)

    with open(output_file, "wb") as f:
        f.write(response.content)

    # Initialize pygame
    pygame.init()
    pygame.mixer.init()

    # Load and play the audio
    pygame.mixer.music.load(output_file)

    pygame.mixer.music.play()

    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # Clean up pygame
    pygame.quit()

'''
user_input = input("x")
generate_and_play_audio(user_input)
'''
