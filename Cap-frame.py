import argparse
import os
import sys
import cv2
import pyzed.sl as sl

def Capture():
    Source , Save_L, Save_R, Out, seed , drop = opt.path , opt.Save_Left , opt.Save_Right , opt.output , opt.seed , opt.dropFrame+1
    
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
            zed.retrieve_image(svo_Left, sl.VIEW.LEFT)
            zed.retrieve_image(svo_Right, sl.VIEW.RIGHT)
            if count % drop == 0 :
                if Save_L:
                    img = svo_Left.get_data()
                    cv2.imwrite( "{}/{}_L_{}.jpg".format(L_Path,seed,count) , img)

                if Save_R:
                    img = svo_Right.get_data()
                    cv2.imwrite( "{}/{}_R_{}.jpg".format(R_Path,seed,count) , img)
            
        
        elif zed.grab() == sl.ERROR_CODE.END_OF_SVOFILE_REACHED:
            sys.exit("Mission Done (Y) Total Number of Frames = {}".format(count))  

        count = count+1 
    
    
            

        
    
    
    
    
    
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', '-p' , required=True , type=str, help='Path to the .svo video')
    parser.add_argument('--seed', '-s' , required=True , type=str, help='Seed to be added to the output img name')
    parser.add_argument('--Save-Left', '-s-l', action='store_true', help='Save LeftSide Image')
    parser.add_argument('--Save-Right', '-s-r', action='store_true', help='Save RightSide Image')
    parser.add_argument('--output', '-o',type=str, default='Output', help='Output Direcotry')  
    parser.add_argument("-d", "--dropFrame", type=int, default= 0, help="Number of Frames to be dropped")
    opt = parser.parse_args()
    
    Capture()
    
    
