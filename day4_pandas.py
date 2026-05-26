import pandas as pd
raw_data = {
    "compound_id": ["Comp-A", "Comp-B", "Comp-C"],
    "ic50_normal": [50.0, 12.5, 80.0],  
    "ic50_cancer": [0.05, 2.50, 0.01]   
}
df = pd.DataFrame(raw_data)

df["selectivity_index"] = df["ic50_normal"] / df["ic50_cancer"]

df["is_safe"] = df["selectivity_index"] >= 1000

print(" 最终处理完的化合物数据集 ")
print(df)


df解释：形式如：df["列名"].这时候，它指的就是表格里的某一列数据。它的作用是精准定位，把这一列当成一个整体拎出来。形式如：df[ 里面是判断句 ]外层这个大括号就变成了一个只能由行（Row）通过的筛子。
import pandas as pd
import numpy as np
raw_data = {
    "compound_id": ["Comp-1", "Comp-2", "Comp-3"],
    "ic50": [0.02, np.nan, 0.08]  # Comp-2 缺失
}
df = pd.DataFrame(raw_data)
df["ic50_is_missing"] = df["ic50"].isna()
mean_ic50 = df["ic50"].mean()
df["ic50"] = df["ic50"].fillna(mean_ic50)
print("工业级清洗后的完美数据集")
print(df)
