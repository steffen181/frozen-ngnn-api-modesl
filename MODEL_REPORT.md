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
