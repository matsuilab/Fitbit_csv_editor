# fitbitデータ整形  
  
1. `edit_filename.py`でcsvファイル名を変更  
スペースが入っているので気持ち悪いためアンダースコアに訂正  
  
2. `fitbit_edit_csv.py`でcsvファイル整形  
DataFrame(二次元データ構造)からSeries(一次元データ構造)に変更  
timeカラムを主キーに  
  
3. `edit_timeinterval.py`で五秒毎の平均にまとめる  
補間方法を試行錯誤中  
