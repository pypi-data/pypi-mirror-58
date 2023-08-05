# TPUCameraManager

```
from TPUCameraManager.TPUCameraManager import CameraManager, GStreamerPipelines
import time
camMan = CameraManager() #Creates new camera manager object
#camMan = CameraManager()
cam2 = camMan.newCam(0,GStreamerPipelines.RGB,(640,480),30) #Creates new RGB camera stream at 640 x 480
time.sleep(1)
camMan.close(cam2) #Closes the camera stream
cam2 = camMan.newCam(0,GStreamerPipelines.H264,(1920,1080),30) #Creates new RGB camera stream at 1920 by 1080
while True:
    if(cam2): #Returns true if there are new values
        image = cam2.getImage() #CAN ONLY BE USED ON RGB IMAGE
        imageBytes = cam2.data #Used on H264 bytes stream
        print(image.shape)
```