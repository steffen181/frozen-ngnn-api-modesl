"""Public package interface for the frozen NGNN general encoder."""

from ngnn_general_encoder import (
    ARTIFACT_SHA256,
    MODEL_NAME,
    MODEL_REVISION,
    NgnnGeneralEncoderError,
)

from .hub import MODEL_CONFIG, NgnnGeneralEncoder

__version__ = "0.1.0"

__all__ = [
    "ARTIFACT_SHA256",
    "MODEL_CONFIG",
    "MODEL_NAME",
    "MODEL_REVISION",
    "NgnnGeneralEncoder",
    "NgnnGeneralEncoderError",
    "__version__",
]
