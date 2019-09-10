# Contributing

Kubeaddons-Configs is an Addon Repository which manages a predefined set of Addons and their configurations for deployment via [Kubeaddons](https://github.com/mesosphere/kubeaddons).

The [Kubeaddons Contributing Documentation](https://github.com/mesosphere/kubeaddons/blob/master/CONTRIBUTING.md) governs contributions to this repo in addition to other sections of this document.

## PR Readiness

PR's should be marked `wip` until the following are taken care of:

1. Manual testing of the Addon has succeeded against the most recent release of the `kubeaddons` controller
2. CI must pass

Once these are complete the PR can be marked as `ready`.

## Creating New Addons

You can create new Addons by providing an `Addon` [resource](https://kubernetes.io/docs/concepts/) in a [manifest](https://kubernetes.io/docs/concepts/cluster-administration/manage-deployment/) placed in the `templates/` directory.

See the [Custom Resource Definition](https://github.com/mesosphere/kubeaddons/blob/master/config/crd/bases/kubeaddons.mesosphere.io_addons.yaml) for the `Addon` type for structure, and the [samples](https://github.com/mesosphere/kubeaddons/tree/master/config/samples) for more explicit implementation examples.

The overall workflow for contributing a new Addon is:

1. define an `Addon` resource as discussed above
2. install the [Kubeaddons Controller](https://github.com/mesosphere/kubeaddons/blob/master/config/samples/manager.yaml) to your Kubernetes cluster
3. deploy the new `Addon`
4. watch the pod logs for the controller, and ensure that the `Addon` status becomes `ready: true`
5. test the addon functionality as appropriate for its type

1. Manual testing of the Addon has succeeded against the most recent release of the `kubeaddons` controller
2. CI must pass

## Customizing Existing Addons

Addons can be customized via their manifests in the `templates/` directory.

Changing an addons name or namespace is done in the `metadata` field.

Configuration of the `Addon` resource itself is primarily done via via the `spec` field, particularly changing the [helm values configuration](https://v3.helm.sh/docs/topics/chart_best_practices/values/) of a helm-based addon is done via the `spec.ChartReference.Values` field.

## ExtraSteps

Some addons may be in need of additional logic beyond what's available in the implementing driver (e.g. Helm). For instance: it may be desired to have an addo generate a password for a user interface on startup and store that in a [Kubernetes Secret](https://kubernetes.io/docs/concepts/configuration/secret/). These kinds of tasks can be accomplished by adding functionality to the [Kubeaddons Extrasteps](https://github.com/mesosphere/kubeaddons-extrasteps) repo which packages tooling into [initContainers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/) and [jobs](https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/) for after-deployment Addon logic.

