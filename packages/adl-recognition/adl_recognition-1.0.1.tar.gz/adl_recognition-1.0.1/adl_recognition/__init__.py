import os
from sklearn.preprocessing import LabelEncoder
from . import audio_data
from . import depth_data
from . import model
from . import predict

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


def predict_continuous_adl(audio_file, depth_file, audio_start_timestamp, depth_start_timestamp,
                           depth_end_timestamp, depth_frame_height=480, depth_frame_width=640, show_video=False,
                           sil_model_path=r"models/2019_09_27_02_56_29_2", classifier_path=r"models/15_07_14_acc_92",
                           depth_skipping_frames=1, depth_win_size=15, hop_length=1,
                           selected_activities=None):
    if selected_activities is None:
        selected_activities = ['StandStill', 'Walking', 'SitStill', 'Sitting', 'PickingObject', 'Sleeping', 'StandUp',
                               'LyingDown', 'Falling', 'WakeUp']
    nr_audio, sample_rate, datetime_audio = audio_data.process_audio_data(audio_file, audio_start_timestamp)

    sil_model = model.get_model(sil_model_path)
    classifier_model = model.get_model(classifier_path)

    video, timestamps = depth_data.get_depth_video(depth_file, sil_model, depth_frame_height, depth_frame_width,
                                                   depth_start_timestamp, depth_end_timestamp)

    lb = LabelEncoder()
    lb.fit_transform(selected_activities)

    predictions = predict.predict_continuous_activities(classifier_model, video, timestamps, nr_audio, sample_rate,
                                                        datetime_audio, selected_activities, depth_skipping_frames,
                                                        depth_win_size, hop_length)

    predict.print_result(predictions, lb, timestamps)

    if show_video:
        predict.show(video, predictions, lb)


def predict_single_adl(audio_file, depth_file, audio_start_timestamp, depth_start_timestamp,
                       depth_end_timestamp, depth_frame_height=480, depth_frame_width=640,
                       sil_model_path=r"models/2019_09_27_02_56_29_2", classifier_path=r"models/15_07_14_acc_92",
                       depth_win_size=15, selected_activities=None):
    if selected_activities is None:
        selected_activities = ['StandStill', 'Walking', 'SitStill', 'Sitting', 'PickingObject', 'Sleeping',
                               'StandUp', 'LyingDown', 'Falling', 'WakeUp']
    nr_audio, sample_rate, datetime_audio = audio_data.process_audio_data(audio_file, audio_start_timestamp)

    sil_model = model.get_model(sil_model_path)
    classifier_model = model.get_model(classifier_path)

    video, time_stamps = depth_data.get_depth_video(depth_file, sil_model, depth_frame_height, depth_frame_width,
                                                    depth_start_timestamp, depth_end_timestamp)

    lb = LabelEncoder()
    lb.fit_transform(selected_activities)

    predictions = predict.predict_single_activity(classifier_model, video, time_stamps, nr_audio, sample_rate,
                                                  datetime_audio, depth_win_size)

    predict.print_result(predictions, lb, time_stamps)
