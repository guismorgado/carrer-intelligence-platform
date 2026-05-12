from fastapi import HTTPException


def validate_domain(domain: str, supported: set[str]) -> None:
    if domain not in supported:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported domain '{domain}'. Choose from: {sorted(supported)}",
        )
