from fastapi import APIRouter, Body, HTTPException, status
from fastapi.responses import Response, JSONResponse
from fastapi.encoders import jsonable_encoder

from datetime import datetime
from bson import ObjectId
from pprint import pprint

from database import db
import models.models as models

collection = 'tools'

router = APIRouter(
    prefix=f'/api/v1/{collection}',
    tags=[f'{collection}']
)

@router.get('/sales/count')
def get_count_sales_books():
    count = db.sales.count_documents({})
    return {'sales_count': count}

@router.get('/sales/sum')
def get_count_sales_books():
    docs_res = db.sales.find()
    sales_sum = 0
    for doc in docs_res:
        sales_sum += (doc['price'] * doc['count'])

    return {'sales_sum': sales_sum}

@router.get('/books/avg')
def get_count_sales_books():
    docs_res = db.books.find()
    count = db.books.count_documents({})
    books_price = 0
    for doc in docs_res:
        books_price += doc['price']

    return {'sales_sum': f'{books_price/count:.2f}'}

@router.get('/books/age')
def get_count_sales_books():
    ages = {}
    doc_res = db.ages.find()
    for doc in doc_res:
        ages[str(doc['age'])] = 0

    print(ages)
    docs_res = db.books.find()
    for doc in docs_res:
        ages[str(doc['age']['age'])] += 1

    return ages

@router.get('/employees/sales')
def get_count_sales_books():
    employees = {}
    doc_res = db.employees.find()
    for doc in doc_res:
        employees[str(doc['phone'])] = 0

    docs_res = db.sales.find()
    for doc in docs_res:
        employees[str(doc['employee']['phone'])] += (doc['price'] * doc['count'])

    return employees

@router.get('/publisher/sales')
def get_count_sales_books():
    publishers = {}
    doc_res = db.publishers.find()
    for doc in doc_res:
        publishers[str(doc['publisher'])] = 0

    docs_res = db.sales.find()
    for doc in docs_res:
        publishers[str(doc['book']['publisher']['publisher'])] += (doc['price'] * doc['count'])

    return publishers

@router.get('/employees/count/sales')
def get_count_sales_books():
    employees = {}
    doc_res = db.employees.find()
    for doc in doc_res:
        employees[str(doc['phone'])] = 0

    docs_res = db.sales.find()
    for doc in docs_res:
        employees[str(doc['employee']['phone'])] += doc['count']

    return employees

@router.get('/publisher/count/sales')
def get_count_sales_books():
    publishers = {}
    doc_res = db.publishers.find()
    for doc in doc_res:
        publishers[str(doc['publisher'])] = 0

    docs_res = db.sales.find()
    for doc in docs_res:
        publishers[str(doc['book']['publisher']['publisher'])] += doc['count']

    return publishers

