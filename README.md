<h1>Convolutional Neural Network</h1>

This is a Convolutional Neural Network that was made to recongise hand written numbers from paint. This was for my school project and something I built for fun using Python.

<h1>Things you will need:</h1>

<ol>
<li>Python 3.6+</li>
<li>Nvidia GPU: Any GPU from NVidia that use GForce Experience should sufficent. AMD cards is not supported by Tensorflow</li>
<li>Tensorflow and Tensorflow GPU (Tensorflow GPU needs a NVidia GPU to work)*</li>
<li>CuDA **For Tensorflow GPU**</li>
<li>Keras</li>
<li>OpenCV</li>
<li>Numpy</li>
<li>Matplotlib</li>
<li>Pycharm as IDE</li>
</ol>

<h1> How to install? </h1>

Installing can be complicated.

**PYTHON 2.0 TO 3.5 IS NOT SUPPORTED. ONLY PYTHON 3.6+ IS SUPPORTED**

To install Python 3.8+, Refer to this link. [Installation Guide](https://www.python.org/downloads/)

To install Tensorflor with Keras, Refer to this Link. [Installation Guide](https://www.youtube.com/watch?v=O8yye2AHCOk&t)

To install Pycharm, Refer to this link. [Installation guide](https://www.youtube.com/watch?v=s-wjHkoQGPs)

To install Numpy, you can install it in Anaconda or Python Terminal with the command: `pip install numpy`
If you have problems installing Numpy, Refer to this link. [Installation Guide](https://numpy.org/install/)

To install OpenCV, you can install it in Anaconda or Python Terminal with the command: `pip install opencv-python`
If you have problems installing OpenCV, Refer to this link. [Installation Guide](https://pypi.org/project/opencv-python/)

To Install Matplotlib, you can install it in Anaconda or Python Terminal with the command `python -m pip install -U matplotlib`
If you have problems installing Matplotlib, Refer to thus link. [Installation Guide](https://matplotlib.org/stable/users/installing.html)

To install Tensorflow and Tensorflow GPU, Please refer to these links that would be the easiest for you. **PLEASE BE PATIENT** It can be hard to get it working.

<br>**Please do note that: You must have Nvidia GPU to run this. Will not work without it. Trust me, I tried.**</br>
<br>**Choose any of the following videos that works best for mental health because you will lose 99% of your braincells overthis:**</br>
<br>[Installing Tensorflow and GPU at the same time](https://www.youtube.com/watch?v=5Ym-dOS9ssA) </br>
<br>[Installing Tensorflow GPU in 5 Minutes](https://www.youtube.com/watch?v=tPq6NIboLSc&t)</br>
<br>[Installing Tensorflow-GPU with a single line](https://www.youtube.com/watch?v=_UCn7EJYdA4)</br>
<br>[Installing Tensorflow and Keras GPU Support-Cuda GPU Setup](https://www.youtube.com/watch?v=IubEtS2JAiY)</br>
<br>[Installing Tensorflow and Keras GPU support for Windows and Anaconda](https://www.youtube.com/watch?v=Ebo8BklTtmc)</br>





<h1> What you need to change </h1>

**THE ONLY THING YOU NEED TO CHANGE IN THE CODE FOR IT TO RUN IS LINE 51:**

`img = cv.imread(fr'C:\Users\Eric\PycharmProjects\pythonProject2\test.model\{x}.png', cv.IMREAD_GRAYSCALE)`

**CHANGE THE DIRECTORY PATH OF WHERE THE IMAGES IS IN THE FOLDER. DO NOT REMOVE THE {x}.png.**

For Example:

`img = cv.imread(fr'C:\Users\DIRECTORYFILETOTHEIMAGES\{x}.png', cv.IMREAD_GRAYSCALE)`

This allows the loop in line 50 to go through every single picture in the directory instead of manually running the code each time just to test one sample picture. 

<h1> Known Bugs </h1>

Current bugs 5/10/2021

<ol>
	<li>100% Failure Prediction on number 6.</li>
	<li>100% Failure Prediction on number 7.</li>
	<li>100% Failure Prediction on number 9.</li>
</ol>

<h1>Updates</h1>

Update on 5/16/2021:
<ol>
	<li> Added extra layer of Conv2D with the filter of 128.</li>
	<li> Decreases 100% Failure Prediction on number 6,7,9 to a 90% Failure Prediction </li>
	<li> The update might be small but this means the network can be improved to read these numbers</li>
</ol>

**Theory on the update:**

My theory on why the numbers 6 and 9 are not being predicted well enough because the network is not able to match the circle shape from the 6 and 9. 

Adding an extra layer of Conv2D with filters of 128 was able to predict these numbers now with a 10% precent chance. 

This means the structure of the layers can be improved somewhere or have more samples for the network to train on.

Problem is that when added another layer with 128 filters, it drastically got slower by two times. Also, it could reach to overfitting. So will needs more testing to see.


<h1> Do note that: </h1>

VERY CPU AND GPU INTENSIVE. SO YOUR COMPUTER MIGHT RUN SLOW THAT IS NORMAL. NUREON NETWORK ARE VERY HARSH ON THE COMPUTER UNLESS YOU HAVE CERTAIN PARTS THAT WAS BUILT FOR IT.
