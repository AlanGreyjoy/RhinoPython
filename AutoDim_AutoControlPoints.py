import rhinoscriptsyntax as rs
import Rhino

#------------------ Auto Dimensions --------------#
#               Writen By: Alan Spurlock          #
#                   3/22/2016, 9:31               #
#-------------------------------------------------#

def Main():
    
    getObject = rs.GetObject("Select Object to dim", 0, False, True)
    rs.Command("_BoundingBox _Output=Curves _Enter")
    rs.UnselectAllObjects()
    
    bB = rs.LastCreatedObjects(True)
    cp = rs.CurvePoints(bB)
    
    p0 = rs.AddPoint(cp[0])
    p1 = rs.AddPoint(cp[1])
    p2 = rs.AddPoint(cp[2])
    p3 = rs.AddPoint(cp[3])
   
    
    wd = rs.Distance(p3,p2)
    wd = wd / 2
    
    ld = rs.Distance(p3, p0)
    ld = ld /2
    
    mwp = rs.AddPoint(cp[2])
    mlp = rs.AddPoint(cp[0])
    
    widthDimPoint = rs.MoveObject(mwp, (-wd,2,0))
    legnthDimPoint = rs.MoveObject(mlp, (-2,ld,0))
    
    #m1 = rs.CurveMidPoint(bB[0])
    
    rs.AddAlignedDimension(p2, p3, widthDimPoint)
    rs.AddAlignedDimension(p0, p3, legnthDimPoint)
    
    
    rs.DeleteObjects([bB, p0,p1,p2,p3,mwp,mlp])
    
    
    
if __name__=="__main__":
    Main()
