from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import QUrl, QFileInfo, QDir, QTime, Qt
from PyQt6.QtGui import QIcon, QShortcut, QKeySequence
from PyQt6.QtWidgets import QFileDialog
from my_py_code.custom_music_listitem import MusicPlayerCustomQWidget
import eyed3

from my_py_code.player import VideoPlayerMain


class MusicListen(QtWidgets.QDialog):
    def __init__(self, parent=None, filepath="C:/Users/dastu/Music/Serhat Durmus hislerim.mp3"):
        super(MusicListen, self).__init__(parent)
        self.filepath = filepath
        self.closeEvent = self.CloseEventMusic

        self.main_music_play = VideoPlayerMain()
        self.main_music_play.loadFilm(filepath)
        self.play_music = None
        self.music_playlist = None
        self.next_music = None
        self.prev_music = None
        self.music_sound_slider = None
        self.music_slider = None
        self.music_point = None
        self.music_point_2 = None
        self.current_music_file_name = None
        self.music_sound = None
        uic.loadUi('./gui/music_listen.ui', self)

        self.list = []
        self.item = []
        self.music_list = []

        self.load_widgets_find()  # find widgets
        self.load_clicked()  # clicked buttons
        self.current_file_name()

    def load_widgets_find(self):
        self.play_music = self.findChild(QtWidgets.QPushButton, 'play_music')
        self.play_music.setIcon(QIcon('./gui/qrc/play.png'))
        self.music_sound = self.findChild(QtWidgets.QPushButton, 'music_sound')
        self.music_point = self.findChild(QtWidgets.QLabel, 'music_point')
        self.music_point_2 = self.findChild(QtWidgets.QLabel, 'music_point_2')
        self.current_music_file_name = self.findChild(QtWidgets.QLabel, 'current_music_file_name')
        self.music_slider = self.findChild(QtWidgets.QSlider, 'music_slider')
        self.music_sound_slider = self.findChild(QtWidgets.QSlider, 'music_sound_slider')
        self.music_sound = self.findChild(QtWidgets.QPushButton, 'music_sound')

    def load_clicked(self):
        #  music
        self.music_sound_slider.valueChanged[int].connect(self.change_music_volume)
        self.play_music.clicked.connect(self.play_music_pause)
        self.music_sound.clicked.connect(self.music_sound_mute)
        self.music_slider.sliderMoved.connect(self.set_position)

        k = self.main_music_play.audioOutput.volume()
        print(k)
        k = int(k * 100)
        self.music_sound_slider.setValue(k)

        self.main_music_play.mediaPlayer.positionChanged.connect(self.positionChang)
        self.main_music_play.mediaPlayer.durationChanged.connect(self.durationChang)
        # shot cut

        self.shortcut = QShortcut(QKeySequence(Qt.Key.Key_Up), self)
        self.shortcut.activated.connect(self.volumeUp)
        self.shortcut = QShortcut(QKeySequence(Qt.Key.Key_Down), self)
        self.shortcut.activated.connect(self.volumeDown)

    def CloseEventMusic(self, event):
        self.main_music_play.handleQuit()
    '''
    music player
    '''

    def current_file_name(self):
        filename2 = QFileInfo(self.filepath)
        self.current_music_file_name.setText(filename2.fileName())

    def set_position(self, position):
        self.main_music_play.mediaPlayer.setPosition(position)

    def play_music_pause(self):
        if self.main_music_play.play():
            self.play_music.setIcon(QIcon('./gui/qrc/play.png'))
        else:
            self.play_music.setIcon(QIcon('./gui/qrc/pause.png'))

    def music_sound_mute(self):
        if self.main_music_play.audioOutput.isMuted():
            self.music_sound.setIcon(QIcon('./gui/qrc/sound.png'))
            self.main_music_play.audioOutput.setMuted(False)
        else:
            self.music_sound.setIcon(QIcon('./gui/qrc/no_sound.png'))
            self.main_music_play.audioOutput.setMuted(True)

    def change_music_volume(self, value):
        self.main_music_play.audioOutput.setMuted(False)
        if value == 0:
            self.music_sound.setIcon(QIcon('./gui/qrc/no_sound.png'))
        else:
            self.music_sound.setIcon(QIcon('./gui/qrc/sound.png'))
        self.main_music_play.audioOutput.setVolume(value / 100)

    def positionChang(self, position):
        self.music_slider.setValue(position)
        mtime = QTime(0, 0, 0, 0)
        time1 = self.main_music_play.mediaPlayer.position()
        mtime = mtime.addMSecs(time1)
        self.music_point.setText(mtime.toString())

        # default next song
        position = self.main_music_play.mediaPlayer.duration()
        if position // 1000 == time1 // 1000:
            self.music_slider.setValue(0)

    def durationChang(self, duration):
        self.music_slider.setRange(0, duration)
        mtime = QTime(0, 0, 0, 0)
        mtime = mtime.addMSecs(self.main_music_play.mediaPlayer.duration())
        self.music_point_2.setText(mtime.toString())

    def volumeUp(self):
        self.main_music_play.audioOutput.setVolume(self.main_music_play.audioOutput.volume() + 0.05)
        k = self.main_music_play.audioOutput.volume()
        k = int(k * 100)
        self.music_sound_slider.setValue(k)

    def volumeDown(self):
        self.main_music_play.audioOutput.setVolume(self.main_music_play.audioOutput.volume() - 0.05)
        k = self.main_music_play.audioOutput.volume()
        k = int(k * 100)
        self.music_sound_slider.setValue(k)
