from fastapi.responses import JSONResponse


def response_success(message: str = "success", resources: dict = None) -> JSONResponse:
    content = {
        "code": 200,
        "success": True,
        "message": message,
    }

    if resources is not None:
        content["resources"] = resources

    return JSONResponse(status_code=200, content=content)


def response_error(message: str = "failed", details: dict = None) -> JSONResponse:
    content = {
        "code": 400,
        "success": False,
        "message": message,
    }

    if details is not None:
        content["details"] = details

    return JSONResponse(status_code=400, content=content)
