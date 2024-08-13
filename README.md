## 用于Click-Through-Rate预测的改进型深度学习网络

在[Deep Interst Network](http://github.com/zhougr1993/DeepInterestNetwork/tree/master/din)之上进行一些探索性研究。

## Conda环境所需的python及其库的版本

* Python >= 3.7.0
* numpy >= 1.21.6
* pandas >= 1.1.5
* tensorflow >= 1.15.0

## 下载数据集并对数据集进行预处理

1.创建amazon_raw_data文件夹并执行下载数据集的shell脚本:

```sh
mkdir amazon_raw_data
cd utils
bash 0_download_raw.sh
```

2.将原始数据转换成pandas dataframe形式并对数据集中的物品id、物品所属类别的id、评论用户id构造映射

```python
python 1_convert_pd.py
python 2_remap_id.py
```

## 模型训练与评价

1.进入din文件夹下并执行train.py，并将输出的内容输入到log.txt中。

```
cd din
python train.py > log.txt 2>&1 & 
```
