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

#字典
# 1. 创建字典：记录某候选小分子的详细档案
compound_data = {
    "id": "COMP-001",
    "smiles": "CC(=O)OC1=CC=CC=C1C(=O)O",  # 分子结构式
    "molecular_weight": 180.16,            # 分子量
    "is_toxic": False                       # 是否有毒（布尔值：真/假）
}

# 2. 通过 Key 去查询对应的 Value
# 就像查字典一样，直接把 Key 扔进方括号里
mw = compound_data["molecular_weight"]
print(mw)  # 屏幕上会打印出 180.16

# 3. 增加或修改属性
# 如果 Key 不存在，就会新建；如果存在，就会覆盖旧值
compound_data["target_protein"] = "COX-2"  # 新增靶点信息
compound_data["is_toxic"] = True           # 实验发现有毒，修改原有的值

# 4. 检查某个信息在不在字典里（常用于条件判断）
has_smiles = "smiles" in compound_data     # 结果是 True


#if else循环
protein = {"name": "SLC25A48", "status": "resolved"}
# 判断这个蛋白质的结构是否被解析
if protein["status"] == "resolved":
    print("结构已解析，可以下载 PDB 文件并用 PyMOL 查看。")
else:
    print("结构未解析，需要尝试用 AlphaFold 3 预测。")
