from fastapi_utils.inferring_router import InferringRouter
from starlette.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from funcoes.services.arduino import Arduino, Comandos

router = InferringRouter()
_arduino = Arduino()


@router.get("/ler_led", status_code=200)
async def ler_led():
    print("Ler Led")
    resposta = _arduino.comunicacao(route=Comandos.ler_led, numero=0)
    if resposta == 0:
        resposta = {"message": "Desligado"}
    else:
        resposta = {"message": "Ligado"}

    return JSONResponse(content=jsonable_encoder(resposta), status_code=200)


@router.get("/ler_botao", status_code=200)
async def ler_botao():
    print("Ler Botao")
    return _arduino.comunicacao(route=Comandos.ler_botao, numero=0)


@router.get("/not_led", status_code=200)
async def not_led():
    print("! LED")
    return _arduino.comunicacao(route=Comandos.not_led, numero=0)


@router.post("/blink_x/{vezes}", status_code=200)
async def blink_x(vezes: str):
    print(f"blink_x: {vezes}")
    return _arduino.comunicacao(route=Comandos.blink_x, numero=vezes)
