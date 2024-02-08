from fastapi import APIRouter

from service.payment import create_pay_link, check_hash

payment_router = APIRouter(
    prefix="/payment",
    tags=["payment"],
    responses={404: {"description": "Not found"}},
)


@payment_router.post("/create_link/")
async def get_pay_link(data: dict):
    """
    {
        "user_id": 10,
        "price": 1000,
        "user_email": "test@test.com",
        "comment": "bla bla bla"
    }
    """
    link = await create_pay_link(data)
    if isinstance(link, str):
        return {"status": "OK", "message": f"Link: {link}"}
    return {"status": "FAIL", "error": link}


@payment_router.post("/callback")
async def callback(data: dict):
    if data:
        if check_hash(data) == data.get("sign"):
            # do something here...
            return "OK"
        return "¯\_(ツ)_/¯"
