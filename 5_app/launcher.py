'''
Copy the script in Maya script editor (python).
change the PATH to yours
Drag and Drop the script in your Maya shelf.
Enjoy !
'''

import sys
from importlib import reload

directory = r"YOUR_PATH\Magic_Renamer"
if directory not in sys.path:
    sys.path.append(directory)

import main
reload(main)
main
print("Launched Magic Renamer.")
