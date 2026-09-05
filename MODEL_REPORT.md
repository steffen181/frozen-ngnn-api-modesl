# Model report: Frozen NGNN API Model

## Model description

Frozen NGNN API Model is a cache-only local study service identified as
`steffen-negabo/ngnn-sparse-v1-api`. The service emits 512-dimensional vectors
and uses cosine similarity. Its frozen serving revision is
`frozen_ngnn_task_router_472a3d9e755d8c8e`.

The service uses explicit routes for SciFact, STSBenchmark, and
Banking77Classification.v2. Each of those routes resolves to the same frozen
generic-default release artifact. Fallback is disabled: unsupported or missing
task routing is rejected rather than silently substituted.

## Availability

The model has been evaluated through a local API. No public general encoder
endpoint is announced and no weights are distributed by this repository.
Controlled inspection can be discussed with [steffen@negabo.com](mailto:steffen@negabo.com).

The API is intended for reproducible review of the documented frozen revision.
It is not a promise of perpetual, unauthenticated, or unrestricted service.

## License and contact

The model report and API contract are published under the MIT License; see
[LICENSE](LICENSE). Operational and MTEB-review questions can be sent to
[steffen@negabo.com](mailto:steffen@negabo.com).

## Training and provenance boundaries

The frozen generic-default artifact was calibrated from the FineWeb
`sample-10BT` configuration at pinned source revision
`9bb295ddab0e05d785b879661af7260fed5140fc`. The local calibration source is
documented as ODC-By-1.0.

For calibration and compressor fitting, SciFact, STSBenchmark, and
Banking77Classification.v2 task text was exclusion-only input. Separate runtime
caches provide base embeddings for the supported evaluation texts. No compressor
fitting occurs during evaluation. The public repository contains no calibration text, evaluation
text, embeddings, cache contents, artifact files, or private provenance paths.

## Task-specific evidence

The local frozen-router replay recorded:

| Task | Metric | Score |
| --- | --- | ---: |
| SciFact | nDCG@10 | 0.750530 |
| STSBenchmark | cosine Spearman | 0.848071 |
| Banking77Classification.v2 | accuracy | 0.784395 |

These values are local evidence for the exact three-task scope. They are not a
claim of an MTEB(eng, v2) aggregate and are not an official MTEB result until
the upstream model and result review process accepts them.

## Matched controls measured on 2026-09-05

A new cache-only run used the same task fixtures and MTEB 2.16 scoring
protocols for raw 3072D embeddings, PCA at 512D, and the frozen 512D NGNN
release. PCA used the same 8,000 FineWeb training rows as the compressor;
2,000 validation rows and all evaluation task rows were excluded from fitting.
The NGNN path preserved the historical request segmentation and 32-text
batches, reproducing all three recorded frozen scores.

| Task | Raw 3072D | PCA 512D | Frozen NGNN 512D |
| --- | ---: | ---: | ---: |
| SciFact nDCG@10 | 0.777120 | 0.766150 | 0.750530 |
| STSBenchmark cosine Spearman | 0.835725 | 0.839986 | 0.848071 |
| Banking77Classification.v2 accuracy | 0.858257 | 0.843791 | 0.784395 |

NGNN exceeds both controls on STS and falls below both on SciFact and Banking77.
Paired 95% percentile bootstrap intervals for NGNN minus PCA were
[-0.031875, -0.002342], [0.003031, 0.013004], and [-0.063431, -0.054321],
respectively (1,000 resamples, seed 20260905). SciFact resamples queries,
STS resamples sentence pairs and recomputes Spearman, and Banking resamples
the ten deterministic few-shot fit outcomes on the fixed test set. The Banking
interval does not estimate uncertainty over new test examples.

Both 512D variants use 2,048 float32 bytes per vector, compared with 12,288
for raw embeddings. This excludes model artifacts and cache serialization.
These results support a task-dependent compression tradeoff, not a general
quality advantage for NGNN. Native provider-512D controls and the additional
NFCorpus retrieval evaluation are prepared but remain unevaluated because
their vector caches are missing. No provider calls were made by this comparison.

## Limitations

- Only the documented frozen revision is in scope.
- Only texts already represented in the frozen runtime caches can be encoded.
- The generic upstream mock inputs are unsupported; this candidate does not
  currently meet the normal MTEB model-integration requirements.
- API availability is controlled and may be time-limited for reviewers.
- Unsupported task routing fails closed.
- Historical inference depends on batch composition. A future encoder with
  deterministic per-text inference is a different model version and requires
  new results.
- [Evaluation request #5278](https://github.com/embeddings-benchmark/mteb/issues/5278)
  was closed on 2026-08-24. No upstream model or results PR has been submitted.
