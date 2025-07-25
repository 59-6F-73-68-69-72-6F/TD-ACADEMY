from Qt.QtCore import QObject
from maya import cmds as m


class RenamerLogic(QObject):
    
    def __init__(self):
        super().__init__()
    
    def rename(self, new_name: str):
        if m.ls(selection=True, type='dagNode'):
            selection = m.ls(selection=True)
            try:
                for shape in selection:
                    m.rename(shape,new_name)
            except RuntimeError as e:
                pass
                
    def prefix(self, prefix_name: str):
        if m.ls(selection=True, type='dagNode'):
            selection = m.ls(selection=True)
            try:
                for shape in selection:
                    m.rename(shape,prefix_name + shape)
            except RuntimeError as e:
                pass

    def suffix(self, suffix_name: str):
        if m.ls(selection=True, type='dagNode'):
            selection = m.ls(selection=True)
            try:
                for shape in selection:
                    m.rename(shape,shape + suffix_name)
            except RuntimeError as e:
                pass
            
    def replace(self, search_text: str, replace_text: str):
        all_nodes = m.ls(type='dagNode')
        selection = m.ls(selection=True, type='dagNode')
        # --- ALL NODES ---
        if search_text and replace_text and selection == []:
            try:
                for node in all_nodes:
                    if search_text in node:
                        transform = m.listRelatives(node, parent=True)
                        if transform:
                            new_name = transform[0].replace(search_text, replace_text)
                            m.rename(transform[0],new_name)
                            
            except RuntimeError as e:
                pass
        # ON SELECTION ---
        elif search_text and replace_text and selection:
            try:
                for shape in selection:
                    if search_text in shape:
                        new_name = shape.replace(search_text, replace_text)
                        m.rename(shape,new_name)
            except RuntimeError as e:
                pass
        # ERROR MESSAGE ---
        else:
            m.inViewMessage(amg='Please fill all fields.', pos='midCenter', fade=True)

