import sys
from PIL import Image, ImageDraw, ImageFilter
from PySide6.QtWidgets import (
QGridLayout, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, 
QWidget, QApplication, QFormLayout, QScrollArea, QFrame, 
QGraphicsDropShadowEffect, QSlider)
from PySide6.QtCore import Qt
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtGui import QPixmap, QColor
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import subprocess, json

import youtube_dl
import os
from pathlib import Path





class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0,0,0,0)

        self.initUI()
        self.index = 1
        self.url = "https://music.youtube.com/watch?v=EmpnN63Rci4&list=RDAOtBZyLAS1sp-wGh12L8Hqbw"
        

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
    
        self.leftbottom = QHBoxLayout()
        self.leftbottom.setContentsMargins(LEFT,40,0,0)
        self.leftbottom.addStretch()
        self.layout.addLayout(self.leftbottom, 3, 1)

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
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0,100)
        self.slider.setValue(35)
        self.slider.setSingleStep(1)
        
        self.volumeValue = QLabel(f"{self.slider.value()}")
        self.volumeValue.setProperty("class", "VolumeText")

        self.sliderLayout.setSpacing(10)
        self.sliderLayout.addWidget(self.volumeValue)
        self.sliderLayout.addWidget(self.slider)
        self.layout.addLayout(self.sliderLayout, 4, 1)

        self.slider.valueChanged.connect(self.volume)
        

        # right
        songListLayout = QVBoxLayout()
        songListLayout.setContentsMargins(300,0,0,0)
        self.layout.addLayout(songListLayout, 0, 2, 5, 1)
        
        self.musicList = set()
        songList  = QFormLayout()
        groupBox  = QFrame()
        
        title = QLabel("TITLE",alignment = Qt.AlignmentFlag.AlignCenter)
        title.setProperty("class", "Title")
        
        songList.addRow(title)

        for i in self.musicList:
            song = QLabel(f"{i}")
            song.setProperty("class", "ScrollAreaText")
            songList.addRow(song)


        groupBox.setLayout(songList)

        scroll = QScrollArea()

        scroll.setWidget(groupBox)
        scroll.setWidgetResizable(True)      
        scroll.setFixedWidth(450)
        scroll.setFixedHeight(1000)


        songListLayout.addWidget(scroll)




    # menu icon
    def menu(self):
        self.leftbar = QVBoxLayout()
        self.leftbar2 = QFrame()
        self.leftbar2.setFixedWidth(100)
        self.leftbar2.setStyleSheet("background-color: #181818")
        self.leftbar.addWidget(self.leftbar2)

        self.menuIcon = QPixmap("images\\application\\menu.png").scaled(40,30, mode = Qt.SmoothTransformation)
        self.menu = QLabel(self.leftbar2)
        self.menu.setGeometry(30,950,40,30)
        self.menu.setPixmap(self.menuIcon)
        self.layout.addLayout(self.leftbar, 0, 0, 5, 1)
        self.menu.mouseReleaseEvent = self.menuClick

    def menuClick(*arg):
        print("A")

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

    def previous():
        pass

    def next():
        pass

    def forward():
        pass

    def backward():
        pass

    def playMusic(self, *arg):
        self.downloadVideo("https://music.youtube.com/playlist?list=OLAK5uy_m-IKq9a28m2ltjhzyAEgAH8Md1Re1XZu8")#https://music.youtube.com/watch?v=EmpnN63Rci4&list=RDAOtBZyLAS1sp-wGh12L8Hqbw
        musicDirectory = "C:\\Users\\ongxu\\Downloads\\test\\music"
        for file in sorted(Path(musicDirectory).iterdir(), key=os.path.getctime):
            filename = os.fsdecode(file)
            if filename.endswith(".wav"):
                idx = filename[::-1].find("\\")
                self.musicList.add(filename[-idx+3:-4])
        print(self.musicList)



    def volume(self):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMasterVolumeLevelScalar(self.slider.value()/100,None)
        self.volumeValue.setText(f"{self.slider.value()}")

    def downloadVideo(self, url:str):
        
        filename = 'C:\\Users\\ongxu\\Downloads\\test\\music\\%(playlist_index)s--%(title)s.%(ext)s'

        while True:
            try:
                ydl_cmd = ['youtube-dl', '--extract-audio', '--audio-format', 'wav', '--audio-quality', '256', '-o', filename, url]
                subprocess.run(ydl_cmd)
            except:
                continue
            else:
                break


app = QApplication(sys.argv)
window = Window()
window.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
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

QSlider::groove{
    margin: 5px 0px 0px 0px;
    border: 1px solid "white";
    border-radius: 5px; 
    height: 10px;
}

QSlider::handle{
    
    padding: 15px 15px 15px 15px;
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);
    width: 10px;
}
QSlider::handle:hover{
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4ff, stop:1 #8f8fff);
}


""")
sys.exit(app.exec())