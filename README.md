# Zed-Camera-Frame-Capture
Python Script to capture eash frame from .SVO Video

## How To Use ?!
  1. Clone the repo
  2. Open Cmd inside the repo 
 
### Sample Cmd Command : 
```python
 $ python Cap-frame.py --path "Path/to-SVO-File/" --Save-Left  --Save-Right --output Vid/ -s Vid_1 --dropFrame 2
 $ python Cap-frame.py --path "E:/Test/Repo/Vid.svo"  -s-l -s-r -s Gate_Vid -d 2

```
### Possible Arguments :
    1. --Save-Left or -s-l : Flag to Save LeftSide Image
    2. --Save-Right or -s-r : Flag to Save RightSide Image
    3. --output or -o : Optional output Directory Path "Default Value /Output"
    4. --seed or -s : Seed to be added to the output img 
    5. --dropFrame or -d : Number of frames to be dropped "Default = 0"


