from Qt.QtCore import QObject
from maya import cmds as m


class RenamerLogic(QObject):
    """
    Handles the core logic for renaming objects in Maya.
    This class contains the methods that are executed when signals are received
    from the UI. It directly uses Maya commands (`maya.cmds`) to manipulate
    objects in the current scene.
    """
    
    def __init__(self):
        super().__init__()
    
    def rename(self, new_name: str):
        """
        Renames selected DAG nodes.
        If multiple objects are selected, Maya's default behavior for renaming
        multiple objects will apply (adding a numeric suffix to subsequent objects).
        Args:
            new_name (str): The new base name for the selected object(s).
        """
        if m.ls(selection=True, type='dagNode'):
            selection = m.ls(selection=True)
            try:
                for shape in selection:
                    m.rename(shape,new_name)
            except RuntimeError as e:

                pass
                
    def prefix(self, prefix_name: str):
        """
        Adds a prefix to the name of each selected DAG node.
        Args:
            prefix_name (str): The string to prepend to the object names.
        """
        if m.ls(selection=True, type='dagNode'):
            selection = m.ls(selection=True)
            try:
                for shape in selection:
                    m.rename(shape,prefix_name + shape)
            except RuntimeError as e:
                pass

    def suffix(self, suffix_name: str):
        """
        Adds a suffix to the name of each selected DAG node.
        Args:
            suffix_name (str): The string to append to the object names.
        """
        if m.ls(selection=True, type='dagNode'):
            selection = m.ls(selection=True)
            try:
                for shape in selection:
                    m.rename(shape,shape + suffix_name)
            except RuntimeError as e:

                pass
            
    def replace(self, search_text: str, replace_text: str):
        """
        Performs a search and replace on object names.
        
        The behavior depends on whether objects are selected:
        - If objects are selected: Performs search and replace on the names of
          the selected objects only.
        - If no objects are selected: Performs search and replace on all DAG
          nodes in the entire scene. It renames the parent transform of any
          node whose name contains the search text.
        - If either search or replace fields are empty, an in-view message
          is displayed to the user in Maya.

        Args:
            search_text (str): The text to search for in object names.
            replace_text (str): The text to replace the search text with.
        """
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
