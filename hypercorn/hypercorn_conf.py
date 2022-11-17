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

import json
import multiprocessing
import os

host = os.getenv("HOST", "0.0.0.0")
port = os.getenv("PORT", "80")
bind = os.getenv("BIND", f"{host}:{port}")

use_loglevel = os.getenv("LOG_LEVEL", "INFO")

web_concurrency_str = os.getenv("WEB_CONCURRENCY", None)

cores = multiprocessing.cpu_count()
default_web_concurrency = cores
if web_concurrency_str:
    web_concurrency = int(web_concurrency_str)
    assert web_concurrency > 0
else:
    web_concurrency = max(int(default_web_concurrency), 2)

accesslog_var = os.getenv("ACCESS_LOG", "-")
use_accesslog = accesslog_var or None
errorlog_var = os.getenv("ERROR_LOG", "-")
use_errorlog = errorlog_var or None
graceful_timeout_str = os.getenv("GRACEFUL_TIMEOUT", "120")
keepalive_str = os.getenv("KEEP_ALIVE", "5")
worker_class = os.getenv("WORKER_CLASS", "uvloop")

# hypercorn config variables
bind = os.getenv("BIND", f"{host}:{port}")
loglevel = use_loglevel
workers = web_concurrency
errorlog = use_errorlog
accesslog = use_accesslog
graceful_timeout = int(graceful_timeout_str)
keepalive = int(keepalive_str)


# For debugging and testing
log_data = {
    "loglevel": loglevel,
    "workers": workers,
    "worker_class": worker_class,
    "bind": bind,
    "graceful_timeout": graceful_timeout,
    "keep_alive_timeout": keepalive,
    "errorlog": errorlog,
    "accesslog": accesslog,
}
print(json.dumps(log_data))
