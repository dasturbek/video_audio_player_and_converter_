import sys
import ffmpeg


class ConverterVideo:
    def __init__(self, inp_file=None, out_file=None, format_out=None, resolution=None, rate=None):
        self.process = None
        self.inp_file = inp_file
        self.out_file = out_file
        self.format_out = format_out
        self.resolution = resolution
        self.rate = rate

    def converter_run(self):

        sys.path.append(r'C:\ffmpeg\bin')  # your ffmpeg file path

        stream = ffmpeg.input(self.inp_file)  # video location

        audio = stream.audio.filter("aecho", 0, 1, 1000, 1)

        if (self.format_out == ".mp3" or self.format_out == ".mpa" or
                self.format_out == ".m4a" or self.format_out == ".wav"):
            out = ffmpeg.output(audio, self.out_file)
        else:
            width, height = self.resolution.split("x")
            fps = int(self.rate.replace(" fps", ""))
            video = stream.filter('fps', fps=fps, round='up').filter('scale', w=int(width), h=int(height))
            out = ffmpeg.output(audio, video, self.out_file)

        ffmpeg.run(out)
