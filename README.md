# Simple-CNN-Number-Hand-Written-Recongition-
A simple CNN network that predicts hand written numbers from paint.


This is a Convolutional Neural Network that was made to recongise hand written numbers from paint. This was for my school project and something I built for fun using Python.

**YOU WILL NEED THE FOLLOWING THINGS TO USE THIS (**You can use Anaconda to install these libaries for python using the "pip install --" function.**):

Python 3.8 
Tensorflow and Tensorflow GPU (Tensorflow GPU needs a NVidia GPU to work)
Keras 
OpenCV
Numpy
Matplotlib
Pycharm as IDE


**THE ONLY THING YOU NEED TO CHANGE IN THE CODE FOR IT TO RUN IS LINE 51:

img = cv.imread(fr'C:\Users\Eric\PycharmProjects\pythonProject2\test.model\{x}.png', cv.IMREAD_GRAYSCALE)

CHANGE THE DIRECTORY PATH OF WHERE THE IMAGES IS IN THE FOLDER. DO NOT REMOVE THE {x}.png.

This allows the loop in line 50 to go through every single picture in the directory instead of manually running the code each time just to test one sample picture. 

**Bugs:**

Have a 100% prediction on the number 6, 7, and 9.

**PLEASE DO NOTE:**
VERY CPU AND GPU INTENSIVE. SO YOUR COMPUTER MIGHT RUN SLOW THAT IS NORMAL. NUREON NETWORK ARE VERY HARSH ON THE COMPUTER UNLESS YOU HAVE CERTAIN PARTS THAT WAS BUILT FOR IT.
