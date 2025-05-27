from fastapi import FastAPI
 
app = FastAPI()

@app.get("/")
def hello():
    return "i am omer"

@app.get("/user")
def show_user():
    return [
 
        {
            "name": "saif",
            "age": 20
        },
        {
            "name": "lala",
            "age": 45
        }
 
    ]