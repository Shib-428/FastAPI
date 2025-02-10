##### 1.Place一覧が空であることを確認
|Method|Request URL|Code|
|--|--|--|
|GET|http://localhost:8000/places|200|

##### Request body
なし

##### Response body
```json
[]
```
---
##### 2.Placeを作成
|Method|Request URL|Code|
|--|--|--|
|POST|http://localhost:8000/places|200|

##### Request body
```json
{
  "keywords": "キーワード"
}
```

##### Response body
```json
{
  "message": "success"
}
```
---
##### 3.作成したPlaceを確認
|Method|Request URL|Code|
|--|--|--|
|GET|http://localhost:8000/places|200|

##### Request body
なし

##### Response body
```json
[
  {
    "formatted_address": "キーワードformatted_address",
    "id": 1,
    "name": "キーワードname",
    "rating": 3.1,
    "url": "キーワードurl",
    "formatted_phone_number": "キーワードformatted_phone_number",
    "place_id": "キーワードplace_id",
    "user_rating_total": 2.5
  }
]
```
---
##### 4.Placeを削除
|Method|Request URL|Code|
|--|--|--|
|DELETE|http://localhost:8000/places/1|200|

##### Request body
なし

##### Response body
```json
{
  "message": "success"
}
```
---