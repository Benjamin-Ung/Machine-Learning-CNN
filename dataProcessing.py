import os, cv2
from sklearn.utils import shuffle

def getData():
    edible = []
    poisonous = []
    dataset = []
    key = []
    path = 'dataset/Edible/'
    fileList = os.listdir(path)

    #read in edible dataset
    for image in fileList:
        sample = cv2.imread(path + image)
        edible.append(sample)

    #print(img.shape)
    # cv2.imshow("image", edible[10])
    # cv2.waitkey(0)'

    print("there should be 1473 images in edible: " + len(edible))

    #Reading in data from poisonous dataset
    path = 'dataset/Poisonous/'
    fileList = os.listdir(path)
    #read in dataset as a [n][2] array. 
    for image in fileList:
        sample = cv2.imread(path + image)
        poisonous.append(sample)

    print("there should be 527 images in poisonous: " + len(poisonous))

    key.append(1*len(edible))
    key.append(0*len(poisonous))

    dataset = edible.append(poisonous)
    shuffle(dataset, key)

    return dataset, key