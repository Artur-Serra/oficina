import uvicorn
from fastapi import FastAPI
from funcoes.routers import arduino


def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(
        arduino.router,
        prefix="/arduino",
        tags=["arduino"],
        dependencies=[],
    )

    return app


if __name__ == "__main__":
    the_app = create_app()
    uvicorn.run(the_app, host="0.0.0.0", port=8000)

