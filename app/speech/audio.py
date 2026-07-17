import os
import time

import sounddevice as sd
import soundfile as sf


class AudioRecorder:

    def __init__(self, sample_rate=16000, channels=1):

        self.sample_rate = sample_rate
        self.channels = channels

    def record(self, duration=6, output_file="temp/recording.wav"):

        os.makedirs(
            os.path.dirname(output_file),
            exist_ok=True
        )

        print("\n🎤 Get ready...")

        time.sleep(1)

        print("🎙️ Recording... Speak now!")

        audio = sd.rec(

            int(duration * self.sample_rate),

            samplerate=self.sample_rate,

            channels=self.channels,

            dtype="float32"

        )

        sd.wait()

        sf.write(
            output_file,
            audio,
            self.sample_rate
        )

        print("✅ Recording completed.")

        return output_file

    def list_microphones(self):

        print("\nAvailable Microphones\n")

        devices = sd.query_devices()

        for index, device in enumerate(devices):

            if device["max_input_channels"] > 0:

                print(f"{index} -> {device['name']}")