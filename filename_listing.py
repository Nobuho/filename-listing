import glob
import os
import re
import pandas as pd

# 親フォルダのパス
dir_path = "C:\\Users\\1300793\\Box\\BIMツール開発室\\050_共通ベンダー\\101_Infosys\\I_T_Shared\\30_設計・開発_DC\\34_データ項目検討\\000_共通_COM\\CD_Tables"

# 除外する文字列
ignore_words = ["_old", "_bak", "参考資料", "PDF（確認用）"]

files_all = [f for f in glob.glob(dir_path + "/**/*.*", recursive=True)]
files_ignored = [i for i in files_all if not any([re.search(".*" + p + ".*", i) for p in ignore_words])]

file_names = [os.path.basename(i) for i in files_ignored]
file_paths = [re.sub(r"C:\\Users\\.*?\\", "", i) for i in files_ignored]

df = pd.DataFrame({"file_name": pd.Series(file_names), "file_path": pd.Series(file_paths)})
df.to_csv("files.csv", encoding='utf_8_sig')