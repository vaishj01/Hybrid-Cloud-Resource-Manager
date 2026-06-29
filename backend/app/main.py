from fastapi import FastAPI

app = FastAPI(
    title="Hybrid Cloud Resource Manager",
    description="A platform to manage AWS cloud resources using Python and Terraform.",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to Hybrid Cloud Resource Manager"
    }