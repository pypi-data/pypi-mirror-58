# TPUCameraManager

```
from TPUCameraManager.TPUCameraManager.TPUCameraManager import CameraManager, GStreamerPipelines

camMan = CameraManager() #Creates new camera manager object
CSICam = camMan.newCam(0) #Creates new RGB CSI-camera

#H264 = CSICam.addPipeline(GStreamerPipelines.H264,(640,480),30,"H264") #Creates an H264 stream at 30 fps and 640x480 for streaming server
#H264.addListener(<yourClass>) #Calls the out function in provided class everytime new data comes in
#AI = CSICam.addPipeline(GStreamerPipelines.RGB,(640,480),30,"AI") #Creates an RGB stream at 30 fps and 640x480 for AI
#CV = CSICam.addPipeline(GStreamerPipelines.RGB,(640,480),30,"CV") #Creates an RGB stream at 30 fps and 640x480 for openCV

MJPEG = CSICam.addPipeline(GStreamerPipelines.MJPEG,(640,480),30,"MJPEG")

CSICam.startPipeline() #Start gstreamer Streams
#CSICam.stopPipeline() #Stops gstreamer Streams

#CSICam.removePipeline("H264") #Removes a specific pipeline
#CSICam.removeAllPipelines() #Removes all pipleines from a camera object

#camMan.close(CSICam) #Close a specific camera object
#camMan.closeAll() #Close all camera objects created
```