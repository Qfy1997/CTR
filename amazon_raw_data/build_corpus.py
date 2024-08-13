import json
import pandas as pd
import pickle

def to_df(file_path):
  with open(file_path, 'r') as fin:
    df = {}
    i = 0
    for line in fin:
      df[i] = eval(line)
      i += 1
    df = pd.DataFrame.from_dict(df, orient='index')
    return df,i

if __name__=='__main__':
    # meta_Electronics="meta_Electronics.json"
    with open('meta.pkl', 'rb') as f:
        meta_df = pickle.load(f)
        meta_df = meta_df[['asin', 'categories']]
        meta_df['categories'] = meta_df['categories'].map(lambda x: x[-1][-1])
    asin_to_categories={}
    for i in range(len(meta_df)):
        asin_to_categories.update({meta_df.loc[i]['asin']:meta_df.loc[i]['categories']})

    reviews_Electronics="reviews_Electronics_5.json"
    # meta_df,meta_df_len=to_df(meta_Electronics)
    reviews_df,reviews_df_len=to_df(reviews_Electronics)
    # meta_sentences=[]
    review_sentences=[]
    # print(meta_df.loc[0])
    # print(meta_df.loc[0]['asin'])
    # print(meta_df.loc[0]['categories'])
    # print(meta_df.loc[0]['title'])
    # print(meta_df.loc[0]['description'])
    # print("===========")
    # print(itemID)
    # print(itemCategories)
    # print(itemTitle)
    # print(itemDescription)
    # print("============")
    # for i in range(meta_df_len):
    #     itemID=meta_df.loc[i]['asin']
    #     itemCategories=meta_df.loc[i]['categories'][-1][-1]
    #     itemTitle=meta_df.loc[i]['title']
    #     itemDescription=meta_df.loc[i]['description']
    #     sentence="The "
    #     sentence+=str(itemID)
    #     sentence+=" is part of "

    #     item_cat=str(itemCategories)
    #     item_cat=item_cat.split()
    #     new_item_cat=""
    #     for item in item_cat:
    #         new_item_cat+=item+"_"
        
    #     sentence+=new_item_cat[:-1]
        
    #     sentence+=" called "
    #     sentence+=str(itemTitle)
    #     sentence+=" . "
    #     # sentence+=str(itemDescription)
    #     meta_sentences.append(sentence)
    # for item in meta_sentences[0].split():
    #     print(item)
    
    # print(meta_df_len)

    # with open("item_corpus", "a") as text_file:
    #     for k in range(meta_df_len):
    #         for item in meta_sentences[k].split():
    #             text_file.write(item+" ")

    # print(len(meta_sentences))
    # print(meta_sentences[0])
    # print("============")
    # print(type(meta_df.loc[0]))
    # print(meta_df.keys())
    # print(reviews_df.loc[0])
    # print(reviews_df.loc[0]['reviewerID'])
    # print(reviews_df.loc[0]['reviewText'])
    # print(reviews_df.loc[0]['summary'])
    # print(type(meta_df.loc[0]))
    # print(reviews_df.keys())
    # print("==============")
    for i in range(reviews_df_len):
        reviewerID=reviews_df.loc[i]['reviewerID']
        # reviewText=reviews_df.loc[i]['reviewText']
        summary=reviews_df.loc[i]['summary']
        asin=reviews_df.loc[i]['asin']
    # print(reviewerID)
    # print(reviewText)
    # print(summary)
    # print("================")
        reviewSentence="The reviewer "
        reviewSentence+=str(reviewerID)
        reviewSentence+=" reviews of "
        reviewSentence+=str(asin)
        category=asin_to_categories[asin]
        item_cat=str(category)
        item_cat=item_cat.split()
        new_item_cat=""
        for item in item_cat:
            new_item_cat+=item+"_"
        reviewSentence+=" which is part of "
        reviewSentence+=new_item_cat[:-1]
        reviewSentence+=" summarized as "
        # reviewSentence+=str(reviewText)
        # reviewSentence+=" ' summarized ' "
        reviewSentence+=str(summary)
        reviewSentence+=" "
        review_sentences.append(reviewSentence)
        # print(review_sentences)
        # break
    # print(review_sentences[0])
    # for item in review_sentences[0].split():
    #     print(item)
    # print(reviews_df_len)
    # print(len(review_sentences))
    # print(review_sentences[0])
    # j=0
    # with open("reviews_corpus", "a") as text_file:
    #     # for k in range(meta_df_len):
    #     #     for item in meta_sentences[k].split():
    #     #         text_file.write(item+" ")
    #     #     print(k)
    #     for j in range(reviews_df_len):
    #         for item in review_sentences[j].split():
    #             text_file.write(item+" ")
    #         print(j)
    with open("item_reviews", "a") as text_file:
        # for k in range(meta_df_len):
        #     for item in meta_sentences[k].split():
        #         text_file.write(item+" ")
        #     print(k)
        for j in range(reviews_df_len):
            for item in review_sentences[j].split():
                text_file.write(item+" ")
            print(j)
   
        
            
