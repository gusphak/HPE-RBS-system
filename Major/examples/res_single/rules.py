import json

from matplotlib import image
from matplotlib import pyplot as plt  
image_data = image.imread('/content/gdrive/MyDrive/Alphapose/AlphaPose/examples/demo_single/coveringnosewithbothhands.jpg')

f = open('alphapose-results.json',)
data = json.load(f)


data = data[0]['keypoints']
coordinates = []
scores = []
c = 0
temp_coordinates = []
for temp in data:
    if c%3 == 0:
        temp_coordinates.append(temp)
    elif c%3 == 1:
        temp_coordinates.append(temp)
        #print(temp_coordinates)
        coordinates.append(temp_coordinates)
    else:
        temp_coordinates = []
        scores.append(temp)
        
    c=c+1
    
#print(coordinates)
#print(scores)
f.close()

Nose = coordinates[0]
LEye = coordinates[1]
REye = coordinates[2]
LEar = coordinates[3]
REar = coordinates[4]
LShoulder = coordinates[5]
RShoulder = coordinates[6]
RWrist = coordinates[10]
LElbow = coordinates[7]
RElbow = coordinates[8]
LWrist = coordinates[9]
LHip = coordinates[11]
RHip = coordinates[12]
LKnee = coordinates[13]
RKnee =coordinates[14]
LAnkle = coordinates[15]
RAnkle = coordinates[16]
print(LAnkle)

plt.plot( Nose[0], Nose[1], marker = 'v', color ="white")
plt.plot( LEye[0], LEye[1], marker = 'v', color ="white")
plt.plot( REye[0], REye[1], marker = 'v', color ="white")
plt.plot( LEar[0], LEar[1], marker = 'v', color ="white")
plt.plot( REar[0], REar[1], marker = 'v', color ="white")
plt.plot( LShoulder[0], LShoulder[1], marker = 'v', color ="white")
plt.plot( RShoulder[0], RShoulder[1], marker = 'v', color ="white")
plt.plot( LElbow[0], LElbow[1], marker = 'v', color ="white")
plt.plot( RElbow[0], RElbow[1],  marker = 'v', color ="white")
plt.plot( LWrist[0], LWrist[1], marker = 'v', color ="white")
plt.plot( RWrist[0], RWrist[1], marker = 'v', color ="white")
plt.plot( LHip[0], LHip[1], marker = 'v', color ="white")
plt.plot( RHip[0], RHip[1], marker = 'v', color ="white")
plt.plot( LKnee[0], LKnee[1], marker = 'v', color ="white")
plt.plot( RKnee[0], RKnee[1], marker = 'v', color ="white")
plt.plot( LAnkle[0], LAnkle[1], marker = 'v', color ="white")
plt.plot( RAnkle[0], RAnkle[1], marker = 'v', color ="white")

plt.axis('off')
plt.imshow(image_data)
plt.show()
