import json
import os

# 저장할 json파일 경로
json_path = "D:/mp/Capture0/annotations1.json"
original_cap = "D:/original/Capture0"


# 가져올 디렉토리의 폴더명
folders = os.listdir(original_cap)
folders_dir = [f for f in folders if os.path.isdir(os.path.join(original_cap, f))]
print(folders_dir)  
 
# original_cap 디렉토리 내의 첫 번째 폴더 선택
first_folder = folders_dir[0] if folders_dir else None
folder_path = os.path.join(original_cap, first_folder)

# 선택한 폴더 내에 있는 파일 목록 가져오기
files_in_first_folder = os.listdir(folder_path)

# 파일 수 확인
file_count = len(files_in_first_folder)



new_data = []

# 원본 JSON 데이터를 기반으로 수정
for i in range(file_count):  # cam0부터 cam3까지
    for cam in range(len(folders_dir)):  # image0부터 image2829까지
        # 파일 이름 및 카메라 값 설정
        file_name = f"cam{cam}/image{i}.jpg"
        camera = str(cam)
        
        # 새 항목 생성
        new_item = {
            "file_name": file_name,
            "subject": 0,
            "camera": camera,
            "2d_keypoints": []
        }
        
        # 새 항목을 리스트에 추가
        new_data.append(new_item)

# 수정된 데이터를 새 JSON 파일로 저장
with open(json_path, "w") as json_file:
    json.dump(new_data, json_file, indent=4)

