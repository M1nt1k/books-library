from fastapi import APIRouter, Body, HTTPException, status
from fastapi.responses import Response, JSONResponse
from fastapi.encoders import jsonable_encoder

from bson import ObjectId

from database import db
import models.models as models

collection = 'isbn'
col = db[collection]

router = APIRouter(
    prefix=f'/api/v1/{collection}',
    tags=[f'{collection}']
)

@router.get('/')
def get_all_docs():
    res = []
    docs_res = col.find()
    for doc in docs_res:
        doc['_id'] = str(doc['_id'])
        res.append(doc)
    return res

@router.post('/', response_model=models.ISBNModel)
def add_doc(doc: models.ISBNModel):
    document = jsonable_encoder(doc)
    doc_id = col.insert_one(document=document)
    created_doc = col.find_one({"_id": doc_id.inserted_id})
    created_doc['_id'] = str(created_doc['_id'])

    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_doc)

@router.get('/{doc_id}', response_model=models.ISBNModel)
def get_doc(doc_id: str):
    if (doc :=  col.find_one({"_id": ObjectId(doc_id)})) is not None:
        return doc

    raise HTTPException(status_code=404, detail=f"doc {doc_id} not found")

@router.put('/{doc_id}')
def put_doc(doc_id: str, doc: dict = Body(...)):
    document = jsonable_encoder(doc)

    updated_doc = col.update_one({"_id": ObjectId(doc_id)}, {'$set': document})
    created_doc = col.find_one({"_id": ObjectId(doc_id)})
    created_doc['_id'] = str(created_doc['_id'])

    return JSONResponse(status_code=status.HTTP_200_OK, content=created_doc)


@router.delete('/{doc_id}')
def delete_task(doc_id: str):
    result = col.delete_one({"_id": ObjectId(doc_id)})

    return JSONResponse(status_code=status.HTTP_200_OK, content={'result': 'Удаление произведено успешно'})