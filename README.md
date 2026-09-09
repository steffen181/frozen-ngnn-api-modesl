# Frozen NGNN API Model

**2026-09-09:** The inference-only Python library `ngnn-encoder` 0.1.0 is
available as a [versioned wheel](https://github.com/steffen181/frozen-ngnn-api-modesl/releases/tag/v0.1.0).
The fixed compressor and model card are also public on
[Hugging Face](https://huggingface.co/steffen-negabo/ngnn-general-encoder-v1).
See [installation and usage](GENERAL_ENCODER.md#installable-inference-library).
It wraps the unchanged general encoder; compressor weights and benchmark
results retain their evaluated identities. The package contains inference
code; fixed weights are distributed separately. The NGNN training algorithm and training
data are not included.

**2026-09-06:** The general encoder's [source](ngnn_general_encoder.py) and
[compressor weights](model.npz) are public under MIT. It runs locally using
the caller's OpenAI API access and accepts previously unseen text as
`steffen-negabo/ngnn-general-encoder-v1`. See [GENERAL_ENCODER.md](GENERAL_ENCODER.md)
for setup, its distinct revision and evaluation status. Its MTEB integration
passed all 28 compatible mock tasks with the real OpenAI provider. Fresh
results for four tasks and both raw3072/native512 controls are documented in
the general encoder report. [Model PR #5400](https://github.com/embeddings-benchmark/mteb/pull/5400) and
[results PR #702](https://github.com/embeddings-benchmark/results/pull/702) are open for review.
Official MTEB acceptance remains pending.

## Historical frozen study

`steffen-negabo/ngnn-sparse-v1-api` is a frozen, cache-only study service for
three text-embedding tasks. The historical study publishes model
information and the API contract. Runtime caches, evaluation texts, embeddings
and access credentials remain private. Its canonical
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

The service has been evaluated locally. No publicly reachable general text
encoder endpoint is announced. Controlled access to the frozen local study can
be discussed with [steffen@negabo.com](mailto:steffen@negabo.com), but access
does not remove the cache-only input restriction. Credentials are never committed.

The external endpoint, reviewer credential, and expiry are deliberately not
published. See [API_CONTRACT.md](API_CONTRACT.md) for the stable interface and
[SECURITY.md](SECURITY.md) for the access boundary.

## Evidence and reproducibility

The frozen router resolves each supported task through an explicit
`generic_default` entry, with fallback disabled. For calibration and compressor
fitting, evaluation-task text was used only as exclusion input. Separate runtime
caches contain the base embeddings of the supported benchmark texts; evaluation
does not fit the compressor. Previously unseen texts cannot be encoded.

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

As of 2026-09-05, the model report is public, but there is no accepted MTEB
model entry or results submission. [Evaluation request #5278](https://github.com/embeddings-benchmark/mteb/issues/5278)
was closed on 2026-08-24 with guidance to add a model and evaluate the public
tasks. The cache-only wrapper fails generic mock inputs, so the existing
candidate does not meet the normal model-integration path. A future general
encoder requires a separate identity and new evaluation; the scores above
cannot be transferred to it.

See [PUBLICATION_GATE.md](PUBLICATION_GATE.md). Do not add credentials, local
paths, cached vectors, unreleased artifacts, raw evaluation data, or evaluation
request/response bodies. The explicitly released general-encoder weights are
documented separately above.
