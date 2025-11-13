from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def index():
    return {'data': {'name': 'Lance Kian Flores'}}

@app.get('/about')
def about():
    return {'data': {'about': 'About Page'}}
