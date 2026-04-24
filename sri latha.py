from fastapi import FastAPI 
srilatha=FastAPI()
@srilatha.get("/")
def home():
    return{"what":"I am Sri latha"}