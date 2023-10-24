# Lane Keeping Degree

![image](https://github.com/Team-LV/rainy-lane-visualization/assets/52441697/bfe4bb13-7863-4590-ba5e-f5565053e18f)

## LKD.py

**Sliding Window**

![Sliding Window1](https://github.com/Team-LV/rainy-lane-visualization/assets/52441697/de53157a-53ed-4334-87a7-f7a4f274e799)
![Sliding Window2](https://github.com/Team-LV/rainy-lane-visualization/assets/52441697/e41ea0aa-15c6-4eab-b44c-37686d0eefa5)

- 이미지를 `Top-view` 변환을 통해 계산에 용이하도록 설계
- `Light-weight Deep Learning` 모델의 인식 성능을 개선하고자 2차 회귀를 수행하여 안정적인 차선 검출
- 픽셀당 거리 계산을 통해 `Lane Keeping Degree` 계산 (`ISO 17361` 참고)


**Calculating Process in Our Mission Track**

![Calculating Process in Our Mission Track](https://github.com/Team-LV/rainy-lane-visualization/assets/52441697/6f36fb7d-8e70-448b-938a-ca3d0fb1fc55)

- 기존 실차 기준이었던 30cm를 1/10으로 축소한 모형 트랙에 적용하여 `3cm`의 기준으로 실험
- 픽셀 당 `0.04688cm`
- 전방 15 ~ 35cm 의 차선을 인식하여 연산 수행


## 함수 정의

1. `wrapping(image)`: 원근 변환을 수행하는 함수, 입력 이미지에 원근 변환 적용. 입력 이미지와 원근 변환 매트릭스 반환
2. `threshold(img)`: 이진 임계값 처리를 수행하는 함수, 입력 이미지를 특정 임계값 이상의 값은 흰색(255)으로, 그 미만의 값은 검은색(0)으로 변환. 임계값과 처리된 이미지 반환
3. `hist(img)`: 이미지의 하단 절반에서 히스토그램 생성, 히스토그램의 중점을 기반으로 좌측 및 우측 차선의 기준점 결정
4. `distance(l_base, r_base, midpoint)`: 좌측 및 우측 차선의 기준점과 중점을 사용하여 차선 간의 거리를 계산하고 미터 단위로 변환
5. `slide_window_search(img, left_current, right_current)`: 슬라이딩 윈도우 방식을 사용하여 차선을 검색하고, 좌측 및 우측 차선의 픽셀 위치 반환
6. `drawline(frame, img, minv, ret)`: 차선 정보를 이용하여 원래 영상 위에 감지된 차선을 그리고, 차선의 중간선을 표시하여 반환
7. 마지막 함수는 하드한 우회전, 좌회전, 우회전, 좌회전, 또는 좋은 주행 상태에 따라 경고 메시지를 생성하고, 이미지를 반환
