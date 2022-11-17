"""
Original code from https://github.com/tiangolo/uvicorn-gunicorn-docker

The MIT License (MIT)

Copyright (c) 2019 Sebastián Ramírez

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import sys


class App:
    def __init__(self, scope):
        assert scope["type"] == "http"
        self.scope = scope

    async def __call__(self, receive, send):
        await send(
            {
                "type": "http.response.start",
                "status": 200,
                "headers": [[b"content-type", b"text/plain"]],
            }
        )
        version = f"{sys.version_info.major}.{sys.version_info.minor}"
        message = f"Hello world! From Hypercorn. Using Python {version}".encode(
            "utf-8"
        )
        await send({"type": "http.response.body", "body": message})


app = App
