import numpy as np
import math as m
import cv2

name = 'exercise-4.jpg'
img = cv2.imread(name)
lower_res = cv2.imread(name)
print img.shape
height, width, ch = img.shape
count = 0
while height > 800 or width > 800:
    print 'lower res'
    count += 1
    lower_res = cv2.pyrDown(lower_res)
    height, width, ch = lower_res.shape

print 'scaled down to', lower_res.shape
def MedianBlur2D(img):
    copy = img
    s=1
    height, width = img.shape
    members = [0, 0]*9
    for y in range(10+s, height-(10+s)):
        for x in range(10+s, width-(10+s)):
            members[0] = img[y - s, x - s]
            members[1] = img[y, x - s]
            members[2] = img[y + s, x - s]
            members[3] = img[y - s, x]
            members[4] = img[y, x]
            members[5] = img[y + s, x]
            members[6] = img[y - s, x + s]
            members[7] = img[y, x + s]
            members[8] = img[y + s, x + s]

            members.sort()
            copy[y, x] = members[4]
    return copy

def skinMap(img):
    b, g, r = cv2.split(img)
    height, width, ch = img.shape

    r_zero_resp = np.nanmin(r[10:height - 10, 10: width - 10])
    g_zero_resp = np.nanmin(g[10:height - 10, 10: width - 10])
    b_zero_resp = np.nanmin(b[10:height - 10, 10: width - 10])
    true_zero = np.nanmin([r_zero_resp, g_zero_resp, b_zero_resp])

    r -= true_zero
    g -= true_zero
    b -= true_zero
    lr = np.zeros((height, width))
    lb = np.zeros((height, width))
    lg = np.zeros((height, width))

    for rows in range(height):
        for cols in range(width):

            lr[rows, cols] = 105*m.log10(r[rows, cols] + 1)
            lb[rows, cols] = 105*m.log10(b[rows, cols] + 1)
            lg[rows, cols] = 105*m.log10(g[rows, cols] + 1)


    I = (lr + lb + lg) / 3
    Rg = lr - lg
    By = lb - ((lg + lr) / 2)
    scale = int(round((width + height) / 320))

    if scale == 0:
        scale = 1

    Rg = MedianBlur2D(Rg)
    By = MedianBlur2D(By)
    I_filt = MedianBlur2D(I)
    MAD = I - I_filt
    MAD = abs(MAD)
    MAD = MedianBlur2D(MAD)

    hue = (np.arctan2(Rg, By) * (180/m.pi))
    saturation = np.sqrt(np.power(Rg, 2) + np.power(By, 2))

    map = np.zeros((height, width))
    zeroes = np.zeros((height, width))

    for rows in range(height):
        for cols in range(width):
            if (MAD[rows, cols] < 4.5) & (120 < hue[rows, cols]) & (hue[rows,cols] < 160 ) & (10 < saturation[rows, cols]) & (saturation[rows, cols] < 60):
                map[rows, cols] = 1
            if (MAD[rows, cols] < 4.5) & (150 < hue[rows, cols]) & (hue[rows, cols] < 180) & (saturation[rows, cols] > 20) & (saturation[rows, cols] < 80):
                map[rows, cols] = 1

    kernal = np.ones((10*scale, 10*scale), np.uint8)

    for y in range(height):
        for x in range(width):
            if (map[y, x] == 1) & (110 <= hue[y, x]) & (0 <= saturation[y, x]) & (saturation[y, x] <= 130):
                map[y, x] = 1;

            else:
                map[y, x] = 0;
    print map[0, 0], 'map cord'
    return map

def findFaces(map, lower, img, upscale):
    grey = cv2.cvtColor(lower, cv2.COLOR_BGR2GRAY)
    grey = cv2.equalizeHist(grey)
    ret, grey = cv2.threshold(grey, 50, 210, cv2.THRESH_BINARY)
    height, width = map.shape


    for rows in range(height):
        for cols in range(width):
            if grey[rows, cols] < 200:
                grey[rows, cols] = 0
            if map[rows, cols] == 0:
                grey[rows, cols] = 0
    # Destroy Holes
    scale = int(round(18 - (height/100)))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    grey = cv2.dilate(grey, kernel, iterations=scale)
    grey = cv2.erode(grey, kernel, iterations=scale)
    #Destroy More Holes
    """
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    ngrey = cv2.morphologyEx(ngrey, cv2.MORPH_CLOSE, kernel)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    ngrey = cv2.erode(ngrey, kernel, iterations = 1)
    ngrey = cv2.dilate(ngrey, kernel, iterations= 1)


    height, width = ngrey.shape
    for rows in range(height):
        for cols in range(width):
            if ngrey[rows, cols] > 200:
                ngrey[rows,cols] = 100
            if map[rows, cols] == 0:
                ngrey[rows, cols] = 0

    diff = grey - ngrey

    for rows in range(height):
        for cols in range(width):
            if (cv2.subtract(grey, ngrey)) > 0:
                diff[rows, cols] = grey[rows,cols] - ngrey[rows,cols]


    temp = cv2.cvtColor(lower, cv2.COLOR_BGR2GRAY)
    height, width = map.shape
    for rows in range(height):
        for cols in range(width):
            if map[rows, cols] != 1:
                temp[rows, cols] = 255
            else:
                temp[rows, cols] = 100
    """


    while upscale > 0:
        grey = cv2.pyrUp(grey)
        #diff = cv2.pyrUp(diff)
        upscale -= 1

    print grey.shape, 'grey upscaled'
    ngrey = 255 - grey

    params = cv2.SimpleBlobDetector_Params()
    params.minThreshold = 10;
    params.maxThreshold = 255;
    params.filterByArea = True
    params.minArea = 8000
    params.maxArea = 1600000
    params.filterByCircularity = True
    params.minCircularity = 0.1
    params.filterByConvexity = True
    params.minConvexity = 0.1
    params.filterByInertia = True
    params.minInertiaRatio = 0.1

    detector = cv2.SimpleBlobDetector(params)

    keypoints = detector.detect(ngrey)

    im_with_keypoints = cv2.drawKeypoints(img, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    """
    for each in keypoints:
        for other in reversed(keypoints):
            if other <= each:
                return
            if (keypoints[each].y < keypoints[other].y + 10) & (keypoints[each].y > keypoints[other].y - 10):
                cv2.Rectangle(im_with_keypoints, (keypoints[each].x - 10, keypoints[each].y-50), (keypoints[other].x - 10, keypoints[other].y+50), (0, 255, 0),
                             thickness =3, lineType = 8)
    """

    cv2.imshow('circled', im_with_keypoints)
    cv2.imshow('grey', grey)
    #cv2.imshow ('c', gradient)
    #cv2.imshow('ngrey', ngrey)


map = skinMap(lower_res)
findFaces(map, lower_res, img, count)


print 'waiting on you'
cv2.waitKey(0)
cv2.destroyAllWindows()

