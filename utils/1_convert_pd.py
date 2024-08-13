import pickle
import pandas as pd

"""
    将原始数据转换成pandas dataframe形式并写入到pickle文件中
"""

# 按行读取文件，并将每行数据转换成pandas.dataframe形式。
def to_df(file_path):
  with open(file_path, 'r') as fin:
    df = {}
    i = 0
    for line in fin:
      df[i] = eval(line)
      i += 1
    df = pd.DataFrame.from_dict(df, orient='index')
    return df

# 对"../amazon_raw_data/reviews_Electronics_5.json"进行处理。
# 该文件中包含的key有:reviewerID、asin、reviewerName、helpful、reviewText、overall、summary、unixReviewTime、reviewTime
reviews_df = to_df('../amazon_raw_data/reviews_Electronics_5.json')
# print(reviews_df.keys())

# 将reviews_df中的数据写入到pickle文件中。
# 该文件中包含的key有:asin、imUrl、description、categories、title、
with open('../amazon_raw_data/reviews.pkl', 'wb') as f:
  pickle.dump(reviews_df, f, pickle.HIGHEST_PROTOCOL)

meta_df = to_df('../amazon_raw_data/meta_Electronics.json')
meta_df = meta_df[meta_df['asin'].isin(reviews_df['asin'].unique())]
meta_df = meta_df.reset_index(drop=True)
# print(meta_df.keys())

# 将meta_df中的数据写入到pickle文件中。
with open('../amazon_raw_data/meta.pkl', 'wb') as f:
  pickle.dump(meta_df, f, pickle.HIGHEST_PROTOCOL)
