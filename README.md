# jaws_calibration

primitive program with GUI to calibrate linac jaws by epid images (test on TrueBeam and TrueBeam STx)

1) first, create a gui *.py from qt designer *.ui:

pyuic6 ui.ui -o ui.py

2) then you can use it as is (python script) or try to convert as fully integrated .exe:

pyinstaller --onefile --windowed --icon=icon.ico jaws_analysis.py