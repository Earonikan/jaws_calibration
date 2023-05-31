import sys
import math
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import QFileDialog
from ui import Ui_mainWindow

import pydicom
import numpy as np
#import matplotlib.pyplot as plt
from scipy import ndimage

# PYLINAC ANALYSIS
from pylinac import FieldAnalysis
#from pylinac import TrajectoryLog
#from pylinac import load_log

try:
    # Include in try/except block if you're also targeting Mac/Linux
    from PyQt6.QtWinExtras import QtWin
    myappid = 'mycompany.myproduct.subproduct.version'
    QtWin.setCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass

class MyWidget(QMainWindow, Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_browse.clicked.connect(self.browse)
        self.pushButton_browse_2.clicked.connect(self.browse_2)
        self.pushButton_analyze.clicked.connect(self.run)
        #self.radioButton_1.toggled.connect(self.onClicked_1)
        #self.radioButton_2.toggled.connect(self.onClicked_2)

        self.inAction = False
        self.action = ""

    def browse(self):
        dialog = QFileDialog()
        fname = dialog.getExistingDirectory(self, 'Select a directory')
        self.DirectoryLine.setText(fname)

    def browse_2(self):
        dialog = QFileDialog()
        fname = dialog.getOpenFileName(self, 'Open File', './',)[0]
        self.DirectoryLine_2.setText(fname)

        
        if self.radioButton_1.isChecked():

            my_img = FieldAnalysis(path=fname)
            my_img.analyze()
            my_img.vert_profile.field_data
            data = my_img.results_data()

            self.X1_5x5_2.setText(str(data.cax_to_left_mm))
            self.X2_5x5_2.setText(str(data.cax_to_right_mm))
            self.Y1_5x5_2.setText(str(data.cax_to_bottom_mm))
            self.Y2_5x5_2.setText(str(data.cax_to_top_mm))

        if self.radioButton_2.isChecked():
            
            data = result_dcm(fname)
            data.calculate()
            self.X1_5x5_2.setText(str(round(data.getX1()*10)/10))
            self.X2_5x5_2.setText(str(round(data.getX2()*10)/10))
            self.Y1_5x5_2.setText(str(round(data.getY1()*10)/10))
            self.Y2_5x5_2.setText(str(round(data.getY2()*10)/10))        
            
    def run(self):

        X1x = np.zeros((5))
        X1y = np.zeros((5))
        X2x = np.zeros((5))
        X2y = np.zeros((5))
        Y1x = np.zeros((5))
        Y1y = np.zeros((5))
        Y2x = np.zeros((5))
        Y2y = np.zeros((5))

        if self.radioButton_1.isChecked():

            #5x5
            fname = self.DirectoryLine.text()+"/SSD100_5x5.dcm"
            my_img = FieldAnalysis(path=fname)
            my_img.analyze()
            my_img.vert_profile.field_data
            data = my_img.results_data()

            X1x[0] = data.cax_to_left_mm
            X1y[0] = self.X1_5x5.text()
            X2x[0] = data.cax_to_right_mm
            X2y[0] = self.X2_5x5.text()
            Y1x[0] = data.cax_to_bottom_mm
            Y1y[0] = self.Y1_5x5.text()
            Y2x[0] = data.cax_to_top_mm
            Y2y[0] = self.Y2_5x5.text()

            self.progressBar.setValue(20)

            #10x10
            fname = self.DirectoryLine.text()+"/SSD100_10x10.dcm"
            my_img = FieldAnalysis(path=fname)
            my_img.analyze()
            my_img.vert_profile.field_data
            data = my_img.results_data()

            X1x[1] = data.cax_to_left_mm
            X1y[1] = self.X1_10x10.text()
            X2x[1] = data.cax_to_right_mm
            X2y[1] = self.X2_10x10.text()
            Y1x[1] = data.cax_to_bottom_mm
            Y1y[1] = self.Y1_10x10.text()
            Y2x[1] = data.cax_to_top_mm
            Y2y[1] = self.Y2_10x10.text()

            self.progressBar.setValue(40)

            #15x15
            fname = self.DirectoryLine.text()+"/SSD100_15x15.dcm"
            my_img = FieldAnalysis(path=fname)
            my_img.analyze()
            my_img.vert_profile.field_data
            data = my_img.results_data()

            X1x[2] = data.cax_to_left_mm
            X1y[2] = self.X1_15x15.text()
            X2x[2] = data.cax_to_right_mm
            X2y[2] = self.X2_15x15.text()
            Y1x[2] = data.cax_to_bottom_mm
            Y1y[2] = self.Y1_15x15.text()
            Y2x[2] = data.cax_to_top_mm
            Y2y[2] = self.Y2_15x15.text()

            self.progressBar.setValue(60)

            #20x20
            fname = self.DirectoryLine.text()+"/SSD100_20x20.dcm"
            my_img = FieldAnalysis(path=fname)
            my_img.analyze()
            my_img.vert_profile.field_data
            data = my_img.results_data()

            X1x[3] = data.cax_to_left_mm
            X1y[3] = self.X1_20x20.text()
            X2x[3] = data.cax_to_right_mm
            X2y[3] = self.X2_20x20.text()
            Y1x[3] = data.cax_to_bottom_mm
            Y1y[3] = self.Y1_20x20.text()
            Y2x[3] = data.cax_to_top_mm
            Y2y[3] = self.Y2_20x20.text()

            self.progressBar.setValue(80)

            #25x25
            fname = self.DirectoryLine.text()+"/SSD100_25x25.dcm"
            my_img = FieldAnalysis(path=fname)
            my_img.analyze()
            my_img.vert_profile.field_data
            data = my_img.results_data()

            X1x[4] = data.cax_to_left_mm
            X1y[4] = self.X1_25x25.text()
            X2x[4] = data.cax_to_right_mm
            X2y[4] = self.X2_25x25.text()
            Y1x[4] = data.cax_to_bottom_mm
            Y1y[4] = self.Y1_25x25.text()
            Y2x[4] = data.cax_to_top_mm
            Y2y[4] = self.Y2_25x25.text()   


            par = np.polyfit(X1x,X1y,1)
            self.X1_1cm.setText(str(round(par[1]+10*par[0])))
            self.X1_19cm.setText(str(round(par[1]+190*par[0])))
            par = np.polyfit(X2x,X2y,1)
            self.X2_1cm.setText(str(round(par[1]+10*par[0])))
            self.X2_19cm.setText(str(round(par[1]+190*par[0])))
            par = np.polyfit(Y1x,Y1y,1)
            self.Y1_1cm.setText(str(round(par[1]+10*par[0])))
            self.Y1_19cm.setText(str(round(par[1]+190*par[0])))
            par = np.polyfit(Y2x,Y2y,1)
            self.Y2_1cm.setText(str(round(par[1]+10*par[0])))
            self.Y2_19cm.setText(str(round(par[1]+190*par[0])))

            self.progressBar.setValue(100)

        if self.radioButton_2.isChecked():

            #5x5
            fname = self.DirectoryLine.text()+"/SSD100_5x5.dcm"
            data = result_dcm(fname)
            data.calculate() 
            X1x[0] = data.getX1()
            X1y[0] = self.X1_5x5.text()
            X2x[0] = data.getX2()
            X2y[0] = self.X2_5x5.text()
            Y1x[0] = data.getY1()
            Y1y[0] = self.Y1_5x5.text()
            Y2x[0] = data.getY2()
            Y2y[0] = self.Y2_5x5.text()

            self.progressBar.setValue(20)

            #10x10
            fname = self.DirectoryLine.text()+"/SSD100_10x10.dcm"
            data = result_dcm(fname)
            data.calculate() 
            X1x[1] = data.getX1()
            X1y[1] = self.X1_10x10.text()
            X2x[1] = data.getX2()
            X2y[1] = self.X2_10x10.text()
            Y1x[1] = data.getY1()
            Y1y[1] = self.Y1_10x10.text()
            Y2x[1] = data.getY2()
            Y2y[1] = self.Y2_10x10.text()

            self.progressBar.setValue(40)

            #15x15
            fname = self.DirectoryLine.text()+"/SSD100_15x15.dcm"
            data = result_dcm(fname)
            data.calculate() 
            X1x[2] = data.getX1()
            X1y[2] = self.X1_15x15.text()
            X2x[2] = data.getX2()
            X2y[2] = self.X2_15x15.text()
            Y1x[2] = data.getY1()
            Y1y[2] = self.Y1_15x15.text()
            Y2x[2] = data.getY2()
            Y2y[2] = self.Y2_15x15.text()

            self.progressBar.setValue(60)

            #20x20
            fname = self.DirectoryLine.text()+"/SSD100_20x20.dcm"
            data = result_dcm(fname)
            data.calculate() 
            X1x[3] = data.getX1()
            X1y[3] = self.X1_20x20.text()
            X2x[3] = data.getX2()
            X2y[3] = self.X2_20x20.text()
            Y1x[3] = data.getY1()
            Y1y[3] = self.Y1_20x20.text()
            Y2x[3] = data.getY2()
            Y2y[3] = self.Y2_20x20.text()

            self.progressBar.setValue(80)

            #25x25
            fname = self.DirectoryLine.text()+"/SSD100_25x25.dcm"
            data = result_dcm(fname)
            data.calculate() 
            X1x[4] = data.getX1()
            X1y[4] = self.X1_25x25.text()
            X2x[4] = data.getX2()
            X2y[4] = self.X2_25x25.text()
            Y1x[4] = data.getY1()
            Y1y[4] = self.Y1_25x25.text()
            Y2x[4] = data.getY2()
            Y2y[4] = self.Y2_25x25.text()   

            #Results
            par = np.polyfit(X1x,X1y,1)
            self.X1_1cm.setText(str(round(par[1]+10*par[0])))
            self.X1_19cm.setText(str(round(par[1]+190*par[0])))
            par = np.polyfit(X2x,X2y,1)
            self.X2_1cm.setText(str(round(par[1]+10*par[0])))
            self.X2_19cm.setText(str(round(par[1]+190*par[0])))
            par = np.polyfit(Y1x,Y1y,1)
            self.Y1_1cm.setText(str(round(par[1]+10*par[0])))
            self.Y1_19cm.setText(str(round(par[1]+190*par[0])))
            par = np.polyfit(Y2x,Y2y,1)
            self.Y2_1cm.setText(str(round(par[1]+10*par[0])))
            self.Y2_19cm.setText(str(round(par[1]+190*par[0])))

            self.progressBar.setValue(100)
            
            
class result_dcm:

    def __init__(self, fname):
        self.name=fname
        self.X1 = 0
        self.X2 = 0
        self.Y1 = 0
        self.Y2 = 0

    def getX1(self):
        return self.X1
    
    def getX2(self):
        return self.X2
    
    def getY1(self):
        return self.Y1
    
    def getY2(self):
        return self.Y2

    def calculate(self):

        data = pydicom.dcmread(self.name).pixel_array
        col = data.shape[0]//2;
        sizeF = 10
        eps = 5
        pix_size = 0.333
        ssd = int(pydicom.dcmread(self.name).RTImageSID/10)

        c = ndimage.median_filter(data, size=sizeF)
        a = np.max(c)
        pos = np.argmax(c)
        posY = pos//c.shape[0]
        posX = pos%c.shape[0]
        maxv = np.mean(c[posY-eps:posY+eps,posX-eps:posX+eps])

        x1 = 0
        while c[posY,x1] < maxv/2:
            x1+=1
        x2 = x1
        while c[posY,x2] > maxv/2:
            x2+=1
        y1 = 0
        while c[y1,posX] < maxv/2:
            y1+=1
        y2 = y1
        while c[y2,posX] > maxv/2:
            y2+=1

        self.Y1=(col-y1+1)*pix_size*100/ssd
        self.Y2=(y2-col-1)*pix_size*100/ssd
        self.X1=(col-x1+1)*pix_size*100/ssd
        self.X2=(x2-col-1)*pix_size*100/ssd

        

app = QApplication(sys.argv)
app.setWindowIcon(QtGui.QIcon('icon1.ico'))
ex = MyWidget()
ex.show()
sys.exit(app.exec())
