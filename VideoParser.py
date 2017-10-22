import cv2


class VideoParser:
    def __init__(self, vidname):
        self.vidname = vidname

    def split_video(self):
        cap = cv2.VideoCapture(self.vidname)
        if not cap.isOpened():
            return
        framerate = cap.get(cv2.CAP_PROP_FPS)
        framecount = 0
        time = round(framerate / 4)
        print(time)
        i = 0
        while not (cv2.waitKey(1) & 0xFF == ord('q')):
            framecount += 1
            success, image = cap.read()
            if not success:
                break
            if not (framecount % time):
                cv2.imwrite("frames/frame%d.jpg" % i, image)
                i += 1
        cap.release()
        cv2.destroyAllWindows()


x = VideoParser("movie.mp4")
x.split_video()
