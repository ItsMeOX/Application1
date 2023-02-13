import sys
from PIL import Image, ImageDraw
from PySide6.QtWidgets import (
QGridLayout, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, 
QWidget, QApplication, QFormLayout, QScrollArea, QFrame, 
QGraphicsDropShadowEffect, QSlider, QGraphicsScene, QGraphicsView,
QStackedWidget, QGraphicsPixmapItem,
)
from PySide6.QtCore import (Qt, QPoint, QThreadPool, QRunnable, QObject, QUrl, 
Signal, QPropertyAnimation, QRect, QTimer)
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtGui import QPixmap, QColor, QPainter, QTransform, QFont, QFontDatabase, QTextDocument, QTextOption
import subprocess
from random import randint
from time import ctime, time
from bs4 import BeautifulSoup
import requests

from PIL import Image
import os
from pathlib import Path

LEFTBARWIDTH = 100


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint) # | Qt.WindowStaysOnTopHint

        self.pool = QThreadPool.globalInstance()

        self.windowDrag = False

        self.fontID = QFontDatabase.addApplicationFont('music\\fonts\\chinese.msyh.ttf')
        self.fontFamilies = QFontDatabase.applicationFontFamilies(self.fontID)

        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0,0,0,0)

        self.stackedWidget = QStackedWidget()
        #self.stackedWidget.setStyleSheet("border: 1px solid yellow;")
        self.homeWidgetFunc()
        self.stackedWidget.addWidget(self.homeWidget)
        self.stackedWidget.setCurrentWidget(self.homeWidget)

        self.layout.addWidget(self.stackedWidget , 1, 1, 7, 1)

        self.initUI()

        # <Clear Music Directory File>
        self.clearMusicDirectory()

        # <Media Player>
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        self.audio_output.setVolume(self.slider.value()/100)
        self.playing = False
        self.currentSongIndex = 0
        self.playingSongIndex = 0
        self.currentPos = 0
        self.setPath = True
        self.then = time()
        self.watched = []
        self.name = ""
        self.addEnabled = False
        self.count = 10
        self.repeatedLyric = False
        self.initialising = True
        self.timerForcePause = True
        
        # init for the first time
        self.repeatCountCurrent = 1
        self.playProcessFunc()

    def homeWidgetFunc(self):
        self.homeWidget = QWidget()
        self.homeLayout = QGridLayout()
        self.homeLayout.setContentsMargins(0,0,0,0)
        self.setHomeLayout()
        
    def setHomeLayout(self, *arg):
        self.homeWidget.setLayout(self.homeLayout)

    def playProcessFunc(self, *arg):
        if self.repeatCountCurrent < self.count:
            self.playProcess = PlayProcess()
            self.pool.start(self.playProcess)
            self.playProcess.signals.completed.connect(self.addMusic)
        else:
            self.initialising = False
            self.repeatCountCurrent = 1

    
    def createLyric(self, *arg):
        print(f"GETTING LYRICS...{self.name}")
        self.lyrics = Lyrics(self.name)
        window.pool.start(self.lyrics)
        self.lyrics.signals.completed.connect(self.repeatCountInc)
        self.lyrics.signals.completed.connect(self.playProcessFunc)  

    def repeatCountInc(self, *arg):
        if self.addEnabled:
            self.repeatCountCurrent += 1

    def mousePressEvent(self, ev):
        self.windowDrag = False
        self.oldPos = ev.globalPosition().toPoint()
        if self.oldPos.y() - self.y() < 75:
            self.windowDrag = True

    def mouseMoveEvent(self, ev):
        if self.windowDrag:
            PosDifference = QPoint(ev.globalPosition().toPoint() - self.oldPos)
            self.move(self.x() + PosDifference.x(), self.y() + PosDifference.y())
            self.oldPos = ev.globalPosition().toPoint()    

    def initUI(self):
        self.menu()
        LEFT_LAYOUT_INDEX = 0
        RIGHT_LAYOUT_INDEX = 1
        # left
        LEFT = 0
        self.left = QVBoxLayout()
        self.homeLayout.addLayout(self.left, 1, LEFT_LAYOUT_INDEX)
        self.left.setContentsMargins(LEFT,100,0,0)
        
        self.angle = 0
        self.coverImage = QPixmap("C:\\Users\\ongxu\\Downloads\\test\\music\\cover_image\\test1.png")
        self.musicCover = QLabel()
        

        self.scene = QGraphicsScene()
        self.view  = QGraphicsView(self.scene)
        self.view.setRenderHint(QPainter.Antialiasing)



        self.coverImage = self.coverImage.scaled(500, 500, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        self.disc = QGraphicsPixmapItem(self.coverImage)
        self.disc.setTransformationMode(Qt.SmoothTransformation)
        self.scene.addItem(self.disc)
        
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setFixedSize(500,500)
        self.view.setStyleSheet('border: none;')
        self.left.addWidget(self.view)





        self.songNameLayout = QHBoxLayout()
        self.songName = QLabel("NAME")
        self.songNameLayout.setContentsMargins(LEFT,50,0,0)
        self.songNameLayout.addWidget(self.songName, alignment=Qt.AlignmentFlag.AlignCenter)
        self.homeLayout.addLayout(self.songNameLayout, 2, LEFT_LAYOUT_INDEX)

        self.songProgressLayout = QVBoxLayout()
        self.songProgressLayout.setContentsMargins(LEFT,0,0,0)
        self.songProgressTime = QLabel("--:-- / --:--")
        self.songProgressTime.setProperty("class", "VolumeText")
        

        self.songProgress = QSlider(Qt.Horizontal)
        self.songProgress.setEnabled(False)
        self.songProgress.setRange(0,100)
        self.songProgress.setSingleStep(1)
        self.songProgressLayout.addWidget(self.songProgress)
        self.songProgressLayout.addWidget(self.songProgressTime, alignment = Qt.AlignmentFlag.AlignCenter)

        

        self.homeLayout.addLayout(self.songProgressLayout, 3, LEFT_LAYOUT_INDEX)

        self.leftbottom = QHBoxLayout()
        self.leftbottom.setContentsMargins(LEFT,40,0,0)
        self.leftbottom.addStretch()
        self.homeLayout.addLayout(self.leftbottom, 4, LEFT_LAYOUT_INDEX)

        self.playPreviousIcon = QPixmap("images\\application\\cover.png").scaled(40,40)
        self.playPrevious     = QLabel()
        self.playPrevious.setPixmap(self.playPreviousIcon)
        self.leftbottom.addWidget(self.playPrevious)
        self.leftbottom.addSpacing(2)
        
        self.fastBackwardIcon = QPixmap("images\\application\\cover.png").scaled(40,40)
        self.fastBackward     = QLabel()
        self.fastBackward.setPixmap(self.fastBackwardIcon)
        self.leftbottom.addWidget(self.fastBackward)
        self.leftbottom.addSpacing(2)

        self.playIcon = QPixmap("images\\application\\play2.png").scaled(40,40, mode = Qt.SmoothTransformation)
        self.play     = QLabel()
        self.play.setPixmap(self.playIcon)
        self.leftbottom.addWidget(self.play)
        self.leftbottom.addSpacing(2)

        self.fastForwardIcon = QPixmap("images\\application\\cover.png").scaled(40,40)
        self.fastForward     = QLabel()
        self.fastForward.setPixmap(self.fastForwardIcon)
        self.leftbottom.addWidget(self.fastForward)
        self.leftbottom.addSpacing(2)

        self.rotIcon = QPixmap("images\\application\\playprevious.png").scaled(40,40)
        self.rotate     = QLabel()
        self.rotate.setPixmap(self.rotIcon)
        self.rotation = 0
        self.leftbottom.addWidget(self.rotate)
        self.leftbottom.addSpacing(2)

        self.playNextIcon = QPixmap("images\\application\\cover.png").scaled(40,40)
        self.playNext     = QLabel()
        self.playNext.setPixmap(self.playNextIcon)
        self.leftbottom.addWidget(self.playNext)
        self.leftbottom.addStretch()
        
        self.playPrevious.mousePressEvent = self.previous
        self.fastForward.mousePressEvent  = self.forward
        self.fastBackward.mouseMoveEvent  = self.backward
        self.play.mousePressEvent         = self.playMusic
        self.playNext.mousePressEvent     = self.next
        self.rotate.mousePressEvent       = self.rot

        self.sliderLayout = QHBoxLayout()
        self.sliderLayout.setContentsMargins(LEFT,0,0,30)
        self.slider = QSlider(Qt.Horizontal, objectName = "Volume")
        self.slider.setRange(0,100)
        self.slider.setValue(30)
        self.slider.setSingleStep(1)
        
        self.volumeValue = QLabel(f"{self.slider.value()}")
        self.volumeValue.setProperty("class", "VolumeText")

        self.sliderLayout.setSpacing(10)
        self.sliderLayout.addWidget(self.volumeValue)
        self.sliderLayout.addWidget(self.slider)
        self.homeLayout.addLayout(self.sliderLayout, 5, LEFT_LAYOUT_INDEX)

        self.slider.valueChanged.connect(self.volume)
        

        # right
        self.SONGLISTLEFT = 200
        windowButtonsLayout = QHBoxLayout()
        windowButtonsLayout.setSpacing(1)
        windowButtonsLayout.setAlignment(Qt.AlignmentFlag.AlignRight)
        windowButtonsLayout.setContentsMargins(0,10,0,0)

        topFrame = QFrame()
        topFrame.setLayout(windowButtonsLayout)
        #topFrame.setStyleSheet('border: 1px solid white;')
        self.layout.addWidget(topFrame, 0, 1)

        closeButton = QLabel()
        closeButton.setFixedSize(50,50)
        closeButton.setPixmap(self.menuIcon)
        closeButton.mouseReleaseEvent = self.windowClose
        minimizeButton = QLabel()
        minimizeButton.setPixmap(self.menuIcon)
        minimizeButton.setFixedSize(50,50)
        minimizeButton.mouseReleaseEvent = self.minimize
        windowButtonsLayout.addWidget(minimizeButton)
        windowButtonsLayout.addWidget(closeButton)
        

        self.rightFrame = QFrame()

        #self.rightFrame.setStyleSheet('border: 1px solid "white"')
        self.homeLayout.addWidget(self.rightFrame, 0, RIGHT_LAYOUT_INDEX, 7, 1)
        
        self.rightLayout = QVBoxLayout()
        self.rightLayout.setSpacing(2)
        self.rightFrame.setLayout(self.rightLayout)
        self.rightLayout.setContentsMargins(self.SONGLISTLEFT,0,0,0)


        self.rightFrameColor = "black"

        self.titleLayout = QHBoxLayout()
        self.titleLayout.setContentsMargins(50,50,0,0)
        self.titleLayout.setSpacing(0)
        self.title = QPushButton("PL",self, clicked = self.playlistShow)
        self.effectTitle = QGraphicsDropShadowEffect()
        self.effectTitle.setBlurRadius(30)
        self.effectTitle.setOffset(0,0)
        self.effectTitle.setColor(QColor(self.rightFrameColor))
        
        self.title.setGraphicsEffect(self.effectTitle)
        self.title.setProperty("class", "Title")
        self.title.setFixedWidth(300)
        self.title.setFixedHeight(75)
        self.titleLayout.addWidget(self.title)
        
        lyrics = QPushButton("L", self, clicked = self.lyricShow)
        self.effectLyrics = QGraphicsDropShadowEffect()
        self.effectLyrics.setBlurRadius(30)
        self.effectLyrics.setOffset(0,0)
        self.effectLyrics.setColor(QColor(self.rightFrameColor))
        lyrics.setGraphicsEffect(self.effectLyrics)
        lyrics.setFixedWidth(300)
        lyrics.setFixedHeight(75)
        lyrics.setProperty("class", "Title")
        lyrics.setStyleSheet("border-style: solid solid solid none;")
        self.titleLayout.addWidget(lyrics)

        self.musicDirectory = "C:\\Users\\ongxu\\Downloads\\test\\music"
        self.musicList = list()
        
        self.QForm  = QFormLayout()
        self.QForm.setSpacing(5)
        self.QForm.setContentsMargins(0,0,0,0)
        self.groupBox  = QFrame()
        self.groupBox.setStyleSheet('background: #181818;')


        #self.groupBox.setStyleSheet('border: 1px solid "white" ')
        
        self.lastRow = 20

        for i in range(0, self.lastRow):
            self.songLabel = QLabel("{:02d}".format(i+1), alignment = Qt.AlignmentFlag.AlignLeft)
            self.songLabel.setFont(QFont(self.fontFamilies[0]))
            self.songLabel.setProperty("class", "ScrollAreaText")
            self.text = self.songLabel.text()
            self.songLabel.mouseReleaseEvent = lambda _ , text=self.text: self.songTapped(int(text))
            self.QForm.addRow(self.songLabel)

        self.groupBox.setLayout(self.QForm)

        self.scrollArea = QScrollArea()
        self.scrollArea.setWidget(self.groupBox)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)      
        self.scrollBar = self.scrollArea.verticalScrollBar()
        self.effectScrollArea = QGraphicsDropShadowEffect()
        self.effectScrollArea.setBlurRadius(30)
        self.effectScrollArea.setOffset(0,0)
        self.effectScrollArea.setColor(QColor(self.rightFrameColor))
        self.scrollArea.setGraphicsEffect(self.effectScrollArea)
        
        self.scrollAreaLayout = QVBoxLayout()
        self.scrollAreaLayout.setContentsMargins(50,0,0,0)
        self.scrollAreaLayout.addWidget(self.scrollArea)

        self.rightLayout.addLayout(self.titleLayout)
        

        self.titleStacked = QStackedWidget()
        self.rightLayout.addWidget(self.titleStacked)

        self.songListWidget = QWidget() 
        self.songListWidget.setLayout(self.scrollAreaLayout)
        self.titleStacked.addWidget(self.songListWidget)
        self.titleStacked.setCurrentWidget(self.songListWidget)


        self.lyricsWidget = QWidget()
        self.titleStacked.addWidget(self.lyricsWidget)
        self.lyricsLayout = QVBoxLayout()
        self.lyricsWidget.setLayout(self.lyricsLayout)
        self.lyricsLayout.setContentsMargins(50,0,0,0)

        self.lyricsScrollArea = QScrollArea()
        self.lyricsScrollArea.setStyleSheet("background: #181818;")
        self.lyricsScrollArea.setFixedHeight(1000)
        self.effectLyrics2 = QGraphicsDropShadowEffect()
        self.effectLyrics2.setBlurRadius(30)
        self.effectLyrics2.setOffset(0,0)
        self.effectLyrics2.setColor(QColor("grey"))
        self.lyricsScrollArea.setGraphicsEffect(self.effectLyrics2)
        #self.lyricsScrollArea.setStyleSheet("border: 1px solid white;")
        self.lyricsLabel = QLabel("", alignment = Qt.AlignmentFlag.AlignTop)
        self.lyricsLabel.setFont(self.fontFamilies[0])
        self.lyricsLabel.setProperty("class", "LyricsText")

        self.lyricsScrollArea.setWidget(self.lyricsLabel)
        self.lyricsLayout.addWidget(self.lyricsScrollArea, alignment=Qt.AlignmentFlag.AlignTop)
      

    def rot(self, *arg):
        self.angle = 0
        self.rot2()
        self.timertimeout = 20
        self.timer = QTimer()
        self.timer.timeout.connect(self.rot2)
        self.timer.start(self.timertimeout)

    def rot2(self, *arg):
        self.angle += 1
        self.transform = QTransform()
        self.transform.translate(self.disc.boundingRect().center().x(), self.disc.boundingRect().center().y())
        self.transform.scale(5, 5)
        self.transform.rotate(self.angle)
        self.transform.scale(1/5, 1/5)
        self.transform.translate(-self.disc.boundingRect().center().x(), -self.disc.boundingRect().center().y())
        self.disc.setTransform(self.transform)

    def minimize(self, *arg):
        try:
            self.timer.stop()
            self.showMinimized()
            self.disc.setPos(self.disc.boundingRect().left() - 250 , self.disc.boundingRect().top() - 250)
        except:
            pass

    def minimize2(self, old, new):
        try:
            if not window.timerForcePause:
                if new is not None:
                    self.timer.start()
                    print("timer started")
                else:
                    self.timer.stop()
                    print("timer stopped")
                
        except:
            pass
        

    def songTapped(self, index):
        self.songDeHighlight()
        self.addRow()
        self.scrollBar.setValue(self.scrollBar.value() + self.QForm.itemAt(self.playingSongIndex).widget().height())
        self.currentPos = 0
        self.setPath = True
        self.playing = False
        self.playingSongIndex = index - 1
        if not self.initialising:
            self.count = 2
            self.playProcessFunc()
        self.playMusic()

    def playlistShow(self, *arg):

        self.titleStacked.setCurrentWidget(self.songListWidget)


    def lyricShow(self, *arg):
        self.titleStacked.setCurrentWidget(self.lyricsWidget)

    # menu
    def menu(self):
        self.leftbar = QVBoxLayout()
        self.leftbar.setContentsMargins(0,0,250,0)
        self.leftbar2 = QFrame()
        self.leftbar2.setFixedWidth(LEFTBARWIDTH)
        self.leftbar2.setStyleSheet("background-color: #181818")
        self.leftbar.addWidget(self.leftbar2)
        self.effectLeftBar = QGraphicsDropShadowEffect()
        self.effectLeftBar.setBlurRadius(30)
        self.effectLeftBar.setOffset(0,0)
        self.effectLeftBar.setColor(QColor("black"))
        self.leftbar2.setGraphicsEffect(self.effectLeftBar)

        self.menuIcon = QPixmap("images\\application\\menu.png").scaled(40,30, mode = Qt.SmoothTransformation)
        self.menuLabel = QLabel(self.leftbar2)
        self.menuLabel.setGeometry(30,1100,40,30)
        self.menuLabel.setPixmap(self.menuIcon)
        self.layout.addLayout(self.leftbar, 0, 0, 8, 1)
        self.menuLabel.mouseReleaseEvent = self.menuClick

        self.menuExpanded = QFrame(self)

        self.menuExpanded.setStyleSheet("""
            background-color: white;
        """)
        self.menuExpanded.setGeometry(0,0,0,1000)
        
        # menu -------------

        self.menuFrame = QFrame(self)
        self.menuFrame.setStyleSheet('border: 1px solid "white" ')
        self.menuFrame.setMidLineWidth(0)
        
        self.menuLayout = QVBoxLayout()
        self.menuLayout.setContentsMargins(0,0,0,0)
        self.menuLayout.setSpacing(0)
        self.menuFrame.setLayout(self.menuLayout)
        
        self.menuInitUi()
        
        self.menuFrame.hide()

        self.menuFrameWidth = 1192

    def menuClick(self, *arg):
        
        self.menuFrame.show()
        self.Animation = QPropertyAnimation(self.menuFrame, b'geometry')
        self.Animation.setDuration(250)
        self.Animation.setStartValue(QRect(0,0,0,self.menuFrameWidth))
        self.Animation.setEndValue(QRect(0,0,350,self.menuFrameWidth))
        self.Animation.start()

    def menuInitUi(self):
        self.menuButton = QPushButton("close", clicked = self.closeMenu)
        self.menuButton.setFixedHeight(100)
        self.menuLayout.addWidget(self.menuButton, alignment=Qt.AlignmentFlag.AlignTop)

        self.historyButton = QPushButton("history", clicked = self.historyFunc)

        self.menuStacked = QStackedWidget()
        self.menuLayout.addWidget(self.menuStacked)


    def closeMenu(self, *arg):
        self.Animation = QPropertyAnimation(self.menuFrame, b'geometry')
        self.Animation.setDuration(250)
        self.Animation.setStartValue(QRect(0,0,350,self.menuFrameWidth))
        self.Animation.setEndValue(QRect(0,0,0,self.menuFrameWidth))
        self.Animation.start()

    def historyFunc(self, *arg):
        pass

    def previous(self, *arg):
        try:
            if self.playingSongIndex >= 1:
                self.songDeHighlight()
                self.scrollBar.setValue(self.scrollBar.value() - self.QForm.itemAt(self.playingSongIndex).widget().height())
                self.playing = False
                self.playingSongIndex -= 1
                self.currentPos = 0
                self.setPath = True
                self.playMusic()
        except:
            print("NO PREVIOUS SONG")

    def next(self, *arg):
        try:
            self.statusChanged(status = QMediaPlayer.EndOfMedia)
        except:
            print("END OF SONG LIST")

    def forward(self, *arg):
        pos = self.player.position() + 10000
        if pos > self.player.duration():
            self.statusChanged(status = QMediaPlayer.EndOfMedia)
        self.player.setPosition(pos)

    def backward(self, *arg):
        pos = self.player.position() - 10000
        if pos < 0:
            pos = 0
        self.player.setPosition(pos)

    def playMusic(self, *arg): #make this button clickable after shuffle
        print(f"CURRENT INDEX: {self.playingSongIndex}")

        self.songHighlight()
        if self.setPath:
            try:
                print(f"CURRENT PLAYING SONG INDEX: {self.playingSongIndex}")
                path = "C:\\Users\\ongxu\\Downloads\\test\music\\" + list(self.musicList)[self.playingSongIndex]+ ".wav" 
                print(self.musicList, self.playingSongIndex, path)
                self.player.setSource(QUrl.fromLocalFile(path))
                self.songName.setText(list(self.musicList)[self.playingSongIndex])
                self.player.mediaStatusChanged.connect(self.statusChanged)
                self.player.positionChanged.connect(self.positionChangedProcess)
                self.songProgress.setRange(0,self.player.duration()/100)
            except IndexError:
                print("index error")

            self.lyricsLabel.setText("")
            for file in os.listdir("C:\\Users\\ongxu\\Downloads\\test\\music\\lyrics"):
                if list(self.musicList)[self.playingSongIndex] == file[:-4]:
                    print(f"filename: {file[:-4]}")
                    with open("C:\\Users\\ongxu\\Downloads\\test\\music\\lyrics\\" + file, "r", encoding='utf-8') as lyricsText:
                        lyrics = list(lyricsText)
                        if len(lyrics)  != 1:
                            for lyric in lyrics:
                                self.lyricsLabel.setText(self.lyricsLabel.text() + lyric)
                    break
            self.lyricsLabel.adjustSize()
            print(f"cover name: {list(self.musicList)[self.playingSongIndex]}")
            
            self.scene.removeItem(self.disc)
            self.coverImage = QPixmap(f'C:\\Users\\ongxu\\Downloads\\test\\music\\cover_image\\{list(self.musicList)[self.playingSongIndex]}.png')
            self.coverImage = self.coverImage.scaled(500, 500, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
            self.disc = QGraphicsPixmapItem(self.coverImage)
            self.disc.setTransformationMode(Qt.SmoothTransformation)
            self.scene.addItem(self.disc)
            
            self.rot()

        if not self.playing:
            self.setPath = False
            self.timerForcePause = False
            self.timer.start(self.timertimeout)
            self.player.play()
        else:
            self.timer.stop()
            self.timerForcePause = True
            self.player.pause()
        
        self.playing = not self.playing
    
    def positionChangedProcess(self, *arg):
        progressBarProcess = ProgressBarProcess()
        self.pool.start(progressBarProcess)

    def statusChanged(self, status):
        if status == QMediaPlayer.EndOfMedia and time() - self.then > 1:
            self.songDeHighlight()
            self.timer.stop()
            self.addRow()
            self.then = time()
            self.scrollBar.setValue(self.scrollBar.value() + self.QForm.itemAt(self.playingSongIndex).widget().height())
            self.currentPos = 0
            self.setPath = True
            self.playing = False
            self.playingSongIndex += 1
            if not self.initialising:
                self.count = 2
                self.playProcessFunc()
            self.playMusic()
            print("END OF MUSIC")
        if status == QMediaPlayer.LoadedMedia:
            self.songProgress.setEnabled(True)
            self.totalMinute = self.player.duration() / 60000
            self.totalSecond = int((self.totalMinute - int(self.totalMinute)) * 60)
            self.songProgressTime.setText("00:00/{0:02d}:{1:02d}".format(int(self.totalMinute),self.totalSecond))
            self.songProgress.setRange(0,int(self.totalMinute)*60 + self.totalSecond)
            self.songProgress.sliderMoved.connect(self.sliderMovedFunc)
            self.songProgress.sliderReleased.connect(self.sliderReleasedFunc)

    def sliderMovedFunc(self, *arg):
        self.player.setPosition(self.songProgress.value()*1000)
        minute = self.songProgress.value() // 60
        second = self.songProgress.value() - int(minute)*60 
        self.songProgressTime.setText("{0:02d}:{1:02d}/{2:02d}:{3:02d}".format(minute,second,int(self.totalMinute),self.totalSecond))
        self.player.pause()

    def sliderReleasedFunc(self, *arg):
        self.player.play()

    def songHighlight(self, *arg):
        setPlaying = self.QForm.itemAt(self.playingSongIndex).widget()
        setPlaying.setStyleSheet("""
            font-size : 30px;
            background-color: #181818;
            border-style: solid;
            border-color: white;
            border-width: 2px;
            margin: 0px 0px 0px 0px;
            padding: 15px;
        """)

    def songDeHighlight(self, *arg):
        setPlaying = self.QForm.itemAt(self.playingSongIndex).widget()
        setPlaying.setStyleSheet("""
                font-size: 20px;
                background-color: #181818;
                border-style: none none solid none;
                border-color: white;
                border-width: 1px;
                margin: 0px 0px 0px 0px;
                padding: 15px;
            """)  
        

    def addMusic(self):    
        self.addMUSIC = AddMusic()
        self.pool.start(self.addMUSIC)
        self.addMUSIC.signals.completed.connect(self.createLyric)
        self.addMUSIC.signals.failed.connect(self.repeatCountInc)
        self.addMUSIC.signals.failed.connect(self.playProcessFunc)

    def addRow(self, *arg):
        blank = QLabel("{:02d}".format(int(self.QForm.itemAt(self.lastRow-1).widget().text()) + 1))
        self.lastRow += 1
        blank.setProperty("class", "ScrollAreaText")
        self.text = blank.text()
        blank.mouseReleaseEvent = lambda _ , text=self.text: self.songTapped(int(text))
        self.QForm.addRow(blank)

    def volume(self):
        self.audio_output.setVolume(self.slider.value()/100)
        self.volumeValue.setText(str(self.slider.value()))

    def windowClose(self, *arg):
        try:
            process.kill()
            process.terminate()
        except:
            pass
        self.player.stop()
        self.clearMusicDirectory()

        with open("C:\\Users\\ongxu\\Downloads\\test\\music\\history.txt", "w") as file:
            file.truncate(0)

        app.quit()

    def clearMusicDirectory(self):
        for file in Path(self.musicDirectory).iterdir():
            try:
                if not file.is_dir() and not file.name == "history.txt":
                    os.remove(file)
            except:
                continue
        
# THREADS -------------------------------------------------------------------------------------------------

class PlayProcess(QRunnable):
    def __init__(self):
        super().__init__()
        self.signals = Signals()

    def run(self):
        self.downloadVideo("https://music.youtube.com/playlist?list=OLAK5uy_nnB_5jjZqPTjrg1I95nII6bTa4tApbPjY")
        
    def downloadVideo(self, url):
        global process
        filename = 'C:\\Users\\ongxu\\Downloads\\test\\music\\%(title)s.%(ext)s'
        while True:
            try:
                randomNum = randint(1,148)
                if randomNum not in window.watched:
                    window.watched.append(randomNum)  
                    print(window.watched, randomNum)
                    ydl_cmd = ['yt-dlp', '--playlist-items', str(randomNum), '--extract-audio', '--audio-format', 'wav', '--audio-quality', '256', '-o', filename, "--download-archive", "C:\\Users\\ongxu\\Downloads\\test\\music\\history.txt" , url]
                    process = subprocess.Popen(ydl_cmd)
                    process.wait()
                    self.signals.completed.emit()
                else:
                    continue
            except:
                print("downloading error...")
                break
            else:
                break     

class AddMusic(QRunnable):
    def __init__(self):
        super().__init__()
        self.signals = Signals()
        self.name = ""
        

    def run(self):
        self.addMusic()

    def addMusic(self):
        window.addEnabled = False
        file = sorted(Path(window.musicDirectory).iterdir(), key=os.path.getctime)[-1]
        print(f"filename: {file}")
        filename = os.fsdecode(file)
        idx = filename[::-1].find("\\")
        self.name = filename[-idx:-4].strip("\n")
        if self.name not in window.musicList and "伴奏" not in self.name and "和音" not in self.name and "Outro" not in self.name and "Intro" not in self.name:
            setName = window.QForm.itemAt(window.currentSongIndex).widget()
            setName.setText("{0:2d}.  {1}".format(window.currentSongIndex + 1 , self.name))
            print(f"ADDING SONG INDEX: {window.currentSongIndex + 1}")
            window.addEnabled = True
            window.name = self.name                    
            if self.name not in window.musicList:
                window.musicList.append(self.name)
                try:
                    with open("music\\history.txt","r", encoding='utf-8') as file:
                        data = file.readlines()
                        data[window.currentSongIndex] = self.name + " --- " + str(ctime()) + " " + data[window.currentSongIndex][:-1] + "\n"         
                        with open("music\\history.txt","w", encoding='utf-8') as file:
                            file.writelines(data)
                except: 
                    print("addmusic error")
            window.currentSongIndex += 1
            self.signals.completed.emit()
        else:
            with open("C:\\Users\\ongxu\\Downloads\\test\\music\\history.txt", "r", encoding='utf-8') as file:
                data = file.readlines()
                with open("C:\\Users\\ongxu\\Downloads\\test\\music\\history.txt", "w", encoding='utf-8') as file2:
                    file2.writelines(data[:-1])
            print("failed signal emmited")
            self.signals.failed.emit()

        print(window.musicList)

class ProgressBarProcess(QRunnable):
    def run(self):
        self.positionChangedFunc()
        
    def positionChangedFunc(self, *arg):
        minute = window.player.position()/60000
        second = window.player.position()/1000 - int(minute)*60
        window.songProgressTime.setText("{0:02d}:{1:02d}/{2:02d}:{3:02d}".format(int(minute),int(second),int(window.totalMinute),window.totalSecond))
        window.songProgress.setValue(int(minute)*60 + int(second))

class Signals(QObject):
    completed = Signal()
    failed = Signal()

class Lyrics(QRunnable):
    def __init__(self, name: str):
        super().__init__()
        self.signals = Signals()
        self.name = name
        self.repeatedLyric = False
        self.timeout = 0

    def run(self):
        self.lyricGet()

    def lyricGet(self, *arg):
        try:
            print("GETTING LYRICS...")
            url = "https://mojim.com/cnh116318.htm"

            page = requests.get(url)
            soup = BeautifulSoup(page.content, "html.parser")

            frame = soup.find("div", id="frame").find("div", id="Tb3").find("div", id="inS").find("dl", class_="ha0")
            contents = frame.find_all("dd")


            for content in contents:
                titles = content.find_all("span", {'class':['hc3','hc4']})
                for title in titles:
                    songNames = title.find_all("a", href = True)
                    for songName in songNames:
                        if ((self.name in songName.getText() or songName.getText() in self.name)  and "伴奏" not in self.name and self.timeout < 5):
                            print(self.name , songName.getText())
                            lyricPage = requests.get("https://mojim.com" + songName['href'])
                            lyricSoup = BeautifulSoup(lyricPage.content, "html.parser")
                            self.timeout += 1
                            break
            self.timeout = 1
                    


            lyricFrame = lyricSoup.find("div", id="frame").find("div", id="Tb3").find_all("table")[1].find("dd", id= "fsZx3")

            lyrics = []

            for lyric in lyricFrame:
                if "<" not in str(lyric) and ":" not in str(lyric) and "更多更详尽歌词" not in str(lyric):
                    lyrics.append(str(lyric))
            for file in os.listdir("C:\\Users\\ongxu\\Downloads\\test\\music\\lyrics\\"):
                if file[:-4] == self.name:
                    self.repeatedLyric = True
                    break
                
            if not self.repeatedLyric:
                with open(f"C:\\Users\\ongxu\\Downloads\\test\\music\\lyrics\\{self.name}.txt","w", encoding='utf-8') as file:
                    file.writelines("\n".join(lyrics[:-1]))

            self.repeatedLyric = False        


            self.addCover()

            

        except:
            with open(f"C:\\Users\\ongxu\\Downloads\\test\\music\\lyrics_failed\\{self.name}.txt","w", encoding='utf-8') as file:
                file.writelines(f"{self.name}")
            self.addCover()

            print(f"{self.name} has no lyric")

    def addCover(self):
        try:
            with open("C:\\Users\\ongxu\\Downloads\\test\\music\\history.txt", "r", encoding='utf-8') as file:
                for line in file.readlines():
                    if self.name in line:
                        for fileName in os.listdir("C:\\Users\\ongxu\\Downloads\\test\\music\\cover_image\\"):
                            if self.name == fileName[:-4]:
                                print(f"skipping {self.name} cover")
                                break

                        idx = line[::-1].index(" ")
                        videoID = line[-idx:].strip("\n")
                        
                        self.pageImg = requests.get("https://music.youtube.com/watch?v=" + videoID)
                        print(f"{self.name} : https://music.youtube.com/watch?v={videoID}")
                        self.soupImg = BeautifulSoup(self.pageImg.content, "html.parser")
                        self.coverImg = self.soupImg.find("meta", property="og:image")
                        pathImg = f'C:\\Users\\ongxu\\Downloads\\test\\music\\cover_image\\{self.name}.png'
                        with open(pathImg, 'wb') as imgDir:
                            imgDir.write(requests.get(self.coverImg['content']).content)
        
                        image = Image.open(pathImg)
                        imageW, imageH = image.size 
                        image.crop((280,0,imageW-280,imageH)).save(pathImg)
                        img = Image.open(pathImg)
                        big = (img.size[0]*10, img.size[1]*10)

                        mask = Image.new('L', big, 0)
                        draw = ImageDraw.Draw(mask)
                        draw.ellipse((0,0) + big, fill=255)
                        draw.ellipse([big[0]//2-500,big[0]//2-500,big[0]//2+500,big[0]//2+500], fill=0) 

                        mask = mask.resize(img.size, Image.Resampling.LANCZOS)

                        img.putalpha(mask)
                        img.save(pathImg)
                        
            try:
                self.signals.completed.emit()
            except:
                print("signal destroyed") 
        
        except:
            print("add Cover Failed")
        

app = QApplication(sys.argv)
window = Window()
window.show()

app.focusChanged.connect(window.minimize2)

window.move(100,100)
window.setStyleSheet("""
.ScrollAreaText{
    font-size: 20px;
    background-color: #181818;
    border-style: none none solid none;
    border-color: white;
    border-width: 1px;
    margin: 0px 0px 0px 0px;
    padding: 15px;
}

.ScrollAreaTextPlaying{
    font-size : 30px;
    background-color: #181818;
    border-style: solid;
    border-color: white;
    border-width: 5px;
    margin: 0px 0px 0px 0px;
    padding: 15px;
}

.Title{
    font-size: 50px;
    border-style: solid;
    border-width: 5px;
    border-color: "white";
    
}

.VolumeText{
    font-size: 20px;
    font-weight: bold;
}

.LyricsText{
    font-size: 25px;
}

QVBoxLayout{
    border-style: solid;
    border-color: white;
    background-color: #202020;
}

QScrollArea{
    border-style: none;
    background-color: grey;
}

QWidget{
    background-color: #121212;
    color: "WHITE";
}



QSlider::groove#Volume{
    margin: 5px 0px 0px 0px;
    border: 1px solid "white";
    border-radius: 5px; 
    height: 10px;
}

QSlider::handle#Volume{
    
    padding: 15px 15px 15px 15px;
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);    border-radius: 10px;
    width: 10px;
}
QSlider::handle:hover#Volume{
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4ff, stop:1 #8f8fff);
}

QStackedWidget{
    margin: 0px;
}

""")
sys.exit(app.exec())