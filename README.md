# jaws_calibration

primitive program with GUI to calibrate linac jaws by epid images (test on TrueBeam and TrueBeam STx)

packages that you need: pydicom, pylinac, pyqt6, pyinstaller

1) first, create a gui *.py from qt designer *.ui:

pyuic6 ui.ui -o ui.py

2) then you can use it as is (python script) or try to build fully integrated .exe:

pyinstaller --onefile --windowed --icon=icon.ico jaws_analysis.py

3) it probably will not started, because you need to add this things 'pydicom.encoders.gdcm','pydicom.encoders.pylibjpeg' into hiddenimports=[] inside jaws_analysis.spec file
4) then use that command:

pyinstaller jaws_analysis.spec

5) ta-da! it works ;)