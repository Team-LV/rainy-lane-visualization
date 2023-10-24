# Lane Detection

![image](https://github.com/Team-LV/rainy-lane-visualization/assets/52441697/3a2da42c-ac99-4b5c-ad81-9654e4f47cf2)

## lanenet.py

**Quantization**

![Quantization](https://github.com/Team-LV/rainy-lane-visualization/assets/52441697/6580d6a1-6c96-4054-96e1-6bfbfe24859d)

- 일반적으로 많이 사용하는 `float32` 파라미터를 `uint8`로 변환한 다음에 실제 추론 수행
- `floating point`들이 어느 정도의 범위 안에 있다면 `weight`는 `uint8`의 범위인 0~255 사이로 위치
- `32bit` 자료형이 `8bit`로 줄어들기에 메모리 사용량 및 수행 속도가 감소

**Lane-net**

![Lane-net](https://github.com/Team-LV/rainy-lane-visualization/assets/52441697/85a7c474-59b0-4e14-881f-a52da381a870)

- 인코더-디코더 아키텍처 :
  - **이진** 의미 분할을 위한 ENet 디코더: 차선의 존재 여부를 판단, 차선의 픽셀은 하나의 클래스로 분류
  - **실체** 의미 분할을 위한 Enet 디코더: 차선의 개별 인스턴스를 식별, 각 차선은 고유한 식별자로 분류
- 손실함수와 포스트 프로세싱 과정을 거쳐 최종 차선을 검출

## How to run

```shell
git clone https://github.com/PINTO0309/PINTO_model_zoo.git
cd 141_lanenet-lane-detection
sh download.sh
```
