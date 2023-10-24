## Project Overview

**Lane Keeping alert for Safe Driving in Rainy day**

![Lane Keeping alert for Safe Driving in Rainy day_Overview](https://github.com/Team-LV/rainy-lane-visualization/assets/52441697/bcb3ba64-254f-49fe-bb85-cb0b5bb08aa8)

**Why do we need this system?**

- **Existing Solution** : 비 오는 날 차선 감지 어려움으로 인해 시스템 신뢰성 하락
- **Our Solution** : 우천 시 낮은 차선 가시성 문제를 해결하여 교통 안전성 향상

**Objectives**

 - 우천 시에 발생하는 빛 번짐과 빛 굴절을 감소시켜 차선 탐지
 - 경량화된 모델로 저사양 디바이스인 라즈베리파이에서의 구동

**Necessity**

- 우천 시 차선 가시성 저하로 인한 사고 예방
- 차선 정보를 정확히 획득하고 시각적으로 운전자에게 전달함으로써 운전 안정성 및 편의성 향

## Demonstration Video

[![Video Label](http://img.youtube.com/vi/KXsIZ9Fu6G0/0.jpg)](https://youtu.be/KXsIZ9Fu6G0')


## System Architecture

![Lane Keeping alert for Safe Driving in Rainy day_System_Architecture](https://github.com/Team-LV/rainy-lane-visualization/assets/52441697/d2c93baf-2ad2-4e91-96c1-9d149c639f67)


## Project Structure

※ 각 폴더의 `README.md` 파일에서 자세한 함수 설명을 확인할 수 있습니다.

[📂 image_filtering](https://github.com/Team-LV/rainy-lane-visualization/tree/main/image_filtering)
[📂 lane_detection](https://github.com/Team-LV/rainy-lane-visualization/tree/main/lane_detection)
[📂 lane_keeping_degree](https://github.com/Team-LV/rainy-lane-visualization/tree/main/lane_keeping_degree)

```
.
├── image_filtering            # 이미지 필터링
│   ├── fuzzyfilter.py
│   └── homomorphic.py               
├── lane_detection             # 차선 검출 및 예측
│   └── lanenet.py               
├── lane_keeping_degree        # 차선 유지 정도 계산 알고리즘
│   └── lanenet.py               
├── README.md
└── main.py
```

## How to run

```shell
git clone https://github.com/Team-LV/rainy-lane-visualization.git
cd rainy-lane-visualization
python main.py
```

## Authors

1. 김다빈

- Position : 팀장
- Github: <https://github.com/kim-da-been>
- Email : ekqlsfnvg@gmail.com
- Role
  - 이미지 필터링
  - 차선 검출 및 예측
  - 차선 유지 정도 계산 알고리즘

2. 신현준

- Position : 팀원
- Github: <https://github.com/HyunJun990119>
- Email : hc17jj29hj@naver.com
- Role
  - 이미지 필터링
  - 차선 검출 및 예측
  - 차선 유지 정도 계산 알고리즘
  - 차선 이탈 경고 시각화

3. 민은영

- Position : 팀원
- Github: <https://github.com/danbom>
- Email : mey990425@gmail.com
- Role
  - 이미지 필터링
  - 차선 검출 및 예측
  - 차선 유지 정도 계산 알고리즘

4. 이동근

- Position : 팀원
- Github: <https://github.com/LLLEEEDDDGGG>
- Email : gmadiq12@knu.ac.kr
- Role
  - 리눅스 환경 구축
  - IP 기반 영상 송수신 환경 구축
 
5. 권희규

- Position : 팀원
- Github: <https://github.com/Kweon00>
- Email : chs3309@naver.com
- Role
  - 리눅스 환경 구축
  - IP 기반 영상 송수신 환경 구축
