from fastapi import FastAPI  
X= FastAPI()
@X.get("/")
def hm():
    return{"hello":"world"}