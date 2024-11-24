# Oracle Data Pipeline Spark

使用 Spark 撰寫把 Oracle 轉換至 Doris 的資料管道。

## Overview

- 語言: Python
- 資料轉換框架: Spark v3.5.1


## Run

### Run Docker Container

修改 docker-compose.yaml 裡面的檔名    
```
docker compose up -d
```


## Entry

### Oracle To Doris

轉換換行符號為空字串  
將 `RATING` 欄位的 NULL 補值為 0  

程式碼參考  
(1) [oracle_to_doris.py](oracle_to_doris.py)  
(2) 將資料格式定義在 yaml [oracle_to_doris_yaml.py](oracle_to_doris_yaml.py) 和 [oracle_to_doris.yaml](oracle_to_doris.yaml)  


- Oracle Table
```
| BOOKID  | TITLE               | AUTHOR              | PUBLICATIONYEAR  | GENRE           | RATING | STATUS      |
|---------|---------------------|---------------------|------------------|-----------------|--------|-------------|
| 1       | Dune                | Frank Herbert       | 1965             | SCIENCE FICTION | 4.5    | AVAILABLE   |
| 2       | 1984                | George Orwell       | 1949             | DYSTOPIAN       | 4.7    | CHECKED OUT |
| 3       | Pride and Prejudice | Jane Austen         | 1813             | ROMANCE         | 4.6    | AVAILABLE   |
| 4       | The Great Gatsby    | F. Scott Fitzgerald | 1925             | CLASSIC         | 4.4    | AVAILABLE   |
| 5       | The Hobbit          | J.R.R. Tolkien      | 1937             | FANTASY         | 4.8    | CHECKED OUT |
```


- Doris Table
```
| book_id | title               | author              | publication_year | genre           | rating | status      |
|---------|---------------------|---------------------|------------------|-----------------|--------|-------------|
| 1       | Dune                | Frank Herbert       | 1965             | SCIENCE FICTION | 4.5    | AVAILABLE   |
| 2       | 1984                | George Orwell       | 1949             | DYSTOPIAN       | 4.7    | CHECKED OUT |
| 3       | Pride and Prejudice | Jane Austen         | 1813             | ROMANCE         | 4.6    | AVAILABLE   |
| 4       | The Great Gatsby    | F. Scott Fitzgerald | 1925             | CLASSIC         | 4.4    | AVAILABLE   |
| 5       | The Hobbit          | J.R.R. Tolkien      | 1937             | FANTASY         | 4.8    | CHECKED OUT |
```
