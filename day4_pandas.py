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

