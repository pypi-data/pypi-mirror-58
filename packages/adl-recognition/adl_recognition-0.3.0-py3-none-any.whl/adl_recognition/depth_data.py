import os
import re
from datetime import datetime
import numpy as np
import cv2


def getDepthVideo(path, silhouette_model, depth_height, depth_width, start_time, end_time):

    X = None
    depthFile = None

    timeStamps = []
    width, height = 160, 120

    for fileName in os.listdir(path):
        if re.match('.*.bin', fileName):
            depthFile = path + fileName

    depthFrames = np.fromfile(depthFile, dtype="uint16")
    numOfFrames = int(depthFrames.shape[0]/(depth_height * depth_width))
    depthFrames = depthFrames.reshape(numOfFrames, depth_height, depth_width)

    avgTime = (end_time - start_time)/numOfFrames

    for i in range(0, numOfFrames, 5):
        frame = depthFrames[i]

        timeStamps.append(start_time+avgTime*i)

        frame = cv2.resize(frame, (320, 240)).reshape((1, 240, 320, 1))
        frame = frame.astype(np.float64)/np.amax(frame)
        # Model gives the silhoutte
        sil = silhouette_model.predict(frame).reshape((240, 320))
        frame = frame.reshape((240, 320))
        # connected component to remove unwanted parts
        fr = (sil > 0.5) * frame
        fr = (fr*255).astype(np.uint8)
        components = cv2.connectedComponents(fr)
        unique, counts = np.unique(components[1], return_counts=True)
        if len(unique) > 1:
            secondHighest = np.where(
                counts == np.partition(counts, -2)[-2])[0][0]
            sil = (components[1] == secondHighest)
        elif len(unique) == 1:
            sil = (components[1] == 0)

        frame = cv2.resize(np.multiply(frame, sil),
                           (width, height)).reshape((1, height, width))
        frame = frame/np.amax(frame)

        if X is None:
            X = frame
        else:
            X = np.concatenate((X, frame), axis=0)
    return X, timeStamps
