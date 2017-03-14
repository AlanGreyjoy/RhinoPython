import rhinoscriptsyntax as rs
import Rhino
import time
#
#                <M
#     o          <M  
#    /| ......  /:M\------------------------------------------------,,,,,,
#  (O)[]XXXXXX[]I:K+}=====<{H}>================================------------>
#    \| ^^^^^^  \:W/------------------------------------------------''''''
#     o          <W  Alan Spurlocks - Auto Part List
#                <W  Writen by Alan Spurlock 2016 / Written at home, owned by Alan Spurlock
#                (O) ver 0.1a
#

#########################################***NOTICE***###############################################
#                                                                                                  #
#                             WILL NOT WORK OUTSIDE OF MY TEMPLATE                                 #
#                                                                                                  #
####################################################################################################

def Main():
    
    exitLoop = 0
    dotInt = 0
    partNameStorage = []
    
    partListPoint1 = rs.ObjectsByName("PART LIST POINT 1")
    partListPoint2 = rs.ObjectsByName("PART LIST POINT 2")
    pLP1Coor = rs.PointCoordinates(partListPoint1)
    pLP2Coor = rs.PointCoordinates(partListPoint2)
    
    gsn = rs.GetInteger("Enter the starting PART number", 1)
    
    if gsn:
        exitLoop = 1
        dotInt = gsn
        
    while exitLoop == 1:
        doubleDis = 1
        tempSet = 1
        
        while dotInt <= 10:
            if dotInt == 1:
                dotLoc = rs.GetPoint("Select Dot Location")
                rs.AddTextDot(dotInt, dotLoc)
                string = rs.StringBox("Enter Part Description:", None, "Part Description")
                partListSingleTitleBlock = rs.InsertBlock("SINGLE LIST PART TITLE BLOCK", pLP1Coor)
                partListSingle = rs.InsertBlock("SINGLE PART SINGLE LIST", pLP1Coor)
                rs.MoveObject(partListSingle, (0,-2.242,0))
                selectPart = rs.SelectObject(partListSingle)
                rs.Command("_Explode", False)
                PartInfo(dotInt, string)
                doubleDis = doubleDis + 1
                dotInt = dotInt + 1
                rs.UnselectAllObjects()
                    
            dotLoc = rs.GetPoint("Select Dot Location")
            rs.AddTextDot(dotInt, dotLoc)
            if tempSet == 1:
                string = rs.StringBox("Enter Part Description:", None, "Part Description")
                partListSingle = rs.InsertBlock("SINGLE PART SINGLE LIST", pLP1Coor)
                rs.MoveObject(partListSingle, (0,-4.49,0))
                selectPart = rs.SelectObject(partListSingle)
                rs.Command("_Explode", False)
                tempSet = 0
                PartInfo(dotInt, string)
                doubleDis = doubleDis + 1
                dotInt = dotInt + 1
                rs.UnselectAllObjects()
            else:
                string = rs.StringBox("Enter Part Description:", None, "Part Description")
                partListSingle = rs.InsertBlock("SINGLE PART SINGLE LIST", pLP1Coor)
                rs.MoveObject(partListSingle, (0,-2.242 * doubleDis,0))
                selectPart = rs.SelectObject(partListSingle)
                rs.Command("_Explode", False)
                PartInfo(dotInt, string)
                doubleDis = doubleDis + 1
                dotInt = dotInt + 1
                rs.UnselectAllObjects()
                    
        tempSet = 1
        doubleDis = 1
        while dotInt > 10:
            
            if dotInt == 11:
                dotLoc = rs.GetPoint("Select Dot Location")
                rs.AddTextDot(dotInt, dotLoc)
                string = rs.StringBox("Enter Part Description:", None, "Part Description")
                partListSingleTitleBlock = rs.InsertBlock("DOUBLE LIST PART TITLE BLOCK", pLP2Coor)
                partListSingle = rs.InsertBlock("SINGLE PART DOUBLE LIST", pLP2Coor)
                rs.MoveObject(partListSingle, (0,-2.242,0))
                selectPart = rs.SelectObject(partListSingle)
                rs.Command("_Explode", False)
                PartInfo(dotInt, string)
                dotInt = dotInt + 1
                doubleDis = doubleDis + 1
                rs.UnselectAllObjects()
                    
                if tempSet == 1:
                    dotLoc = rs.GetPoint("Select Dot Location")
                    rs.AddTextDot(dotInt, dotLoc)
                    string = rs.StringBox("Enter Part Description:", None, "Part Description")
                    partListSingleTitleBlock = rs.InsertBlock("DOUBLE LIST PART TITLE BLOCK", pLP2Coor)
                    partListSingle = rs.InsertBlock("SINGLE PART DOUBLE LIST", pLP2Coor)
                    rs.MoveObject(partListSingle, (0,-4.49,0))
                    selectPart = rs.SelectObject(partListSingle)
                    rs.Command("_Explode", False)
                    PartInfo(dotInt, string)
                    dotInt = dotInt + 1
                    doubleDis = doubleDis + 1
                    tempSet = 0
                    rs.UnselectAllObjects()
                        
            dotLoc = rs.GetPoint("Select Dot Location")
            rs.AddTextDot(dotInt, dotLoc)
            string = rs.StringBox("Enter Part Description:", None, "Part Description")
            partListSingle = rs.InsertBlock("SINGLE PART DOUBLE LIST", pLP2Coor)
            rs.MoveObject(partListSingle, (0,-2.242 * doubleDis,0))
            selectPart = rs.SelectObject(partListSingle)
            rs.Command("_Explode", False)
            PartInfo(dotInt, string)
            dotInt = dotInt + 1
            doubleDis = doubleDis + 1
            rs.UnselectAllObjects()
        
        
        exitLoop = 0
        
def PartInfo(id, text):
    partDescription = rs.ObjectsByName("PART DESCRIPTION")
    partNumber = rs.ObjectsByName("PART NUMBER")
    
    rs.TextObjectText(partDescription, text)
    rs.TextObjectText(partNumber, id)
    
    rs.ObjectName(partDescription, "FIN")
    rs.ObjectName(partNumber, "FIN")
    
if( __name__ == "__main__" ):
    Main()
    
