from picamera import PiCamera
from time import sleep


def main():
    print("TEST")
    camera = PiCamera()
    camera.start_recording("test.h264")
    sleep(5)
    camera.stop_recording()


if __name__ == "__main__":
    main()
