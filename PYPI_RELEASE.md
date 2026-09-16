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
[immutable download and verification](verification/uv_lock_2026-09-16.json)
record the SHA-256, `uv lock --check` and a frozen NGNN sync dry-run.
The portable patch above contains only adapter, dependency declarations
and mock report; use the full PR checkout for frozen uv installation.
Regeneration also reconciles the base configuration's already-declared
MTEB version and LanguageBind dependencies with its older lock.
