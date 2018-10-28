# csvの整形

import pandas as pd
import os

input_filepath = 'C:\\Users\\sakai\\Desktop\\workshop\\Fitbit\\output\\'
output_filepath = 'C:\\Users\\sakai\\Desktop\\workshop\\Fitbit\\output_editinterval\\'

# filenameパス配下のフォルダ名を全取得
filename_list = os.listdir(input_filepath)

for filename in filename_list:

    csv_path_before = input_filepath + filename

    #index_col=0にすることでcsv読み込みするときにindexを読み込まなくなる
    df = pd.read_csv(csv_path_before)

    # 型直し
    df['time'] = pd.to_datetime(df['time'])
    df['value'] = df['value'].astype(int)
    df['unix'] = df['unix'].astype(int)

    # indexにした後だと型変更できないので、型変換した後にindexを設定
    dfi = df.set_index('time')

    # 5秒毎平均をとる
    fm = dfi.resample('5S', label='left').mean().interpolate(method = 'spline', order=2)

    csv_path_after = output_filepath + 'spline_' + filename[:len(filename)-4] + '_out.csv'

    fm.to_csv(csv_path_after)
