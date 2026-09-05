# NGNN general encoder

Model: `steffen-negabo/ngnn-general-encoder-v1`  
Revision: `ngnn_general_encoder_singleton_e55ba679_20260906`

The general encoder uses the caller's OpenAI `text-embedding-3-large` API
access to produce 3072-dimensional base embeddings, normalizes each vector,
and applies the published fixed compressor to produce 512 float32 values.
It accepts previously unseen text. Each vector is transformed independently,
so the compressor output does not depend on neighboring texts or batch size.
The provider model is externally managed; future provider changes can still
affect embeddings despite the fixed local weights and code.

## Published artifact

`model.npz` is the original immutable compressor: a 3072-by-512 dictionary,
512 unit channel scales, no bias, and provenance metadata. Ridge solving uses
regularization `1e-6` plus `1e-8` numerical jitter, singleton RMS normalization
and top-256 selection. The CPU PyTorch 2.11.0 tie behavior is part of this
revision. Cached Cholesky factorization preserves the original singleton
outputs bit for bit in the tested parity cases.

| Property | Value |
| --- | --- |
| Artifact SHA-256 | `e55ba67998039ba7cb4837798b0464e06e5939245d3275802cbbd6f0aa3fcb6a` |
| Download bytes | 5,843,713 |
| Uncompressed tensor bytes | 6,293,504 |
| Output vector bytes | 2,048 in float32 |
| Code and compressor license | MIT, see [LICENSE](LICENSE) |
| Base model weights and training data | Not publicly available; OpenAI API terms apply |

The code verifies the artifact SHA-256 before loading tensors or initializing
the provider. Loading uses NumPy with `allow_pickle=False`. No private
repository, runtime vector cache or hosted NGNN service is required.

## Run locally

Clone this repository, create a Python 3.10 environment, and install
[`requirements.txt`](requirements.txt). CPU PyTorch is sufficient. Keep
`ngnn_general_encoder.py` and `model.npz` together. Supply your own
`OPENAI_API_KEY` through your environment, then run:

```python
from ngnn_general_encoder import NgnnGeneralEncoder

model = NgnnGeneralEncoder()
vectors = model.encode(["A previously unseen sentence.", "Another sentence."])
assert vectors.shape == (2, 512)
```

`encode` makes billable OpenAI embedding requests. The tokenizer may download
its public vocabulary on first use. You can instead pass an OpenAI-compatible
`client` to the constructor. Never put keys in repository files or MTEB model
keyword arguments: MTEB saves those arguments in result metadata.

The proposed self-contained MTEB implementation is in
[`mteb_models/ngnn.py`](mteb_models/ngnn.py). Copy it to
`mteb/models/model_implementations/ngnn.py` in the pinned MTEB checkout before
installing that checkout. With `OPENAI_API_KEY` in the environment:

```python
import mteb

model = mteb.get_model(
    "steffen-negabo/ngnn-general-encoder-v1",
    revision="ngnn_general_encoder_singleton_e55ba679_20260906",
    device="cpu",
)
```

The MTEB loader downloads the weights from immutable public commit
`83773ff1ad83accc729c8d748d6991077842fbc0` and checks their SHA-256. It requires
PyTorch 2.11.0 because top-k tie behavior affects this compressor. This model
is not yet included in an official MTEB release.

## Input rules

- Empty or whitespace-only text produces a local zero vector.
- Nonempty text up to 8,191 `cl100k_base` tokens is passed unchanged.
- Longer text is truncated to the token prefix, with the decoded token count
  checked again before sending it.
- Requests contain at most 2,048 inputs and 300,000 tokens in total; the
  default batch size is 100 inputs. Literal tokenizer special-token strings
  are treated as ordinary text.
- Provider response indices, dimensions, finite values and nonzero norms are
  checked before applying the compressor. Provider errors omit response bodies.

These boundaries follow the [OpenAI embeddings API constraints](https://developers.openai.com/api/reference/ruby/resources/embeddings/methods/create),
using the same conservative 8,191-token input limit as MTEB's OpenAI model.

## Evaluation and submission

Publication of the weights does not constitute an accepted MTEB entry. Fresh
evaluation is being prepared with MTEB 2.20.10, upstream commit
`ed47a25455157433b458db2625e72960468597ab`. Planned tasks are SciFact,
original STSBenchmark, Banking77Classification.v2 and NFCorpus. Original STS
is superseded by STSBenchmark.v2 upstream; results must retain their actual
task identity.

Current native `mteb.get_model` / `get_model_meta` registration was verified.
All 28 compatible text mock tasks passed with synthetic provider embeddings;
see the complete [offline mock report](verification/offline_mock_run.md).
That report verifies interfaces, not embedding quality or live API access.
The actual API smoke test and real-provider mock run are still pending.

The historical [frozen study report](MODEL_REPORT.md) evaluates a different,
batch-dependent cache-only model. Its scores do not describe this general
encoder. No global MTEB aggregate is claimed. The local compressor was fit
on the archived FineWeb calibration split; evaluation texts were exclusion
inputs. Training provenance of the OpenAI base model is unknown, so MTEB
metadata must not claim an empty training-dataset set or a fully open model.

The earlier private prototype revision ending in `20260905` uses the same
singleton mathematical transform. This public revision separately specifies
blank handling, truncation and request limits. New results belong to the
revision ending in `20260906`.
