"""HTTP ping subcommand: send a GET request and report status code and latency."""


def ping_url(url: str, timeout: float = 10.0) -> dict[str, object]:
    """Send a GET request to *url* and return status and latency.

    Args:
        url: The URL to request.
        timeout: Request timeout in seconds.

    Returns:
        Dict with keys ``url``, ``status`` (int), ``latency_ms`` (float),
        and ``ok`` (bool).

    Raises:
        httpx.RequestError: On connection or timeout failure.
    """
    ...  # implemented in a later commit
