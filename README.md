# Handpose estimate
MediaPipe란 구글에서 제공하는 AI 프레임워크로서, 비디오형식 데이터를 이용한 다양한 비전 AI 기능을 파이프라인 형태로 손쉽게 사용할 수 있도록 제공된다.  

인체를 대상으로 하는 detect(인식)에 대해서 얼굴인식, 포즈, 객체감지, 모션트레킹 등 다양한 형태의 기능과 모델을 제공하는 프레임워크이다.  
![img1 daumcdn](https://github.com/dmswneunju/handpose/assets/109281949/78d36265-cff4-4285-9d92-8753ef68090c)

AI 모델개발 및 수많은 데이터셋을 이용한 학습도 마친 상태로 제공되므로 라이브러브 불러 사용하듯이 간편하게 호출하여 사용하기만 하면 되는 형태로 비전 AI 기능을 개발할 수 있다.   

## 코드 요약
json파일을 불러와 손 이미지의 x, y 좌표, width, height를 추출하였다.

---
### 다양한 Pose Estimation API
대표적으로 MediaPipe와 Open Pose가 있다.
1. MediaPipe
* 제작사: Google
* 2D 지원 여부: O
* 2D 포즈 추정 : O
* 3D 지원 여부: O
* 멀티포즈 지원 여부: X
* 지원 언어 : Python, C++, JavaScript
* 특징:
  - Google에서 개발한 오픈소스 라이브러리
  - 비디오 및 이미지에서 3D 포즈와 트래킹, 페이셜 랜드마크 검출 등 다양한 기능을 제공
  - MediaPipe Pose는 높은 정확도와 실시간성을 보장
  
2. Open Pose
* 제작사: Carnegie Mellon University
* 2D 지원 여부: O
* 2D 포즈 추정 : O
* 3D 지원 여부: O
* 멀티포즈 지원 여부: O 
* 지원 언어 : C++, Python, MATLAB, Java, JavaScript  
*특징:
  - 인간의 포즈를 비디오나 이미지에서 감지하기 위한 오픈소스 라이브러리
  - OpenPose는 딥러닝 모델을 기반으로 함
  - 각 관절의 위치와 방향을 추정하는 것 외에도 손가락 추적, 얼굴 감지 등 다양한 기능을 제공
 

## 분석결과
![frame0](https://github.com/user-attachments/assets/25a04bca-d757-42d2-876e-9d1eaee33be4)
![Untitled](https://github.com/user-attachments/assets/fa3e174e-d446-49ed-aa57-84c9849c4029)

