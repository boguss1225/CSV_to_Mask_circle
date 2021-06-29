# Import
import csv
from PIL import Image, ImageDraw
import os

# Generate color code base on input string
# With each string will generated only one color code


def hashCode(label):
    hash = 0
    for i in range(len(label)):
        hash = ord(label[i]) + ((hash << 5) - hash)
    return hash

def intToRGB(i):
    c = (i & 0x00FFFFFF)
    c = hex(c).lstrip('0x')
    c.upper()
    str = "00000"
    return str[0:6-len(c)] + c

# Draw dot
def drawDot(image, x, y, radius, label, imageHeight):
    # get dot color
    dotColor = "#" + intToRGB(hashCode(label))
    draw = ImageDraw.Draw(image)
    draw.ellipse((x-radius, y-radius, x+radius,
                 y+radius), fill=dotColor, outline=dotColor)


# Save previous row's file name
previousFileName = ""
# Check param for while loop: enter the csv path
checkEnterCSV = True
while(checkEnterCSV):
    # Enter the csv path from console
    csvPath = input("Enter the path of your csv file: ")
    if(os.path.isfile(csvPath)):
        checkEnterCSV = False

        # Check param for while loop: enter images path
        checkEnterImgPath = True
        while(checkEnterImgPath):
            # Enter path for save result images
            imagesPath = input(
                "Enter the path to the folder where you want to save the image: ")
            # If images path not exist
            if not os.path.isdir(imagesPath):
                confirmCreateImgPath = input(
                    "The path that you entered not exist, Do you want to create this link? (Y/N)")
                if confirmCreateImgPath == 'Y' or confirmCreateImgPath == 'y':
                    # Create path
                    os.mkdir(imagesPath)
                    checkEnterImgPath = False
                elif confirmCreateImgPath == 'N' or confirmCreateImgPath == 'n':
                    #Confirm: 'N' or 'n'
                    print("Your answer is 'no'. Please retype!")
                else:
                    # confirm with other character
                    print("Your answer is not valid!")
            else:
                # Entered images path right
                print(f'Your images path that you entered is: {imagesPath}')
                checkEnterImgPath = False

        # Open csv file
        with open(csvPath) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            # row_count = sum(1 for row in fileObject);
            for row in csv_reader:
                if line_count == 0:
                    print('Processing ...')
                    line_count += 1
                else:
                    print(
                        f'line {line_count}: images: {row[0]} with label: {row[1]}')
                    # Same file name
                    if(previousFileName == row[0]):
                        # open exist file
                        image = Image.open(imagesPath + '/'+row[0])
                        # Draw dot
                        drawDot(image, float(row[2]), float(row[3]),
                                float(row[4]), row[1], float(row[6]))
                        image.save(imagesPath+'/'+row[0])
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
                        drawDot(image, float(row[2]), float(row[3]),
                                float(row[4]), row[1], float(row[6]))
                        image.save(imagesPath+'/'+row[0])
                        line_count += 1
            print(f'Processed {line_count} lines.')
    else:
        print("Entered csv file not exist!")
