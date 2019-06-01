import cv2
import dlib
import numpy as np
import time
from glob import glob
from sql import  *
#使用模型检测128个特征向量
def face_feature(image):
   detector = dlib.get_frontal_face_detector()
   landmark_predictor = dlib.shape_predictor('E:/shape_predictor_68_face_landmarks/shape_predictor_68_face_landmarks.dat')#dat 模型地址
   face_rec_model = dlib.face_recognition_model_v1('E:/dlib_face_recognition_resnet_model_v1.dat')
   face = detector(image,1)
   dist = []
   if (len(face) > 0):
    for k,d in enumerate(face):
        cv2.rectangle(image,(d.left(),d.top()),(d.right(),d.bottom()),(255,255,255))
        shape = landmark_predictor(image,d)
        face_descriptor = face_rec_model.compute_face_descriptor(image, shape)
        dist.append(list(face_descriptor))
        #在图中显示68个特征点的位置
        #for i in range(68):
        #   cv2.circle(image, (shape.part(i).x, shape.part(i).y),5,(0,255,0), -1, 8)
        #   cv2.putText(image,str(i),(shape.part(i).x,shape.part(i).y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,2555,255)
    return  dist      #如果检测不出则返回None

#欧式距离计算
def oshi_distance(dist1,dist2):
    try:
      dis = np.sqrt(np.sum(np.square(np.array(dist1) - np.array(dist2))))
      return dis
    except:
        return None

#获得脸部图片（测试用）
def get_face():
    cap = cv2.VideoCapture(0)
    while (1):
        ret, frame = cap.read()
        cv2.imshow("capture", frame)
        if cv2.waitKey(1) & 0xFF == 32:
            cv2.imwrite("face/st.jpg", frame)
            break
    cap.release()
    cv2.destroyAllWindows()

#获得时间
def get_time():
    time_format = '%Y-%m-%d  %X'
    a = time.strftime(time_format, time.localtime())
    return a

#加载图片名字（测试用）
def load_image():
    file_name = glob('C:/Users/DELL/PycharmProjects/aiprogram/image/*')
    file_name1= file_name[0][:45]+'/'+file_name[0][46:]
    return(file_name1)

#识别
def rec_face(dist):
 try:
    cnxn = con_sql()
    row=get_feature(cnxn)
    cd = []
    m=[]
    minindex=0
    for k in range(len(row)):
       a = row[k][3]
       ab = a.split(',')
       for i in range(0, 128):
          cd.append(float(ab[i]))
       asp = [cd]
       cd=[]
       mark=oshi_distance(asp,dist)
       m.append(mark)
    for i in range(len(m)):
         if (m[i]< m[minindex]):
            minindex=i
    if(m[minindex]>0.5):
        result= 0
    else:
        print("签到成功")
        result=[row[minindex][0],row[minindex][1],row[minindex][2],row[minindex][4]]
    return result
 except:
     print("error")
     return None
