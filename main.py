from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True



@app.get("/")
def root():
    return {"message": "welcome to my api!!!"}
@app.get("/posts")
def get_post():
    return{"data": "This is your post"}

@app.post("/createposts")
def create_post(new_post: Post):
    print(new_post.published)
    return{"data": f"new post "}

# title str, content str, category, Bool published
