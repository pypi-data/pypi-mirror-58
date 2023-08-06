import os
from sklearn.preprocessing import LabelEncoder
from . import audio_data
from . import depth_data
from . import model
from . import predict

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


def predictADL(audio_file_path, depth_file_path, audio_start_timestamp, depth_start_timestamp, depth_end_timestamp, show_video=False,
               sil_model_path=r"models/2019_09_27_02_56_29_2", classifier_path=r"models/15_07_14_acc_92", depth_skipping_frames=1,
               depth_win_size=15, hop_length=1, selectedActivities=['StandStill', 'Walking', 'SitStill', 'Sitting', 'PickingObject',
                                                                    'Sleeping', 'StandUp', 'LyingDown', 'Falling', 'WakeUp']):

    nr_audio, sample_rate, datetime_audio = audio_data.processAudioData(
        audio_file_path, audio_start_timestamp)

    sil_model = model.getModel(sil_model_path)
    classifier_model = model.getModel(classifier_path)

    video, timeStamps = depth_data.getDepthVideo(
        depth_file_path, sil_model, 480, 640, depth_start_timestamp, depth_end_timestamp)

    lb = LabelEncoder()
    lb.fit_transform(selectedActivities)

    predictions = predict.predict(classifier_model, video, timeStamps, nr_audio, sample_rate,
                                  datetime_audio, selectedActivities, depth_skipping_frames, depth_win_size, hop_length)

    predict.printResult(predictions, lb, timeStamps)

    if(show_video):
        predict.show(video, predictions, lb)
