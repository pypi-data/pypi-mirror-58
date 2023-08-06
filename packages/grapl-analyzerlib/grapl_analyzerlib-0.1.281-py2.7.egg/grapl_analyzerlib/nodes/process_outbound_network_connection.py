from grapl_analyzerlib.schemas import NodeSchema


class ProcessOutboundNetworkConnectionSchema(NodeSchema):
    def __init__(self):
        super(ProcessOutboundNetworkConnectionSchema, self).__init__()
        (
            self
            .with_str_prop('ip_address')
            .with_str_prop('protocol')
            .with_int_prop('created_timestamp')
            .with_int_prop('terminated_timestamp')
            .with_int_prop('last_seen_timestamp')
            .with_int_prop('port')
            .with_forward_edge(
                'process_outbound_connection',
                # The IP + Port that was connected to
                ManyToOne(IpPortSchema),
                'connections_from_processes'
            )
            .with_forward_edge(
                'connected_over',
                # The IP + Port that was connected to
                ManyToOne(IpPortSchema),
                'process_connections'
            )
        )

    @staticmethod
    def self_type() -> str:
        return "ProcessOutboundNetworkConnection"


def main():
    schema = ProcessOutboundNetworkConnectionSchema()

    query = generate_plugin_query(schema)
    view = generate_plugin_view(schema)
    query_extensions = generate_plugin_query_extensions(schema)
    view_extensions = generate_plugin_view_extensions(schema)

    print(query)
    print(view)
    print(query_extensions)
    print(view_extensions)


from grapl_analyzerlib.schemas.schema_builder import generate_plugin_query, generate_plugin_view, \
    generate_plugin_query_extensions, generate_plugin_view_extensions, ManyToOne
from grapl_analyzerlib.nodes.ip_port_node import IpPortSchema


if __name__ == '__main__':
    main()

