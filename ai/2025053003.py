import numpy as np
import cv2
import matplotlib.pyplot as plt
def plotHistogram(image, title, mask=None):
    chans = cv2.split(image)
    colors = ("b", "g", "r")
    plt.figure()
    plt.title(title)
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")

    for (chan, color) in zip(chans, colors) :
        hist = cv2.calcHist([chan], [0], mask, [256], [0,256])
        plt.plot(hist, color = color)
        plt.xlim([0, 256])

image = cv2.imread("image_dark.jpg")
cv2.imshow("Original", image)

plotHistogram(image, "Histogram for Origin...")
# mask = np.zeros(image.shape[:2], dtype="uint8")
# # cv2.rectangle(mask, (700, 340), (790, 555), 255, -1)
# cv2.rectangle(mask, (700, 550), (790, 805), 255, -1)
# cv2.imshow("Mask", mask)

# masked = cv2.bitwise_and(image, image, mask=mask)
# cv2.imshow("Applying... Mask", masked)
# plotHistogram(image, "Histogram... for Masked.", mask=mask)

# image1 = cv2.imread("image_dark.jpg", cv2.IMREAD_GRAYSCALE)
# cv2.imshow("IMREAD_GRAYSCALE...", image1)
chans = cv2.split(image)
colors = ("b", "g", "r")
histoEqualBlue = cv2.equalizeHist(chans[0])
histoEqualGreen = cv2.equalizeHist(chans[1])
histoEqualRed = cv2.equalizeHist(chans[2])
equals = cv2.merge([histoEqualBlue, histoEqualGreen, histoEqualRed])
cv2.imshow("HistoEqual", equals)
plotHistogram(equals, "HistoEqual...")

# for (chan, color) in zip(chans, colors) : # color = colors[0]
    
#     histoEqual = cv2.equalizeHist(chan)
#     cv2.imshow("HistoEqual : {}".format(color), histoEqual)
#     i = i + 1
#     # plotHistogram(histoEqual, "Histogram... for HistoEqual:{}".format(color))
#     hist = cv2.calcHist([chan], [0], None, [256], [0,256])
#     plt.plot(hist)
#     plt.show()

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
