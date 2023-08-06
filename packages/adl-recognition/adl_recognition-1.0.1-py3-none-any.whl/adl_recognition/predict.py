from . import audio_data
import numpy as np
import cv2


def predict_continuous_activities(model, video, time_stamps, nr_audio, sample_rate, datetime_audio, activities,
                                  depth_skipping_frames, depth_win_size, hop_length):
    width, height = 160, 120
    start_frame_number = 0
    num_of_frames = video.shape[0]
    num_of_activities = len(activities)
    predictions = np.zeros((num_of_frames, num_of_activities))
    for i in range(0, num_of_frames - depth_win_size * depth_skipping_frames + depth_skipping_frames, hop_length):
        array = [j for j in range(i, i + depth_win_size * depth_skipping_frames, depth_skipping_frames)]
        clip = video[array]
        audio_features = audio_data.getX_a(nr_audio, sample_rate, datetime_audio,
                                           time_stamps[array[0] + start_frame_number],
                                           time_stamps[array[-1] + start_frame_number])
        res = model.predict(
            [clip.reshape((1, clip.shape[0], height, width, 1)), audio_features.reshape((1, audio_features.shape[0]))])
        k = 0
        mid_val = (depth_win_size - 1) / 2
        for j in array:
            weight = (1 / mid_val) * (mid_val - abs(k - mid_val))
            predictions[j] += res.reshape(num_of_activities) * weight
            k += 1
    return predictions


def predict_single_activity(model, video, time_stamps, nr_audio, sample_rate, datetime_audio, depth_win_size):
    width, height = 160, 120
    start_frame_number = 0
    num_of_frames = video.shape[0]

    depth_sample_rate = num_of_frames / depth_win_size

    array = []
    for i in range(15):
        array.append(int(i * depth_sample_rate))
    clip = video[array]
    audio_features = audio_data.getX_a(nr_audio, sample_rate, datetime_audio,
                                       time_stamps[array[0] + start_frame_number],
                                       time_stamps[array[-1] + start_frame_number])
    res = model.predict(
        [clip.reshape((1, clip.shape[0], height, width, 1)), audio_features.reshape((1, audio_features.shape[0]))])
    return res


def show(video, predictions, label_encoder):
    i = 0
    previous = -1

    while True:
        if i == -1:
            i = len(predictions)
        if i == len(predictions):
            i = 0

        if i != previous:
            pred = predictions[i].copy()
            total = sum(pred)
            action = label_encoder.inverse_transform([np.argmax(pred)])[0]
            confidence = "NaN"
            if not total == 0:
                confidence = str(round(pred[np.argmax(pred)] / total, 2))

            pred[np.argmax(pred)] = 0

        img = cv2.resize((video[i] * 255).astype(np.uint8), (960, 720))
        cv2.putText(img, action + " " + confidence, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (60000, 60000, 60000),
                    lineType=cv2.LINE_AA)
        cv2.putText(img, "Controls", (20, 680), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (30000, 30000, 30000),
                    lineType=cv2.LINE_AA)
        cv2.putText(img, "Next : n / spacebar           Back : b or backspace           Exit : Esc or q", (20, 700),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (30000, 30000, 30000), lineType=cv2.LINE_AA )

        cv2.imshow("ADL predictions", img)
        k = cv2.waitKey(33)
        previous = i
        if k == 110 or k == 32:  # key n or space bar
            i += 1
        elif k == 98 or k == 8:  # key b or backspace
            i -= 1
        elif k == 113 or k == 27:  # key q or esc
            break
        if i == len(predictions):
            break

    cv2.destroyAllWindows()


def print_result(predictions, label_encoder, timestamps):
    activity = ""
    start = 0
    print()
    print("----------------------------------------------------------------------------")
    print("                               Predictions")
    print("----------------------------------------------------------------------------")
    print()
    for i in range(len(predictions)):
        new_activity = label_encoder.inverse_transform(
            [np.argmax(predictions[i])])[0]
        if activity != "" and new_activity != activity:
            print(timestamps[start], "to", timestamps[i], " : ", activity)
            start = i
        activity = new_activity
    print(timestamps[start], "to", timestamps[-1], " : ", activity)
    print()
    print("----------------------------------------------------------------------------")
