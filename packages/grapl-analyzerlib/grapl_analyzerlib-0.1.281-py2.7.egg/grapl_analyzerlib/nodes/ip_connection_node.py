from grapl_analyzerlib.schemas import NodeSchema

class IpConnectionQuery():
    pass

class IpConnectionView():
    pass

class IpConnectionSchema(NodeSchema):
    def __init__(self):
        super(IpConnectionSchema, self).__init__()
        (
            self
            .with_str_prop('src_ip_address')
            .with_str_prop('src_port')
            .with_str_prop('dst_ip_address')
            .with_str_prop('dst_port')
            .with_int_prop('created_timestamp')
            .with_int_prop('terminated_timestamp')
            .with_int_prop('last_seen_timestamp')
            .with_forward_edge(
                'inbound_connection_to',
                ManyToOne(IpAddressSchema),
                'network_connections_from',
            )
        )

    @staticmethod
    def self_type() -> str:
        return "IpConnection"


def main():
    schema = IpConnectionSchema()

    query = generate_plugin_query(schema)
    view = generate_plugin_view(schema)
    query_extensions = generate_plugin_query_extensions(schema)
    view_extensions = generate_plugin_view_extensions(schema)

    print(query)
    print(view)
    print(query_extensions)
    print(view_extensions)


from grapl_analyzerlib.nodes.ip_address_node import IpAddressSchema

from grapl_analyzerlib.schemas.schema_builder import generate_plugin_view_extensions, generate_plugin_query_extensions, \
    generate_plugin_view, generate_plugin_query, ManyToOne


# if __name__ == '__main__':
#     main()
