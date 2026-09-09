# ngnn-encoder

`ngnn-encoder` provides the inference-only Python interface for
`steffen-negabo/ngnn-general-encoder-v1`. It includes the standalone inference
module, but does not include model weights, training code, cached results, or
credentials.

Install the wheel and load an immutable Hugging Face revision. The Hub
repository and commit are distribution coordinates assigned at publication;
they are separate from the scientific `MODEL_REVISION` exported by the
package:

```python
from ngnn_encoder import NgnnGeneralEncoder

encoder = NgnnGeneralEncoder.from_pretrained(
    repo_id,
    revision=hub_commit,
)
vectors = encoder.encode(["Example text"])
```

The package requires Python 3.10 or newer and torch 2.11.0. Encoding nonblank
text calls OpenAI's `text-embedding-3-large` with the caller's API key and can
incur provider charges. Pass an OpenAI-compatible `client` for controlled or
offline use. Public Hub downloads explicitly disable authentication tokens and
verify the configuration and model artifact before creating a provider client.

For a local artifact, pass its path directly:

```python
encoder = NgnnGeneralEncoder("model.npz", client=client)
```

Licensed under the MIT License.
