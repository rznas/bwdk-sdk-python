# BWDK Python SDK — Integration Guide for Agents

You are integrating **BWDK (Buy With DigiKala)** into a Python project via this SDK. Read this file **first**, then consult the companion references below.

## BWDK constants

- **Host:** `https://bwdk-backend.digify.shop`
- **Auth scheme:** `MerchantAPIKeyAuth` — header `Authorization: <api_key>`.
- **Main API class:** `bwdk_sdk.Api` (contains every endpoint — there is no sub-API).
- **Package:** `bwdk_sdk`.
- **Python:** 3.9+.

## Companion references (authoritative for the topics they cover)

| File           | When to read                                                   |
|----------------|----------------------------------------------------------------|
| `README.md`    | Install, auth wiring, full "Getting Started" snippet. Follow it verbatim. |
| `FLOWCHART.md` | Canonical order state machine. All callback/webhook branching MUST match these state names. |
| `docs/Api.md`  | Exact method names and signatures per endpoint.                |
| `docs/*.md`    | Per-model reference (e.g. `docs/OrderCreate.md`).              |

Do **not** duplicate install or method-signature details here — fetch the files above.

## Minimal wrapper pattern

```python
import os
import bwdk_sdk
from bwdk_sdk.rest import ApiException

cfg = bwdk_sdk.Configuration(host="https://bwdk-backend.digify.shop")
cfg.api_key["MerchantAPIKeyAuth"] = os.environ["BWDK_API_KEY"]

with bwdk_sdk.ApiClient(cfg) as client:
    api = bwdk_sdk.Api(client)
    order = api.order_api_v1_create_order_create(payload)
```

Method names are long and OpenAPI-generated (e.g. `order_api_v1_create_order_create`, not `create_order`). Look them up in `docs/Api.md`; do **not** guess.

## Integration invariants

1. **SDK only.** Never call BWDK via `requests`, `httpx`, `urllib`, `aiohttp`, or any raw HTTP client.
2. **Callback flow.** When BWDK redirects the customer to your `callback_url`, load the order (`order_api_v1_manager_retrieve`), branch on `status` per `FLOWCHART.md`, then call `order_api_v1_manager_verify_create` — `verify` is mandatory before `SHIPPED`.
3. **Errors.** Catch `bwdk_sdk.rest.ApiException`; inspect `.status` and `.body`. Retry only on transport errors, never on 4xx.
4. **Pinning.** Depend on a concrete tag (`vX.Y.Z`), not `latest`, in `requirements.txt` / `pyproject.toml`.

## Project conventions

- Respect the project's package manager (pip / poetry / uv / pipenv). Follow the `README.md` install command that matches.
- Put the SDK call inside a thin service wrapper (`services/bwdk.py` or similar); do not scatter `Api(...)` instantiations across views.
- Persist `order_uuid` + `status` in your DB; never re-derive `status` locally — always trust BWDK.
