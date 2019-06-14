# facerecognitionai

Simple Python Based Face Recognizer
Need to install dlib,face_recognition

# dlib
To Install dlib
Do the following

'''bash
sudo apt-get install build-essential cmake pkg-config
sudo apt-get install libx11-dev libatlas-base-dev
sudo apt-get install libgtk-3-dev libboost-python-dev
sudo apt-get install python-dev python-pip python3-dev python3-pip
sudo -H pip2 install -U pip numpy
sudo -H pip3 install -U pip numpy
'''

Compile dlib now..

'''bash
wget http://dlib.net/files/dlib-19.6.tar.bz2
tar xvf dlib-19.6.tar.bz2
cd dlib-19.6/
mkdir build
cd build
cmake ..
cmake --build . --config Release
sudo make install
sudo ldconfig
cd ..
'''

Install Python Modules
cd dlib-19.6
python setup.py install

# face_recognition
Install python face recognition module using

'''bash
pip install face_recognition
'''
