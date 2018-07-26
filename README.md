## jenkins-job-builder-multibranch-pipeline

A plugin for [jenkins-job-builder](http://docs.openstack.org/infra/jenkins-job-builder) V1 to support [multibranch pipeline](https://wiki.jenkins-ci.org/display/JENKINS/Pipeline+Multibranch+Plugin) job generation.

#### Usage:

Plugin adds a new project-type `multibranch-pipeline` and a job definition field `multibranch-pipeline`.
There are two distinct job definitions.

Create a multibranch pipeline job loading pipeline script from SCM.
```yaml
- job:
    name: example-scm-script
    project-type: multibranch-pipeline
    multibranch-pipeline:
      source: # normal scm definitions
        - git:
            remote: 'git@github.com:github-username/repository-name.git'
            credentials-id: 'credentialsId'
            includes: 'develop release/* feature/*'
            excludes: 'test/*'
            ignore-on-push-notifications: false

```

Definition type is chosen automatically by detecting presence of "source" field.
