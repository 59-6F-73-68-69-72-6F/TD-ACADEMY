# STYLE ***************************************************************************
# content = assignment (Python Advanced)
#
# date    = 2025-07-01
# email   = rudyleti@gmail.com
#**********************************************************************************

from maya import cmds as mc


# COMMENT --------------------------------------------------

def set_color(ctrlList:list=None, color:int=None):
    colorset = {1 : 4,2 : 13,3 : 25,4 : 17,5 : 17,6 : 15,7 : 6,8 : 16} # COLOR SET VALUE DICTIONNARY
    
    for ctrlName in ctrlList:
        try:
            mc.setAttr(ctrlName + 'Shape.overrideEnabled', 1)
        except:
            pass
        
        try:
            for key,value in colorset.items():
                if color == key:
                    mc.setAttr(ctrlName + 'Shape.overrideColor', value)
        except:
            pass
        
        
            
# EXAMPLE
# set_color(['circle','circle1'], 8)
