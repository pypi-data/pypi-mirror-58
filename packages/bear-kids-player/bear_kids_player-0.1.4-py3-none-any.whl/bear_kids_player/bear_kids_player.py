# -*- coding: utf-8 -*-

from PyQt5.QtCore import QDir, Qt, QUrl,QTimer
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel,
        QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget)
from PyQt5.QtWidgets import QMainWindow,QWidget, QPushButton, QAction
from PyQt5.QtGui import QIcon
import sys,time
import threading
from question_database_operation import generate_question,count_correct_fre,reset_statistics_column

from config_processing import get_config

class VideoWindow(QMainWindow):

    def __init__(self,config_load=get_config(),parent=None):
        super(VideoWindow, self).__init__(parent)
        self.setWindowTitle("bear_kids_player")

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        videoWidget = QVideoWidget()

        self.playButton = QPushButton()
        self.playButton.setEnabled(False)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)

        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)

        self.errorLabel = QLabel()
        self.errorLabel.setSizePolicy(QSizePolicy.Preferred,
                QSizePolicy.Maximum)

        # Create new action
        openAction = QAction(QIcon('open.png'), '&Open', self)
        openAction.setShortcut(config_load['open_shotcut'])
        openAction.setStatusTip('Open movie')
        openAction.triggered.connect(self.openFile)

        # Create exit action
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut(config_load['exit_shotcut'])
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.exitCall)

        # Create menu bar and add action
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        #encoding="GBK"fileMenu.addAction(newAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(exitAction)

        # Create a widget for window contents
        wid = QWidget(self)
        self.setCentralWidget(wid)

        # Create layouts to place inside widget
        controlLayout = QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)
        controlLayout.addWidget(self.playButton)
        controlLayout.addWidget(self.positionSlider)

        layout = QVBoxLayout()
        layout.addWidget(videoWidget)
        layout.addLayout(controlLayout)
        layout.addWidget(self.errorLabel)

        # Set widget to contain window contents
        wid.setLayout(layout)

        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        self.mediaPlayer.error.connect(self.handleError)

        # Set
        # print(config_load['reset_statistics_column'])
        self.pop_window_open_status = False
        if config_load['reset_statistics_column']:
            print('reset')
            reset_statistics_column()

    def openFile(self):

        fileName, _ = QFileDialog.getOpenFileName(self, "Open Movie",
                QDir.homePath())

        if fileName != '':
            self.mediaPlayer.setMedia(
                    QMediaContent(QUrl.fromLocalFile(fileName)))
            self.playButton.setEnabled(True)

            self.mediaPlayer.play()
            # self.timer1 = QTimer(self)
            # self.timer1.timeout.connect(self.delay)
            self.timer = QTimer(self)
            # self.timer.setSingleShot(True)
            self.timer.timeout.connect(self.popup_question)
            self.timer.start()
            # self.popup_question()

    def popup_question(self):
        # if self.pop_window_open_status:
        #     # self.timer1.start(150000)
        #     self.pop_window_open_status=False
        #     # print(self.pop_window_open_status)
        # else:
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        self.timer.stop()
        start_time = time.time()
        self.child = childWindow()
        self.child.show()
        self.pop_window_open_status = self.child.exec_()
        end_time = time.time()
        self.mediaPlayer.play()
        self.answer_time = end_time-start_time

        if self.answer_time>config_load['error_time_threhold']:
            count_correct_fre(index = self.child.q['index'], correct = False)
        else:
            count_correct_fre(index = self.child.q['index'], correct = True)

        self.timer.start(config_load['Intervals']*1000)
            # self.child.exec_()


    def exitCall(self):
        sys.exit(app.exec_())

    def play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def mediaStateChanged(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPlay))

    def positionChanged(self, position):
        self.positionSlider.setValue(position)

    def durationChanged(self, duration):
        self.positionSlider.setRange(0, duration)

    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)

    def handleError(self):
        self.playButton.setEnabled(False)
        self.errorLabel.setText("Error: " + self.mediaPlayer.errorString())

# Dialog window
from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtWidgets import QApplication,QMainWindow,QDialog
dialog1 = 'Question_dialog.ui'
Ui_DialogWindow, QtBaseClass = uic.loadUiType(dialog1)
class childWindow(QDialog,Ui_DialogWindow):
    def __init__(self):
        QDialog.__init__(self)
        Ui_DialogWindow.__init__(self)
        # Ui_DialogWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setupUi(self)
        self.lineEdit.textChanged.connect(self.lineEdit_textchanged_callback)
        self.q = generate_question(type_filter = config_load['type_filter'],
        correct_fre_filter_threhold=config_load['correct_fre_filter_threhold'],
        error_fre_filter_threhold=config_load['error_fre_filter_threhold'],
        correct_rate_filter_threhold=config_load['correct_rate_filter_threhold'])
        self.label.setText(self.q['question'])

    def lineEdit_textchanged_callback(self):
        if str(self.lineEdit.text()) == self.q['answer']:
            # Disable the ESC button which used for exiting the dialog window
            self.authenticated = True
            self.accept()
    # Disable the ESC button which used for exiting the dialog window
    def keyPressEvent(self, event):
        if not event.key() == Qt.Key_Escape:
            super(QDialog, self).keyPressEvent(event)
    # Disable the ESC button which used for exiting the dialog window
    def closeEvent(self, event):
        if not self.authenticated:
            event.ignore()

if __name__ == '__main__':
    # config_load = get_config()
    app = QApplication(sys.argv)
    player = VideoWindow()
    player.resize(680, 550)
    # showMaximized()
    # show()
    player.setStyleSheet("background-color:black;");
    player.showFullScreen()
    sys.exit(app.exec_())
