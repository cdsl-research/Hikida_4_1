from prometheus_api_client import PrometheusConnect

## CPUの使用率（％）を取得
def get_cpu(svcs, cpu_limits):
    pro = PrometheusConnect(url = "http://hikida-m:9090")
    data = []
    for i in range (len(svcs)):
        cpu_usage_query = "rate(container_cpu_usage_seconds_total{service=\"kubelet\", namespace=\"sock-shop\", container=\"" + svcs[i] + "\"}[5m])"

        cpu_usage = pro.custom_query(query=cpu_usage_query)[0].get('value')[1]

        usage = 100 * (float(cpu_usage) / cpu_limits[i])
        
        data.append(usage)
    
    return data

## メモリの使用率（％）を取得
def get_memory(svcs, memory_limits):
    pro = PrometheusConnect(url = "http://hikida-m:9090")
    data = []
    for i in range (len(svcs)):
        # memory_usage_query = "container_memory_usage_bytes {service=\"kubelet\", container=\"" + svcs[i] + "\"}"
    
        memory_usage_query = "container_memory_working_set_bytes {service=\"kubelet\", container=\"" + svcs[i] + "\"}"

        memory_usage = pro.custom_query(query=memory_usage_query)[0].get('value')[1]

        usage = 100 * (float(memory_usage) / memory_limits[i])

        data.append(usage)
        
    
    return data

## fs readを取得
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