from prometheus_api_client import PrometheusConnect
from kubernetes import client, config

pro = PrometheusConnect(url = "http://hikida-m:9090")
svc_list = []
config.load_kube_config()
v1 = client.CoreV1Api()
svcs = v1.list_namespaced_service('sock-shop')

def get_read(svcs):
    pro = PrometheusConnect(url = "http://hikida-m:9090")
    data = []
    for i in range (len(svcs)):
    
        fs_read_query = "container_fs_reads_bytes_total {service=\"kubelet\", container=\"" + svcs[i] + "\"}"

        fs_read = pro.custom_query(query=fs_read_query)[0].get('value')[1]

        data.append(fs_read)
        
    
    return data


## fs writeを取得
def get_write(svcs):
    pro = PrometheusConnect(url = "http://hikida-m:9090")
    data = []
    for i in range (len(svcs)):
    
        fs_write_query = "container_fs_writes_bytes_total {service=\"kubelet\", container=\"" + svcs[i] + "\"}"

        fs_write = pro.custom_query(query=fs_write_query)[0].get('value')[1]

        data.append(fs_write)
        
    
    return data

for svc in svcs.items:
    svc_name = svc.metadata.name
    if ('db' not in svc_name) and ('rabbit' not in svc_name):
        svc_list.append(svc_name)

print(get_read(svc_list))
print(get_write(svc_list))


"""
for svc in svc_list:
    pro = PrometheusConnect(url = "http://hikida-m:9090")
    print(svc)
    cpu_limit_query = "kube_pod_container_resource_limits{resource=\"cpu\", container=\"" + svc + "\"}"
    cpu_limit = (pro.get_metric_range_data(metric_name=cpu_limit_query)[0].get('values')[-1][1])#float [-1][1]
    print(cpu_limit) # 
"""
