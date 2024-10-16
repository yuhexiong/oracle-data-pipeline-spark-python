# Oracle Data Pipeline Spark

Data pipeline written by Spark to transfer Oracle to Doris.  

## Overview

- Language: Python
- Data Processing Framework: Spark v3.5.1


## Run

### Run Docker Container

edit filename in docker-compose.yaml  
```
docker compose up -d
```


## Entry

### Oracle To Doris

code refer to  
(1) [oracle_to_doris.py](oracle_to_doris.py)  
(2) define schema in yaml [oracle_to_doris_yaml.py](oracle_to_doris_yaml.py) and [oracle_to_doris.yaml](oracle_to_doris.yaml)  


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
