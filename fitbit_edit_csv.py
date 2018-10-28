# fitbitのcsvファイルを整形します

import pandas as pd
import os

input_filepath = 'C:\\Users\\sakai\\Desktop\\workshop\\Fitbit\\'
output_filepath = 'C:\\Users\\sakai\\Desktop\\workshop\\Fitbit\\output\\'

# filenameパス配下のフォルダ名を全取得
filename_list = os.listdir(input_filepath)

for filename in filename_list:
    # 末尾四文字がが.csv以外のものには処理をしない
    if filename[-4:] != '.csv':
        continue
    
    csv_path_before = input_filepath + filename

    #index_col=0にすることでcsv読み込みするときにindexを読み込まなくなる
    df = pd.read_csv(csv_path_before, index_col=0)

    # 二次元から一次元に変更（indexを消してcolumnに）
    df = df.reset_index()

    # columnの順番を以下に変更(timeを主キーに)
    df = df.loc[:, ['time', 'value', 'unix']]

    csv_path_after = output_filepath + filename[:len(filename)-4] + '_out.csv'

    df.to_csv(csv_path_after, index=False)