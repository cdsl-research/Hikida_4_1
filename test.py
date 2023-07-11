from prometheus_api_client import PrometheusConnect
from kubernetes import client, config

pro = PrometheusConnect(url = "http://hikida-m:9090")
svc_list = []
config.load_kube_config()
v1 = client.CoreV1Api()
svcs = v1.list_namespaced_service('sock-shop')

for svc in svcs.items:
    svc_name = svc.metadata.name
    if ('db' not in svc_name) and ('rabbit' not in svc_name):
        svc_list.append(svc_name)

for i in range (len(svc_list)):

    memory_usage_query = "container_memory_working_set_bytes {service=\"kubelet\", container=\"" + svc_list[i] + "\"}"
    #cpu_limit_query = "kube_pod_container_resource_limits{resource=\"cpu\", container=\"" + svc_list[i] + "\"}"
    memory_limit_query = "kube_pod_container_resource_limits{resource=\"memory\", container=\"" + svc_list[i] + "\"}"
    cpu_usage_query = "rate(container_cpu_usage_seconds_total{service=\"kubelet\", namespace=\"sock-shop\", container=\"" + svc_list[i] + "\"}[5m])"

    cpu_usage = pro.custom_query(query=cpu_usage_query)[0].get('value')[1]

    memory_usage = pro.custom_query(query=memory_usage_query)[0].get('value')[1]
    cpu_limit = pro.get_metric_range_data(metric_name=memory_limit_query)[0].get('values')[-1][1]

    print(100 * float(memory_usage) / float(cpu_limit))
    print(svc_list[i], memory_usage)
    print(svc_list[i], cpu_limit)
"""
for svc in svc_list:
    pro = PrometheusConnect(url = "http://hikida-m:9090")
    print(svc)
    cpu_limit_query = "kube_pod_container_resource_limits{resource=\"cpu\", container=\"" + svc + "\"}"
    cpu_limit = (pro.get_metric_range_data(metric_name=cpu_limit_query)[0].get('values')[-1][1])#float [-1][1]
    print(cpu_limit) # 
"""
