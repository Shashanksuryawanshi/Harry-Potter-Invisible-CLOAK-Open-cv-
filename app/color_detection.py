import cv2
import numpy as np
from sklearn.cluster import KMeans

def auto_detect_dominant_color(frame, roi):
    x, y, w, h = roi
    roi_img = frame[y:y+h, x:x+w]
    roi_reshaped = roi_img.reshape((-1, 3))

    kmeans = KMeans(n_clusters=1, n_init=10)
    kmeans.fit(roi_reshaped)
    dominant_bgr = kmeans.cluster_centers_[0].astype(int)

    # Convert BGR to HSV
    dominant_hsv = cv2.cvtColor(np.uint8([[dominant_bgr]]), cv2.COLOR_BGR2HSV)[0][0]
    h, s, v = dominant_hsv

    lower_hsv = np.array([max(h - 10, 0), 120, 70])
    upper_hsv = np.array([min(h + 10, 180), 255, 255])

    return lower_hsv, upper_hsv, dominant_bgr
