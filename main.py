from kubernetes import client, config
from prometheus_api_client import PrometheusConnect
from get_metrics import *
import time

def main():
    pro = PrometheusConnect(url = "http://hikida-m:9090")

    svc_list = []
    config.load_kube_config()
    v1 = client.CoreV1Api()

    svcs = v1.list_namespaced_service('sock-shop')
    for svc in svcs.items:
        svc_name = svc.metadata.name
        if ('db' not in svc_name) and ('rabbit' not in svc_name):
            svc_list.append(svc_name)


    cpu_limit_list = []
    memory_limit_list = []
    for svc in svc_list:
        cpu_limit_query = "kube_pod_container_resource_limits{resource=\"cpu\", container=\"" + svc + "\"}"
        memory_limit_query = "kube_pod_container_resource_limits{resource=\"memory\", container=\"" + svc + "\"}"

        cpu_limit = float(pro.get_metric_range_data(metric_name=cpu_limit_query)[0].get('values')[-1][1])
        cpu_limit_list.append(cpu_limit)

        memory_limit = float(pro.get_metric_range_data(metric_name=memory_limit_query)[0].get('values')[-1][1])
        memory_limit_list.append(memory_limit)

    header = ['Time'] + svc_list
    cpu_data = [header]
    memory_data = [header]

    Time = 0
    while Time <= 300:
        cpu_data += [[Time] + metrics.get_cpu(svc_list, cpu_limit_list)]
        memory_data += [[Time] + metrics.get_memory(svc_list, memory_limit_list)]
        Time += 5
        time.sleep(5)

    path = "/home/hikida/promethe/csvfiles/"
    csv.generate_csv(cpu_data, path, "cpu_req0509a.csv")
    csv.generate_csv(memory_data, path, "memory_req0509a.csv")

if __name__ == "__main__":
    main()