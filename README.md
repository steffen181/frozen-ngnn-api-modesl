# Frozen NGNN API Model

`steffen-negabo/ngnn-sparse-v1-api` is a frozen, API-only text-embedding
model prepared for task-specific MTEB review. This repository publishes model
information and the API contract; it does not publish model weights, runtime
caches, evaluation texts, embeddings, or access credentials. Its canonical
public model report is this repository:
<https://github.com/steffen181/frozen-ngnn-api-modesl>.

## Scope

The intended MTEB evidence covers exactly these tasks:

- SciFact
- STSBenchmark
- Banking77Classification.v2

The evidence is task-specific. It must not be interpreted as, or used to
derive, a global MTEB benchmark aggregate.

## Public model identity

| Field | Value |
| --- | --- |
| Model name | `steffen-negabo/ngnn-sparse-v1-api` |
| Frozen revision | `frozen_ngnn_task_router_472a3d9e755d8c8e` |
| Embedding dimension | 512 |
| Similarity | cosine |
| API schema | v1 |
| Model form | API-only; no weights are distributed |
| License | MIT; see [LICENSE](LICENSE) |
| Contact | [steffen@negabo.com](mailto:steffen@negabo.com) |

## Access

The serving process is operated by the model provider. MTEB reviewers may
request time-limited API access from [steffen@negabo.com](mailto:steffen@negabo.com).
Access is issued separately from this source repository and credentials are
never committed here.

The external endpoint, reviewer credential, and expiry are deliberately not
published. See [API_CONTRACT.md](API_CONTRACT.md) for the stable interface and
[SECURITY.md](SECURITY.md) for the access boundary.

## Evidence and reproducibility

The frozen router resolves each supported task through an explicit
`generic_default` entry, with fallback disabled. Evaluation-task text was used
only as exclusion input: it was not used for calibration, cache fill, or model
fitting.

Local replay evidence recorded the following task metrics. These are local
release-evidence values, not an official MTEB submission or global score.

| Task | Metric | Local replay value |
| --- | --- | ---: |
| SciFact | nDCG@10 | 0.750530 |
| STSBenchmark | cosine Spearman | 0.848071 |
| Banking77Classification.v2 | accuracy | 0.784395 |

Further methodology, provenance boundaries, and limitations are in
[MODEL_REPORT.md](MODEL_REPORT.md).

## Publication status

The public model report, MIT license, and reviewer contact are now recorded.
The remaining operational release checks are in
[PUBLICATION_GATE.md](PUBLICATION_GATE.md). Do not add credentials, local
paths, cached vectors, model artifacts, raw evaluation data, or evaluation
request/response bodies.
