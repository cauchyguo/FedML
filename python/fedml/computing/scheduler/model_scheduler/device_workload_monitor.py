
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
