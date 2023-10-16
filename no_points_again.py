import cv2
import mediapipe as mp
import os
import glob
import pandas as pd
import json

mp_drawing = mp.solutions.drawing_utils #점으로 손가락 마디 표시
mp_hands = mp.solutions.hands # 미디어 파이프의 손 모델 초기화
mp_drawing_styles = mp.solutions.drawing_styles

# 가져올 json파일
path = "D:/mp/Capture0/annotations.json"
# 이미지 저장할 디렉토리
output_dir = 'D:/mp/Capture0/images'
# 가져올 이미지 파일
input_dir = 'D:/original/Capture0'

# 가져올 디렉토리의 폴더명
folders = os.listdir(input_dir)
folders_dir = [f for f in folders if os.path.isdir(os.path.join(input_dir, f))] # ['cam0', 'cam1', 'cam2', 'cam3']
 
# input_dir 디렉토리 내의 첫 번째 폴더 선택
first_folder = folders_dir[0] if folders_dir else None
folder_path = os.path.join(input_dir, first_folder)

# 선택한 폴더 내에 있는 파일 목록 가져오기
files_in_first_folder = os.listdir(folder_path)

                
with open(path, "r") as json_file:
    data = json.load(json_file)
    

with mp_hands.Hands(
    model_complexity=0, #모델 복잡성은 0 또는 1. 랜드마크 정확도와 추론 지연 시간은 모델 복잡성과 함께 증가. 기본값은 1
    min_detection_confidence=0.5, #최소 탐지 신뢰도. 탐지가 성공한 것으로 간주되는 손 감지 모델의 최소 신뢰 값([0.0, 1.0]). 기본값은 0.5
    min_tracking_confidence=0.5) as hands:
    
    
    for frame_data in data: # {'file_name': 'cam0/image0.jpg', 'subject': 0, 'camera': '0', '2d_keypoints': []} 
        if not frame_data['2d_keypoints']:

            file_name = frame_data['file_name'] # cam2/image2828.jpg
            image_filename = os.path.join(output_dir, file_name)


            # 이미지를 읽어 들이고
            image = cv2.imread(os.path.join(input_dir, file_name))
        
            # 작업 전에 BGR 이미지를 RGB로 변환합니다.
            results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            # result.multi_hand_landmarks[0] : 0번째 이미지의 0~20번까지 x, y좌표,
            
            joints = []

            # 결과에서 손의 랜드마크 얻기
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                                    image,
                                    hand_landmarks,
                                    mp_hands.HAND_CONNECTIONS,
                                    mp_drawing_styles.get_default_hand_landmarks_style(), # 포인트
                                    mp_drawing_styles.get_default_hand_connections_style()) # 선
                                    
                    # 이미지 저장
                    image_filename = os.path.join(output_dir, file_name)
                    cv2.imwrite(image_filename, image)
                    
                    # 좌표 추출
                    for lm in hand_landmarks.landmark:
                        cx, cy = lm.x, lm.y
                        joints.append([cx, cy]) # [0.0, 1.0]. 만일 정수로 하고싶을 경우 cx*image_width, cy*image_height
                        #print(joint) #0번 랜드마크의 [x, y]

            frame_data['2d_keypoints'] = joints



            
with open(path, 'w', encoding='utf-8') as make_file:
    json.dump(data, make_file, indent='\t')
    
print("저장완료")