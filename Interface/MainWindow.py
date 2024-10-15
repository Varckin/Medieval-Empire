from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from pathlib import Path

from JSON.json import getValue


class MainInterface(QWidget):
    def __init__(self):
        super().__init__()
        self.pathIcon: str = f"{str(Path.cwd())}/Interface/Icon/"
        self.fillingWidget()
        self.setupWidget()
        self.setuplayout()

    def fillingWidget(self) -> None:
        self.nameContry: QLabel = QLabel()
        self.government: QLabel = QLabel()
        self.resource: QLabel = QLabel()

        self.silver: QLabel = QLabel()
        self.wheat: QLabel = QLabel()
        self.wood: QLabel = QLabel()
        self.stone: QLabel = QLabel()
        self.iron: QLabel = QLabel()
        self.wine: QLabel = QLabel()
        self.amber: QLabel = QLabel()
        self.emptylabel: QLabel = QLabel()

        self.gold: QLabel = QLabel()
        self.army: QLabel = QLabel()
        self.sizeArmy: QLabel = QLabel()

        self.mainlayout: QGridLayout = QGridLayout()
        self.firstbox: QVBoxLayout = QVBoxLayout()
        self.secondbox: QVBoxLayout = QVBoxLayout()

        self.build: QPushButton = QPushButton()
        self.chronicle: QPushButton = QPushButton()
        self.trainArmy: QPushButton = QPushButton()
        self.diplomacy: QPushButton = QPushButton()
        self.nextMove: QPushButton = QPushButton()

    def setupWidget(self) -> None:
        self.nameContry.setText(getValue("countryName"))
        self.nameContry.setStyleSheet("QLabel { font-size: 18px; font-weight: bold; }")
        self.resource.setText(getValue("resourceName"))
        self.resource.setStyleSheet("QLabel { font-size: 15px; font-weight: bold; }")
        self.government.setText(f'<img src="{self.pathIcon}Government_monarchy.png" width="22" height="22"> {getValue("government")}')
        self.silver.setText(f'<img src="{self.pathIcon}Silver.png" width="22" height="22"> {getValue("resourceSilver")}')
        self.wheat.setText(f'<img src="{self.pathIcon}Wheat.png" width="22" height="22"> {getValue("resourceWheat")}')
        self.wood.setText(f'<img src="{self.pathIcon}Wood.png" width="22" height="22"> {getValue("resourceWood")}')
        self.stone.setText(f'<img src="{self.pathIcon}Stone.png" width="22" height="22"> {getValue("resourceStone")}')
        self.iron.setText(f'<img src="{self.pathIcon}Iron.png" width="22" height="22"> {getValue("resourceIron")}')
        self.wine.setText(f'<img src="{self.pathIcon}Wine.png" width="22" height="22"> {getValue("resourceWine")}')
        self.amber.setText(f'<img src="{self.pathIcon}Amber.png" width="22" height="22"> {getValue("resourceAmber")}')
        self.gold.setText(f'<img src="{self.pathIcon}Gold.png" width="22" height="22"> {getValue("resourceGold")}')
        self.gold.setAlignment(Qt.AlignRight)
        self.army.setText(f'<img src="{self.pathIcon}Army.png" width="22" height="22"> {getValue("armyName")}')
        self.sizeArmy.setText(f'<img src="{self.pathIcon}Size_army.png" width="22" height="22"> {getValue("armySize")}')

        self.build.setText(getValue("actionConstruction"))
        self.chronicle.setText(getValue("actionChronicles"))
        self.trainArmy.setText(getValue("actionTrainArmy"))
        self.diplomacy.setText(getValue("actionDiplomacy"))
        self.nextMove.setText(getValue("actionNextTurn"))

        self.build.setIcon(QIcon(f"{self.pathIcon}Build.png"))
        self.chronicle.setIcon(QIcon(f"{self.pathIcon}Chronicle.png"))
        self.trainArmy.setIcon(QIcon(f"{self.pathIcon}Train_army.png"))
        self.diplomacy.setIcon(QIcon(f"{self.pathIcon}Diplomaticy.png"))
        self.nextMove.setStyleSheet("QPushButton { border: none; color: green; }")

    def setuplayout(self) -> None: 
        self.mainlayout.addWidget(self.nameContry, 0, 0)
        self.mainlayout.addWidget(self.government, 1, 0)
        self.mainlayout.addWidget(self.resource, 2, 0)

        self.mainlayout.addWidget(self.silver, 3, 0)
        self.mainlayout.addWidget(self.wheat, 4, 0)
        self.mainlayout.addWidget(self.wood, 5, 0)
        self.mainlayout.addWidget(self.stone, 6, 0)
        self.mainlayout.addWidget(self.iron, 7, 0)
        self.mainlayout.addWidget(self.wine, 8, 0)
        self.mainlayout.addWidget(self.amber, 9, 0)
        self.mainlayout.addWidget(self.emptylabel, 10, 0)

        self.mainlayout.addWidget(self.build, 11, 0)
        self.mainlayout.addWidget(self.chronicle, 12, 0)

        self.mainlayout.addWidget(self.gold, 0, 1)

        self.mainlayout.addWidget(self.army, 3, 1)
        self.mainlayout.addWidget(self.sizeArmy, 4, 1)
        self.mainlayout.addWidget(self.trainArmy, 5, 1)

        self.mainlayout.addWidget(self.diplomacy, 11, 1)
        self.mainlayout.addWidget(self.nextMove, 12, 1)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.interface: MainInterface = MainInterface()
        self.setWindowTitle(getValue("gameName"))
        self.setMinimumSize(500, 500)
        self.setMaximumSize(750, 750)
        self.setWindowIcon(QIcon(f"{self.interface.pathIcon}Logo.png"))
        self.setLayout(self.interface.mainlayout)
