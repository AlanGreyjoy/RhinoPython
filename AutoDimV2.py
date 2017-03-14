import rhinoscriptsyntax as rs

def Main():
    
    getObject = rs.GetObject("Select Object to dim", 0, False, True)
    rs.Command("_BoundingBox _Output=Curves _Enter")
    rs.UnselectAllObjects()
    
    bB = rs.LastCreatedObjects(True)
    
    curve1 = bB
    
    curve2 = getObject
    
    intersection_list = rs.CurveCurveIntersection(curve1, curve2)
    
    garbageCan = []
    for intersection in intersection_list:
        point = rs.AddPoint(intersection[1])
        garbageCan.append(point)
        
    rs.UnselectAllObjects()
    rs.DeleteObjects(bB)
    
    rs.Command("_Dim")
    rs.Command("_Dim")
    
    aa = 0
    for k in garbageCan:
        rs.DeleteObject(garbageCan[aa])
        aa = aa + 1
        
Main()

