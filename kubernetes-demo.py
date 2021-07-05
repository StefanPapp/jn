import yaml
from kubernetes import client, config
config.load_kube_config()


with open("./spark-pi.yaml") as f:
    dep = yaml.safe_load(f)
    custom_object_api = client.CustomObjectsApi()

    custom_object_api.create_namespaced_custom_object(
        group="sparkoperator.k8s.io",
        version="v1beta2",
        namespace="default",
        plural="sparkapplications",
        body=dep,
    )
    print("SparkApplication created")