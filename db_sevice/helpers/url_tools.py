
def make_url(*parts: str) -> str:
    return '/'.join(part.strip('/') for part in parts)

