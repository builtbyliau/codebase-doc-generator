# Requests: HTTP for Humans

## Description
**Requests** is an elegant and simple HTTP library for Python, built for human beings. While Python's built-in `urllib` module provides most of the HTTP capabilities you need, the API is notoriously broken and requires an enormous amount of work (and methods) to perform simple tasks.

Requests allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs, or to form-encode your POST data. Keep-alive and HTTP connection pooling are 100% automatic.

## Features
- **Keep-Alive & Connection Pooling:** Improved performance for multiple requests to the same host.
- **International Domains and URLs:** Full support for IDN.
- **Sessions with Cookie Persistence:** Maintain state across multiple requests.
- **Browser-style SSL Verification:** Secure connections verified against trusted CA bundles.
- **Automatic Content Decoding:** Automatically decodes GZip and Deflate content.
- **Unicode Response Bodies:** Responses are automatically decoded into Unicode.
- **Multipart File Uploads:** Simple interface for uploading files.
- **HTTP(S) Proxy Support:** Easy configuration for working behind proxies.
- **Connection Timeouts:** Prevent your application from hanging on unresponsive servers.
- **Chunked Requests:** Support for sending and receiving chunked data.

## Installation

Requests requires Python 3.8 or later. You can install it via `pip`:

```bash
$ python -m pip install requests
```

### Dependencies
Requests relies on the following industry-standard packages:
- `charset_normalizer`: For character encoding detection.
- `idna`: For Internationalized Domain Names.
- `urllib3`: The underlying HTTP connection pooler.
- `certifi`: For SSL certificate verification.

## Usage

### Simple GET Request
```python
import requests

r = requests.get('https://api.github.com/events')
print(r.status_code)
# 200
print(r.headers['content-type'])
# 'application/json; charset=utf8'
print(r.json())
```

### POSTing Data
```python
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("https://httpbin.org/post", data=payload)
print(r.text)
```

### Using Sessions
Sessions allow you to persist certain parameters and cookies across multiple requests.
```python
s = requests.Session()
s.auth = ('user', 'pass')
s.headers.update({'x-test': 'true'})

# both requests will include the auth and the custom header
s.get('https://httpbin.org/headers', headers={'x-test2': 'true'})
s.get('https://httpbin.org/get')
```

## Project Structure
The repository is organized to separate the core logic from testing and documentation:

- `src/requests/`: The core library source code.
    - `api.py`: The main entry point for the library (get, post, request).
    - `sessions.py`: Implements the Session object for stateful requests.
    - `models.py`: Defines the primary objects: Request, Response, and PreparedRequest.
    - `adapters.py`: Handles the actual transport of the request (via urllib3).
    - `auth.py`: Built-in authentication handlers (Basic, Digest).
    - `cookies.py`: Utilities for managing HTTP cookies.
    - `utils.py`: A collection of internal helper functions.
- `tests/`: A comprehensive test suite using `pytest`.
    - `test_requests.py`: Core functional tests.
    - `test_utils.py`: Unit tests for helper functions.
- `docs/`: Source documentation files.
- `.github/`: Community health files including issue templates and contribution guides.

## Contributing
Contributions are welcome and appreciated! 

1. **Check for Issues:** Look through the GitHub issues to see if your bug or feature is already being discussed.
2. **Setup Environment:** Install the development dependencies:
   ```bash
   $ pip install -r requirements-dev.txt
   ```
3. **Run Tests:** Ensure all tests pass before submitting a PR:
   ```bash
   $ pytest
   ```
4. **Follow the Style Guide:** Please ensure your code follows the established coding standards defined in the repository.

For more detailed information, please read [CONTRIBUTING.md](.github/CONTRIBUTING.md).