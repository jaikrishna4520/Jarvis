import sounddevice as sd
import numpy as np
from openwakeword.model import Model


class WakeWordDetector:
    def __init__(self):
        print("Loading Wake Word Model...")

        self.model = Model(inference_framework="onnx")

        self.sample_rate = 16000
        self.chunk_size = 1280  # 80 ms of audio

        print("Wake Word Model Loaded Successfully.")

    def start(self):
        print("\nListening for wake word...\n")

        with sd.InputStream(
            samplerate=self.sample_rate,
            channels=1,
            dtype="int16",
            blocksize=self.chunk_size,
        ) as stream:

            while True:
                audio_chunk, _ = stream.read(self.chunk_size)

                audio_chunk = audio_chunk.flatten().astype(np.int16)

                predictions = self.model.predict(audio_chunk)

                for wakeword, score in predictions.items():

                    if score > 0.5:
                        print(f"\nWake Word Detected: {wakeword}")
                        print(f"Confidence: {score:.2f}")
                        return