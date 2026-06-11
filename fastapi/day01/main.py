'''
문제 1. 쉬움
요구사항
/items/ 경로를 만든다.
쿼리 매개변수:
q: 선택값
문자열이어야 함
최소 길이 3
최대 길이 20
동작:
q가 없으면 {"q": null} 반환
q가 있으면 {"q": q} 반환
'''

# from fastapi import FastAPI, Query
# from pydantic import Annotated

# app = FastAPI()

# @app.get('/items/')
# def get_item(q: Annotated[str | None, Query(min_length=3, max_length=20)] = None):
#     return {"q": q}

'''
문제 2. 쉬움
요구사항
/users/{user_id} 경로를 만든다.
경로 매개변수:
user_id: 정수
1 이상이어야 함
'''

# from fastapi import FastAPI, Path
# from pydantic import Annotated

# app = FastAPI()

# @app.get('/users/{user_id}')
# def get_user_id(user_id: Annotated[int, Path(ge=1)]):
#     return {"user_id": user_id}

'''
문제 3. 중간
요구사항
/products/ 경로를 만든다.
쿼리 매개변수:
keyword: 필수 문자열
최소 길이 2
최대 길이 30
category: 선택 문자열
기본값은 "all"
허용 패턴은 영어 소문자와 하이픈만 가능
예: book, food, home-appliance
'''

# from fastapi import FastAPI, Query
# from pydantic import Annotated

# app = FastAPI()

# @app.get('/products/')
# def find_product(
#     keyword: Annotated[str, Query(min_length=2, max_length=30)],
#     category: Annotated[str, Query(pattern="^[a-z-]+$")] = "all"
# ):
#     return {"keyword": keyword, "category": category}

'''
문제 4. 중간
요구사항
/orders/{order_id} 경로를 만든다.
경로 매개변수:
order_id: 정수
1000 이상
9999 이하
쿼리 매개변수:
include_detail: 불리언
기본값은 False
'''

# from fastapi import FastAPI, Path
# from pydantic import Annotated

# app = FastAPI()

# @app.get('/orders/{order_id}')
# def order(
#     order_id: Annotated[int, Path(ge=1000,le=9999)],
#     include_detail: Annotated[bool] = False
# ):
#     return {"order_id": order_id, "include_detail": include_detail}

'''
문제 5. 실전형
요구사항
도서 검색 API를 만든다.
경로:
GET /books/{book_id}
경로 매개변수:
book_id: 정수
1 이상
100000 이하
쿼리 매개변수:
title: 선택 문자열최소 길이 2
최대 길이 50

author: 선택 문자열최소 길이 2
최대 길이 30

isbn: 선택 문자열패턴: 숫자 13자리만 허용

page: 정수기본값 1
1 이상

size: 정수기본값 10
1 이상
100 이하

동작:
요청받은 값을 그대로 JSON으로 반환한다.
응답 형태:
{
  "book_id": book_id,
  "title": title,
  "author": author,
  "isbn": isbn,
  "page": page,
  "size": size
}
'''

# from fastapi import FastAPI, Query, Path
# from pydantic import Annotated

# app = FastAPI()

# @app.get('/books/{book_id}')
# def search_book(
#     book_id: Annotated[int, Path(ge=1, le=100000)],
#     title: Annotated[str | None, Query(min_length=2, max_length=50)] = None,
#     author: Annotated[str | None, Query(min_length=2, max_length=30)] = None,
#     isbn: Annotated[str | None, Query(pattern="^[0-9]{13$}")] = None,
#     page: Annotated[int, Query(ge=1)] = 1,
#     size: Annotated[int, Query(ge=1,le=100)] = 10
# ):
#     return{
#         "book_id": book_id,
#         "title": title,
#         "author": author,
#         "isbn": isbn,
#         "page": page,
#         "size": size
#     }