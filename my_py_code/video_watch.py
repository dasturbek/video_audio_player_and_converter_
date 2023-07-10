from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import QUrl, Qt, QTime
from PyQt6.QtGui import QIcon, QShortcut, QKeySequence
from PyQt6.QtWidgets import QVBoxLayout

from my_py_code.player import VideoPlayerMain


class VideoWatch(QtWidgets.QDialog):
    def __init__(self, parent=None, filepath="C:/Users/dastu/Videos/Chroma Music - We Will End This Fight.mp4"):
        super(VideoWatch, self).__init__(parent)
        self.filepath = filepath
        self.video_slider = None
        self.video_point_2 = None
        self.main_video_player = VideoPlayerMain()
        self.main_video_player.loadFilm(filepath)

        self.filepath = None
        self.video_media_player = None
        self.video_out_put = None
        self.video_size = None
        self.video_sound_slider = None
        self.video_proses = None
        self.video_point = None
        self.video_sound = None
        self.add_video_file = None
        self.stop_video = None
        self.bool_sound = True
        self.play_video = None
        self.video_player_widget = None

        uic.loadUi('./gui/video_watch.ui', self)

        # video load
        vbox = QVBoxLayout()
        self.main_video_player.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.main_video_player.hideSlider()
        vbox.setContentsMargins(0, 0, 0, 0)
        vbox.addWidget(self.main_video_player)
        self.video_player_widget.setLayout(vbox)

        self.load_widgets_find()  # find widgets
        self.load_clicked()  # clicked buttons

        # shot cut

        self.shortcut = QShortcut(QKeySequence(Qt.Key.Key_Up), self)
        self.shortcut.activated.connect(self.volumeUp)
        self.shortcut = QShortcut(QKeySequence(Qt.Key.Key_Down), self)
        self.shortcut.activated.connect(self.volumeDown)

    def load_widgets_find(self):
        #  video player
        self.video_player_widget = self.findChild(QtWidgets.QWidget, 'video_player_widget')
        self.play_video = self.findChild(QtWidgets.QPushButton, 'play_video')
        self.video_sound = self.findChild(QtWidgets.QPushButton, 'video_sound')
        self.video_point = self.findChild(QtWidgets.QLabel, 'video_point')
        self.video_point_2 = self.findChild(QtWidgets.QLabel, 'video_point_2')
        self.video_size = self.findChild(QtWidgets.QLabel, 'video_size')
        self.video_proses = self.findChild(QtWidgets.QProgressBar, 'video_prosses')
        self.video_slider = self.findChild(QtWidgets.QSlider, 'video_slider')
        self.video_sound_slider = self.findChild(QtWidgets.QSlider, 'video_sound_slider')
        k = self.main_video_player.audioOutput.volume()
        k = int(k*100)
        self.video_sound_slider.setValue(k)

    def load_clicked(self):
        self.play_video.clicked.connect(self.played_video)
        self.video_sound_slider.valueChanged[int].connect(self.change_video_volume)
        self.video_sound.clicked.connect(self.video_sound_mute)
        self.main_video_player.mediaPlayer.positionChanged.connect(self.positionChang)
        self.main_video_player.mediaPlayer.durationChanged.connect(self.durationChang)
        self.video_slider.sliderMoved.connect(self.set_position)


    '''
    video player
    '''
    def set_position(self, position):
        self.main_video_player.mediaPlayer.setPosition(position)

    def positionChang(self, position):
        self.video_proses.setValue(position)
        self.video_slider.setValue(position)
        mtime = QTime(0, 0, 0, 0)
        mtime = mtime.addMSecs(self.main_video_player.mediaPlayer.position())
        self.video_point.setText(mtime.toString())

    def durationChang(self, duration):
        self.video_slider.setRange(0, duration)
        self.video_proses.setRange(0, duration)
        mtime = QTime(0, 0, 0, 0)
        mtime = mtime.addMSecs(self.main_video_player.mediaPlayer.duration())
        self.video_point_2.setText(mtime.toString())

    def change_duration(self, duration):
        self.video_slider.setRange(0, duration)

    def change_video_volume(self, value):
        if value == 0:
            self.video_sound.setIcon(QIcon('./gui/qrc/no_sound.png'))
        else:
            self.video_sound.setIcon(QIcon('./gui/qrc/sound.png'))
        self.main_video_player.audioOutput.setVolume(value/100)

    def video_sound_mute(self):
        if self.main_video_player.audioOutput.isMuted():
            self.video_sound.setIcon(QIcon('./gui/qrc/sound.png'))
            self.main_video_player.audioOutput.setMuted(False)
        else:
            self.video_sound.setIcon(QIcon('./gui/qrc/no_sound.png'))
            self.main_video_player.audioOutput.setMuted(True)

    def played_video(self):
        if self.main_video_player.play():
            self.play_video.setIcon(QIcon('./gui/qrc/play.png'))
        else:
            self.play_video.setIcon(QIcon('./gui/qrc/pause.png'))

    def volumeUp(self):
        self.main_video_player.audioOutput.setVolume(self.main_video_player.audioOutput.volume() + 0.05)
        k = self.main_video_player.audioOutput.volume()
        k = int(k*100)
        self.video_sound_slider.setValue(k)
        print(k)

    def volumeDown(self):
        self.main_video_player.audioOutput.setVolume(self.main_video_player.audioOutput.volume() - 0.05)
        k = self.main_video_player.audioOutput.volume()
        k = int(k*100)
        self.video_sound_slider.setValue(k)
        print(k)
