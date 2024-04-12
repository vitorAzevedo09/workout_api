from fastapi import FastAPI
from workout_api.routers import api_router
from fastapi_pagination import add_pagination

# Starting the app
app = FastAPI(title='WorkoutApi')

# Including the app's routers
app.include_router(api_router)

# Adding pagination
add_pagination(app)
