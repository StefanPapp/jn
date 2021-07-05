import yaml
import subprocess
from kubernetes import client, config


class calculate():

    @staticmethod
    def calculate_pi():
        config.load_kube_config()
        subprocess.run("kubectl delete sparkapplication spark-pi", shell=True, check=True)
        with open("/opt/spark-on-k8s-operator/examples/spark-pi.yaml") as f:
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

    @staticmethod
    def get_pi():
        return subprocess.run("kubectl logs spark-pi-driver | grep ^Pi", shell=True, capture_output=True, text=True).stdout