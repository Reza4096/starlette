from starlette.applications import Starlette
from starlette.responses import PlainTextResponse, JSONResponse
from starlette.routing import Route, Mount, WebSocketRoute
from starlette.staticfiles import StaticFiles

# http://127.0.0.1:8000
def homepage(request):
    return PlainTextResponse("Hello, world!")


# http://127.0.0.1:8000/user/me
def user_me(request):
    username = "John Doe"
    return PlainTextResponse("Hello, %s!" % username)


# http://127.0.0.1:8000/user/reza
def user(request):
    username = request.path_params["username"]
    return PlainTextResponse("Hello, %s!" % username)


# ws://127.0.0.1:8000/ws
async def websocket_endpoint(websocket):
    await websocket.accept()
    await websocket.receive_text()
    await websocket.send_text("Hello, websocket!")
    await websocket.close()

# http://127.0.0.1:8000/state
def app_state(request):
    return JSONResponse(
        {"request.app.state.ADMIN_EMAIL": request.app.state.ADMIN_EMAIL}
    )


def startup():
    print("Ready to go")


routes = [
    Route("/", homepage),
    Route("/user/me", user_me),
    Route("/user/{username}", user),
    WebSocketRoute("/ws", websocket_endpoint),
    Mount("/static", StaticFiles(directory="static")),
    Route("/state", app_state),
]

app = Starlette(debug=True, routes=routes, on_startup=[startup])

app.state.ADMIN_EMAIL = "reza4096@yahoo.com"
