# Security and reviewer access

The gateway sections below describe the historical cache-only study. The
[general encoder](GENERAL_ENCODER.md) runs locally with the caller's OpenAI
client; it does not require a hosted NGNN service or reviewer credential.

## Serving boundary

The Python model service remains loopback-only. A separate TLS gateway is the
only externally reachable component and forwards solely to the allow-listed
review endpoints described in [API_CONTRACT.md](API_CONTRACT.md).

## Reviewer access

Reviewer access is issued for a named reviewer and a documented expiry. The
credential is stored only in the gateway's secret store or process environment.
It is never committed, printed, copied into result artifacts, or placed in a
model wrapper's metadata.

At expiry, the provider disables both the credential and the gateway listener.
On suspected credential disclosure or unexpected traffic, the provider revokes
access immediately, removes the gateway route, and stops the loopback service.

## Data handling

The gateway may retain timestamp, request identifier, method, allow-listed
path, status, duration, and a credential-identifier hash. It must not retain
authorization headers, request or response bodies, input texts, embeddings,
query parameters, source IP addresses, or local artifact/cache locations.

The public repository must not include credentials, private endpoint URLs,
local paths, runtime cache material or raw evaluation data. The audited
`model.npz` compressor is explicitly released under MIT; its hash and exact
scope are listed in [artifact_manifest.json](artifact_manifest.json).
