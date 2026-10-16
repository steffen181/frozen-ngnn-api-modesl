# PyPI release

Published on 2026-09-16: [ngnn-encoder 0.1.0](https://pypi.org/project/ngnn-encoder/0.1.0/).
The wheel and source distribution pass `twine check --strict`. Both public
PyPI downloads match the previously reviewed GitHub release archives.

```bash
python -m pip install ngnn-encoder==0.1.0
```

The existing wheel is unchanged (SHA-256
`1ea29b3717175aacc2b6f1465d456201446a2c4eec835428526807bd6c7833e3`).
The source distribution contains only the six allowlisted package/license
inputs plus generated packaging metadata. Rebuilding it produces the same
inference code. Neither archive contains weights, training code or data.
Weights remain at the pinned public Hugging Face artifact commit.

The [source archive](https://github.com/steffen181/frozen-ngnn-api-modesl/releases/download/v0.1.0/ngnn_encoder-0.1.0.tar.gz)
now accompanies the wheel in the existing v0.1.0 GitHub release.
Its anonymous download was verified against SHA-256
`ac4cc406a4499121baea1454346eef4b51b6866cd3a68ac162de12c7b50b84ff`.

The [MTEB integration patch](verification/pypi_model.patch) adds
`ngnn = ["ngnn-encoder==0.1.0"]` to MTEB's optional dependencies and uses
`extra_requirements_groups=["ngnn"]`. It removes the custom installer/version
checker and delegates to MTEB's native dependency handling.
A locally rebuilt MTEB 2.20.10 wheel installed `ngnn-encoder` through that
extra from the public PyPI index. The verification environment reused the
recorded numerical dependencies; the NGNN package was initially absent.
49 focused tests and all 28 compatible mock tasks passed. The latter used
fresh anonymous HF downloads and synthetic provider embeddings, with no
paid OpenAI calls. See the [publication receipt](verification/pypi_publication.json),
[installation receipt](verification/pypi_installation.json), and
[mock report](verification/public_hub_mock_run.md).

The native extra is proposed in [MTEB PR #5400](https://github.com/embeddings-benchmark/mteb/pull/5400).
Until that PR is merged and released, install its checkout with `pip install '.[ngnn]'`;
the existing PyPI MTEB release does not yet contain this model or extra.
The adapter contains no GitHub-wheel installer or custom package version checker.

The PR also includes the generated universal `uv.lock`. Its
[immutable download and verification](verification/uv_lock_2026-10-16.json)
record the SHA-256, `uv lock --check` and a frozen NGNN sync dry-run.
The portable patch above contains only the adapter and dependency declarations; the mock report was removed from the upstream PR on review request.
Use the full PR checkout for frozen uv installation.
The current portable patch targets MTEB base `b5b023003a8341b3b697b03ee81cc484aee2ec95`.
The October 16 lock record supersedes the historical September and October 3
records for this patch; the PyPI 0.1.0 archives are unchanged.
Regeneration preserves all existing external dependency versions and artifact
hashes. It also reconciles requirements already present in the upstream
configuration: MTEB 2.26.2 and Sentence Transformers >=6.1.0 for the optional
`nemotron-3-5-vl` extra. The older lock had not yet recorded those requirements.

A fresh Python 3.11.15 environment installed the actual MTEB 2.26.2 checkout
with its `ngnn` extra and CPU torch 2.11.0+cpu. All 8 adapter tests and all 28
compatible mocks pass with the installed PyPI library, local verified Hub
files and synthetic HTTP responses through the real OpenAI SDK. The CI
extractor finds the correct model name; its loading helper skips runtime
loading for unknown total parameter counts, so mocks test that separately.
This fresh installation and the frozen universal-lock dry-run are separate
checks. [Current mock report](verification/mock_run_current_2026-10-16.md),
[review verification](verification/review_2026-10-16.json).
