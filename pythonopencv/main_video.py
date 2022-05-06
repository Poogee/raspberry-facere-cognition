import cv2
from simple_facerec import SimpleFacerec
import cmake
import time
from threading import Thread

import numpy as np
# Encode faces from a folder


class VideoStreamWidget(object):
    def __init__(self, src=0):
        self.capture = cv2.VideoCapture(src)
        # Start the thread to read frames from the video stream
        self.thread = Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()

    def update(self):
        # Read the next frame from the stream in a different thread
        while True:
            if self.capture.isOpened():
                (self.status, self.frame) = self.capture.read()
            time.sleep(.01)

    def show_frame(self):
        # Display frames in main program
        face_locations, face_names = sfr.detect_known_faces(self.frame)
        for face_loc, name in zip(face_locations, face_names):
            y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

            cv2.putText(self.frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 2)
            cv2.rectangle(self.frame, (x1, y1), (x2, y2), (255, 255, 255), 2)
        # img = cv2.imread("images/dima utkin.jpg")
        # Hori = np.concatenate((frame, img), axis=1)
        # cv2.imshow('HORIZONTAL', Hori)
        cv2.imshow("Frame", self.frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            self.capture.release()
            cv2.destroyAllWindows()
            exit(1)


if __name__ == '__main__':
    sfr = SimpleFacerec()
    sfr.load_encoding_images("images/")

    # Load Camera
    video_stream_widget = VideoStreamWidget()
    while True:
        try:
            video_stream_widget.show_frame()
        except AttributeError:
            pass