import os
import numpy as np
import cv2

args = {"rfcnn": os.path.join("..", "data", "coco-rfcnn"), 'confidence': 0.5, 'threshold': 0.3}


def loadnet(args):

    # load the COCO class labels our fcnn was trained on
    labelsPath = os.path.sep.join([args["rfcnn"],
        "object_detection_classes_coco.txt"])
    LABELS = open(labelsPath).read().strip().split("\n")

    # initialize a list of colors to represent each possible class label
    np.random.seed(42)
    COLORS = np.random.randint(0, 255, size=(len(LABELS), 3),
        dtype="uint8")

    # derive the paths to the Mask R-CNN weights and model configuration
    weightsPath = os.path.sep.join([args["rfcnn"],
        "frozen_inference_graph.pb"])
    configPath = os.path.sep.join([args["rfcnn"],
        "coco.pbtxt"])

    # from disk
    # print("[INFO] loading Mask Faster-FCNN from disk...")
    net = cv2.dnn.readNetFromTensorflow(weightsPath, configPath)

    return net,LABELS

TP_IMAGE=0
FP_IMAGE=0
FN_IMAGE=0

def tpfpfn():
    global TP_IMAGE
    global FP_IMAGE
    global FN_IMAGE

    return (TP_IMAGE,FP_IMAGE,FN_IMAGE)

def im_detect(sess,net,frame,LABELS):
    global args
    global TP_IMAGE
    global FP_IMAGE
    global FN_IMAGE

    TP_IMAGE=0
    FP_IMAGE = 0
    FN_IMAGE = 0

    blob = cv2.dnn.blobFromImage(frame, swapRB=True, crop=False)
    net.setInput(blob)
    (boxes) = net.forward(["detection_out_final"])
    boxes2 = []

    # loop over the number of detected objects
    for i in range(0, boxes[0].shape[2]):
        # extract the class ID of the detection along with the
        # confidence (i.e., probability) associated with the
        # prediction
        classID = int(boxes[0][0, 0, i, 1])
        confidence = boxes[0][0, 0, i, 2]

        if LABELS[classID] in ['person']:
            FP_IMAGE += 1

            if confidence > args["confidence"]:
                TP_IMAGE += 1

                (H, W) = frame.shape[:2]
                box = boxes[0][0, 0, i, 3:7] * np.array([W, H, W, H])
                (startX, startY, endX, endY) = box.astype("int")

                boxes2.append([startX,startY,endX,endY,LABELS[classID],confidence])
            else:
                FN_IMAGE += 1

    return boxes2
