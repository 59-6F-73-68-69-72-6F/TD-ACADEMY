from Qt.QtWidgets import QWidget,QLabel,QLineEdit,QPushButton,QVBoxLayout,QHBoxLayout,QFrame
from Qt.QtGui import QFont
from Qt.QtCore import Qt, Signal

FONT = "Nimbus Sans, Bold"
COLOR_TITLE = "#c0c0c0"
COLOR_ENTRY = "#222b33"
TEXT_COLOR = "#c0c0c0"
FONT_SIZE = 12


class MagicRenamer(QWidget):
    """
    Widget that provides a user interface for renaming, adding prefixes/suffixes,
    and replacing text in object names.
    It emits signals when actions are performed, allowing other components to respond accordingly.
    """
    rename_signal_request = Signal(str)
    prefix_signal_request = Signal(str)
    suffix_signal_request = Signal(str)
    replace_signal_request = Signal(str, str)
    
    def __init__(self):
        """ Initializes the MagicRenamer widget, builds the UI, and connects signals. """
        super().__init__()
        self.buildUI()
        self.connect_signals()

    # SET WINDOW --------------------------------------------
    def buildUI(self):
        """ Constructs and arranges all the UI elements for the UI widget. """
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
        self.logo.setAlignment(Qt.AlignCenter)

        # ROW 1 ---
        row1_layout = QHBoxLayout()
        NameInsert = self.label_text("Name:")
        NameInsert.setContentsMargins(0,30,0,0)
        
        #ROW 2 ---
        row2_layout = QHBoxLayout()
        self.EntryNameInsert = self.bar_text("Name")
        self.ButtonName = self.push_button("N")
        
        # ROW 3 ---
        row3_layout = QHBoxLayout()
        PreSuf = self.label_text("Prefix/Suffix:")
        PreSuf.setContentsMargins(0,30,0,0)
        
        # ROW 4 ---
        row4_layout = QHBoxLayout()
        self.EntryPrefix = self.bar_text("Prefix")
        self.ButtonPrefix = self.push_button("P")
        
        # ROW 5 ---
        row5_layout = QHBoxLayout()
        self.EntrySuffix = self.bar_text("Suffix")
        self.ButtonSuffix = self.push_button("S")
        
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
        self.ButtonReplace = self.push_button("R")
        
        
        # ADD SEPARATORS TO LAYOUTS ---
        self.sep1_layout.addWidget(separator_1)
        self.sep2_layout.addWidget(separator_2)
        self.sep3_layout.addWidget(separator_3)
        self.sep4_layout.addWidget(separator_4)
        self.sep5_layout.addWidget(separator_5)
        self.sep6_layout.addWidget(separator_6)
        
        # HORIZONTAL LAYOUTS ---
        row0_layout.addWidget(self.logo)
        row1_layout.addWidget(NameInsert)
        row2_layout.addWidget(self.EntryNameInsert)
        row2_layout.addWidget(self.ButtonName)
        row3_layout.addWidget(PreSuf)
        row4_layout.addWidget(self.EntryPrefix)
        row4_layout.addWidget(self.ButtonPrefix)
        row5_layout.addWidget(self.EntrySuffix)
        row5_layout.addWidget(self.ButtonSuffix)
        row6_layout.addWidget(SearchReplace)
        row7_layout.addWidget(self.EntrySearch)
        row8_layout.addWidget(self.EntryReplace)
        row8_layout.addWidget(self.ButtonReplace)

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
    def label_text(self,text: str) -> QLabel:
        """
        Creates a QLabel with predefined styling.
        Args:
            text (str): The text to display on the label.
        """
        label = QLabel(text=text)
        label.setFont(QFont(FONT,FONT_SIZE))
        label.setStyleSheet(f"color:{COLOR_TITLE}")
        return label

    def bar_text(self,text:str=None) -> QLineEdit:
        """
        Creates a QLineEdit with predefined styling.
        Args:
            text (str, optional): The placeholder text for the line edit. Defaults to None.
        """
        line_edit = QLineEdit(placeholderText=text)
        line_edit.setFont(QFont(FONT,FONT_SIZE))
        line_edit.setStyleSheet(f" background-color: {COLOR_ENTRY} ; color: {TEXT_COLOR};")
        return line_edit

    def push_button(self,text:str) -> QPushButton:
        """
        Creates a QPushButton with predefined styling.
        Args:
            text (str): The text to display on the button.
        """
        button = QPushButton(text)
        button.setFont(QFont(FONT,FONT_SIZE))
        button.setFixedSize(80,23)
        button.setStyleSheet(f" background-color: #2a9d8f ; color:#222831;")
        return button
    
    def splitter(self) -> QFrame:
        """ Creates a QFrame to be used as a horizontal separator with predefined styling. """
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        separator.setFixedSize(300,2)
        separator.setStyleSheet(f"background-color: #c0c0c0;")
        return separator

    # SIGNALS --------------------------------------------
    def connect_signals(self):
        """ Connects UI element signals (e.g., button clicks) to their corresponding slots. """
        self.EntryNameInsert.returnPressed.connect(self.on_name)
        self.ButtonName.clicked.connect(self.on_name)
        
        self.EntryPrefix.returnPressed.connect(self.on_prefix)
        self.ButtonPrefix.clicked.connect(self.on_prefix)
        
        self.EntrySuffix.returnPressed.connect(self.on_suffix)
        self.ButtonSuffix.clicked.connect(self.on_suffix)
        
        self.ButtonReplace.clicked.connect(self.on_replace)

    # EMITTERS --------------------------------------
    def on_name(self):
        """ Slot for the rename action. Emits the rename_signal_request with the new name. """
        new_name = self.EntryNameInsert.text()
        self.rename_signal_request.emit(new_name)
        self.EntryNameInsert.clear()
        
    def on_prefix(self):
        """ Slot for the add prefix action. Emits the prefix_signal_request with the new prefix. """
        new_prefix = self.EntryPrefix.text()
        self.prefix_signal_request.emit(new_prefix)
        self.EntryPrefix.clear()
        
    def on_suffix(self):
        """ Slot for the add suffix action. Emits the suffix_signal_request with the new suffix. """
        new_suffix = self.EntrySuffix.text()
        self.suffix_signal_request.emit(new_suffix)
        self.EntrySuffix.clear()
    
    def on_replace(self):
        """ Slot for the search and replace action. Emits the replace_signal_request with the search and replace text. """
        search_text = self.EntrySearch.text()
        replace_text = self.EntryReplace.text()
        self.replace_signal_request.emit(search_text, replace_text)
        self.EntrySearch.clear()
        self.EntryReplace.clear()
