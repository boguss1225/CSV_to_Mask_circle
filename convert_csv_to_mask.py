# Import
import csv
from PIL import Image, ImageDraw
import os

# Color definition
ECHINODERMS = 'red'
MOLLUSCS = 'green'
FISH = 'orange'
WORMS = 'yellow'
CRUSTACEA = 'blue'

# Get color by label
# strip() : label string from csv file may have \n


def getColorByLabel(label):
    if label.strip() == 'Echinoderms':
        return ECHINODERMS
    elif label.strip() == 'Molluscs':
        return MOLLUSCS
    elif label.strip() == 'Fish':
        return FISH
    elif label.strip() == 'Worms':
        return WORMS
    else:
        return CRUSTACEA

# Draw dot


def drawDot(x, y, radius, label, imageHeight):
    dotColor = getColorByLabel(label)
    draw = ImageDraw.Draw(image)
    draw.ellipse((x-radius, imageHeight-(y+radius), x+radius,
                 imageHeight-y+radius), fill=dotColor, outline=dotColor)


# Create folder images if not exist
IMG_PATH = "images/"
if not os.path.exists(IMG_PATH):
    os.makedirs(IMG_PATH)
# Save previous row's file name
previousFileName = ""
# Open csv file
with open('testcsv.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    # row_count = sum(1 for row in fileObject);
    for row in csv_reader:
        if line_count == 0:
            print('Processing ...')
            line_count += 1
        else:
            # Same file name
            if(previousFileName == row[0]):
                # open exist file
                image = Image.open(IMG_PATH+row[0])
                # Draw dot
                drawDot(float(row[2]), float(row[3]),
                        float(row[4]), row[1], float(row[6]))
                image.save(IMG_PATH+row[0])
                line_count += 1
            # Different file name
            else:
                # Save the current filename to check if the filename matches in the next loop
                previousFileName = row[0]
                # Create image
                imgWidth = int(row[5])
                imgHeight = int(row[6])
                image = Image.new('RGB', (imgWidth, imgHeight))
                # Draw dot
                drawDot(float(row[2]), float(row[3]),
                        float(row[4]), row[1], float(row[6]))
                image.save(IMG_PATH+row[0])
                line_count += 1
    print(f'Processed {line_count} lines.')
