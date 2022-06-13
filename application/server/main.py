import uvicorn
from fastapi import FastAPI, File, UploadFile
from starlette.responses import RedirectResponse
from . import serve_model

app_desc = """<h2>To use this app, try to upload food image to `predict/image`</h2>
<br>Kukus: """

app = FastAPI(title='ML Model API Bangkit 2022 Capstone', description=app_desc)


@app.get("/", include_in_schema=False)
async def index():
    return RedirectResponse(url="/docs")


@app.post("/predict/image")
async def predict_api(file: UploadFile = File(...)):
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return "Image must be jpg or png format!"
    image = serve_model.read_imagefile(await file.read())
    prediction = serve_model.predict(image)

    return prediction

if __name__ == "__main__":
    uvicorn.run(app, debug=True)
