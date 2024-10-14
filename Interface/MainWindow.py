from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QPushButton
from PyQt5.QtGui import QPixmap
from pathlib import Path


class MainInterface(QWidget):
    def __init__(self):
        super().__init__()
        self.currentPath: str = str(Path.cwd())

    def fillingWidget(self) -> None:
        self.nameContry: QLabel = QLabel()
        self.resource: QLabel = QLabel()
        self.gold: QLabel = QLabel()
        self.iron: QLabel = QLabel()
        self.wine: QLabel = QLabel()
        self.silver: QLabel = QLabel()
        self.army: QLabel = QLabel()
        self.wheat: QLabel = QLabel()
        self.wood: QLabel = QLabel()
        self.stone: QLabel = QLabel()
        self.amber: QLabel = QLabel()
        self.government: QLabel = QLabel()
        self.sizeArmy: QLabel = QLabel()

        self.mainlayout: QGridLayout = QGridLayout()

        self.build: QPushButton = QPushButton()
        self.diplomacy: QPushButton = QPushButton()
        self.trainArmy: QPushButton = QPushButton()
        self.nextMove: QPushButton = QPushButton()
        self.chronicle: QPushButton = QPushButton()

    def setupWidget(self) -> None:
        pass

    def setuplayout(self) -> None:
        pass

    def iconPixmap(self) -> None:
        self.goldIcon: QPixmap = QPixmap()
        self.ironIcon: QPixmap = QPixmap()
        self.amberIcon: QPixmap = QPixmap()
        self.armyIcon: QPixmap = QPixmap()
        self.silverIcon: QPixmap = QPixmap()
        self.governmentIcon: QPixmap = QPixmap()
        self.woodIcon: QPixmap = QPixmap()
        self.stoneIcon: QPixmap = QPixmap()
        self.wheatIcon: QPixmap = QPixmap()
        self.wineIcon: QPixmap = QPixmap()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.interface: MainInterface = MainInterface()
