import cv2
import numpy as np

def homomorphic(frame, gamma1, gamma2):
    yuv = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
    y,u,v = cv2.split(yuv)

    rows = frame.shape[0]    
    cols = frame.shape[1]

    imgLog = np.log1p(np.array(y, dtype='float') / 255)

    M = 2*rows + 1
    N = 2*cols + 1

    sigma = 10
    (X, Y) = np.meshgrid(np.linspace(0, N-1, N), np.linspace(0, M-1, M)) # 0~N-1(and M-1) 까지 1단위로 space를 만듬
    Xc = np.ceil(N/2) # 올림 연산
    Yc = np.ceil(M/2)
    gaussianNumerator = (X - Xc)**2 + (Y - Yc)**2 # 가우시안 분자 생성

    ### low pass filter와 high pass filter 생성
    LPF = np.exp(-gaussianNumerator / (2*sigma*sigma))
    HPF = 1 - LPF

    LPF_shift = np.fft.ifftshift(LPF.copy())
    HPF_shift = np.fft.ifftshift(HPF.copy())
 
    ### Log를 씌운 이미지를 FFT해서 LPF와 HPF를 곱해 LF성분과 HF성분을 나눔
    img_FFT = np.fft.fft2(imgLog.copy(), (M, N))
    img_LF = np.real(np.fft.ifft2(img_FFT.copy() * LPF_shift, (M, N))) # low frequency 성분
    img_HF = np.real(np.fft.ifft2(img_FFT.copy() * HPF_shift, (M, N))) # high frequency 성분
 
    ### 각 LF, HF 성분에 scaling factor를 곱해주어 조명값과 반사값을 조절함
    
    img_adjusting = gamma1*img_LF[0:rows, 0:cols] + gamma2*img_HF[0:rows, 0:cols]
 
    ### 조정된 데이터를 이제 exp 연산을 통해 이미지로 만들어줌
    img_exp = np.expm1(img_adjusting) # exp(x) + 1
    img_exp = (img_exp - np.min(img_exp)) / (np.max(img_exp) - np.min(img_exp)) # 0~1사이로 정규화
    img_out = np.array(255*img_exp, dtype = 'uint8') # 255를 곱해서 intensity값을 만들어줌


    out_yuv = cv2.merge([img_out,u,v])
    result = cv2.cvtColor(out_yuv, cv2.COLOR_YUV2BGR)

    return result

