from Maruzensky import Maruzen
from Characters import *

#===================================================
# List of known debuffs for easier arrangement
#====================================================

debuffs = []

#==============================================
# For Maruzen
#==============================================
m = Maruzen()

def sabotage():
    if m.enraged():
        debuffs.append("Sabotaged!")
        return True
    else:
        return False
