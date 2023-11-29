
from collections import defaultdict

class FedMLWorkloadMonitor():

    def __init__(self):
        # We need to keep the history of all previous
        # latencies (qps) and response times (rt) to 
        # construct better predictive models.
        self.state = defaultdict(dict())

    def update_state(self, index, qps, rt):
        # index is an incremental counter
        self.state[index]["qps"] = qps
        self.state[index]["rt"] = rt
    
    def scale_out(self) -> bool:        
        latest_index = max(self.state.keys())
        latest_qps = self.state[latest_index]["qps"]        
        qps_threshold = 200 # 200ms
        if latest_qps >= qps_threshold:
            return True
        else:
            return False
    
    def scale_in(self) -> bool:
        latest_index = max(self.state.keys())
        latest_qps = self.state[latest_index]["qps"]        
        qps_threshold = 200 # 200ms
        if latest_qps < qps_threshold:
            return True
        else:
            return False

if __name__ == "__main__":
    ms_per_sec = 1000
    ns_per_ms = 1000 * 1000

    import time    
    start_time = time.time_ns()
    delay_ns = 1000000
    end_time = time.time_ns() + delay_ns
    latency_ms = (end_time - start_time) / ns_per_ms
    latency_sec = latency_ms / ms_per_sec
    qps = 1 / latency_sec

    # Throughout or QPS (queries-per-second) is measured 
    # as the number of requests the system can handle per 
    # unit of time (elapsed/cost). For a total number of 
    # issued requests over a total elapsed time in seconds:
    # throughout or qps = #total_requests / #total_time_sec

    # e.g., #total_requests = 1 and #total_time_sec = 10sec
    #   qps = 1/10 = 0.1 queries-per-second
    # e.g., #total_requests = 100 and #total_time_sec = 60sec
    #   qps = 100/60 = 1.66 queries-per-second

    # Response Time (RT) is the end-to-end time or round-trip time.
    # That is, the total time it takes for an end user to receive a reply 
    # to a submitted request. For instance, in a Web Application with a 
    # Backend platform, Response Time will represent the time it takes to 
    # perform a round-trip similar to the following:
    #   UI Request -> Web App -> Backend -> Web App -> UI Reply

    # Latency is a more fine-grained metric and has a more precise 
    # and narrow definition compared to Response Time. System latency 
    # is measured as the time it takes for a system to handle k
    # operations/requests. For instance if a backend system handles 
    # 200 requests within 300 seconds, then its latency is:
    #   latency = 300 / 200 = 1.5 seconds-per-request


    print("Latency: {}\nQPS: {}".format(latency_sec, qps), flush=True)

