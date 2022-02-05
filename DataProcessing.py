import matplotlib.pyplot as plt
import pandas as pd
import os, json


def create_player_table(match_num, player_num):
    rdir = 'eSports_Sensors_Dataset-master/matches/match_' + str(match_num) + '/player_' + str(player_num)
    df0 = pd.DataFrame
    fin_df = pd.DataFrame
    ind = 0

    for subdir, dirs, files in os.walk(rdir):
        for file in files:
            split_tup = os.path.splitext(file)
            file_name = split_tup[0]
            file_extension = split_tup[1]

            if file_extension == '.csv':
                # print(os.path.join(subdir, file))
                # print(ind)
                df0 = pd.read_csv(os.path.join(subdir, file))

                ind += 1

                if ind == 1:
                    fin_df = df0
                    continue

                if file_name == 'imu_chair_back':
                    fin_df = fin_df.merge(df0, on='time', how='outer').rename(columns={'linaccel_x': 'linaccel_x_back',
                    'linaccel_y': 'linaccel_y_back', 'linaccel_z': 'linaccel_z_back', 'gravity_x': 'gravity_x_back',
                    'gravity_y': 'gravity_y_back', 'gravity_z': 'gravity_z_back', 'gyro_x': 'gyro_x_back',
                    'gyro_y': 'gyro_y_back',  'gyro_z': 'gyro_z_back', 'euler_x': 'euler_x_back', 'euler_y': 'euler_y_back',
                    'euler_z': 'euler_z_back', 'quaternion_w': 'quaternion_w_back', 'quaternion_x': 'quaternion_x_back',
                    'quaternion_y': 'quaternion_y_back', 'quaternion_z': 'quaternion_z_back'})

                elif file_name == 'imu_chair_seat':
                    fin_df = fin_df.merge(df0, on='time', how='outer').rename(columns={'linaccel_x': 'linaccel_x_seat',
                                                                                       'linaccel_y': 'linaccel_y_seat',
                                                                                       'linaccel_z': 'linaccel_z_seat',
                                                                                       'gravity_x': 'gravity_x_seat',
                                                                                       'gravity_y': 'gravity_y_seat',
                                                                                       'gravity_z': 'gravity_z_seat',
                                                                                       'gyro_x': 'gyro_x_seat',
                                                                                       'gyro_y': 'gyro_y_seat',
                                                                                       'gyro_z': 'gyro_z_seat',
                                                                                       'euler_x': 'euler_x_seat',
                                                                                       'euler_y': 'euler_y_seat',
                                                                                       'euler_z': 'euler_z_seat',
                                                                                       'quaternion_w': 'quaternion_w_seat',
                                                                                       'quaternion_x': 'quaternion_x_seat',
                                                                                       'quaternion_y': 'quaternion_y_seat',
                                                                                       'quaternion_z': 'quaternion_z_seat'})

                elif file_name == 'imu_right_hand':
                    fin_df = fin_df.merge(df0, on='time', how='outer').rename(columns={'linaccel_x': 'linaccel_x_rh',
                                                                                       'linaccel_y': 'linaccel_y_rh',
                                                                                       'linaccel_z': 'linaccel_z_rh',
                                                                                       'gravity_x': 'gravity_x_rh',
                                                                                       'gravity_y': 'gravity_y_rh',
                                                                                       'gravity_z': 'gravity_z_rh',
                                                                                       'gyro_x': 'gyro_x_rh',
                                                                                       'gyro_y': 'gyro_y_rh',
                                                                                       'gyro_z': 'gyro_z_rh',
                                                                                       'euler_x': 'euler_x_rh',
                                                                                       'euler_y': 'euler_y_rh',
                                                                                       'euler_z': 'euler_z_rh',
                                                                                       'quaternion_w': 'quaternion_w_rh',
                                                                                       'quaternion_x': 'quaternion_x_rh',
                                                                                       'quaternion_y': 'quaternion_y_rh',
                                                                                       'quaternion_z': 'quaternion_z_rh'})

                elif file_name == 'imu_left_hand':
                    fin_df = fin_df.merge(df0, on='time', how='outer').rename(columns={'linaccel_x': 'linaccel_x_lh',
                                                                                       'linaccel_y': 'linaccel_y_lh',
                                                                                       'linaccel_z': 'linaccel_z_lh',
                                                                                       'gravity_x': 'gravity_x_lh',
                                                                                       'gravity_y': 'gravity_y_lh',
                                                                                       'gravity_z': 'gravity_z_lh',
                                                                                       'gyro_x': 'gyro_x_lh',
                                                                                       'gyro_y': 'gyro_y_lh',
                                                                                       'gyro_z': 'gyro_z_lh',
                                                                                       'euler_x': 'euler_x_lh',
                                                                                       'euler_y': 'euler_y_lh',
                                                                                       'euler_z': 'euler_z_lh',
                                                                                       'quaternion_w': 'quaternion_w_lh',
                                                                                       'quaternion_x': 'quaternion_x_lh',
                                                                                       'quaternion_y': 'quaternion_y_lh',
                                                                                       'quaternion_z': 'quaternion_z_lh'})

                else:
                    fin_df = pd.merge(fin_df, df0, on='time', how='outer')

    # Check the team and create a column
    json_file = open('eSports_Sensors_Dataset-master/matches/match_' + str(match_num) + '/meta_info.json')
    team = json.load(json_file)

    fin_df = fin_df.assign(team=team['team'])

    return fin_df


if __name__ == "__main__":
    dfc = create_player_table(0, 0)
    print(dfc.columns.tolist())

    for i in range(0, 22):
        for j in range(0, 5):
            if not(i == 0 and j == 0):
                df = create_player_table(i, j)
                dfc = pd.concat([dfc, df], ignore_index=True).sort_index()

    dfc.to_csv('DataFrame.csv')

    # for subdir, dirs, files in os.walk(rootdir):
    #     for file in files:
    #         print(os.path.join(subdir, file))
