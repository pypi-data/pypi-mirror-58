import cv2
import numpy as np


def get_depth_video(depth_file, silhouette_model, depth_height, depth_width, start_time, end_time):
    X = None

    time_stamps = []
    width, height = 160, 120

    depth_frames = np.fromfile(depth_file, dtype="uint16")
    num_of_frames = int(depth_frames.shape[0] / (depth_height * depth_width))
    depth_frames = depth_frames.reshape(num_of_frames, depth_height, depth_width)

    avg_time = (end_time - start_time) / num_of_frames

    for i in range(0, num_of_frames, 5):
        frame = depth_frames[i]

        time_stamps.append(start_time + avg_time * i)

        frame = cv2.resize(frame, (320, 240)).reshape((1, 240, 320, 1))
        frame = frame.astype(np.float64) / np.amax(frame)
        # Model gives the silhouette
        sil = silhouette_model.predict(frame).reshape((240, 320))
        frame = frame.reshape((240, 320))
        # connected component to remove unwanted parts
        fr = (sil > 0.5) * frame
        fr = (fr * 255).astype(np.uint8)
        components = cv2.connectedComponents(fr)
        unique, counts = np.unique(components[1], return_counts=True)
        if len(unique) > 1:
            second_highest = np.where(
                counts == np.partition(counts, -2)[-2])[0][0]
            sil = (components[1] == second_highest)
        elif len(unique) == 1:
            sil = (components[1] == 0)

        frame = cv2.resize(np.multiply(frame, sil),
                           (width, height)).reshape((1, height, width))
        frame = frame / np.amax(frame)

        if X is None:
            X = frame
        else:
            X = np.concatenate((X, frame), axis=0)
    return X, time_stamps
