import cv2
import numpy as np



def sketch(image):
    # Convert image to grayscale
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Clean up image by using Guassian Blur
    img_gray_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)

    # Trich xuat cac canh
    canny_edges = cv2.Canny(img_gray_blur, 10, 70)

    # dao nguoc nhi phan hinh anh
    ret, mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV)
    print(type(mask))
    return mask


# Khởi tạo webcam, cap là đối tượng do VideoCapture cung cấp
# Nó chứa một boolean cho biết nếu nó đã thành công (ret)
# Nó cũng chứa các hình ảnh được thu thập từ webcam (khung hình)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('Our Live Sketcher', sketch(frame))
    if cv2.waitKey(1) == 13:  # 13 is the Enter Key
        break

# dong ung dung
cap.release()
cv2.destroyAllWindows()