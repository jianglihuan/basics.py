# 1. 字符串类型（给抽屉起名叫 protein_name，里面塞入文本）
protein_name = "SLC25A48"
amino_acid_seq = "MAGAAAG..."

# 2. 整数类型（数量、长度）
sequence_length = 315
atom_count = 2450

# 3. 浮点数类型（小数、实验数据）
molecular_weight = 34.8  # 单位是 kDa
binding_affinity = 1.25  # 单位是 uM

# 4. 怎么把它们打印出来看？用 print() 函数
print(protein_name)
print(sequence_length)
# 假设这是一个蛋白质的部分氨基酸序列列表
seq_list = ["M", "A", "G", "A", "A", "A", "G"]

# 截取前 3 个氨基酸（注意：切片规则是“顾头不顾尾”，不包含结束位置本身）
sub_seq = seq_list[0:3]  # 拿到 ["M", "A", "G"]
