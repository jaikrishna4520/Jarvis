import os
import sounddevice as sd
import soundfile as sf


class AudioRecorder:
    def __init__(self, sample_rate=16000, channels=1):
        self.sample_rate = sample_rate
        self.channels = channels

    def record(self, duration=5, output_file="temp/recording.wav"):
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        print("🎤 Recording...")
        print("Speak now...")

        audio = sd.rec(
            int(duration * self.sample_rate),
            samplerate=self.sample_rate,
            channels=self.channels,
            dtype="float32",
        )

        sd.wait()

        sf.write(output_file, audio, self.sample_rate)

        print("✅ Recording complete.")
        print(f"Saved to: {output_file}")

        return output_file