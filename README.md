# rainy-lane-visalization
Visualizing road conditions in rainy weather for improved traffic safety using weather data and vehicle sensors.

## Table of Contents
1. [Requirements](#requirements)
2. [Project Structure](#project-structure)
3. [Modules](#modules)
    * Retinex
    * Image Processing
4. [Main](#main)
5. [Usage](#usage)
6. [Reference](#reference)
7. [Authors](#authors)

## Requirements
* Python 3.x
* OpenCV (cv2) 라이브러리
* NumPy 라이브러리

## Project Structure

```
.
├── image_processing.py        # 설명 1
├── main.py                    # 설명 2
├── retinex.py                 # 설명 3
├── etc                        # 설명 4
│   ├── aaa                    # 설명 5
│   │   └── bbb                # 설명 6
│   ├── cc                     # 설명 7
│   │   ├── D                  # 설명 8
│   │   │   ├── eeee           # 설명 9
└── ff                         # 설명 10
```

## Modules

### retinex.py

이 모듈은 Retinex 알고리즘과 관련된 함수들을 제공합니다.

- `singleScaleRetinex(img, variance)`: 단일 스케일 Retinex를 계산하는 함수입니다.
- `multiScaleRetinex(img, variance_list)`: 다중 스케일 Retinex를 계산하는 함수입니다.
- `MSR(img, variance_list)`: Multi-Scale Retinex를 적용하고 영상을 조정하는 함수입니다.
- `SSR(img, variance)`: Single-Scale Retinex를 적용하고 영상을 조정하는 함수입니다.

### image_processing.py

이 모듈은 영상 처리 관련 함수들을 제공합니다.

- `wrapping(img)`: 원근 변환을 사용하여 이미지를 래핑하는 함수입니다.
- `threshold(img)`: 이미지를 이진화하는 함수입니다.
- `hist(img)`: 이미지 히스토그램을 계산하는 함수입니다.
- `distance(l_base, r_base, midpoint)`: 레인 중심 및 거리를 계산하는 함수입니다.

## Main

### main.py

메인 프로그램 파일은 비디오 파일을 읽고 Retinex 알고리즘 및 영상 처리 함수를 적용하여 결과를 표시하는 기능을 포함합니다.

- `variance_list`: 다중 스케일 Retinex에 사용되는 분산 값 목록을 정의합니다.
- `cap`: 비디오 파일을 엽니다.
- `while` 루프: 비디오 프레임을 읽고 처리하는 메인 루프입니다.
- `MSR`, `wrapping`, `threshold`, `hist`, `distance` 함수를 사용하여 영상 처리 및 Retinex 알고리즘을 적용합니다.

## Usage

1. Python 환경에서 프로젝트를 실행합니다.
2. `main.py` 파일을 실행하여 비디오 처리 및 Retinex 알고리즘을 확인합니다.

## Reference

- [OpenCV 공식 웹사이트](https://opencv.org/)

## Authors

- 김다빈 ([@kim-da-been](https://github.com/kim-da-been))
- 신현준 ([@HyunJun990119](https://github.com/HyunJun990119))
- 민은영 ([@danbom](https://github.com/danbom))
- 이동근 ([@LLLEEEDDDGGG](https://github.com/LLLEEEDDDGGG))

