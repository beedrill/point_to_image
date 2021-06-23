## usage
Use the function `points_to_img` to map any 3d points into 2d image. The points is 4xn 2d array where n is the number of points, each points has 4 dimension, [x, y, z, 1], see `lidar_to_img.py` for the example. The view_matrix is the matrix directly from the processed data.

View matrix:
```python
## for 3-8:
view_matrix = [[1761.0311509944504, 1215.6173377650678, -216.26240467008654, 1446.552182438541], [-62.84696332328157, 776.5641728621133, -1913.5534916885958, 9518.355917565557], [0.0, 0.0, 0.0, 1.0], [-0.019736923344066067, 0.9897750156351667, -0.14126522783081075, 0.6050046300820235]]
## for 3-9:
view_matrix = np.array([[1760.1102658536129, 1223.4021926753574, -176.13796102887775, 1248.7261649672898], [-82.34105075124923, 868.2208837190936, -1872.9925438615098, 9348.837192233239], [0.0, 0.0, 0.0, 1.0], [-0.020030480682725345, 0.9954613680718195, -0.09303460019248397, 0.36507968336045765]])
   
```