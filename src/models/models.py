from pydantic import BaseModel, Field
from typing import Optional, List, Union
from bson import ObjectId
from datetime import datetime
from pprint import pprint
from database import MongoTools as db

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __get_pydantic_json_schema__(cls, field_schema):
        field_schema.update(type="string")


class PublisherModel(BaseModel):
    # id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    _id: str = None
    publisher: str
    address: str

    class Config:
        arbitrary_types_allowed = True
        allow_population_by_field_name = True
        
        json_encoders = {ObjectId: str}

class YearModel(BaseModel):
    # id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    _id: str = None
    year: int

    class Config:
        arbitrary_types_allowed = True
        allow_population_by_field_name = True
        
        json_encoders = {ObjectId: str}

class ISBNModel(BaseModel):
    # id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    _id: str = None
    isbn: str

    class Config:
        arbitrary_types_allowed = True
        allow_population_by_field_name = True
        
        json_encoders = {ObjectId: str}

class AgeModel(BaseModel):
    # id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    _id: str = None
    age: int

    class Config:
        arbitrary_types_allowed = True
        allow_population_by_field_name = True
        
        json_encoders = {ObjectId: str}

class EmployeeModel(BaseModel):
    # id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    _id: str = None
    name: str
    surname: str
    phone: str

    class Config:
        arbitrary_types_allowed = True
        allow_population_by_field_name = True
        
        json_encoders = {ObjectId: str}

class BookModel(BaseModel):
    # id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    _id: str = None
    title: str
    publisher: PublisherModel
    year: YearModel
    pages_count: int
    ISBN: ISBNModel
    age: AgeModel
    price: int
    circulation: int

    class Config:
        arbitrary_types_allowed = True
        allow_population_by_field_name = True
        
        json_encoders = {ObjectId: str}

class SalesModel(BaseModel):
    # id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    _id: str = None
    book: BookModel
    sale_date: str
    price: float
    count: int
    employee: EmployeeModel

    class Config:
        arbitrary_types_allowed = True
        allow_population_by_field_name = True
        
        json_encoders = {ObjectId: str}