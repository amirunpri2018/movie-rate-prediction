# NAVER Movie Rate Prediction
네이버 영화 평점 예측 with Tensorflow

## Environments
* OS  : Windows 10 / Linux Ubuntu x86-64 ~
* CPU : any (quad core ~)
* GPU : GTX 1060 6GB ~
* RAM : 16GB ~
* Library : TF 1.x with CUDA 9.0~ + cuDNN 7.0~
* Python 3.x

## Prerequisites
* python 3.x
* tensorflow 1.x
* numpy
* gensim or konlpy or soynlp
* pymysql
* tqdm
* Internet :)

## DataSets

| DataSet  |  Language  | Sentences | Size |
|:---:|:---:|:---:|:---:|
| [NAVER Movie Review](http://movie.naver.com) | *Korean* | ```5.36M``` | ```About 557MB``` | 

## Usage
### 1. Installing Dependencies
    $ sudo python3 -m pip install -r requirements.txt
### 2. Parsing the DataSet
    $ python3 movie-parse.py --n_threads 8
### 3. Making DataSet DB
    # you need to edit 'db_infos' at line 13, fitting in your env.
    $ python3 db.py
### 4. Making w2v dictionary
    $ python3 preprocessing.py
### 5. Training a M.L Model
    $ python3 train.py
### 6. Testing a M.L Model
    $ python3 test.py

## Repo Tree
```
│
├── comments
│    ├── 10000.sql
│    ├── ...
│    └── 200000.sql   (NAVER Movie Review DataSets)
├── movie-parser.py   (NAVER Movie Review Parser)
├── db.py             (DataBase processing)
├── preprocessing.py  (Korean NLP verctoize)
├── train.py          (for model training)
└── test.py           (for evaluation)
```

## Pre-Trained Models

Here's a **google drive link**. You can download pre-trained models from [~~here~~]() !

## Models

soon!

## Results

soon!

## To-Do
1. Pre-Processing DataSet
2. Implement Models

## ETC

**Any suggestions and PRs and issues are WELCONE :)**

## Author
HyeongChan Kim / [@kozistr](http://kozistr.tech)
