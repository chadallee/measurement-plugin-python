import grpc
from grpc.framework.foundation import logging_pool

from driver_service import DriverService
import driver_pb2_grpc
from ni_measurementlink_service.discovery import DiscoveryClient, ServiceLocation
from ni_measurementlink_service.measurement.info import ServiceInfo

if __name__ == "__main__":
    servicer = DriverService()
    server = grpc.server(
            logging_pool.pool(max_workers=10),
            options=[
                ("grpc.max_receive_message_length", -1),
                ("grpc.max_send_message_length", -1),
            ],
        )
    driver_pb2_grpc.add_InstrumentInteractionServicer_to_server(servicer, server)

    host = "[::1]"
    port = str(server.add_insecure_port(f"{host}:57816"))
    address = f"http://{host}:{port}"
    server.start()
    print(f"[INFO] The server is now listening on 'localhost:{port}'")

    discovery_client = DiscoveryClient()
    service_location = ServiceLocation("localhost", port, "")
    service_info = ServiceInfo("ni.measurementlink.drivers.nivisa", "", ["ni.measurementlink.drivers"], display_name="NI-VISA DMM")
    registration_id = discovery_client.register_service(service_info=service_info, service_location=service_location)

    _ = input("Press enter to stop the server.")
    discovery_client.unregister_service(registration_id)
    server.stop(grace=5)
