import audioop
import time
from collections import deque

from speech_recognition import AudioSource

BYTES_PER_FRAME_STEREO = 3840
SAMPLES_PER_FRAME_MONO = 960


class PCMSource(AudioSource):
    """Creates a new instance which stores PCM frames temporarily for SpeechRecognition."""

    def __init__(self):
        self.SAMPLE_WIDTH = 2
        self.SAMPLE_RATE = 48000
        self.CHUNK = SAMPLES_PER_FRAME_MONO  # For SpeechRecognition time calculations
        self.stream = self  # SpeechRecognition workaround
        self.buffer = deque()

    def write(self, frames):
        for i in range(0, len(frames), BYTES_PER_FRAME_STEREO):
            self.buffer.append(frames[i : i + BYTES_PER_FRAME_STEREO])

    def _read(self, size=-1):
        if size < 0:
            size = len(self.buffer)
        else:
            # Size in number of frames
            size = size // SAMPLES_PER_FRAME_MONO

        frames = bytearray()
        while self.buffer and size > 0:
            frames.extend(self.buffer.popleft())
            size -= 1

        return audioop.tomono(frames, self.SAMPLE_WIDTH, 1, 1)

    def read(self, size=-1):
        # If there is no data left, SpeechRecognition takes it as the sentence is finished.
        # So we try to read a second time after one second.
        b = self._read(size)

        if b:
            return b

        time.sleep(1)
        return self._read(size)
