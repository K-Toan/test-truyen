from routes.manga_route import *
from routes.author_route import *


app.include_router(aut)
app.include_router(man)


@app.get("/")
async def root():
    return {"message": "hello test_truyen"}