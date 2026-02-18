# _Helm Charts_: the package manager for Kubernetes

- It is a tool that simplifies Kubernetes application deployment by bundling its resources (like pods, services, deployments, configmaps, etc.) into a single package called a Helm Chart.
- It automates the process of defining, installing and upgrading Kubernetes applications.
- They are packages for Kubernetes that help you define, install, and manage Kubernetes applications.

## But what is it?

A helm chart is a collection of files organised in a specific directory structure, which includes:

1. chart.yaml: Metadata about the chart (name, version,description)
1. values.yaml: defualt configuration values (can be overridden)
1. templates/ : Kubernetes manifest templates (in YAML) that Helm renders using values from `values.yaml`
1. NOTES.txt: `optional`, provides user instructions after installing the chart

## Helm Chart Structure

```
myapp/
├── Chart.yaml
├── values.yaml
├── templates/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── ingress.yaml
└── NOTES.txt
```

## Why use this?

- Simpilifies complex Kubernetes deployments
- Supports versioning and rollbacks
- Enables reuse and sharing of charts
- Manages configurations cleanly with `values.yaml`

## How it Works

1. _Create_ a Chart: Define Kubernetes resources using templates.
1. _Install_ the Chart:

   ```sh
   helm install my-release ./myapp
   ```

   - Helm takes the templates, substitutes values, and deploys the resources to Kubernetes.

1. _Upgrade_: Modify values.yaml or templates and upgrade using:

   ```sh
   helm upgrade my-release ./myapp
   ```

1. _Rollback_: If the upgrade fails:

   ```sh
   helm rollback my-release
   ```

1. _Uninstall_: To remove an application:

   ```sh
   helm uninstall my-release
   ```

## Example: deployment template

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: { { .Release.Name } }
spec:
  replicas: { { .Values.replicaCount } }
  template:
    spec:
      containers:
        - name: my-container
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
```

## Example: values.yaml

```yaml
replicaCount: 2
image:
  repository: nginx
  tag: latest
```

---

```json
{
  "Kubernetes-counter": 10
}
```
