from fastapi import FastAPI, Depends
from config.configs import host, port, is_develop, swagger_config
from auth.auth import get_api_key
from config.configs import swagger_config, summary, description
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.openapi.docs import get_swagger_ui_html
from config.base_auth import get_current_username

    
app = FastAPI(
    summary=summary,
    description=description,
    title="FastAPI full configured swagger.",
    docs_url=None,
    redoc_url=None,
    openapi_url=None,
    swagger_css_url="/swagger-ui.css"
)

@app.get("/items/", dependencies=[Depends(get_api_key)])
async def read_items():
    return [{"name": "Foo"}]

@app.get("/", include_in_schema=False)
async def go_to_swagger():
    return RedirectResponse(url=f'/docs')


@app.get("/docs", include_in_schema=False)
async def get_swagger_documentation(username: str = Depends(get_current_username)):
    return get_swagger_ui_html(
        title="FastAPI full configured swagger.",
        swagger_ui_parameters=swagger_config,
        swagger_css_url="/swagger-ui.css",
        openapi_url="/openapi.json"
    )


@app.get("/swagger-ui.css", include_in_schema=False)
async def get_documentation_css(username: str = Depends(get_current_username)):
    return FileResponse("config/swagger.css")


@app.get("/openapi.json", include_in_schema=False)
async def openapi(username: str = Depends(get_current_username)):
    return app.openapi()


if __name__ == '__main__':
    import uvicorn
    if is_develop:
        uvicorn.run("main:app", host=host, port=port, reload=True)
    else:
        uvicorn.run("main:app", host=host, port=port)