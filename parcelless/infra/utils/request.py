import httpx


async def request(
    method: str,
    auth: tuple[str, str] | None = None,
    *args,
    **kwargs,
) -> httpx.Response:
    """Wrapper around the httpx library."""
    async with httpx.AsyncClient(auth=auth, timeout=20) as client:
        resp = await client.request(method, *args, **kwargs)
    resp.raise_for_status()
    return resp
