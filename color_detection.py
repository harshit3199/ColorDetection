import numpy as np
import pandas as pd
import argparse
import cv2

clicked = False
r = g = b = xpos = ypos = 0

#function to calculate minimum distance from all colors and get the most matching color from the csv 

def getColorName(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname


#function to get x,y coordinates of mouse double click

def draw_function(event, x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)



#Reading the colors.csv file using pandas

index=["color","color_name","hex","R","G","B"]
csv = pd.read_csv('colors2.csv', names=index, header=None,encoding= 'unicode_escape')


           
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_function)
f=0

#using opencv starting the camera

cap = cv2.VideoCapture(0)
while(1):
    
    #reading the images captures 

    _, img = cap.read()

    #if the user hits 'q' break out of the outer loop.
    if f==1:
        break
    while(1):
        
        
        #displaying the image frame captured

        cv2.imshow("image",img)
            
        if (clicked):

            #display the color with its values in hte top of the screen.

            cv2.rectangle(img,(20,20), (750,60), (b,g,r), -1)

            text = getColorName(r,g,b) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)

            cv2.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)

                #For very light colours we will display text in black colour

            if(r+g+b>=600):
                cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
                    
            clicked=False

            #Break the loop when user hits 'q' key and shut down video capturing    

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            f+=1
            break

        #break the loop and go to the next frame if the user hits 'n' key

        elif cv2.waitKey(1) & 0xFF == ord('n'):
            break
