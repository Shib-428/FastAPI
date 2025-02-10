from fastapi import FastAPI, Depends
import uvicorn

from Schemas import PostKeywords
from Model import PlaceModel
from settings import SessionLocal

from sqlalchemy.orm import Session

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Hello World"}


# データベースからPlace一覧を取得するAPI
@app.get("/places")
def get_place(
        db: Session = Depends(get_db)
    ):
    # query関数でmodels.pyで定義したモデルを指定し、.all()関数ですべてのレコードを取得
    return db.query(PlaceModel).all()

# Placeを作成するAPI
@app.post("/places")
def post_place(
        keywords: PostKeywords, 
        db: Session = Depends(get_db)
    ):
    # 受け取ったkeywordsを元にGoogleMapAPIにリクエストを送信
    # レスポンスデータを元にPlaceモデルを作成
    """Mapper, APIHundler実装までの一時的な処理"""
    db_model = PlaceModel(
        name=keywords.keywords + 'name',
        place_id=keywords.keywords + 'place_id',
        formatted_address=keywords.keywords + 'formatted_address',
        formatted_phone_number=keywords.keywords + 'formatted_phone_number',
        rating=3.1,
        user_rating_total=2.5,
        url=keywords.keywords + 'url',
    )
    # データベースに登録（インサート）
    db.add(db_model)
    # 変更内容を確定
    db.commit()
    """ここまで一時的な処理"""

    return {"message": "success"}

# Placeを削除するAPI
@app.delete("/places/{id}")
def delete_place(
        id: int,
        db: Session = Depends(get_db)
    ):
    delete_place = db.query(PlaceModel).filter(PlaceModel.id==id).one()
    db.delete(delete_place)
    db.commit()

    return {"message": "success"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")