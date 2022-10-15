from fastapi_utils.inferring_router import InferringRouter
router = InferringRouter()


@router.get("/ler_led", status_code=200)
async def ler_led():
    print("Ler Led")


@router.get("/ler_botao", status_code=200)
async def ler_botao():
    print("Ler Botao")


@router.get("/not_led", status_code=200)
async def not_led():
    print("! LED")


@router.post("/blink_x", status_code=200)
async def blink_x(vezes):
    print(f"blink_x: {vezes}")
