import matplotlib.pyplot as plt
import pandas as pd
import os, json

rootdir = "C:/Users/Karol/Desktop/ML_Project/eSports_Sensors_Dataset-master/matches"


def create_player_table(match_num, player_num):
    rdir = 'eSports_Sensors_Dataset-master/matches/match_' + str(match_num) + '/player_' + str(player_num)
    df1_0 = pd.read_csv(rdir + '/emg.csv')
    df1_1 = pd.read_csv(rdir + '/facial_skin_temperature.csv')
    df1_2 = pd.read_csv(rdir + '/gsr.csv')
    df1_3 = pd.read_csv(rdir + '/heart_rate.csv')
    df1_4 = pd.read_csv(rdir + '/imu_chair_back.csv')
    df1_5 = pd.read_csv(rdir + '/imu_chair_seat.csv')
    df1_6 = pd.read_csv(rdir + '/imu_right_hand.csv')
    df1_7 = pd.read_csv(rdir + '/imu_left_hand.csv')
    df1_8 = pd.read_csv(rdir + '/spo2.csv')

    fin_df = pd.merge(df1_0, df1_1, on='time', how='outer')
    fin_df = pd.merge(fin_df, df1_2, on='time', how='outer')
    fin_df = pd.merge(fin_df, df1_3, on='time', how='outer')
    fin_df = pd.merge(fin_df, df1_4, on='time', how='outer')

    fin_df = pd.merge(fin_df, df1_5, on='time', how='outer', suffixes=['_back', '_seat']).merge(df1_6, on='time',
    how='outer').rename(columns={'linaccel_x': 'linaccel_x_rh', 'linaccel_y': 'linaccel_y_rh',
    'linaccel_z': 'linaccel_z_rh', 'gravity_x': 'gravity_x_rh', 'gravity_y': 'gravity_y_rh',
    'gravity_z': 'gravity_z_rh', 'gyro_x': 'gyro_x_rh',  'gyro_y': 'gyro_y_rh',  'gyro_z': 'gyro_z_rh',
    'euler_x': 'euler_x_rh', 'euler_y': 'euler_y_rh', 'euler_z': 'euler_z_rh', 'quaternion_w': 'quaternion_w_rh',
    'quaternion_x': 'quaternion_x_rh', 'quaternion_y': 'quaternion_y_rh', 'quaternion_z': 'quaternion_z_rh'}).merge(
    df1_7, on='time', how='outer').rename(columns={'linaccel_x': 'linaccel_x_lh', 'linaccel_y': 'linaccel_y_lh',
    'linaccel_z': 'linaccel_z_lh', 'gravity_x': 'gravity_x_lh', 'gravity_y': 'gravity_y_lh',
    'gravity_z': 'gravity_z_lh', 'gyro_x': 'gyro_x_lh',  'gyro_y': 'gyro_y_lh',  'gyro_z': 'gyro_z_lh',
    'euler_x': 'euler_x_lh', 'euler_y': 'euler_y_lh', 'euler_z': 'euler_z_lh', 'quaternion_w': 'quaternion_w_lh',
    'quaternion_x': 'quaternion_x_lh', 'quaternion_y': 'quaternion_y_lh', 'quaternion_z': 'quaternion_z_lh'})

    fin_df = pd.merge(fin_df, df1_8, on='time', how='outer')

    return fin_df


if __name__ == "__main__":
    df2 = pd.read_csv('eSports_Sensors_Dataset-master/matches/match_0/player_1/emg.csv')
    df1 = create_player_table(0, 0)
    print(df1)
    print(df1.columns.tolist())
    #print(df2.head())
    #print(pd.concat([df1, df2], ignore_index=True).sort_index())
    # print(pd.merge(df1, df2, on=['time', 'emg_right_hand', 'emg_left_hand'], how='outer'))

    # for subdir, dirs, files in os.walk(rootdir):
    #     for file in files:
    #         print(os.path.join(subdir, file))
