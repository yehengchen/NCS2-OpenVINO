# Install OpenVINO™ toolkit for Raspbian* OS 
### [OpenVINO toolkit](https://docs.openvinotoolkit.org/latest/_docs_install_guides_installing_openvino_raspbian.html#install-package)

#### openvino_toolkit_raspbi_p_2019.1.094.tgz - [[download]](https://download.01.org/opencv/2019/openvinotoolkit/)
Open the Terminal* or your preferred console application.

#### 1.Go to the directory in which you downloaded the OpenVINO toolkit. This document assumes this is your ~/Downloads directory. If not, replace 
    
    ~/Downloads with the directory where the file is located.
    cd ~/Downloads/

#### 2.By default, the package file is saved as l_openvino_toolkit_raspbi_p_<version>.tgz.
Create an installation folder.
    
    sudo mkdir -p /opt/intel/openvino
  
#### 3.Unpack the archive: 
    
    sudo tar -xf l_openvino_toolkit_raspbi_p_<version>.tgz --strip 1 -C /opt/intel/openvino
    
   
