######################################################
# - MAGIC RENAMER -
# AUTHOR : RUDY LETI
# DATE : 2025/07/25
# MAGIC RENAMER UI
######################################################


from Qt.QtGui import QPixmap
import MR_logic
import MR_UI
import os

logic = None
ui = None

def getMayaMainWindow() -> MR_UI.MagicRenamer:
    """Initializes and displays the Magic Renamer UI window.

    This function serves as the main entry point for the tool. It performs
    the following steps:
    1.  Instantiates the user interface (MagicRenamer) and the business logic
        (RenamerLogic), assigning them to global variables for persistence.
    2.  Constructs the path to the application logo relative to the script's
        location and loads the image into the UI.
    3.  Connects the signals emitted by the UI (e.g., button clicks) to the
        corresponding methods in the logic class. This establishes the
        communication between the front-end and the back-end operations.
    4.  Displays the UI window.

    Returns:
        MR_UI.MagicRenamer: The instance of the created UI window.
    """
    global ui,logic
    ui = MR_UI.MagicRenamer()
    logic = MR_logic.RenamerLogic()
    
    # LOAD LOGO IMAGE
    script_path = os.path.dirname(os.path.abspath(__file__))  # GET THE PATH OF THE CURRENT SCRIPT
    logo_path = os.path.join(script_path, "img", "logo.png")
    img = QPixmap(logo_path)
    ui.logo.setPixmap(img)
    
    # CONNECT SIGNALS
    ui.rename_signal_request.connect(logic.rename)
    ui.prefix_signal_request.connect(logic.prefix)
    ui.suffix_signal_request.connect(logic.suffix)
    ui.replace_signal_request.connect(logic.replace)
    
    ui.show()
    return ui
getMayaMainWindow()
