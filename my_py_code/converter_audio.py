import sys
import ffmpeg


class ConverterAudio:
    def __init__(self, inp_file=None, out_file=None):
        self.process = None
        self.inp_file = inp_file
        self.out_file = out_file

    def converter_run(self):
        sys.path.append(r'C:\ffmpeg\bin')  # your ffmpeg file path

        stream = ffmpeg.input(self.inp_file)  # video location

        audio = stream.audio.filter("aecho", 0, 1, 1000, 1)
        out = ffmpeg.output(audio, self.out_file)
        ffmpeg.run(out)
