######################################################
# - MAGIC MANAGER -
# AUTHOR : RUDY LETI
# DATE : 2025/07/18
# RENAMER UI
######################################################


from PySide2.QtWidgets import QWidget,QLabel,QLineEdit,QPushButton,QVBoxLayout,QHBoxLayout,QFrame
from PySide2.QtGui import QFont,QPixmap
from PySide2.QtCore import Qt
from maya import cmds as m

FONT = "Nimbus Sans, Bold"
COLOR_TITLE = "#c0c0c0"
COLOR_ENTRY = "#222b33"
TEXT_COLOR = "#c0c0c0"
FONT_SIZE = 12


class MagicRenamer(QWidget):
    def __init__(self):
        super().__init__()
        self.buildUI()

    # SET WINDOW --------------------------------------------
    def buildUI(self):
        # WINDOW ---
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)  # KEEP WINDOW ON TOP
        self.setFixedSize(310,460)
        self.setWindowTitle("Magic Renamer")
        self.window().setStyleSheet(" background-color: #393E46  ;")
        
        # MAIN LAYOUT ---
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(3,0,3,30)
        main_layout.setSpacing(4)
        
        # SEPARATOR ---
        self.sep1_layout = QHBoxLayout()
        self.sep2_layout = QHBoxLayout()
        self.sep3_layout = QHBoxLayout()
        self.sep4_layout = QHBoxLayout()
        self.sep5_layout = QHBoxLayout()
        self.sep6_layout = QHBoxLayout()
        separator_1 = self.splitter()
        separator_2 = self.splitter()
        separator_3 = self.splitter()
        separator_4 = self.splitter()
        separator_5 = self.splitter()
        separator_6 = self.splitter()
        
        # ROW 0 ---
        row0_layout = QHBoxLayout()
        self.logo = QLabel()
        img = QPixmap(r"TD-ACADEMY\4_ui\img\logo.png")
    
        # ROW 1 ---
        row1_layout = QHBoxLayout()
        NameInsert = self.label_text("Name:")
        NameInsert.setContentsMargins(0,30,0,0)
        
        #ROW 2 ---
        row2_layout = QHBoxLayout()
        self.EntryNameInsert = self.bar_text("Name")
        self.EntryNameInsert.returnPressed.connect(self.rename) # press Enter to rename
        ButtonName = self.push_button("N")
        ButtonName.clicked.connect(self.rename)
        
        # ROW 3 ---
        row3_layout = QHBoxLayout()
        PreSuf = self.label_text("Prefix/Suffix:")
        PreSuf.setContentsMargins(0,30,0,0)
        
        # ROW 4 ---
        row4_layout = QHBoxLayout()
        self.EntryPrefix = self.bar_text("Prefix")
        self.EntryPrefix.returnPressed.connect(self.prefix) # press Enter to prefix
        ButtonPrefix = self.push_button("P")
        ButtonPrefix.clicked.connect(self.prefix)
        
        # ROW 5 ---
        row5_layout = QHBoxLayout()
        self.EntrySuffix = self.bar_text("Suffix")
        self.EntrySuffix.returnPressed.connect(self.suffix) # press Enter to suffix
        ButtonSuffix = self.push_button("S")
        ButtonSuffix.clicked.connect(self.suffix)
        
        # ROW 6 ---
        row6_layout = QHBoxLayout()
        SearchReplace = self.label_text("Search/Replace:")
        SearchReplace.setContentsMargins(0,30,0,0)
        
        # ROW 7 ---
        row7_layout = QHBoxLayout()
        self.EntrySearch = self.bar_text("Search")
        
        # ROW 8 ---
        row8_layout = QHBoxLayout()
        self.EntryReplace = self.bar_text("Replace")
        ButtonReplace = self.push_button("R")
        ButtonReplace.clicked.connect(self.replace)
        
        
        # ADD SEPARATORS TO LAYOUTS ---
        self.sep1_layout.addWidget(separator_1)
        self.sep2_layout.addWidget(separator_2)
        self.sep3_layout.addWidget(separator_3)
        self.sep4_layout.addWidget(separator_4)
        self.sep5_layout.addWidget(separator_5)
        self.sep6_layout.addWidget(separator_6)
        
        # HORIZONTAL LAYOUTS ---
        row0_layout.addWidget(self.Qlabel)
        row1_layout.addWidget(NameInsert)
        row2_layout.addWidget(self.EntryNameInsert)
        row2_layout.addWidget(ButtonName)
        row3_layout.addWidget(PreSuf)
        row4_layout.addWidget(self.EntryPrefix)
        row4_layout.addWidget(ButtonPrefix)
        row5_layout.addWidget(self.EntrySuffix)
        row5_layout.addWidget(ButtonSuffix)
        row6_layout.addWidget(SearchReplace)
        row7_layout.addWidget(self.EntrySearch)
        row8_layout.addWidget(self.EntryReplace)
        row8_layout.addWidget(ButtonReplace)

        # VERTICAL LAYOUTS ---
        main_layout.addLayout(row0_layout)
        main_layout.addLayout(row1_layout)
        main_layout.addLayout(self.sep1_layout)
        main_layout.addLayout(row2_layout)
        main_layout.addLayout(self.sep2_layout)
        main_layout.addLayout(row3_layout)
        main_layout.addLayout(self.sep3_layout)
        main_layout.addLayout(row4_layout)
        main_layout.addLayout(row5_layout)
        main_layout.addLayout(self.sep4_layout)
        main_layout.addLayout(row6_layout)
        main_layout.addLayout(self.sep5_layout)
        main_layout.addLayout(row7_layout)
        main_layout.addLayout(row8_layout)
        main_layout.addLayout(self.sep6_layout)
        
        self.setLayout(main_layout)


    # GENERIC WIDGETS --------------------------------------------
    def label_text(self,text):
        label = QLabel(text=text)
        label.setFont(QFont(FONT,FONT_SIZE))
        label.setStyleSheet(f"color:{COLOR_TITLE}")
        return label

    def bar_text(self,text=None):
        line_edit = QLineEdit(placeholderText=text)
        line_edit.setFont(QFont(FONT,FONT_SIZE))
        line_edit.setStyleSheet(f" background-color: {COLOR_ENTRY} ; color: {TEXT_COLOR};")
        return line_edit

    def push_button(self,text):
        button = QPushButton(text)
        button.setFont(QFont(FONT,FONT_SIZE))
        button.setFixedSize(80,23)
        button.setStyleSheet(f" background-color: #2a9d8f ; color:#222831;")
        return button
    
    def splitter(self):
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        separator.setFixedSize(300,2)
        separator.setStyleSheet(f"background-color: #c0c0c0;")
        return separator


    # FUNCTIONS --------------------------------------------
    def rename(self):
        pass
                
    def prefix(self):
        pass

    def suffix(self):
        pass
            
    def replace(self):
        pass

# --- MAYA INTEGRATION UTILITIES ---
ui = None
def getMayaMainWindow():
    global ui
    ui = MagicRenamer()
    ui.show()
    return ui

getMayaMainWindow()
