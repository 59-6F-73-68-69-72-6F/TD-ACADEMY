######################################################
# - MAGIC MANAGER -
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

def getMayaMainWindow():
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





