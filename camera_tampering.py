#importing necessary libaries
import numpy as np
import cv2
#Video capturing starts
cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()
ret, frame = cap.read()
fgmask = fgbg.apply(frame)
kernel = np.ones((5,5), np.uint8)
from twilio.rest import Client

# Twilio account SID, Auth Token, and Twilio phone number
account_sid = 'AC659a709460c9b655a97ecfdceabc02bd'
auth_token = '053234457ea222b57258778cfb3d601c'
twilio_phone_number = '+15034069206'
sms_out=1
client = Client(account_sid, auth_token)

def send_sms(to, message):
    try:
        # Send the SMS
        message = client.messages.create(
            body=message,
            from_=twilio_phone_number,
            to=to
        )
        print(f"SMS sent successfully! SID: {message.sid}")
    except Exception as e:
        print(f"Error sending SMS: {str(e)}")

while(True):
    # global sms_out
    ret, frame = cap.read()
    if(frame is None):
        print("End of frame")
        break
    else:
        a = 0
        bounding_rect = []
        fgmask = fgbg.apply(frame)
        fgmask= cv2.erode(fgmask, kernel, iterations=5) 
        fgmask = cv2.dilate(fgmask, kernel, iterations = 5)
        cv2.imshow('frame',frame)
        
        contours,_ = cv2.findContours(fgmask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for i in range(0,len(contours)):
            bounding_rect.append(cv2.boundingRect(contours[i]))
        for i in range(0,len(contours)):
            if bounding_rect[i][2] >=40 or bounding_rect[i][3] >=40:
                a = a+(bounding_rect[i][2])*bounding_rect[i][3]
            if(a >=int(frame.shape[0])*int(frame.shape[1])/3):
                cv2.putText(frame,"TAMPERING DETECTED",(5,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),2)
                if sms_out==1:
                    recipient_number = '+916266114341'  # Replace with the recipient's phone number
                    sms_message = "Subject: Urgent: Possible Camera Tampering, Durga Nagar,CCTV No.454 in Durga Nagar, Vidisha, may be tampered. Addressing this swiftly is vital for community safety. Investigate promptly to ensure surveillance integrity. Contact us for more information.Sincerely SafeEye Studio"
                    send_sms(recipient_number, sms_message)
                    sms_out=0
            cv2.imshow('frame',frame)

               
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
#releasing camera and closing all the windows
cap.release()
cv2.destroyAllWindows()