# NGNN general encoder

Model: `steffen-negabo/ngnn-general-encoder-v1`  
Submission revision: `d6969c26400944d4f5200ebddfdc04a083fd7b75`

This is the immutable public source commit. The evaluation label
`ngnn_general_encoder_singleton_e55ba679_20260906` was renamed to satisfy the
official results revision format. Only the registration constant and saved
ModelMeta revision changed: inference code, weights and all four TaskResult
files are unchanged. [Source comparison and hash mapping](verification/revision_alias.json)
preserve the connection to the original evaluation evidence.

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
    revision="d6969c26400944d4f5200ebddfdc04a083fd7b75",
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

Publication does not constitute an accepted MTEB entry. Fresh native
evaluation completed with MTEB 2.20.10, upstream commit
`ed47a25455157433b458db2625e72960468597ab`, on all four planned tasks.
Original STSBenchmark retains its actual identity even though upstream now
supersedes it with STSBenchmark.v2.

| Task / main metric | General NGNN 512D | Raw 3072D | Provider-native 512D |
| --- | ---: | ---: | ---: |
| SciFact / nDCG@10 | 0.635170 | 0.777120 | 0.750040 |
| STSBenchmark / cosine Spearman | 0.824895 | 0.835725 | 0.828178 |
| Banking77Classification.v2 / accuracy | 0.832575 | 0.858257 | 0.845579 |
| NFCorpus / nDCG@10 | 0.311920 | 0.421090 | 0.398100 |

NGNN falls below both controls on all four tasks. Both 512D variants use
2,048 float32 bytes per vector; raw 3072D uses 12,288 bytes. These results do
not demonstrate a NGNN advantage over the provider's native dimensionality
reduction. No global MTEB aggregate is claimed.

The full3072 cache combines 15,658 verified archived raw responses with 3,914
new NFCorpus vectors. Every archived raw vector was verified by reproducing
its original L2-normalized value against the immutable release archive. The
native512 control uses 19,572 new responses with explicit `dimensions=512`.
All comparisons use the same task inputs and current native evaluators.
Archived full3072 and fresh native512 responses were obtained at different
times; the externally managed provider alias is not an immutable snapshot.

The [manifest and exact TaskResults](evaluation/2026-09-06/summary.json)
record all task/data revisions, source hashes and file hashes. Preparation
completed in 236 successful requests after one interruption; completed batches
were reused on resumption. Reported token usage gives USD 0.55328182 including
live verification. Conservatively reserving the ambiguous failed attempt gives
USD 0.55727399, below the USD 0.60 budget. These are calculations from token
usage at the [USD 0.13 per million token price](https://developers.openai.com/api/docs/models/text-embedding-3-large),
not an account invoice. See [preparation evidence](evaluation/2026-09-06/provider_preparation.json).

Native `mteb.get_model` / `get_model_meta` registration, the real OpenAI smoke
test and all 28 compatible text mock tasks passed. The smoke checks unseen
text, finite 512D output and blank handling. See the complete
[live mock report](verification/live_mock_run.md) and
[machine-readable verification](verification/live_mock_run.json). The earlier
[offline interface report](verification/offline_mock_run.md) is retained.
The [model implementation PR #5400](https://github.com/embeddings-benchmark/mteb/pull/5400) and
[four-task results PR #702](https://github.com/embeddings-benchmark/results/pull/702) are open for review.
The results PR depends on the model implementation. Its initial comparison
workflow reports that the model is not yet in the upstream registry. Model
workflows require maintainer approval to run. Neither PR is merged.
After the revision rename, native registration and all 28 offline mock tasks
passed again; see [current interface verification](verification/submission_revision/offline_mock_run.json).
The live report retains the actual earlier evaluation label.

The historical [frozen study report](MODEL_REPORT.md) evaluates a different,
batch-dependent cache-only model. Its scores do not describe this general
encoder. No global MTEB aggregate is claimed. The local compressor was fit
on the archived FineWeb calibration split; evaluation texts were exclusion
inputs. Training provenance of the OpenAI base model is unknown, so MTEB
metadata must not claim an empty training-dataset set or a fully open model.

The earlier private prototype revision ending in `20260905` uses the same
singleton mathematical transform. This public revision separately specifies
blank handling, truncation and request limits. New results belong to the
evaluation label ending in `20260906`, now mapped to the public source commit above.
