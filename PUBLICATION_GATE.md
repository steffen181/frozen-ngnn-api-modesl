# Publication gate

The public model report, MIT license, and contact are established. Do not open
the upstream MTEB model PR until every remaining operational item is resolved.

- [x] The publication license is MIT; see [LICENSE](LICENSE). The FineWeb
  calibration-source license is not automatically the model/API license.
- [x] The public operational and MTEB-review contact is
  [steffen@negabo.com](mailto:steffen@negabo.com).
- [x] The public model report/reference URL is
  <https://github.com/steffen181/frozen-ngnn-api-modesl>.
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
