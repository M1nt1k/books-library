from fastapi import APIRouter, Body, HTTPException, status
from fastapi.responses import Response, JSONResponse
from fastapi.encoders import jsonable_encoder

from datetime import datetime
from bson import ObjectId

from database import db
import models.models as models

collection = 'sales'
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

@router.post('/', response_model=models.SalesModel)
def add_doc(doc: models.SalesModel):
    document = jsonable_encoder(doc)
    doc_id = col.insert_one(document=document)
    created_doc = col.find_one({"_id": doc_id.inserted_id})
    created_doc['_id'] = str(created_doc['_id'])

    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_doc)

@router.get('/{doc_id}', response_model=models.SalesModel)
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

@router.get('/employee/{doc_id}')
def get_doc_from_employee(doc_id: str):
    if (doc :=  db.employees.find_one({"_id": ObjectId(doc_id)})) is not None: 
        del doc['_id']

        res = []
        docs_res = col.find({"employee": doc})
        for doc in docs_res:
            doc['_id'] = str(doc['_id'])
            res.append(doc)
        return res

    raise HTTPException(status_code=404, detail=f"doc {doc_id} not found")

@router.get('/date/{date}')
def get_doc_from_employee(date: str):
    res = []
    docs_res = col.find({'sale_date': date})
    for doc in docs_res:
        doc['_id'] = str(doc['_id'])
        res.append(doc)
    return res

@router.get('/employee/date/{employee_id}/{date}')
def get_doc_from_employee(employee_id:str, date: str):
    if (doc :=  db.employees.find_one({"_id": ObjectId(employee_id)})) is not None: 
        del doc['_id']

        res = []
        docs_res = col.find({
            "employee": doc,
            'sale_date': date
            })
        
        for doc in docs_res:
            doc['_id'] = str(doc['_id'])
            res.append(doc)
        return res