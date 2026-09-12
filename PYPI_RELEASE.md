# PyPI release preparation

Status on 2026-09-12: the `ngnn-encoder==0.1.0` wheel and source distribution
are prepared and pass `twine check --strict`. PyPI upload is pending publishing
authentication; this page does not claim the package is available on PyPI.

The existing wheel is unchanged (SHA-256
`1ea29b3717175aacc2b6f1465d456201446a2c4eec835428526807bd6c7833e3`).
The source distribution contains only the six allowlisted package/license
inputs plus generated packaging metadata. Rebuilding it produces the same
inference code. Neither archive contains weights, training code or data.
Weights remain at the pinned public Hugging Face artifact commit.

The source archive will accompany the wheel in the existing
[v0.1.0 release](https://github.com/steffen181/frozen-ngnn-api-modesl/releases/tag/v0.1.0).

The [prepared MTEB patch](verification/pypi_model.patch) adds
`ngnn = ["ngnn-encoder==0.1.0"]` to MTEB's optional dependencies and uses
`extra_requirements_groups=["ngnn"]`. It removes the custom installer/version
checker and delegates to MTEB's native dependency handling.
A rebuilt MTEB wheel installed the package through that extra from the local
release archive. Native missing-dependency handling, 49 focused tests and all
28 compatible mock tasks passed. The latter used actual anonymous HF
downloads and synthetic provider embeddings, with no paid OpenAI calls.

After the PyPI upload: anonymously verify both archive hashes, install using
the public index, recheck dependency resolution/lockfile as required by the
upstream checkout, and apply the prepared patch to the existing MTEB PR.
The active adapter remains functional through the existing GitHub wheel
while this step is pending.
