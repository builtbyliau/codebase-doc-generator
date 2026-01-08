# FastAPI
High-performance Python web framework for building APIs with standard Python type hints.

## Description
FastAPI is a modern web framework designed for building robust APIs using Pydantic for data validation and Starlette for web routing. It leverages Python type annotations to provide automatic serialization, deep validation of request bodies, and built-in generation of OpenAPI schemas.

## Features
*   **Automatic Data Validation:** Uses Pydantic models to validate complex data types, including decimals, lists, and custom objects, with detailed error reporting.
*   **Built-in Security:** Native support for multiple security schemes, including OAuth2, HTTP Basic, and HTTP Digest authentication.
*   **Exception Handling:** Integrated handling for both FastAPI and Starlette HTTP exceptions, allowing for custom headers and detailed error responses.
*   **File Handling:** Robust support for multipart file uploads via `UploadFile` with integrated SpooledTemporaryFile management.
*   **OpenAPI Integration:** Automatically generates standard-compliant OpenAPI (Swagger) documentation based on function signatures and security dependencies.

## Installation
Install FastAPI using `pip` or `uv`:

```bash
# Using pip
pip install fastapi

# Using uv
uv add fastapi
```

## Usage
Based on the project's implementation of HTTP exceptions and request handling:

```python
from fastapi import FastAPI, HTTPException, UploadFile

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id != "foo":
        raise HTTPException(
            status_code=404, 
            detail="Item not found",
            headers={"X-Error": "Custom Header"}
        )
    return {"item": "The Foo Wrestlers"}

@app.post("/upload/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}
```

## Project Structure
*   `fastapi/`: Core library source code containing routing, security, and data structure logic.
*   `tests/`: Comprehensive test suite categorized by feature (e.g., security, multi-body errors, datastructures).
*   `docs/`: Extensive documentation and tutorials in Markdown format.
*   `pdm_build.py`: Internal build script for managing package metadata and slim builds.

## Contributing
1.  Check `CONTRIBUTING.md` for local development setup.
2.  Ensure all tests pass using `pytest`.
3.  Follow the internal coding standards for type annotations and Pydantic v2 compatibility.