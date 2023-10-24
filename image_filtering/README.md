# Image Filtering

![image](https://github.com/Team-LV/rainy-lane-visualization/assets/52441697/f0f8a1e7-3ed7-422f-9db2-e9b4d7a2a281)

## fuzzyfilter.py

![Variable Filtering by Fuzzy Logic](https://github.com/Team-LV/rainy-lane-visualization/assets/52441697/a81fe7b1-5ed2-4629-a15d-2fc157a695f0)

**Gamma Variable**
| | NB | NS | ZE | PS | PB |
| - | - | - | - | - | - |
| NB | NB | NS | ZE | PS | PS |
| NS | NB | NS | ZE | PS | PS |
| ZE | NB | NS | ZE | PS | PS |
| PS | NB | NS | ZE | PS | PS |
| PB | NB | NS | ZE | PS | PS |

- 이미지의 조명 값에 따라 필터링 계수를 조정하여 조도 변화에 강인한 이미지 필터링 기술 구축
- 이미지를 gray scale로 변환 후 평균과 표준편차를 바탕으로 밝은 정도, 어두운 정도를 판단하고 gamma를 할당
- 판단 기준은 AI HUB의 데이터셋을 바탕으로 데이터를 추출하여 histogram을 분석하고 경험적으로 선정

**코드 요약**

- `a, b, c, d`: 밝기 값 범위
- `e, f, g, h`: 안개 값 범위
- `vs, s, m, l, vl`: 감마 값 범위
- `low_func_avg`, `mid_func_avg`, `high_func_avg`, `fuzzy_avg`: 퍼지 논리 함수를 정의하여 밝기 값에 따라 영상 품질을 판단
- `low_func_std`, `mid_func_std`, `high_func_std`, `fuzzy_std`: 퍼지 논리 함수를 정의하여 안개 값에 따라 영상 품질을 판단
- `filtersigma`: 두 가지 퍼지 결과를 조합하여 필터 시그마 값을 선택하는 함수

## homomorphic.py

![Homomorphic Filter](https://github.com/Team-LV/rainy-lane-visualization/assets/52441697/845d8874-86d0-4f74-a67e-53152c255647)

- 이미지의 경우 조명 성분과 반사 성분의 곱으로 이루어져 있으며, 조명 성분의 경우 저주파 대역, 조명 성분의 경우 고주파 대역에 존재한다고 가정
- 로그 스케일을 취한 후 주파수 변환과 High-pass filter를 적용한다면 쉽게 조명 성분의 이미지를 제거할 수 있으며, 이후 역변환을 통해 다음과 같이 선명한 이미지 추출
- BGR이미지를 YUV필터로 변환 후, 밝기 정도를 나타내는 Y값을 기준으로 적용
- 이후 Canny Edge를 추가로 필터링하여 차선 탐지 모델에서 기능을 우수하게 함

**함수 정의**

1. 입력으로 들어온 이미지 `frame`을 `YUV` 컬러 스페이스로 변환
2. `Y, U, V` 채널 분리
3. 이미지의 로그 스케일 적용
4. 주파수 도메인으로 이미지를 변환하기 위한 `FFT(Fast Fourier Transform)`를 수행하기 위해 행과 열 크기 확장
5. 가우시안 필터링을 사용하여 저주파 및 고주파 부분을 분리하는데 사용될 `Low Pass Filter(LPF)`와 `High Pass Filter(HPF)` 생성
6. `LPF`와 `HPF`를 이미지의 FFT에 적용하여 저주파 및 고주파 성분 분리
7. 저주파 성분과 고주파 성분에 스케일링 요인(gamma1, gamma2)을 곱하여 이미지 조정
8. 조정된 데이터를 지수 함수를 사용해 다시 이미지로 변환
9. 결과 이미지를 0~1 사이로 정규화하고 최종 결과를 8비트 부호 없는 정수로 변환하여 반환
