from PySide2.QtCore import QSettings, QThread, Signal
import torch
import os
import numpy as np
import cv2
from src.box import Box
from math import ceil

class VideoBlurrer(QThread):
    setMaximum = Signal(int)
    updateProgress = Signal(int)

    def __init__(self, weights_name, parameters=None):
        """
        Constructor
        :param weights_name: file name of the weights to be used
        :param parameters: all relevant paremeters for the blurring process
        """
        super(VideoBlurrer, self).__init__()
        self.parameters = parameters
        self.detections = []
        weights_path = os.path.join("weights", f"{weights_name}.pt")
        self.detector = setup_detector(weights_path)
        print("Worker created")

    def apply_blur(self, frame: np.array, new_detections: list):
        """
        Apply Gaussian blur to regions of interests
        :param frame: input image
        :param new_detections: list of newly detected faces and plates
        :return: processed image
        """
        # gather inputs from self.parameters
        blur_size = self.parameters["blur_size"]
        blur_memory = self.parameters["blur_memory"]
        roi_multi = self.parameters["roi_multi"]

        # gather and process all currently relevant detections
        self.detections = [[x[0], x[1] + 1] for x in self.detections if
                           x[1] <= blur_memory]  # throw out outdated detections, increase age by 1
        for detection in new_detections:
            scaled_detection = detection.scale(frame.shape, roi_multi)
            self.detections.append([scaled_detection, 0])

        for detection in [x[0] for x in self.detections]:
            # two-fold blurring: softer blur on the edge of the box to look smoother and less abrupt
            outer_box = detection
            inner_box = detection.scale(frame.shape, 0.8)
            frame[outer_box.coords_as_slices()] = cv2.blur(
                frame[outer_box.coords_as_slices()], (blur_size, blur_size))
            frame[inner_box.coords_as_slices()] = cv2.blur(
                frame[inner_box.coords_as_slices()],
                (blur_size * 2 + 1, blur_size * 2 + 1))
        return frame

    def detect_identifiable_information(self, image: np.array):
        """
        Run plate and face detection on an input image
        :param image: input image
        :return: detected faces and plates
        """
        scale = ceil(image.shape[1] * self.parameters[
            "inference_scale"] / self.detector.stride.max()) * self.detector.stride.max()
        results = self.detector(image, size=scale.item())
        boxes = []
        for res in results.xyxy[0]:
            boxes.append(Box(res[0].item(), res[1].item(), res[2].item(), res[3].item(), res[4].item(), res[5].item()))
        return boxes

    def run(self):
        """
        Write a copy of the input video stripped of identifiable information, i.e. faces and license plates
        """

        # gather inputs from self.parameters
        print("Worker started")
        input_path = self.parameters["input_path"]
        output_path = self.parameters["output_path"]
        threshold = self.parameters["threshold"]

        # customize detector
        self.detector.conf = threshold

        # open video file
        cap = cv2.VideoCapture(input_path)

        # get the height and width of each frame
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = cap.get(cv2.CAP_PROP_FPS)

        # save the video to a file
        fourcc = cv2.VideoWriter_fourcc(*'H264')
        writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

        # update GUI's progress bar on its maximum frames
        self.setMaximum.emit(length)

        if cap.isOpened() == False:
            print('error file not found')
            return

        # loop through video
        current_frame = 0
        while cap.isOpened():
            ret, frame = cap.read()

            if ret == True:
                new_detections = self.detect_identifiable_information(frame.copy())
                frame = self.apply_blur(frame, new_detections)
                writer.write(frame)

            else:
                break

            current_frame += 1
            self.updateProgress.emit(current_frame)

        self.detections = []
        cap.release()
        writer.release()

def setup_detector(weights_path: str):
    """
    Load YOLOv5 detector from torch hub and update the detector with this repo's weights
    :param weights_path: path to .pt file with this repo's weights
    :return: initialized yolov5 detector
    """
    model = torch.hub.load('ultralytics/yolov5', 'custom', weights_path)
    if torch.cuda.is_available():
        print(f"Using {torch.cuda.get_device_name(torch.cuda.current_device())}.")
        torch.backends.cudnn.benchmark = True
        model.cuda()
    else:
        print("Using CPU.")
    return model