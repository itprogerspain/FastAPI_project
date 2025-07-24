from typing import Annotated

from fastapi import FastAPI, Path, Query

app = FastAPI()



@app.get("/user")
async def search(people: Annotated[list[str], Query()]) -> dict:
    return {"user": people}


# @app.get("/user/{username}")
# async def login(
#         username: Annotated[
#             str, Path(min_length=3, max_length=15, description='Enter your username',
#                       example='permin0ff')],
#         first_name: Annotated[
#             str | None, Query(max_length=10, pattern="^J|s$")] = None) -> dict:
#     return {"user": username, "Name": first_name}
#
#
#
# @app.get("/user/{name}")
# async def user(
#         name: Annotated[str, Path(
#                 min_length=4,
#                 max_length=20,
#                 description='Enter your name')])-> dict:
#     return {"user_name": name}




# @app.get("/category/{category_id}/products")
# async def category(
#         category_id: Annotated[int, Path(gt=0, description='Category ID')],
#         page: Annotated[int, Query()])-> dict:
#     return {"category_id": category_id, 'page': page}



# profiles_dict = {
#     'alex': {'name': 'Александр', 'age': 33, 'phone': '+79463456789', 'email': 'alex@my-site.com'}}
#
#
# @app.get("/users")
# async def retrieve_user_profile(
#         username: Annotated[str, Query(min_length=2, max_length=50, description='Имя пользователя')])-> dict:
#     if username in profiles_dict:
#         data = profiles_dict[username]
#         return data
#     else:
#         return {"message": f'Пользователь {username} не найден.'}



# from fastapi import FastAPI, Path, Query
# from typing import Annotated
#
#
# app = FastAPI()
#
#
# @app.get('/users')
# async def retrieve_user_profile(username: str = Query(min_length=2, max_length=50, description='Имя пользователя')) -> dict:
#     return profiles_dict.get(username, {'message': f'Пользователь {username} не найден.'})





