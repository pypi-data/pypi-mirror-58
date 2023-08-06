from typing import *

from pydgraph import DgraphClient

from grapl_analyzerlib.nodes.comparators import Cmp, IntCmp, _int_cmps, StrCmp, _str_cmps
from grapl_analyzerlib.nodes.types import PropertyT
from grapl_analyzerlib.nodes.viewable import EdgeViewT, ForwardEdgeView
from grapl_analyzerlib.prelude import *
from grapl_analyzerlib.schemas import NodeSchema


class IpPortSchema(NodeSchema):
    def __init__(self):
        super(IpPortSchema, self).__init__()
        (
            self
            .with_str_prop('ip_address')
            .with_str_prop('protocol')
            .with_int_prop('port')
            .with_int_prop('first_seen_timestamp')
            .with_int_prop('last_seen_timestamp')
            .with_forward_edge(
                'network_connections',
                ManyToMany(NetworkConnectionSchema),
                'connections_from',
            )
        )

    @staticmethod
    def self_type() -> str:
        return "IpPort"


def main():
    schema = IpPortSchema()

    query = generate_plugin_query(schema)
    view = generate_plugin_view(schema)
    query_extensions = generate_plugin_query_extensions(schema)
    view_extensions = generate_plugin_view_extensions(schema)

    print(query)
    print(view)
    print(query_extensions)
    print(view_extensions)



if __name__ == '__main__':
    main()

from grapl_analyzerlib.nodes.network_connection_node import NetworkConnectionSchema
from grapl_analyzerlib.schemas.schema_builder import generate_plugin_query, generate_plugin_view, \
    generate_plugin_query_extensions, generate_plugin_view_extensions, ManyToMany
