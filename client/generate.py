import random
import sys
import grpc
from datetime import datetime, timedelta, timezone
from threading import Event

# Import generated gRPC classes
from proto.generated.service_mesh_pb2_grpc import ServiceMeshMetricServiceStub
from proto.generated.service_mesh_pb2 import (
    ServiceMeshMetrics,
    HTTPServiceMeshMetric,
    HTTPServiceMeshMetrics,
    Protocol,
    DetectPoint,
)

# gRPC server address
oap_address = sys.argv[1] if len(sys.argv) > 1 else "localhost:18080"
days = int(sys.argv[2]) if len(sys.argv) > 2 else 1

# Set up gRPC channel and stub
channel = grpc.insecure_channel(oap_address)
stub = ServiceMeshMetricServiceStub(channel)

def format_timestamp(timestamp_ms):
    return datetime.fromtimestamp(timestamp_ms / 1000).strftime('%Y-%m-%d %H:%M')

def send_metrics(metrics: [ServiceMeshMetrics]):
    """Send metrics to gRPC server."""
    latch = Event()

    def response_handler(response):
        latch.set()

    def error_handler(exception):
        print("Error:", exception)
        latch.set()

    # Open gRPC stream
    stub.collect(iter(metrics))

    try:
        response_handler(None)
    except grpc.RpcError as e:
        error_handler(e)

    latch.wait()


def generate():
    """Generate and send metrics for the given number of days."""
    now = datetime.now()
    start_time = now - timedelta(days=days + 1)

    metrics_list = []
    while start_time <= now:
        end_time = start_time + timedelta(minutes=1)

        metric = HTTPServiceMeshMetric(
            sourceServiceName="e2e-test-source-service",
            sourceServiceInstance="e2e-test-source-service-instance",
            destServiceName="e2e-test-dest-service",
            destServiceInstance="e2e-test-dest-service-instance",
            endpoint="e2e/test",
            latency=random.randint(50, 70),
            responseCode=200,
            status=True,
            protocol=Protocol.HTTP,
            detectPoint=DetectPoint.server,
            startTime=int(start_time.timestamp() * 1000),
            endTime=int(end_time.timestamp() * 1000)
        )

        service_mesh_metrics = ServiceMeshMetrics(
            httpMetrics=HTTPServiceMeshMetrics(
                metrics=[metric]
            )
        )
        metrics_list.append(service_mesh_metrics)

        if len(metrics_list) == 600:
            send_metrics(metrics_list)
            print("Sending metrics for interval:", format_timestamp(metrics_list[0].httpMetrics.metrics[0].startTime),
                  "-", format_timestamp(metrics_list[-1].httpMetrics.metrics[0].endTime))
            metrics_list = []

        start_time = end_time  # Move to the next interval

    if metrics_list:
        send_metrics(metrics_list)
        print("Sending metrics for interval:", format_timestamp(metrics_list[0].httpMetrics.metrics[0].startTime),
              "-", format_timestamp(metrics_list[-1].httpMetrics.metrics[0].endTime))

    print("Metrics send success!")


if __name__ == "__main__":
    generate()
