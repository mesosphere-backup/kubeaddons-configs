**NOTE**: this repository **is now deprecated**. Please only update [kubernetes-base-addons](https://github.com/mesosphere/kubernetes-base-addons) unless a fix from there should also be backported for konvoy <= 1.2.

# Addon Repository

This is a repository for `Addon` resources managed by `Kubeaddons`.

# Contributing

See our [contributing documentation](/CONTRIBUTING.md) for details on how to contribute to this repo.

## Goals

* provides a repository for storing addon resources with default configurations
* provides alternative configurations for addons for specific cloud providers

## Non-Goals

Logic for addon configurations doesn't belong in these configurations, nor should changes here cover the scope of adding or managing additional resources for an addon (resources can be added via [charts](https://github.com/mesosphere/charts)).

If optional [initContainer](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/) or [job](https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/) functionality is needed for an addon you're working on you may want to use [kubeaddons extrasteps](https://github.com/mesosphere/kubeaddons-extrasteps) to add your custom logic and build a docker image for use here. It may be more appropriate to add these containers to [Charts](https://github.com/mesosphere/charts) however if they're absolutely required for the application's function.

