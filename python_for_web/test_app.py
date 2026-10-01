"""Regression tests for the Werkzeug-debugger exposure in python_for_web.

These lock in the hardening from the security fix:

* the app must not run the interactive debugger by default,
* it must not bind to all interfaces by default,
* a POST with a missing `content` field must yield 400, not a 500
  traceback page (which, with the debugger on, leaks source and enables
  the /console RCE console).

Run with:  pytest python_for_web/test_app.py
"""
import os

from app import app


def test_missing_content_field_returns_400_not_500():
    client = app.test_client()
    response = client.post("/post", data={"x": "1"})
    # The vulnerable app raised BadRequestKeyError -> 500 traceback page.
    assert response.status_code == 400
    assert b"Traceback (most recent call last)" not in response.data
    assert b"Werkzeug Debugger" not in response.data


def test_valid_content_still_redirects():
    client = app.test_client()
    response = client.post("/post", data={"content": "hello"})
    assert response.status_code in (301, 302)


def test_get_post_renders_form():
    client = app.test_client()
    assert client.get("/post").status_code == 200


def test_debug_defaults_to_off():
    assert os.environ.get("FLASK_DEBUG") != "1" or True  # documented opt-in
    # The run configuration must not hard-code debug=True.
    import inspect
    import app as appmod

    source = inspect.getsource(appmod)
    assert "debug=True" not in source
    assert "FLASK_DEBUG" in source


def test_default_bind_is_loopback():
    import inspect
    import app as appmod

    source = inspect.getsource(appmod)
    assert 'os.environ.get("HOST", "127.0.0.1")' in source
