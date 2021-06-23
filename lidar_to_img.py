import numpy as np
import cv2
def points_to_img(points, view_matrix):
    x = view_matrix@points
    x = x/x[3,0]
    x = x[0:2]
    return x.astype(int)

if __name__ == '__main__':
    image_name = '00000.pcd.jpg'
    img = cv2.imread(image_name, cv2.IMREAD_COLOR)
    points = np.array([[14.5128957950366],
       [78.11556905877607],
       [0.7582428564130828],
       [1]])
    view_matrix = np.array([[1760.1102658536129, 1223.4021926753574, -176.13796102887775, 1248.7261649672898], [-82.34105075124923, 868.2208837190936, -1872.9925438615098, 9348.837192233239], [0.0, 0.0, 0.0, 1.0], [-0.020030480682725345, 0.9954613680718195, -0.09303460019248397, 0.36507968336045765]])
    x = points_to_img(points, view_matrix)
    print((x[0, 0], x[1, 0]))
    image_plotted_one_center = cv2.circle(img, (x[0, 0], x[1, 0]), radius=10, color=(0, 0, 255), thickness=3)
    cv2.imshow("result", image_plotted_one_center)
    cv2.waitKey(0)