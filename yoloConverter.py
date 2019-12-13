from PIL import Image
import os

def convertToYolo(imgPath, label, subdir):
    fname = imgPath.split("/")[-1]

    with open("labels/"+subdir+"/"+fname.split(".")[0] + ".txt", "wt") as outfile:    
        outfile.write(str(label) + " 0 0 1 1")
    return


    THRESHOLD = 80

    im = Image.open(imgPath)
    pix = im.load()
    width, height = im.size


    data = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(pix[j, i])
        data.append(row)

    l = 10000
    r = -1
    t = 10000
    b = -1

    def isValid(pix, height, width, loci, locj):
        nonlocal THRESHOLD
        for i in range(-5, 5):
            for j in range(-5, 5):
                if (i+loci >= height or i+loci < 0 or j+locj < 0 or j+locj >= width): continue
                if (pix[locj+j, loci+i] < THRESHOLD): return False
        return True


    for i in range(height):
        for j in range(width):
            if (pix[j, i] > THRESHOLD and isValid(pix, height, width, i, j)): 
                l = min(l, j)
                r = max(r, j)
                b = max(b, i)
                t = min(t, i)

    objectWidth = min(r-l+20, width-l)
    objectHeight = min(height-t, b-t+20)
    x = (max(l-10, 0))
    y = (max(t-10, 0))

    midX = x + objectWidth/2
    midY = y + objectHeight/2
    fname = imgPath.split("/")[-1]
   # print(objectWidth, objectHeight, midX, midY)
    with open("labels/"+fname.split(".")[0] + ".txt", "wt") as outfile:    
        outfile.write(
            str(label) + " " + 
            str(float(midX/width)) + " " +
            str(float(midY/height)) + " " + 
            str(float(objectWidth/width)) + " " + 
            str(float(objectWidth/height))
        )  


folder = './jpg/data_c'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    convertToYolo(file_path, 0, 'data_c')


folder = './jpg/data_longhorn'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    convertToYolo(file_path, 1, 'data_longhorn')

folder = './jpg/data_palm'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    convertToYolo(file_path, 2, 'data_palm')

