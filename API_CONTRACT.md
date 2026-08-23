# API contract

## Transport and authentication

The API is exposed through HTTPS by a provider-operated gateway. The service
uses JSON request and response bodies. Protected endpoints require:

```text
Authorization: Bearer <reviewer credential>
```

Credentials are issued to reviewers out of band. They must not be placed in a
repository, issue, pull request, command example, result file, or log.

Only these paths are part of the review interface:

| Method | Path | Authentication | Purpose |
| --- | --- | --- | --- |
| `GET` | `/healthz` | no | Gateway/service liveness probe |
| `GET` | `/v1/model-info` | yes | Frozen model identity and interface metadata |
| `POST` | `/v1/encode` | yes | Text embeddings |

All other paths and methods are rejected.

## `GET /v1/model-info`

The endpoint returns the public frozen identity. Consumers must reject a
response whose model name, revision, embedding dimension, similarity, batch
limit, or schema version differs from the expected values.

```json
{
  "model_name": "steffen-negabo/ngnn-sparse-v1-api",
  "model_revision": "frozen_ngnn_task_router_472a3d9e755d8c8e",
  "embedding_dim": 512,
  "base_embedding_source": "OpenAI text-embedding-3-large",
  "similarity_fn_name": "cosine",
  "max_batch_size": 32,
  "api_schema_version": "v1"
}
```

## `POST /v1/encode`

The request body contains a list of UTF-8 strings and optional task metadata.
The batch length must not exceed `max_batch_size` from `/v1/model-info`.

```json
{
  "inputs": ["first input", "second input"],
  "task_name": "SciFact",
  "hf_split": "test",
  "hf_subset": "default",
  "prompt_type": "query"
}
```

`task_name` is either a string or `null`. For the task-specific review scope,
clients use only `SciFact`, `STSBenchmark`, and `Banking77Classification.v2`.
`hf_split`, `hf_subset`, and `prompt_type` are optional contextual fields for
the MTEB wrapper; the frozen embedding service does not derive alternate
embeddings from them.

A successful response preserves input order and returns one finite 512-element
vector for every input:

```json
{
  "model_revision": "frozen_ngnn_task_router_472a3d9e755d8c8e",
  "embedding_dim": 512,
  "embeddings": [[0.0, 0.0]]
}
```

The vector values above are schematic only; consumers must not assume any
particular embedding content. Identity or shape mismatches are failures, not
fallback conditions.

## Errors and logging

Protected endpoints return `401` for absent or invalid credentials. Invalid
JSON, invalid request shape, unsupported task routing, oversized batches, or
non-finite backend output fail closed. Gateway logs are body-free: they must
not contain credentials, texts, embeddings, query parameters, or source IP
addresses.
