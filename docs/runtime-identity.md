# Runtime Identity

## Purpose

`RuntimeIdentity` is the canonical description of who a running MXM process is.

It answers the question:

```text
Who is this runtime?
```

This identity is used to:

- resolve configuration
- authorize secret access
- construct runtime context
- make deployment behaviour explicit and reproducible

Applications should not discover their own environment.

Applications should receive a constructed `RuntimeContext`, derived from an explicit `RuntimeIdentity`.

## Ownership

mxm-types owns the definition of RuntimeIdentity.

mxm-runtime owns discovery of RuntimeIdentity.

mxm-config consumes RuntimeIdentity.

mxm-secrets consumes RuntimeIdentity.

Applications consume RuntimeContext.


## Model

A first version of `RuntimeIdentity` consists of:

```python
RuntimeIdentity(
    app="mxm-moneymachine",
    environment="dev",
    machine="bridge",
    substrate="local-process",
    role="research",
)
```

The proposed dimensions are:

```text
app
environment
machine
substrate
role
```

These dimensions describe:

```text
which application
which operational world
which physical host
which execution mechanism
which responsibility
```

A future optional dimension may be added:

```text
instance
```

for distinguishing multiple equivalent workers, containers, or runtime replicas.

No separate `profile` dimension is currently included.

The current MXM architecture does not require a distinction between:

```text
what the runtime is doing
```

and

```text
which behavioural variant it represents
```

The existing examples previously considered for profiles:

```text
research
trading
marketdata
execution
backtest
```

are more naturally understood as runtime responsibilities and therefore belong in `role`.

If a genuine need for configuration variants emerges in the future, a separate profile dimension can be introduced later.

The initial design should remain as small as possible while fully describing the runtime.
```

## Role

`role` identifies the responsibility the runtime is performing.

Examples:

```text
research
marketdata
execution
backtest
reconciliation
prefect-server
prefect-worker
```

`role` answers:

```text
What job is this runtime doing?
```

This is the primary application-specific dimension of runtime identity.

For example:

```text
app=mxm-moneymachine
environment=prod
machine=monolith
substrate=prefect-docker-worker
```

does not tell us whether the runtime is:

```text
collecting market data
placing orders
running backtests
performing reconciliation
hosting Prefect
```

Those distinctions matter for:

```text
configuration
secret access
permissions
scheduling
logging
monitoring
operational safety
```

The key rule is:

```text
Role describes responsibility.
```

Changing role may legitimately change:

```text
which configuration is loaded
which secrets are accessible
which infrastructure services are used
```

because the runtime is performing a different operational function.

