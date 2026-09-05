# Publication gate

As of 2026-09-05, the frozen candidate remains a documented local study.
Its cache-only input restriction prevents the normal MTEB model-integration
path. Operational gateway work alone cannot resolve that restriction.
No upstream model or results PR has been submitted.

- [x] The publication license is MIT; see [LICENSE](LICENSE). The FineWeb
  calibration-source license is not automatically the model/API license.
- [x] The public operational and MTEB-review contact is
  [steffen@negabo.com](mailto:steffen@negabo.com).
- [x] The public model report/reference URL is
  <https://github.com/steffen181/frozen-ngnn-api-modesl>.
- [x] Document the restriction to previously cached texts, unsupported mock
  inputs, and the closed [evaluation request](https://github.com/embeddings-benchmark/mteb/issues/5278).
- [ ] A future general encoder must receive its own identity, support unseen
  text with deterministic per-text semantics, and pass current MTEB `mock_run`.
- [ ] Evaluate that future encoder anew before submitting its results; do not
  reuse the historical frozen scores.
- [ ] For that future version, describe actual API availability and verify
  model metadata against the deployed implementation.
- [ ] Review any future public changes for credentials, local filesystem paths,
  raw evaluation text, cached vectors, artifact binaries, and private hashes.
- [ ] Keep the MTEB scope explicit: SciFact, STSBenchmark, and
  Banking77Classification.v2 only; no global aggregate claim.
