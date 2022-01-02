import cv2
import glob
from vehicle_detector import VehicleDetector
class counter:
    def __init__(self):
        # Load Veichle Detector
        self.vd = VehicleDetector()
        self.vehicles_folder_count = 0

    # Loop through all the images
    def imag(self,img_path):
        print("Img path", img_path)
        img = cv2.imread(img_path)

        vehicle_boxes = self.vd.detect_vehicles(img)
        vehicle_count = len(vehicle_boxes)


        for box in vehicle_boxes:
            x, y, w, h = box

            cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)

            cv2.putText(img, "Vehicles: " + str(vehicle_count), (20, 50), 0, 2, (100, 200, 0), 3)

        #cv2.imshow("Cars", img)
        #cv2.waitKey(0)
        print("Total current count", vehicle_count)
        return img,vehicle_count

