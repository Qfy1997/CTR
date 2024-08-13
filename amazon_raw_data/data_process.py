import pickle 
import numpy as np
import random
import chardet

with open('reviews.pkl', 'rb') as f:
  reviews_df = pickle.load(f)
  reviews_df = reviews_df[['reviewerID', 'asin', 'unixReviewTime']]
with open('meta.pkl', 'rb') as f:
  meta_df = pickle.load(f)
  meta_df = meta_df[['asin', 'categories']]
  meta_df['categories'] = meta_df['categories'].map(lambda x: x[-1][-1])


def build_map(df, col_name):
  key = sorted(df[col_name].unique().tolist())
  m = dict(zip(key, range(len(key))))
  df[col_name] = df[col_name].map(lambda x: m[x])
  return m, key


if __name__=='__main__':
    vec_file="../din/glove/soft_embed_for_item_reviews"
    item_emb_file="../din/glove/item_emb.txt"
    user_emb_file="../din/glove/user_emb.txt"
    category_file="../din/glove/category_emb.txt"

    all_vec={}
    with open(vec_file,"r") as f:
        lines=f.readlines()
        for line in lines:
            # print(line.split())
            key=line.split()[0]
            value=line.split()[1:]
            # print(key)
            # print(value)
            all_vec.update({key:value})
    #         # break
    # # print(all_vec)
    # print(len(all_vec))
    asin_map, asin_key = build_map(meta_df, 'asin')
    cate_map, cate_key = build_map(meta_df, 'categories')
    revi_map, revi_key = build_map(reviews_df, 'reviewerID')
    # # print(asin_map)
    # # print(cate_map)
    new_cate_map={}
    for (key,value) in cate_map.items():
        new_key=""
        for item in key.split():
            new_key+=item+"_"
        new_key=new_key[:-1]
        # print("key:",key,"value:",value)
        # print("new_key:",new_key,"value:",value)
        new_cate_map.update({new_key:value})
        # break
    # print(new_cate_map)
    with open(item_emb_file, "a") as text_file:
        for (key,value) in asin_map.items():
            emb=all_vec[key]
            text_file.write(key+" ")
            for item in emb:
                text_file.write(item+" ")
            text_file.write("\n")
    
    with open(user_emb_file, "a") as text_file:
        for (key,value) in revi_map.items():
            emb=all_vec[key]
            text_file.writelines(key+" ")
            for item in emb:
                text_file.write(item+" ")
            text_file.write("\n")
    
    with open(category_file, "a") as text_file:
        for (key,value) in new_cate_map.items():
            emb=all_vec[key]
            text_file.writelines(key+" ")
            for item in emb:
                text_file.write(item+" ")
            text_file.write("\n")
    # print("finish")
    


    # for (key,value) in revi_map.items():
    #     print("key:",key,"value:",value)
    #     break
    # for (key,value) in asin_map.items():
    #     print("key:",key,"value:",value)
    #     break

    # print(len(revi_map))
    # print(len(asin_map))
    # print(revi_map)
    # file1=open("meta.pkl","rb")
    # file2=open("reviews.pkl","rb")
    # file3=open("remap.pkl","rb")
    # file4=open("../din/dataset.pkl","rb")
    # # file5=open("../din/aa","rb") 
    # reviews_df = pickle.load(file3)
    # cate_list = pickle.load(file3)
    # user_count, item_count, cate_count, example_count = pickle.load(file3)
    # print(reviews_df)
    # print(cate_list)
    # print(user_count)
    # print(item_count)
    # print(cate_count)
    # print(reviews_df.groupby('reviewerID'))
    # print(reviews_df.loc[5])
    # train_set=[]
    # test_set=[]
    # for reviewerID, hist in reviews_df.groupby('reviewerID'):
    #     print(reviewerID)
    #     print(hist)
    #     pos_list = hist['asin'].tolist()
    #     print(pos_list)
    #     def gen_neg():
    #         neg = pos_list[0]
    #         while neg in pos_list:
    #             neg = random.randint(0,item_count-1)
    #         return neg
    #     neg_list = [gen_neg() for i in range(len(pos_list))]
    #     print(neg_list)
    #     for i in range(1,len(pos_list)):
    #         hist = pos_list[:i]
    #         if i != len(pos_list) -1:
    #             train_set.append((reviewerID,hist,pos_list[i],1))
    #             train_set.append((reviewerID,hist,neg_list[i],0))
    #         else:
    #             label = (pos_list[i],neg_list[i])
    #             test_set.append((reviewerID,hist,label))
    #     print(train_set)
    #     print(test_set)
    #     break
    # data = file5.read()
    # print(type(data))
    # # print(chardet.detect(data))
    # result=chardet.detect(data)
    # print(result['encoding'])
    # data.decode(encoding="UTF-8",errors="strict")
    # print(data[:120])
    # train_set = pickle.load(file4)
    # test_set= pickle.load(file4)
    # cate_list = pickle.load(file4)
    # print(len(train_set))
    # print(len(train_set))