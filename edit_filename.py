#filenameにスペースが入っているのでアンダースコアに訂変更

import os

filepath = 'C:\\Users\\sakai\\Desktop\\workshop\\Fitbit\\'
filename_list = os.listdir(filepath)

for filename in filename_list:
    after_filename = filename.replace(' ', '_')
    os.rename(filepath + filename, filepath + after_filename)