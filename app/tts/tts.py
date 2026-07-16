import asyncio
import edge_tts
import pygame
import os


class TextToSpeech:
    def __init__(
        self,
        voice="en-US-AriaNeural",
        output_file="temp/response.mp3"
    ):
        self.voice = voice
        self.output_file = output_file

        os.makedirs("temp", exist_ok=True)

    async def _generate_audio(self, text):
        communicate = edge_tts.Communicate(
            text=text,
            voice=self.voice
        )

        await communicate.save(self.output_file)

    def speak(self, text):
        """
        Convert text to speech and play it.
        """

        asyncio.run(self._generate_audio(text))

        pygame.mixer.init()

        pygame.mixer.music.load(self.output_file)

        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        pygame.mixer.music.unload()