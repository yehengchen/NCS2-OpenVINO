# Install OpenVINO™ toolkit for Raspbian* OS 
### [OpenVINO toolkit](https://docs.openvinotoolkit.org/latest/_docs_install_guides_installing_openvino_raspbian.html#install-package)

#### openvino_toolkit_raspbi_p_2019.1.094.tgz - [[download]](https://download.01.org/opencv/2019/openvinotoolkit/)

#### Open the Terminal* or your preferred console application.

#### 1. Go to the directory in which you downloaded the OpenVINO toolkit. This document assumes this is your ~/Downloads directory. If not, replace 
    
    ~/Downloads with the directory where the file is located.
    cd ~/Downloads/

#### 2. By default, the package file is saved as l_openvino_toolkit_raspbi_p_<version>.tgz.
Create an installation folder.
    
    sudo mkdir -p /opt/intel/openvino
  
#### 3. Unpack the archive: 
    
    sudo tar -xf l_openvino_toolkit_raspbi_p_<version>.tgz --strip 1 -C /opt/intel/openvino
    
#### 4. Modify the setupvars.sh script by replacing <INSTALLDIR> with the absolute path to the installation folder:
    
    sudo sed -i "s|<INSTALLDIR>|/opt/intel/openvino|" /opt/intel/openvino/bin/setupvars.sh

## Install External Software Dependencies
#### CMake* version 3.7.2 or higher is required for building the Inference Engine sample application. To install, open a Terminal* window and run the following command: 
    
    sudo apt install cmake
    
## Set the Environment Variables

#### You must update several environment variables before you can compile and run OpenVINO toolkit applications. Run the following script to temporarily set the environment variables:

    source /opt/intel/openvino/bin/setupvars.sh

#### (Optional) The OpenVINO environment variables are removed when you close the shell. As an option, you can permanently set the environment variables as follows:

    echo "source /opt/intel/openvino/bin/setupvars.sh" >> ~/.bashrc

#### To test your change, open a new terminal. You will see the following:

    [setupvars.sh] OpenVINO environment initialized

#### Continue to the next section to add USB rules for Intel® Movidius™ Neural Compute Stick and Intel® Neural Compute Stick 2 devices.

## Add USB Rules
#### 1. Add the current Linux user to the users group:
    
    sudo usermod -a -G users "$(whoami)"

#### Log out and log in for it to take effect.
    
#### 2. To perform inference on the Intel® Movidius™ Neural Compute Stick or Intel® Neural Compute Stick 2, install the USB rules running the install_NCS_udev_rules.sh script:
    
    sh /opt/intel/openvino/install_dependencies/install_NCS_udev_rules.sh

#### You are ready to compile and run the Object Detection sample to verify the Inference Engine installation.

## Build and Run Object Detection Sample

### Follow the next steps to run pre-trained Face Detection network using Inference Engine samples from the OpenVINO toolkit.
#### 1. Navigate to a directory that you have write access to and create a samples build directory. This example uses a directory named build:
    
    mkdir build && cd build

#### 2. Build the Object Detection Sample:
    cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_FLAGS="-march=armv7-a" /opt/intel/openvino/deployment_tools/inference_engine/samples
    make -j2 object_detection_sample_ssd
    
#### 3. Download the pre-trained Face Detection model or copy it from the host machine:

* To download the .bin file with weights:
        
        wget --no-check-certificate https://download.01.org/opencv/2019/open_model_zoo/R1/models_bin/face-detection-adas-0001/FP16/face-detection-adas-0001.bin
    
* To download the .xml file with the network topology:
    
        wget --no-check-certificate https://download.01.org/opencv/2019/open_model_zoo/R1/models_bin/face-detection-adas-0001/FP16/face-detection-adas-0001.xml
        
#### 4. Run the sample with specifying the model and a path to the input image:

    ./armv7l/Release/object_detection_sample_ssd -m face-detection-adas-0001.xml -d MYRIAD -i <path_to_image>

## Run Inference of Face Detection Model Using OpenCV* API

To validate OpenCV* installation, run the OpenCV deep learning module with the Inference Engine backend. Here is a Python* sample, which works with the pre-trained Face Detection model:

#### 1. Download the pre-trained Face Detection model or copy it from a host machine:
* To download the .bin file with weights:
        
        wget --no-check-certificate https://download.01.org/opencv/2019/open_model_zoo/R1/models_bin/face-detection-adas-0001/FP16/face-detection-adas-0001.bin
 
* To download the .xml file with the network topology:
        
        wget --no-check-certificate https://download.01.org/opencv/2019/open_model_zoo/R1/models_bin/face-detection-adas-0001/FP16/face-detection-adas-0001.xml
    
### 2. Create a new Python* file named as openvino_fd_myriad.py and copy the following script [[here]](https://github.com/yehengchen/NCS2-OpenVINO/blob/master/openvino_fd_myriad.py)
### 3. Run the script:

    python3 openvino_fd_myriad.py
    
 

