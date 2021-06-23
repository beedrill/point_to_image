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
    ## for 3-8:
    # view_matrix = [[1761.0311509944504, 1215.6173377650678, -216.26240467008654, 1446.552182438541], [-62.84696332328157, 776.5641728621133, -1913.5534916885958, 9518.355917565557], [0.0, 0.0, 0.0, 1.0], [-0.019736923344066067, 0.9897750156351667, -0.14126522783081075, 0.6050046300820235]]
    ## for 3-9:
    view_matrix = np.array([[1760.1102658536129, 1223.4021926753574, -176.13796102887775, 1248.7261649672898], [-82.34105075124923, 868.2208837190936, -1872.9925438615098, 9348.837192233239], [0.0, 0.0, 0.0, 1.0], [-0.020030480682725345, 0.9954613680718195, -0.09303460019248397, 0.36507968336045765]])
    x = points_to_img(points, view_matrix)
    print((x[0, 0], x[1, 0]))
    image_plotted_one_center = cv2.circle(img, (x[0, 0], x[1, 0]), radius=10, color=(0, 0, 255), thickness=3)
    cv2.imshow("result", image_plotted_one_center)
    cv2.waitKey(0)