from fastapi import FastAPI

from routes.books import router as books
from routes.ages import router as ages
from routes.employees import router as employees
from routes.isbn import router as isbn
from routes.publisher import router as publishers
from routes.sales import router as sales
from routes.years import router as years
from routes.tools import router as tools

app = FastAPI(title='LIBRARY API')

app.include_router(books)
app.include_router(ages)
app.include_router(employees)
app.include_router(isbn)
app.include_router(publishers)
app.include_router(sales)
app.include_router(years)
app.include_router(tools)
