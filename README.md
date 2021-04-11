# CSVtoMask
This python code converts csv file into mask image file.

## Input Data
The input data (csv) consists of filename, label, x & y cordinates of label, radius of the label, framse size (Width & Height)
[IMPORTANT] THE INPUT DATA IS NEEDED TO BE SORTED BY FILENAME!!!\n
![picture](https://github.com/boguss1225/CSVtoMask/blob/main/screenshot/screenshot1.PNG)

## Running 
It can be run through terminal.\n
![picture](https://github.com/boguss1225/CSVtoMask/blob/main/screenshot/screenshot2.PNG)

## Output
The output will be a series of mask images which are created according to filename.
Each mask image is saved as the name of the designated filename.\n
![picture](https://github.com/boguss1225/CSVtoMask/blob/main/screenshot/screenshot3.PNG)
The file contains one to many labels which are circle shape in multiple locations within the image frame.
And the label is distinguishable by colour which is set inside of the code.
