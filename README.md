# jaws_calibration

This is the primitive program with GUI (pyQt6) that can perform linac jaws calibration using EPID-images (it was tested on TrueBeam and TrueBeam STx).

Some packages that you need: pydicom, pylinac, pyqt6, pyinstaller.

1) First, create a python gui-file (*.py) from qt designer form (*.ui):

$ pyuic6 ui.ui -o ui.py

2) Then you can use it as is (like python script) or try to build fully integrated binary execution file:

$ pyinstaller --onefile --windowed --icon=icon.ico jaws_analysis.py

3) it probably will not started, because you need to add this change this variable hiddenimports=[] to hiddenimports=['pydicom.encoders.gdcm','pydicom.encoders.pylibjpeg'] inside jaws_analysis.spec file.

4) Now use that command to rebuild binary:

$ pyinstaller jaws_analysis.spec

5) Ta-da! It works and you can test it using dicom images from data_test folder. Just browse inside this folder and push Analyze button.

P.S. Tested on Linux (WSL2 Ubuntu 22.04) and Windows 11 (Home 22H2).
