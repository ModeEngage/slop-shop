# Permanent Implementation Examples

Use these examples to clarify how the permanent implementation format applies to common changes. Adapt the detail to the
available evidence; do not copy requirements that are not supported by the user's context. Add the type marker specified
in SKILL.md when using these examples to draft an issue.

## Concrete Bug

```markdown
Title: Support Pod Identity in `manifest-renderer` service accounts

Description:

## Problem Statement

`manifest-renderer` adds the IRSA annotation to every service account that has an IAM role, including service accounts that
use Pod Identity and do not need the annotation.

## Acceptance Criteria

- Service accounts that use IRSA include the `eks.amazonaws.com/role-arn` annotation
- Service accounts that use Pod Identity do not include the IRSA annotation
- Existing IRSA configurations continue to render without changes
- Automated tests verify both authentication modes

## Implementation Details

- Current annotation logic: [serviceaccount.go#L35-L36](https://github.com/example-org/platform-config/blob/052400db5d8b244c18b1464b845afec73ef34071/go/cmd/manifest-renderer/pkg/render/serviceaccount.go#L35-L36)
- Existing tests: [serviceaccount_test.go](https://github.com/example-org/platform-config/blob/052400db5d8b244c18b1464b845afec73ef34071/go/cmd/manifest-renderer/pkg/render/serviceaccount_test.go)

[repo=example-org/platform-config]
```

## New Functionality

```markdown
Title: Add resource metrics to single-tenant clusters

Description:

## Problem Statement

Single-tenant clusters do not provide resource metrics, so teams cannot use CPU or memory metrics for autoscaling
or inspect resource use with `kubectl top`.

## Acceptance Criteria

- Resource metrics are available in every single-tenant cluster
- Horizontal Pod Autoscalers can use CPU and memory metrics
- `kubectl top nodes` and `kubectl top pods` return current resource data
- The service remains available when one replica is unavailable

## Implementation Details

- Multi-tenant reference: [metrics_server](https://github.com/example-org/platform-config/tree/master/infrastructure/kubernetes/argocd/addons/metrics_server)
- Single-tenant infrastructure nodes require the existing addon tolerations and scheduling constraints

[repo=example-org/platform-config]
```

## High-Risk Migration

```markdown
Title: Migrate Thanos services to Pod Identity in development clusters

Description:

## Problem Statement

Thanos services in development clusters still use IRSA while the platform is moving to Pod Identity. The migration
must preserve metric ingestion, historical queries, and access to S3.

## Acceptance Criteria

- Each Thanos service authenticates through Pod Identity in both development clusters
- Metric ingestion and historical queries continue without data loss
- Each service remains healthy and retains its required S3 access
- Authentication can be restored through IRSA if a migrated service fails
- Production services are not changed by this issue

## Implementation Details

- Current Thanos IAM configuration: [iam.tf#L425-L438](https://github.com/example-org/platform-config/blob/437d6e517d3429ab393dcff0da51d64a9d9f2ada/infrastructure/tf_modules/kubernetes_cluster/iam.tf#L425-L438)
- The migration must limit the effect of a failure to one service at a time
- The rollback strategy must restore IRSA authentication without data loss

[repo=example-org/platform-config]
```
