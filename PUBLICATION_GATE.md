# Publication gate

This starter package is intentionally incomplete until the repository owner
provides the following public metadata. Do not open the upstream MTEB model PR
until every item is resolved.

- [ ] Add the model's publication license. The FineWeb calibration-source
  license is not automatically the model/API license.
- [ ] Add a public contact, preferably a GitHub handle, for MTEB reviewer
  access and operational questions.
- [ ] After creating the public repository, use its HTTPS URL as the model
  report/reference URL in the upstream MTEB `ModelMeta`.
- [ ] Define the reviewer-access request channel and actual HTTPS API hostname
  outside the repository; never commit the endpoint if it is not intended to
  be public.
- [ ] Verify the deployed `/v1/model-info` response against the frozen identity
  in [README.md](README.md) before sharing reviewer access.
- [ ] Validate the API-only wrapper against the then-current upstream MTEB
  release and run its local `mock_run` before opening the upstream PR.
- [ ] Review the public repository for credentials, local filesystem paths,
  raw evaluation text, cached vectors, artifact binaries, and private hashes.
- [ ] Keep the MTEB scope explicit: SciFact, STSBenchmark, and
  Banking77Classification.v2 only; no global aggregate claim.
