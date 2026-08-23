# Model report: Frozen NGNN API Model

## Model description

Frozen NGNN API Model is an API-only text-embedding service identified as
`steffen-negabo/ngnn-sparse-v1-api`. The service emits 512-dimensional vectors
and uses cosine similarity. Its frozen serving revision is
`frozen_ngnn_task_router_472a3d9e755d8c8e`.

The service uses explicit routes for SciFact, STSBenchmark, and
Banking77Classification.v2. Each of those routes resolves to the same frozen
generic-default release artifact. Fallback is disabled: unsupported or missing
task routing is rejected rather than silently substituted.

## Availability

The model is served through a controlled API. No model weights are distributed
by this repository. MTEB reviewers can request time-limited access from the
model contact once that contact is published in the release metadata.

The API is intended for reproducible review of the documented frozen revision.
It is not a promise of perpetual, unauthenticated, or unrestricted service.

## Training and provenance boundaries

The frozen generic-default artifact was calibrated from the FineWeb
`sample-10BT` configuration at pinned source revision
`9bb295ddab0e05d785b879661af7260fed5140fc`. The local calibration source is
documented as ODC-By-1.0.

SciFact, STSBenchmark, and Banking77Classification.v2 task text was
exclusion-only input. It was not used for calibration, cache completion, or
model fitting. The public repository contains no calibration text, evaluation
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
- API availability is controlled and may be time-limited for reviewers.
- Unsupported task routing fails closed.
- A future upstream MTEB wrapper must be validated against the current MTEB
  release before any result submission.
- The model's license and public contact must be added before publication.
