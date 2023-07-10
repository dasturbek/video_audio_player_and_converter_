# import qdarktheme
from PyQt6.QtGui import QIcon
# from qt_material import apply_stylesheet
from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import QPropertyAnimation, QEasingCurve, QUrl, QFileInfo, QStandardPaths, QDir
from PyQt6.QtWidgets import QFileDialog, QMessageBox, QDialogButtonBox

from my_py_code.converter_progress import ConverterProgress
from my_py_code.custom_music_converter_listitem import MusicConverterCustomQWidget
from my_py_code.custom_video_converter_listitem import VideoConverterPlayerCustomQWidget
from my_py_code.finish_custom_music_converter_listitem import FinishMusicConverterCustomQWidget
from my_py_code.finish_custom_video_converter_listitem import FinishVideoConverterPlayerCustomQWidget
from my_py_code.about import About
from my_py_code.settings import Settings
from my_py_code.music_player import MusicPlayer
from my_py_code.video_player import VideoPlayer


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        # finish video
        self.bool_color_audio = True
        self.bool_color_audio_finish = True
        self.bool_color_video = True
        self.bool_color_video_finish = True
        self.converter_progress = None
        # cnvert finish
        self.item_video_list_finish = []
        self.item_video_finish = []
        # converting video
        self.item_video_list_converting = []
        self.item_video_converting = []
        # converting audio
        self.item_audio_list_converting = []
        self.item_audio_converting = []
        # finish audio
        self.item_audio_list_finish = []
        self.item_audio_finish = []

        self.frame_7 = None
        self.finished_audio_list = None
        self.stop_con_audio = None
        self.run_con_audio = None
        self.clear_finish_audio = None
        self.finished_audio = None
        self.converting_audio = None
        self.video = None
        self.music = None
        self.aboutT = None
        self.settings_dialog = None
        self.stop_con_video = None
        self.clear_finish_video = None
        self.run_con_video = None
        self.finshed_video = None
        self.converting_video = None
        self.finished_video_list = None
        self.music_out_path = None
        self.video_out_path = None
        self.video_converter_listwidget = None
        self.audio_converter_listwidget = None
        self.music_converter_add_file = None
        self.video_converter_add_file = None
        self.anim2 = None
        self.page_show = None
        self.leftmenu = None
        self.footer = None
        self.anim = None
        self.new_width_leftmenu = None
        self.width_leftmenu = None
        self.v_bool = None
        self.style_button = None
        self.style_button = str(".QPushButton{"
                                "background-color: rgb(218, 218, 218, 0);"
                                "border: none;"
                                "color: #1A6DFF;"
                                "text-align: left;"
                                "font-size: 22px;"
                                "padding: 10px;"
                                "margin:0 0 0 0;"
                                "}"
                                ".QPushButton:hover{"
                                "background-color: qlineargradient(spread:pad, x1:0, y1:0.489, x2:0.511636, "
                                "y2:0.500318, stop:0 rgba(193, 193, 193, 244), stop:1 rgba(250, 250, 250, "
                                "237)); "
                                "}")
        self.style_button_clicked = str(".QPushButton{"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0.489, x2:0.511636, "
                                        "y2:0.500318, stop:0 rgba(193, 193, 193, 244), stop:1 rgba(250, 250, 250, "
                                        "237)); "
                                        "border: none;"
                                        "color: #1A6DFF;"
                                        "text-align: left;"
                                        "font-size: 22px;"
                                        "padding: 10px;"
                                        "margin:0 0 0 0;"
                                        "border-left: 3px solid rgb(85, 85, 85)"
                                        "}"
                                        ".QPushButton:hover{"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0.489, x2:0.511636, "
                                        "y2:0.500318, stop:0 rgba(193, 193, 193, 244), stop:1 rgba(250, 250, 250, "
                                        "237)); "
                                        "}")
        self.strstyle = str(".QPushButton {"
                            "background-color: rgb(255, 255, 255, 0);"
                            "border: none;"
                            "color: #1A6DFF;"
                            "text-align: center;"
                            "font: 500 22px 'Segoe UI';"
                            "padding: 5px;"
                            "margin:0 0 0 0;"
                            "border-bottom: 3px solid rgb(85, 85, 85)"
                            "}")
        self.settings = None,
        self.dashboard = None,
        self.audio_player = None,
        self.about = None
        self.stars = None
        self.video_player = None
        self.audio_converter = None
        self.video_converter = None

        uic.loadUi('./gui/mainwindow.ui', self)

        # video converter load
        self.list_video_convert = None
        self.item_video_convert = None
        # finish convert video
        self.finish_list_video_convert = None
        self.finish_item_video_convert = None

        # audio converter load
        self.list_music_convert = None
        self.item_music_convert = None
        # finish converter audio
        self.finish_list_music_convert = None
        self.finish_item_music_convert = None

        self.load_widgets_find()  # find widgets
        self.load_clicked()  # clicked buttons

        self.converting_video_def()
        self.converting_audio_def()

        self.show()

    def load_widgets_find(self):
        self.video_converter = self.findChild(QtWidgets.QPushButton, 'video_converter')
        self.audio_converter = self.findChild(QtWidgets.QPushButton, 'audio_converter')
        self.video_player = self.findChild(QtWidgets.QPushButton, 'video_player')
        self.audio_player = self.findChild(QtWidgets.QPushButton, 'audio_player')
        self.about = self.findChild(QtWidgets.QPushButton, 'about')
        self.dashboard = self.findChild(QtWidgets.QPushButton, 'dashboard')
        self.settings = self.findChild(QtWidgets.QPushButton, 'settings')
        self.leftmenu = self.findChild(QtWidgets.QWidget, 'leftmenu')
        self.footer = self.findChild(QtWidgets.QWidget, 'fotter')
        self.page_show = self.findChild(QtWidgets.QStackedWidget, 'stackedWidget')
        self.page_show.setCurrentIndex(2)

        # video converter
        self.video_out_path = self.findChild(QtWidgets.QPushButton, "video_out_path")
        self.video_converter_add_file = self.findChild(QtWidgets.QPushButton, 'video_converter_add_file')
        self.video_converter_listwidget = self.findChild(QtWidgets.QListWidget, 'video_converter_listwidget')
        self.converting_video = self.findChild(QtWidgets.QPushButton, 'converting_video')
        self.finshed_video = self.findChild(QtWidgets.QPushButton, 'finshed_video')
        self.clear_finish_video = self.findChild(QtWidgets.QPushButton, 'clear_finish_video')
        self.run_con_video = self.findChild(QtWidgets.QPushButton, 'run_con_video')
        self.stop_con_video = self.findChild(QtWidgets.QPushButton, 'stop_con_video')
        self.finished_video_list = self.findChild(QtWidgets.QListWidget, 'finished_video_list')
        self.frame_9 = self.findChild(QtWidgets.QFrame, 'frame_9')

        # music converter
        self.music_out_path = self.findChild(QtWidgets.QPushButton, "music_out_path")
        self.music_converter_add_file = self.findChild(QtWidgets.QPushButton, 'music_converter_add_file')
        self.audio_converter_listwidget = self.findChild(QtWidgets.QListWidget, 'audio_converter_listwidget')
        self.converting_audio = self.findChild(QtWidgets.QPushButton, 'converting_audio')
        self.finished_audio = self.findChild(QtWidgets.QPushButton, 'finished_audio')
        self.clear_finish_audio = self.findChild(QtWidgets.QPushButton, 'clear_finish_audio')
        self.run_con_audio = self.findChild(QtWidgets.QPushButton, 'run_con_audio')
        self.stop_con_audio = self.findChild(QtWidgets.QPushButton, 'stop_con_audio')
        self.finished_audio_list = self.findChild(QtWidgets.QListWidget, 'finished_audio_list')
        self.frame_7 = self.findChild(QtWidgets.QFrame, 'frame_7')

    def load_clicked(self):
        self.video_converter.clicked.connect(self.video_converter_window)
        self.audio_converter.clicked.connect(self.audio_converter_window)
        self.video_player.clicked.connect(self.video_player_window)
        self.audio_player.clicked.connect(self.audio_player_window)
        self.about.clicked.connect(self.about_window)
        self.dashboard.clicked.connect(self.dashboard_window)
        self.settings.clicked.connect(self.settings_window)

        # video converter
        self.finshed_video.clicked.connect(self.finish_video_def)
        self.converting_video.clicked.connect(self.converting_video_def)
        self.video_out_path.clicked.connect(self.video_out_path_dialog)
        self.video_converter_add_file.clicked.connect(self.add_video_convert_file)
        self.clear_finish_video.clicked.connect(self.clear_finish_video_all)
        self.run_con_video.clicked.connect(self.run_con_video_show)

        self.video_converter_listwidget.itemClicked.connect(self.item_clicked_vc)
        self.finished_video_list.itemClicked.connect(self.item_clicked_vf)

        music_location = QDir.homePath() + "/Music"
        self.music_out_path.setText(music_location)

        # music converter
        self.music_converter_add_file.clicked.connect(self.add_music_convert_file)
        self.converting_audio.clicked.connect(self.converting_audio_def)
        self.finished_audio.clicked.connect(self.finish_audio_def)
        self.music_out_path.clicked.connect(self.music_out_path_dialog)
        self.clear_finish_audio.clicked.connect(self.clear_finish_audio_all)
        self.run_con_audio.clicked.connect(self.run_con_audio_show)

        self.audio_converter_listwidget.itemClicked.connect(self.item_clicked_ac)
        self.finished_audio_list.itemClicked.connect(self.item_clicked_af)

        movies_location = QDir.homePath() + "/Videos"
        self.video_out_path.setText(movies_location)

    # converter video

    def add_video_convert_file(self):
        movies_location = QDir.homePath() + "/Videos"
        song = QFileDialog.getOpenFileName(self, "Open Video", movies_location, "Sound Files (*.mp4 *.mov *.mkv *.m4v "
                                                                               "*.avi)")
        filepath = song[0]
        if filepath != '':
            url = QUrl.fromLocalFile(filepath)
            filename = QFileInfo(filepath)

            self.list_video_convert = VideoConverterPlayerCustomQWidget(None, filename.fileName(),
                                                                        filename.completeSuffix(),
                                                                        str(round(
                                                                            float(filename.size()) / (2 ** 20),
                                                                            2)),
                                                                        filepath,
                                                                        self.bool_color_video
                                                                        )
            if self.bool_color_video:
                self.bool_color_video = False
            else:
                self.bool_color_video = True

            self.item_video_convert = QtWidgets.QListWidgetItem(self.video_converter_listwidget)

            self.item_video_convert.setSizeHint(self.list_video_convert.sizeHint())
            self.video_converter_listwidget.setItemWidget(self.item_video_convert, self.list_video_convert)

            self.item_video_list_converting.append(self.list_video_convert)
            self.item_video_converting.append(self.item_video_convert)
            self.list_video_convert.close_f.clicked.connect(self.close_item_video_convert)

            self.converting_video_def()

    def run_con_video_show(self):
        row = self.video_converter_listwidget.currentRow()
        if row >= 0:
            filepath = self.item_video_list_converting[row].filepath
            filetype = self.item_video_list_converting[row].format_out
            resolution = self.item_video_list_converting[row].resolution
            rate = self.item_video_list_converting[row].rate
            self.converter_progress = ConverterProgress(self, filepath, self.video_out_path.text(), filetype,
                                                        finish="video", resolution=resolution, rate=rate)
            self.converter_progress.submitClicked.connect(self.on_sub_window_confirm)
            # self.setEnabled(False)
            self.converter_progress.exec()
        else:
            if self.video_converter_listwidget.count() == 0:
                message = QMessageBox()
                message.setWindowTitle("Warning")
                message.setIcon(QMessageBox.Icon.Warning)
                message.setWindowIcon(QIcon("./gui/qrc/dasturbek.png"))
                message.setText("Add video file")
                message.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
                message = message.exec()
                if message == QMessageBox.StandardButton.Yes:
                    self.add_video_convert_file()
            else:
                close = QMessageBox()
                close.setWindowTitle("Warning")
                close.setIcon(QMessageBox.Icon.Warning)
                close.setWindowIcon(QIcon("./gui/qrc/dasturbek.png"))
                close.setText("Sellect Item")
                close.setStandardButtons(QMessageBox.StandardButton.Yes)
                close.exec()

    def close_item_video_convert(self):
        index = None
        btn = self.sender()
        for item_f_l in self.item_video_list_converting:
            if item_f_l.close_f == btn:
                index = self.item_video_list_converting.index(item_f_l)
        # delete item
        self.video_converter_listwidget.takeItem(index)
        self.item_video_list_converting.pop(index)
        self.item_video_converting.pop(index)

    def close_item_video_finish(self):
        index = None
        btn = self.sender()
        for item_f_l in self.item_video_list_finish:
            if item_f_l.close_f == btn:
                index = self.item_video_list_finish.index(item_f_l)
        # delete item
        self.finished_video_list.takeItem(index)
        self.item_video_list_finish.pop(index)
        self.item_video_finish.pop(index)

    def clear_finish_video_all(self):
        self.finished_video_list.clear()

    def video_out_path_dialog(self):
        movies_location = QDir.homePath() + "/Videos"
        video_path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder', movies_location)
        if video_path == "":
            self.video_out_path.setText(self.video_out_path.text())
        else:
            self.video_out_path.setText(video_path)

    '''
    dizayn video converter
    '''

    def converting_video_def(self):
        self.finished_video_list.setHidden(True)
        self.finsh_and_converting_video()
        self.converting_video.setStyleSheet(self.strstyle)
        self.run_con_video.setHidden(False)
        self.stop_con_video.setHidden(False)
        self.video_converter_listwidget.setHidden(False)
        self.frame_9.setHidden(False)
        self.clear_finish_video.setHidden(True)

    def finish_video_def(self):
        self.video_converter_listwidget.setHidden(True)
        self.finsh_and_converting_video()
        self.finshed_video.setStyleSheet(self.strstyle)
        self.run_con_video.setHidden(True)
        self.stop_con_video.setHidden(True)
        self.frame_9.setHidden(True)
        self.finished_video_list.setHidden(False)
        self.clear_finish_video.setHidden(False)

    # converter audio

    def add_music_convert_file(self):
        music_location = QDir.homePath() + "/Music"
        song = QFileDialog.getOpenFileName(self, "Open Audio", music_location, "Sound Files (*.mp3 *.ogg *.wav *.m4a)")
        filepath = song[0]
        if filepath != '':
            url = QUrl.fromLocalFile(filepath)
            filename = QFileInfo(filepath)

            self.list_music_convert = MusicConverterCustomQWidget(None, filename.fileName(),
                                                                  filename.completeSuffix(),
                                                                  str(round(float(filename.size()) / (2 ** 20),
                                                                            2)),
                                                                  filepath,
                                                                  self.bool_color_audio
                                                                  )
            if self.bool_color_audio:
                self.bool_color_audio = False
            else:
                self.bool_color_audio = True

            self.item_music_convert = QtWidgets.QListWidgetItem(self.audio_converter_listwidget)
            self.item_music_convert.setSizeHint(self.list_music_convert.sizeHint())
            self.audio_converter_listwidget.setItemWidget(self.item_music_convert, self.list_music_convert)

            self.item_audio_list_converting.append(self.list_music_convert)
            self.item_audio_converting.append(self.item_music_convert)
            self.list_music_convert.close_f.clicked.connect(self.close_item_audio_convert)

            self.converting_audio_def()

    def run_con_audio_show(self):
        row = self.audio_converter_listwidget.currentRow()
        if row >= 0:
            filepath = self.item_audio_list_converting[row].filepath
            filetype = self.item_audio_list_converting[row].filetype
            converter_progress = ConverterProgress(self, filepath, self.music_out_path.text(), filetype, finish="audio")
            converter_progress.submitClicked.connect(self.on_sub_window_confirm)
            # self.setEnabled(False)
            converter_progress.exec()
        else:
            if self.audio_converter_listwidget.count() == 0:
                message = QMessageBox()
                message.setIcon(QMessageBox.Icon.Warning)
                message.setWindowTitle("Warning")
                message.setWindowIcon(QIcon("./gui/qrc/dasturbek.png"))
                message.setText("Add audio file")
                message.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
                message = message.exec()
                if message == QMessageBox.StandardButton.Yes:
                    self.add_music_convert_file()
            else:
                close = QMessageBox()
                close.setWindowTitle("Warning")
                close.setIcon(QMessageBox.Icon.Warning)
                close.setWindowIcon(QIcon("./gui/qrc/dasturbek.png"))
                close.setText("Sellect Item")
                close.setStandardButtons(QMessageBox.StandardButton.Yes)
                close.exec()

    def close_item_audio_convert(self):
        index = None
        btn = self.sender()
        for item_f_l in self.item_audio_list_converting:
            if item_f_l.close_f == btn:
                index = self.item_audio_list_converting.index(item_f_l)
        # delete item
        self.audio_converter_listwidget.takeItem(index)
        self.item_audio_list_converting.pop(index)
        self.item_audio_converting.pop(index)

    def close_item_audio_finish(self):
        index = None
        btn = self.sender()
        for item_f_l in self.item_audio_list_finish:
            if item_f_l.close_f == btn:
                index = self.item_audio_list_finish.index(item_f_l)
        # delete item
        self.finished_audio_list.takeItem(index)
        self.item_audio_list_finish.pop(index)
        self.item_audio_finish.pop(index)

    def clear_finish_audio_all(self):
        self.finished_audio_list.clear()

    def music_out_path_dialog(self):
        music_location = QDir.homePath() + "/Music"
        music_path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder', music_location)
        if music_path == "":
            self.music_out_path.setText(self.music_out_path.text())
        else:
            self.music_out_path.setText(music_path)

    '''
    dizayn audio converter
    '''

    def converting_audio_def(self):
        self.finsh_and_converting_audio()
        self.converting_audio.setStyleSheet(self.strstyle)
        self.run_con_audio.setHidden(False)
        self.stop_con_audio.setHidden(False)
        self.audio_converter_listwidget.setHidden(False)
        self.frame_7.setHidden(False)
        self.finished_audio_list.setHidden(True)
        self.clear_finish_audio.setHidden(True)

    def finish_audio_def(self):
        self.finsh_and_converting_audio()
        self.finished_audio.setStyleSheet(self.strstyle)
        self.run_con_audio.setHidden(True)
        self.stop_con_audio.setHidden(True)
        self.audio_converter_listwidget.setHidden(True)
        self.frame_7.setHidden(True)
        self.finished_audio_list.setHidden(False)
        self.clear_finish_audio.setHidden(False)

    # finish audio and video
    def on_sub_window_confirm(self, filepath, type_file):
        if type_file == "video":
            self.finish_video_add(filepath)
        else:
            self.finish_audio_add(filepath)

    def finish_video_add(self, filepath):
        self.setEnabled(True)
        filename = QFileInfo(filepath)
        self.finish_list_video_convert = FinishVideoConverterPlayerCustomQWidget(None, filename.fileName(),
                                                                                 filename.completeSuffix(),
                                                                                 str(round(
                                                                                     float(filename.size()) / (
                                                                                             2 ** 20),
                                                                                     2)),
                                                                                 filepath,
                                                                                 self.bool_color_video_finish
                                                                                 )
        if self.bool_color_video_finish:
            self.bool_color_video_finish = False
        else:
            self.bool_color_video_finish = True

        self.finish_item_video_convert = QtWidgets.QListWidgetItem(self.finished_video_list)
        self.finish_item_video_convert.setSizeHint(self.finish_list_video_convert.sizeHint())
        self.finished_video_list.setItemWidget(self.finish_item_video_convert, self.finish_list_video_convert)

        self.item_video_list_finish.append(self.finish_list_video_convert)
        self.item_video_finish.append(self.finish_item_video_convert)
        self.finish_list_video_convert.close_f.clicked.connect(self.close_item_video_finish)
        self.finish_video_def()

    def finish_audio_add(self, filepath):
        self.setEnabled(True)
        filename = QFileInfo(filepath)
        self.finish_list_music_convert = FinishMusicConverterCustomQWidget(None, filename.fileName(),
                                                                           filename.completeSuffix(),
                                                                           str(round(
                                                                               float(filename.size()) / (2 ** 20),
                                                                               2)),
                                                                           filepath,
                                                                           self.bool_color_audio_finish
                                                                           )
        if self.bool_color_audio_finish:
            self.bool_color_audio_finish = False
        else:
            self.bool_color_audio_finish = True
        self.finish_item_music_convert = QtWidgets.QListWidgetItem(self.finished_audio_list)
        self.finish_item_music_convert.setSizeHint(self.finish_list_music_convert.sizeHint())
        self.finished_audio_list.setItemWidget(self.finish_item_music_convert, self.finish_list_music_convert)

        self.item_audio_list_finish.append(self.finish_list_music_convert)
        self.item_audio_finish.append(self.finish_item_music_convert)
        self.finish_list_music_convert.close_f.clicked.connect(self.close_item_audio_finish)
        self.finish_audio_def()

    '''
    dizayn show
    '''

    def video_converter_window(self):
        self.set_style_button_clicked()
        self.video_converter.setStyleSheet(self.style_button_clicked)
        self.page_show.setCurrentIndex(2)

    def audio_converter_window(self):
        self.set_style_button_clicked()
        self.audio_converter.setStyleSheet(self.style_button_clicked)
        self.page_show.setCurrentIndex(1)

    def video_player_window(self):
        self.video = VideoPlayer()
        self.video.show()
        self.hide()
        self.video.closeEvent = self.CloseEventVideo

    def audio_player_window(self):
        self.music = MusicPlayer()
        self.music.show()
        self.hide()
        self.music.closeEvent = self.CloseEventMusic

    def CloseEventMusic(self, event):
        self.show()
        self.music.main_music_play.handleQuit()

    def CloseEventVideo(self, event):
        self.video.main_video_player.handleQuit()
        self.show()

    def settings_window(self):
        self.settings_dialog = Settings()
        self.settings_dialog.exec()

    def about_window(self):
        self.aboutT = About()
        self.aboutT.exec()

    def dashboard_window(self):
        self.width_leftmenu = self.leftmenu.width()
        if self.width_leftmenu == 55:
            self.v_bool = False
            self.new_width_leftmenu = 222
        else:
            self.v_bool = True
            self.new_width_leftmenu = 55

        self.anim = QPropertyAnimation(self.leftmenu, b"minimumWidth")
        self.anim.setDuration(500)
        self.anim.setStartValue(self.width_leftmenu)
        self.anim.setEndValue(self.new_width_leftmenu)
        # self.anim.setEasingCurve(QEasingCurve.InOutCubic)
        self.anim.start()
        self.footer.setHidden(self.v_bool)

    def set_style_button_clicked(self):
        self.video_converter.setStyleSheet(self.style_button)
        self.audio_converter.setStyleSheet(self.style_button)
        self.video_player.setStyleSheet(self.style_button)
        self.audio_player.setStyleSheet(self.style_button)
        self.about.setStyleSheet(self.style_button)
        self.settings.setStyleSheet(self.style_button)

    def finsh_and_converting_video(self):
        strstyle = str(".QPushButton {"
                       "background-color: rgb(255, 255, 255, 0);"
                       "border: none;"
                       "color: #1A6DFF;"
                       "text-align: center;"
                       "padding: 5px;"
                       "margin:0 0 0 0;"
                       "font: 22px 'Segoe UI';"
                       "}"
                       )
        self.converting_video.setStyleSheet(strstyle)
        self.finshed_video.setStyleSheet(strstyle)

    def finsh_and_converting_audio(self):
        strstyle = str(".QPushButton {"
                       "background-color: rgb(255, 255, 255, 0);"
                       "border: none;"
                       "color: #1A6DFF;"
                       "text-align: center;"
                       "padding: 5px;"
                       "margin:0 0 0 0;"
                       "font: 22px 'Segoe UI';"
                       "}"
                       )
        self.converting_audio.setStyleSheet(strstyle)
        self.finished_audio.setStyleSheet(strstyle)

    def item_clicked_vc(self):
        for i in range(0, len(self.item_video_list_converting)):
            if i % 2 == 0:
                self.item_video_list_converting[i].frame.setStyleSheet("#frame{"
                                                                       "border:none;"
                                                                       "background-color: rgb(234, 234, 234);"
                                                                       "}"
                                                                       "#frame:hover{"
                                                                       "background-color:rgb(176, 227, 227);"
                                                                       "}")
            else:
                self.item_video_list_converting[i].frame.setStyleSheet("#frame{"
                                                                       "border:none;"
                                                                       "background-color:rgb(250, 250, 250);"
                                                                       "}"
                                                                       "#frame:hover{"
                                                                       "background-color:rgb(176, 227, 227);"
                                                                       "}")

        x = self.video_converter_listwidget.currentRow()
        self.item_video_list_converting[x].frame.setStyleSheet("background-color: #99c5c5;")

    def item_clicked_vf(self):
        for i in range(0, len(self.item_video_list_finish)):
            if i % 2 == 0:
                self.item_video_list_finish[i].frame.setStyleSheet("#frame{"
                                                                   "border:none;"
                                                                   "background-color: rgb(234, 234, 234);"
                                                                   "}"
                                                                   "#frame:hover{"
                                                                   "background-color:rgb(176, 227, 227);"
                                                                   "}")
            else:
                self.item_video_list_finish[i].frame.setStyleSheet("#frame{"
                                                                   "border:none;"
                                                                   "background-color:rgb(250, 250, 250);"
                                                                   "}"
                                                                   "#frame:hover{"
                                                                   "background-color:rgb(176, 227, 227);"
                                                                   "}")

        x = self.finished_video_list.currentRow()
        self.item_video_list_finish[x].frame.setStyleSheet("background-color: #99c5c5;")

    def item_clicked_ac(self):
        for i in range(0, len(self.item_audio_list_converting)):
            if i % 2 == 0:
                self.item_audio_list_converting[i].frame.setStyleSheet("#frame{"
                                                                       "border:none;"
                                                                       "background-color: rgb(234, 234, 234);"
                                                                       "}"
                                                                       "#frame:hover{"
                                                                       "background-color:rgb(176, 227, 227);"
                                                                       "}")
            else:
                self.item_audio_list_converting[i].frame.setStyleSheet("#frame{"
                                                                       "border:none;"
                                                                       "background-color:rgb(250, 250, 250);"
                                                                       "}"
                                                                       "#frame:hover{"
                                                                       "background-color:rgb(176, 227, 227);"
                                                                       "}")

        x = self.audio_converter_listwidget.currentRow()
        self.item_audio_list_converting[x].frame.setStyleSheet("background-color: #99c5c5;")

    def item_clicked_af(self):
        for i in range(0, len(self.item_audio_list_finish)):
            if i % 2 == 0:
                self.item_audio_list_finish[i].frame.setStyleSheet("#frame{"
                                                                   "border:none;"
                                                                   "background-color: rgb(234, 234, 234);"
                                                                   "}"
                                                                   "#frame:hover{"
                                                                   "background-color:rgb(176, 227, 227);"
                                                                   "}")
            else:
                self.item_audio_list_finish[i].frame.setStyleSheet("#frame{"
                                                                   "border:none;"
                                                                   "background-color:rgb(250, 250, 250);"
                                                                   "}"
                                                                   "#frame:hover{"
                                                                   "background-color:rgb(176, 227, 227);"
                                                                   "}")

        x = self.finished_audio_list.currentRow()
        self.item_audio_list_finish[x].frame.setStyleSheet("background-color: #99c5c5;")
