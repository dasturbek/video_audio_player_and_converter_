from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import QUrl, QFileInfo, QDir, QTime, Qt
from PyQt6.QtGui import QIcon, QShortcut, QKeySequence
from PyQt6.QtWidgets import QFileDialog
from my_py_code.custom_music_listitem import MusicPlayerCustomQWidget
import eyed3

from my_py_code.player import VideoPlayerMain


class MusicPlayer(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.song_index = None
        self.main_music_play = VideoPlayerMain()
        self.bool_color = True
        self.play_music = None
        self.music_playlist = None
        self.next_music = None
        self.prev_music = None
        self.bool_sound = True
        self.music_media_playlist = None
        self.music_media_player = None
        self.music_sound_slider = None
        self.music_slider = None
        self.music_size = None
        self.music_point = None
        self.music_point_2 = None
        self.current_music_file_name = None
        self.music_sound = None
        self.stop_music = None
        self.add_music_file = None
        uic.loadUi('./gui/music_player.ui', self)

        self.list = []
        self.item = []
        self.music_list = []

        self.load_widgets_find()  # find widgets
        self.load_clicked()  # clicked buttons

    def load_widgets_find(self):
        #  music player
        self.music_playlist = self.findChild(QtWidgets.QListWidget, 'music_playlist')
        self.play_music = self.findChild(QtWidgets.QPushButton, 'play_music')
        self.play_music.setIcon(QIcon('./gui/qrc/play.png'))
        self.stop_music = self.findChild(QtWidgets.QPushButton, 'stop_music')
        self.add_music_file = self.findChild(QtWidgets.QPushButton, 'add_music_file')
        self.music_sound = self.findChild(QtWidgets.QPushButton, 'music_sound')
        self.music_point = self.findChild(QtWidgets.QLabel, 'music_point')
        self.music_point_2 = self.findChild(QtWidgets.QLabel, 'music_point_2')
        self.current_music_file_name = self.findChild(QtWidgets.QLabel, 'current_music_file_name')
        self.music_size = self.findChild(QtWidgets.QLabel, 'music_size')
        self.music_slider = self.findChild(QtWidgets.QSlider, 'music_slider')
        self.music_sound_slider = self.findChild(QtWidgets.QSlider, 'music_sound_slider')
        self.prev_music = self.findChild(QtWidgets.QPushButton, 'prev_music')
        self.next_music = self.findChild(QtWidgets.QPushButton, 'next_music')
        self.music_sound = self.findChild(QtWidgets.QPushButton, 'music_sound')

    def load_clicked(self):
        #  music
        self.music_sound_slider.valueChanged[int].connect(self.change_music_volume)
        self.add_music_file.clicked.connect(self.music_files)
        self.play_music.clicked.connect(self.play_music_pause)
        self.stop_music.clicked.connect(self.main_music_play.handleQuit)
        self.next_music.clicked.connect(self.nextSong)
        self.prev_music.clicked.connect(self.prevSong)
        self.music_sound.clicked.connect(self.music_sound_mute)
        self.music_slider.sliderMoved.connect(self.set_position)

        self.music_playlist.itemDoubleClicked.connect(self.music_player_list_item_clicked)

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
        self.music_playlist.itemClicked.connect(self.item_clicked)

    '''
    music player
    '''

    def item_clicked(self):
        for i in range(0, len(self.list)):
            if i % 2 == 0:
                self.list[i].frame.setStyleSheet("#frame{"
                                                 "border:none;"
                                                 "background-color: rgb(234, 234, 234);"
                                                 "}"
                                                 "#frame:hover{"
                                                 "background-color:rgb(176, 227, 227);"
                                                 "}")
            else:
                self.list[i].frame.setStyleSheet("#frame{"
                                                 "border:none;"
                                                 "background-color:rgb(250, 250, 250);"
                                                 "}"
                                                 "#frame:hover{"
                                                 "background-color:rgb(176, 227, 227);"
                                                 "}")

        x = self.music_playlist.currentRow()
        self.list[x].frame.setStyleSheet("background-color: #99c5c5;")

    def current_file_name(self):
        filename2 = QFileInfo(self.music_list[self.song_index])
        self.current_music_file_name.setText(filename2.fileName())

    def music_files(self):
        count_music = len(self.music_list)
        music_location = QDir.homePath() + "/Music"
        songs = QFileDialog.getOpenFileNames(self, "Open Song", music_location, "Sound Files (*.mp3 *.wav "
                                                                                "*.flac* *.m4a"
                                                                                "*.mpa *.wma)")

        self.song_index = 0
        (music_list, f_type) = songs

        for filepath in music_list:
            self.music_list.append(filepath)
            if filepath != '':
                url = QUrl.fromLocalFile(filepath)
                # self.music_media_playlist.addMedia(url)
                filename = QFileInfo(filepath)
                position = int(eyed3.load(filepath).info.time_secs)
                hour = position // 3600
                min = (position % 3600) // 60
                sec = position % 60
                duration = ''
                if hour < 10:
                    duration += '0' + str(hour) + ':'
                else:
                    duration += str(hour) + ':'
                if min < 10:
                    duration += '0' + str(min) + ':'
                else:
                    duration += str(min) + ':'
                if sec < 10:
                    duration += '0' + str(sec) + ':'
                else:
                    duration += str(sec)
                self.list.append(MusicPlayerCustomQWidget(None, filepath,
                                                          filename.completeSuffix(),
                                                          str(round(float(filename.size()) / (2 ** 20), 2)),
                                                          duration,
                                                          self.bool_color
                                                          ))
                if self.bool_color:
                    self.bool_color = False
                else:
                    self.bool_color = True
                self.item.append(QtWidgets.QListWidgetItem(self.music_playlist))
                self.current_song_name = f'{music_list[self.song_index]}'
        if count_music == 0 and len(music_list) != 0:
            self.main_music_play.loadFilm(self.current_song_name)

        for i in range(len(self.list)):
            self.item[i].setSizeHint(self.list[i].sizeHint())
            self.music_playlist.setItemWidget(self.item[i], self.list[i])

    def set_position(self, position):
        self.main_music_play.mediaPlayer.setPosition(position)

    def play_music_pause(self):
        if self.main_music_play.play():
            self.play_music.setIcon(QIcon('./gui/qrc/play.png'))
        else:
            self.play_music.setIcon(QIcon('./gui/qrc/pause.png'))

    def nextSong(self):
        self.song_index += 1
        if self.song_index < len(self.music_list):
            self.next_song_name = f'{self.music_list[self.song_index]}'
        else:
            self.song_index = 0
            self.next_song_name = f'{self.music_list[self.song_index]}'
        self.main_music_play.loadFilm(self.next_song_name)
        self.current_song_name = self.next_song_name

    def prevSong(self):
        self.song_index -= 1
        if self.song_index >= 0:
            self.previous_song_name = f'{self.music_list[self.song_index]}'
        else:
            self.song_index = len(self.music_list) - 1
            self.previous_song_name = f'{self.music_list[self.song_index]}'

        self.main_music_play.loadFilm(self.previous_song_name)
        self.current_song_name = self.previous_song_name

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

    def music_player_list_item_clicked(self):
        item_row = self.music_playlist.currentRow()
        clicked_music = f'{self.music_list[item_row]}'
        self.main_music_play.loadFilm(clicked_music)

    def positionChang(self, position):
        self.music_slider.setValue(position)
        mtime = QTime(0, 0, 0, 0)
        time1 = self.main_music_play.mediaPlayer.position()
        mtime = mtime.addMSecs(time1)
        self.music_point.setText(mtime.toString())
        self.current_file_name()
        # default next song
        position = self.main_music_play.mediaPlayer.duration()
        if position // 1000 == time1 // 1000:
            self.nextSong()

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
