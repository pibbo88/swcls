import pandas as pd
import numpy as np

## parse table 2007 ##
df = pd.read_csv("tables/2007.csv", dtype=str)
l1_name_index = df[df["一级行业名称"].notna()].index
l2_name_index = df[df["二级行业名称"].notna()].index
l3_name_index = df[df["三级行业名称"].notna()].index

table1 = []
for l3_idx in l3_name_index:
    l2_idx = l2_name_index[np.searchsorted(l2_name_index, l3_idx) - 1]
    l1_idx = l1_name_index[np.searchsorted(l1_name_index, l3_idx) - 1]
   
    table1.append((df.iloc[l3_idx]["三级行业代码"], df.iloc[l3_idx]["三级行业名称"], 
                   df.iloc[l2_idx]["二级行业代码"], df.iloc[l2_idx]["二级行业名称"],
                   df.iloc[l1_idx]["一级行业代码"], df.iloc[l1_idx]["一级行业名称"],))

table1_df = pd.DataFrame(table1, columns=["l3_code", "l3_name", "l2_code", "l2_name", "l1_code", "l1_name"])
table1_df.to_csv("swcls_2007.csv")

## parse table 2011 ##
df = pd.read_csv("tables/2011.csv", dtype=str)

l1_name_index = df[df["一级行业名称"].notna()].index
l2_name_index = df[df["二级行业名称"].notna()].index
l3_name_index = df[df["三级行业名称"].notna()].index

table2 = []
for l3_idx in l3_name_index:
    l2_idx = l2_name_index[np.searchsorted(l2_name_index, l3_idx) - 1]
    l1_idx = l1_name_index[np.searchsorted(l1_name_index, l3_idx) - 1]
   
    table2.append((df.iloc[l3_idx]["三级行业代码"], df.iloc[l3_idx]["三级行业名称"], 
                   df.iloc[l2_idx]["二级行业代码"], df.iloc[l2_idx]["二级行业名称"],
                   df.iloc[l1_idx]["一级行业代码"], df.iloc[l1_idx]["一级行业名称"],))

table2_df = pd.DataFrame(table2, columns=["l3_code", "l3_name", "l2_code", "l2_name", "l1_code", "l1_name"])
table2_df.to_csv("swcls_2011.csv")

## parse table 2014 and 2021 ##
df = pd.read_excel(
    "tables/2014to2021.xlsx", 
    sheet_name="新旧对比版本2",
    header=1,
    dtype=str
)[:-1]

old_l1_name_index = df[df["旧版一级行业"].notna()].index
old_l2_name_index = df[df["旧版二级行业"].notna()].index
old_l3_name_index = df[df["旧版三级行业"].notna()].index

table3 = []
for old_l3_idx in old_l3_name_index:
    old_l2_idx = old_l2_name_index[np.searchsorted(old_l2_name_index, old_l3_idx) - 1]
    old_l1_idx = old_l1_name_index[np.searchsorted(old_l1_name_index, old_l3_idx) - 1]

    
    table3.append((df.iloc[old_l3_idx]["行业代码"], df.iloc[old_l3_idx]["旧版三级行业"], 
                   df.iloc[old_l2_idx]["行业代码"], df.iloc[old_l2_idx]["旧版二级行业"],
                   df.iloc[old_l1_idx]["行业代码"], df.iloc[old_l1_idx]["旧版一级行业"],))

table3_df = pd.DataFrame(table3, columns=["l3_code", "l3_name", "l2_code", "l2_name", "l1_code", "l1_name"])
table3_df.to_csv("swcls_2014.csv")

new_l1_name_index = df[df["新版一级行业"].notna()].index
new_l2_name_index = df[df["新版二级行业"].notna()].index
new_l3_name_index = df[df["新版三级行业"].notna()].index

table4 = []
for new_l3_idx in new_l3_name_index:
    new_l2_idx = new_l2_name_index[np.searchsorted(new_l2_name_index, new_l3_idx) - 1]
    new_l1_idx = new_l1_name_index[np.searchsorted(new_l1_name_index, new_l3_idx) - 1]

    
    table4.append((df.iloc[new_l3_idx]["行业代码.1"], df.iloc[new_l3_idx]["新版三级行业"], 
                   df.iloc[new_l2_idx]["行业代码.1"], df.iloc[new_l2_idx]["新版二级行业"],
                   df.iloc[new_l1_idx]["行业代码.1"], df.iloc[new_l1_idx]["新版一级行业"],))

table4_df = pd.DataFrame(table4, columns=["l3_code", "l3_name", "l2_code", "l2_name", "l1_code", "l1_name"])
table4_df.to_csv("swcls_2021.csv")
