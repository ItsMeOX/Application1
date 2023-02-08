import sys
from PIL import Image, ImageDraw, ImageFilter
from PySide6.QtWidgets import (
QGridLayout, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, 
QWidget, QApplication, QFormLayout, QScrollArea, QFrame, 
QGraphicsDropShadowEffect, QSlider, QStyle)
from PySide6.QtCore import Qt, QPoint, QThreadPool, QRunnable, QObject, QUrl, Signal
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtGui import QPixmap, QColor
import subprocess
from random import randint
from time import ctime, time


import os
from pathlib import Path

LEFTBARWIDTH = 100


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint) # | Qt.WindowStaysOnTopHint

        self.pool = QThreadPool.globalInstance()

        self.windowDrag = False

        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0,0,0,0)
        
        self.initUI()

        # <Clear Music Directory File>
        self.clearMusicDirectory()

        # <Media Player>
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        self.audio_output.setVolume(self.slider.value()/100)
        self.playing = False
        self.currentSongIndex = 1
        self.playingSongIndex = 0
        self.currentPos = 0
        self.setPath = True
        self.then = time()

        with open("music\\history.txt","r", encoding='utf-8') as file:
            self.datalen = len(file.readlines())
            print(f"data length: {self.datalen}")
        if self.datalen > 0:
            self.historyDec = 2
        else:
            self.historyDec = 1

        
        # init for the first time
        self.repeatCountCurrent = 1
        self.playProcessInit = PlayProcess()
        self.pool.start(self.playProcessInit)
        self.playProcessInit.signals.completed.connect(self.addMusic)
        
        # add 9 more songs 
        self.playProcessInit.signals.completed.connect(self.playProcessFuncInit)
        self.repeatCountCurrent = 1
        # </Media Player>

    def playProcessFuncInit(self, count=3,*arg):
        if self.repeatCountCurrent < count:
            self.playProcess = PlayProcess()
            self.pool.start(self.playProcess)
            self.playProcess.signals.completed.connect(self.addMusic)
            self.playProcess.signals.completed.connect(self.repeatCountInc)
            self.playProcess.signals.completed.connect(self.playProcessFuncInit)
            
    def playProcessFunc(self, *arg):
        self.playProcess2 = PlayProcess()
        self.pool.start(self.playProcess2)
        self.playProcess2.signals.completed.connect(self.addMusic)
        

    def repeatCountInc(self, *arg):
        if self.addEnabled:
            self.repeatCountCurrent += 1

    def mousePressEvent(self, ev):
        self.windowDrag = False
        self.oldPos = ev.globalPosition().toPoint()
        if self.oldPos.y() - self.y() < 100:
            self.windowDrag = True

    def mouseMoveEvent(self, ev):
        if self.windowDrag:
            PosDifference = QPoint(ev.globalPosition().toPoint() - self.oldPos)
            self.move(self.x() + PosDifference.x(), self.y() + PosDifference.y())
            self.oldPos = ev.globalPosition().toPoint()    
        

    def initUI(self):
        self.menu()

        # left
        LEFT = 200
        self.left = QVBoxLayout()
        self.layout.addLayout(self.left, 1, 1)
        self.left.setContentsMargins(LEFT,100,0,0)
        
        self.maskedCoverImage = self.mask(Image.open("images\\application\\cover.png"))
        self.maskedCoverImage.save('images\\application\\cover2.png')
        self.coverImage = QPixmap('images\\application\\cover.png').scaled(500,500, mode = Qt.SmoothTransformation)
        self.musicCover = QLabel()
        self.musicCover.setPixmap(self.coverImage)
        self.left.addWidget(self.musicCover)

        self.songNameLayout = QHBoxLayout()
        self.songName = QLabel("NAME")
        self.songNameLayout.setContentsMargins(LEFT,50,0,0)
        self.songNameLayout.addWidget(self.songName, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addLayout(self.songNameLayout, 2, 1)

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

        self.layout.addLayout(self.songProgressLayout, 3, 1)

        self.leftbottom = QHBoxLayout()
        self.leftbottom.setContentsMargins(LEFT,40,0,0)
        self.leftbottom.addStretch()
        self.layout.addLayout(self.leftbottom, 4, 1)

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
        self.layout.addLayout(self.sliderLayout, 5, 1)

        self.slider.valueChanged.connect(self.volume)
        

        # right
        windowButtonsLayout = QHBoxLayout()
        windowButtonsLayout.setContentsMargins(300,10,10,0)
        self.layout.addLayout(windowButtonsLayout, 0, 2)
        closeButton = QLabel()
        closeButton.setPixmap(self.menuIcon)
        closeButton.mouseReleaseEvent = self.windowClose
        windowButtonsLayout.addWidget(closeButton, alignment=Qt.AlignmentFlag.AlignRight)
        


        self.SONGLISTLEFT = 300
        self.songListLayout = QVBoxLayout()
        self.songListLayout.setContentsMargins(self.SONGLISTLEFT,130,0,0)
        self.layout.addLayout(self.songListLayout, 1, 2, 7, 1)
    
    

        self.musicDirectory = "C:\\Users\\ongxu\\Downloads\\test\\music"
        self.musicList = list()
        
        self.QForm  = QFormLayout()
        self.groupBox  = QFrame()
        
        self.lastRow = 20 + 1

        for i in range(self.lastRow): 
            blank = QLabel("{:02d}".format(i))
            blank.setProperty("class", "ScrollAreaText")


            self.QForm.addRow(blank)
        


        self.groupBox.setLayout(self.QForm)

        self.scroll = QScrollArea()

        SCROLLWIDTH = 450
        self.scroll.setWidget(self.groupBox)
        self.scroll.setWidgetResizable(True)      
        self.scroll.setFixedWidth(SCROLLWIDTH)
        self.scroll.setFixedHeight(1000)
        self.scrollBar = self.scroll.verticalScrollBar()
    
        self.songListLayout.addWidget(self.scroll)

        title = QLabel("TITLE",self)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setProperty("class", "Title")
        title.setFixedWidth(440)
        title.setFixedHeight(150)
        
        # LEFT(300) + LEFTBARWIDTH(100) + COVERWIDTH(500) + LEFTLISTLEFT(300) + SCROLLWIDTH(450)
        title.move(LEFT+LEFTBARWIDTH+300+500+21,100)


    # menu icon
    def menu(self):
        self.leftbar = QVBoxLayout()
        self.leftbar2 = QFrame()
        self.leftbar2.setFixedWidth(LEFTBARWIDTH)
        self.leftbar2.setStyleSheet("background-color: #181818")
        self.leftbar.addWidget(self.leftbar2)

        self.menuIcon = QPixmap("images\\application\\menu.png").scaled(40,30, mode = Qt.SmoothTransformation)
        self.menu = QLabel(self.leftbar2)
        self.menu.setGeometry(30,1100,40,30)
        self.menu.setPixmap(self.menuIcon)
        self.layout.addLayout(self.leftbar, 0, 0, 8, 1)
        self.menu.mouseReleaseEvent = self.menuClick

    def menuClick(self, *arg):
        pass


    # music cover mask
    def mask(self,img):
        size = min(img.size)
        imgResized = img.resize((450,450))
        mask = Image.new("L", (450,450), 0)
        draw = ImageDraw.Draw(mask) 
        draw.ellipse((0,0,450,450),fill = 255)
        mask = mask.filter(ImageFilter.GaussianBlur(1))

        result = imgResized.copy()
        result.putalpha(mask)
        
        return result

    def previous(self, *arg):
        try:
            if self.playingSongIndex - 1 >= 0:
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
        self.songHighlight()
        print(f"CURRENT INDEX: {self.playingSongIndex}")
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

        if not self.playing:
            self.setPath = False
            self.player.play()
        else:
            self.player.pause()
        
        self.playing = not self.playing
    
    def positionChangedProcess(self, *arg):
        progressBarProcess = ProgressBarProcess()
        self.pool.start(progressBarProcess)

    def statusChanged(self, status):
        if status == QMediaPlayer.EndOfMedia and time() - self.then > 3:
            self.songDeHighlight()
            self.addRow()
            self.then = time()
            self.scrollBar.setValue(self.scrollBar.value() + self.QForm.itemAt(self.playingSongIndex).widget().height())
            self.currentPos = 0
            self.setPath = True
            self.playing = False
            self.playingSongIndex += 1
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
        setPlaying = self.QForm.itemAt(self.playingSongIndex+1).widget()
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
        setPlaying = self.QForm.itemAt(self.playingSongIndex+1).widget()
        setPlaying.setStyleSheet("""
                font-size: 20px;
                background-color: #181818;
                border-style: none none solid none;
                border-color: white;
                border-width: 1px;
                margin: 0px 0px 0px 0px;
                padding: 15px;
            """)

    def loadMusic(self, *arg):
        self.playProcessFunc()
        
        

    def addMusic(self):    
        self.addEnabled = False
        for file in sorted(Path(self.musicDirectory).iterdir(), key=os.path.getctime):
            filename = os.fsdecode(file)
            if filename.endswith(".wav"):
                idx = filename[::-1].find("\\")
                name = filename[-idx:-4]
                if name not in self.musicList and "伴奏" not in name and "和音" not in name and "Outro" not in name and "Intro" not in name:
                    setName = self.QForm.itemAt(self.currentSongIndex).widget()
                    setName.setText("{0:2d}.  {1}".format(self.currentSongIndex , name))
                    
                    self.addEnabled = True
                    if name not in self.musicList:
                        self.musicList.append(name)
                        with open("music\\history.txt","r", encoding='utf-8') as file:
                            data = file.readlines()
                            data[self.datalen + self.currentSongIndex - self.historyDec] = name + " --- " + str(ctime()) + " " + data[self.datalen + self.currentSongIndex - self.historyDec][:-2] + "\n"         
                            with open("music\\history.txt","w", encoding='utf-8') as file:
                                file.writelines(data)
                    self.currentSongIndex += 1
                
        print(self.musicList)

    def addRow(self, *arg):
        blank = QLabel("{:02d}".format(int(self.QForm.itemAt(self.lastRow-1).widget().text()) + 1))
        self.lastRow += 1
        blank.setProperty("class", "ScrollAreaText")
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
        app.quit()

    def clearMusicDirectory(self):
        for file in Path(self.musicDirectory).iterdir():
            try:
                if not file.is_dir() and not file.name == "history.txt":
                    os.remove(file)
            except:
                continue

class PlayProcess(QRunnable):
    def __init__(self):
        super().__init__()
        self.signals = Signals()

    def run(self):
        self.downloadVideo("https://music.youtube.com/playlist?list=OLAK5uy_nnB_5jjZqPTjrg1I95nII6bTa4tApbPjY")
        
    def downloadVideo(self, url):
        filename = 'C:\\Users\\ongxu\\Downloads\\test\\music\\%(title)s.%(ext)s'
        while True:
            try:  
                global process
                ydl_cmd = ['yt-dlp', '--playlist-items', str(randint(1,146)), '--extract-audio', '--audio-format', 'wav', '--audio-quality', '256', '-o', filename, "--download-archive", "C:\\Users\\ongxu\\Downloads\\test\\music\\history.txt" , url]
                process = subprocess.Popen(ydl_cmd)
                process.wait()
                self.signals.completed.emit()
            except:
                print("error, retrying...")
                continue
            else:
                break     

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

    


app = QApplication(sys.argv)
window = Window()
window.show()

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
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);
    width: 10px;
}
QSlider::handle:hover#Volume{
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4ff, stop:1 #8f8fff);
}


""")
sys.exit(app.exec())