import argparse
import os
import sys
import cv2
import pyzed.sl as sl

def Capture():
    Source , Save_L, Save_R, Out = opt.path , opt.Save_Left , opt.Save_Right , opt.output
    L_Path = "LeftSide-Frames"
    R_Path = "RightSide-Frames"

    if os.path.exists(Out) == False:
        os.makedirs(Out)
        os.chdir(Out)
        if Save_L:
            os.mkdir("LeftSide-Frames")
        if Save_R:
            os.mkdir("RightSide-Frames")
    else :
        os.chdir(Out)
        if  os.path.exists(L_Path) == False and Save_L :
            os.mkdir(L_Path)
        if os.path.exists(R_Path) == False and Save_R:
            os.mkdir(R_Path)
    
            

    # Create a ZED camera object
    zed = sl.Camera()
    # Set SVO path for playback

    init_parameters = sl.InitParameters()
    init_parameters.set_from_svo_file(Source)
    
    # Open the ZED
    zed = sl.Camera()
    err = zed.open(init_parameters)

    svo_Left = sl.Mat()
    svo_Right = sl.Mat()
    count = 1 
    while 1 :
        if zed.grab() == sl.ERROR_CODE.SUCCESS:
            # Read side by side frames stored in the SVO
            if Save_L:
                zed.retrieve_image(svo_Left, sl.VIEW.LEFT)
                img = svo_Left.get_data()
                cv2.imwrite( L_Path + "/L_" +str(count) + ".jpg" , img)
            if Save_R:
                zed.retrieve_image(svo_Right, sl.VIEW.RIGHT)
                img = svo_Right.get_data()
                cv2.imwrite( R_Path + "/R_" +str(count) + ".jpg" , img)
        
        elif zed.grab() == sl.ERROR_CODE.END_OF_SVOFILE_REACHED:
            sys.exit("Mission Done (Y) Total Number of Frames = {}".format(count))  

        count = count+1 
    
    
            

        
    
    
    
    
    
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', '-p' , required=True , type=str, help='Path to the .svo video')
    parser.add_argument('--Save-Left', '-s-l', action='store_true', help='Save LeftSide Image')
    parser.add_argument('--Save-Right', '-s-r', action='store_true', help='Save RightSide Image')
    parser.add_argument('--output', '-o',type=str, default='Output', help='Output Direcotry')  

    opt = parser.parse_args()


    Capture()
    
    
