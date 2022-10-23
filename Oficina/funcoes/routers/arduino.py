from fastapi_utils.inferring_router import InferringRouter

from funcoes.services.arduino import Arduino, Comandos

router = InferringRouter()
_arduino = Arduino()


@router.get("/ler_led", status_code=200)
async def ler_led():
    print("Ler Led")
    resposta = _arduino.comunicacao(route=Comandos.ler_led)
    if resposta == 0:
        return {"message": "Desligado"}
    else:
        return {"message": "Ligado"}

@router.get("/ler_botao", status_code=200)
async def ler_botao():
    print("Ler Botao")
    return _arduino.comunicacao(route=Comandos.ler_botao)


@router.get("/not_led", status_code=200)
async def not_led():
    print("! LED")
    return _arduino.comunicacao(route=Comandos.not_led)


@router.post("/blink_x/{vezes}", status_code=200)
async def blink_x(vezes: str):
    print(f"blink_x: {vezes}")
    return _arduino.comunicacao(route=Comandos.blink_x)
