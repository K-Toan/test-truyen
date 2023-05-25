from routes.manga_route import *
from routes.author_route import *
from routes.user_route import *
from routes.history_route import *

app = FastAPI()
app.include_router(aut)
app.include_router(man)
app.include_router(usr)
app.include_router(his)


@app.get("/")
async def root():
    return {"message": "hello test_truyen"}