## Requirements

- Python 3.5 or 3.6. <a href="https://www.youtube.com/watch?v=T8wK5loXkXg">Anaconda Installation</a>
- Tensorflow <a href="https://www.youtube.com/watch?v=RplXYjxgZbw">Installation</a>
- openCV 

## Installation

#### Clone the repo
``` bash
$ https://github.com/kuunn43/trafficsign-detector.git
```
download trained <a href="https://drive.google.com/drive/folders/1FPkcCP3y8IlXdnIfEhIhx57hy6F7vCDI?usp=sharing">Models</a>, make a folder called "ckpt" and move the downloaded files into ckpt folder

#### Go into app's directory
``` bash
$ cd trafficsign-detector-master
```
#### Start the detection system
``` bash
$ python predict_video.py
```

#### Result Preview
a video will appear like the following image if successful

![image](https://user-images.githubusercontent.com/71715817/97081041-f122ec00-1629-11eb-95fc-33dcb806a0db.jpg)
