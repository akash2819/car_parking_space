import cv2   #till 24 min
import pickle

width,height=107,48
try:
    with open('CarParkPos','rb') as f:
        posList=pickle.loads(f)
except:
    posList= []
    
path="Assets/carParkImg.png"
# print(img.shape)

#get mouse click
def mouseClick(events,x,y,flags,params):
    if events==cv2.EVENT_LBUTTONDOWN:
        posList.append((x,y))
    if events==cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1=pos    
            if x1 <x < x1 + width and y1 <y < y1+height:
                posList.pop(i)

    with open('CarParkPos','wb') as f:
        pickle.dump(posList,f)

while True:
    img=cv2.imread(path)

    for pos in posList:
        cv2.rectangle(img,pos,(pos[0]+width,pos[1]+height),(255,43,67),2)

    cv2.imshow("parking",img)
    cv2.setMouseCallback("parking",mouseClick)
    cv2.waitKey(1)
    # if cv2.waitKey(1) & 0xff==ord('q'):
    #      break
