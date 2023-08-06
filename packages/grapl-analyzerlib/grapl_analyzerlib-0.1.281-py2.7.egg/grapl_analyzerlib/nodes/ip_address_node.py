from typing import *

from grapl_analyzerlib.nodes.types import PropertyT
from grapl_analyzerlib.nodes.viewable import EdgeViewT, ForwardEdgeView
from grapl_analyzerlib.nodes.comparators import Cmp, IntCmp, _int_cmps, StrCmp, _str_cmps
from grapl_analyzerlib.prelude import *

from pydgraph import DgraphClient

from grapl_analyzerlib.schemas import NodeSchema


class IpAddressSchema(NodeSchema):
    def __init__(self):
        super(IpAddressSchema, self).__init__()

        (
            self
                .with_str_prop('ip_address')
                .with_int_prop('first_seen_timestamp')
                .with_int_prop('last_seen_timestamp')
                .with_forward_edge(
                'ip_connections',
                ManyToMany(IpConnectionSchema),
                'connecting_ips'
            )
        )

    @staticmethod
    def self_type() -> str:
        return "IpAddress"


from typing import *

from grapl_analyzerlib.nodes.types import PropertyT
from grapl_analyzerlib.nodes.viewable import EdgeViewT, ForwardEdgeView
from grapl_analyzerlib.nodes.comparators import Cmp, IntCmp, _int_cmps, StrCmp, _str_cmps
from grapl_analyzerlib.prelude import *

from pydgraph import DgraphClient

IIpAddressQuery = TypeVar('IIpAddressQuery', bound='IpAddressQuery')


class IpAddressQuery(DynamicNodeQuery):
    def __init__(self):
        super(IpAddressQuery, self).__init__('IpAddress', IpAddressView)
        self._first_seen_timestamp = []  # type: List[List[Cmp[int]]]
        self._last_seen_timestamp = []  # type: List[List[Cmp[int]]]

        self._ip_address = []  # type: List[List[Cmp[str]]]

        self._ip_connections = None  # type: Optional[IIpConnectionQuery]

    def with_ip_address(
            self,
            eq: Optional['StrCmp'] = None,
            contains: Optional['StrCmp'] = None,
            ends_with: Optional['StrCmp'] = None,
    ) -> 'NQ':
        self.set_str_property_filter(
            "ip_address", _str_cmps("ip_address", eq=eq, contains=contains, ends_with=ends_with)
        )
        return self

    def with_first_seen_timestamp(
            self: 'NQ',
            eq: Optional['IntCmp'] = None,
            gt: Optional['IntCmp'] = None,
            lt: Optional['IntCmp'] = None,
    ) -> 'NQ':
        self.set_int_property_filter(
            "first_seen_timestamp", _int_cmps("first_seen_timestamp", eq=eq, gt=gt, lt=lt)
        )
        return self

    def with_last_seen_timestamp(
            self: 'NQ',
            eq: Optional['IntCmp'] = None,
            gt: Optional['IntCmp'] = None,
            lt: Optional['IntCmp'] = None,
    ) -> 'NQ':
        self.set_int_property_filter(
            "last_seen_timestamp", _int_cmps("last_seen_timestamp", eq=eq, gt=gt, lt=lt)
        )
        return self

    def with_ip_connections(
            self: 'NQ',
            ip_connections_query: Optional['IIpConnectionQuery'] = None
    ) -> 'NQ':
        ip_connections = ip_connections_query or IpConnectionQuery()

        self.set_forward_edge_filter("ip_connections", ip_connections)
        ip_connections.set_reverse_edge_filter("~ip_connections", self, "ip_connections")
        return self


IIpAddressView = TypeVar('IIpAddressView', bound='IpAddressView')


class IpAddressView(DynamicNodeView):

    def __init__(
            self,
            dgraph_client: DgraphClient,
            node_key: str,
            uid: str,
            node_type: str,
            first_seen_timestamp: Optional[int] = None,
            last_seen_timestamp: Optional[int] = None,
            ip_address: Optional[str] = None,
            ip_connections: 'Optional[List[IpConnectionView]]' = None,

    ):
        super(IpAddressView, self).__init__(
            dgraph_client=dgraph_client, node_key=node_key, uid=uid, node_type=node_type
        )
        self.dgraph_client = dgraph_client
        self.node_key = node_key
        self.uid = uid
        self.node_type = node_type

        self.first_seen_timestamp = first_seen_timestamp
        self.last_seen_timestamp = last_seen_timestamp
        self.ip_address = ip_address
        self.ip_connections = ip_connections

    def get_first_seen_timestamp(self) -> Optional[int]:
        if not self.first_seen_timestamp:
            self.first_seen_timestamp = cast(Optional[int], self.fetch_property("first_seen_timestamp", int))
        return self.first_seen_timestamp

    def get_last_seen_timestamp(self) -> Optional[int]:
        if not self.last_seen_timestamp:
            self.last_seen_timestamp = cast(Optional[int], self.fetch_property("last_seen_timestamp", int))
        return self.last_seen_timestamp

    def get_ip_address(self) -> Optional[str]:
        if not self.ip_address:
            self.ip_address = cast(Optional[str], self.fetch_property("ip_address", str))
        return self.ip_address

    @staticmethod
    def _get_property_types() -> Mapping[str, "PropertyT"]:
        return {
            'first_seen_timestamp': int,
            'last_seen_timestamp': int,
            'ip_address': str,
        }

    @staticmethod
    def _get_forward_edge_types() -> Mapping[str, "EdgeViewT"]:
        f_edges = {
            'ip_connections': [IpConnectionView],
        }  # type: Dict[str, Optional["EdgeViewT"]]

        return cast(Mapping[str, "EdgeViewT"], {
            fe[0]: fe[1] for fe in f_edges.items() if fe[1]
        })

    def _get_forward_edges(self) -> "Mapping[str, ForwardEdgeView]":
        f_edges = {
            'ip_connections': self.ip_connections,
        }  # type: Dict[str, Optional[ForwardEdgeView]]

        return cast(
            "Mapping[str, ForwardEdgeView]",
            {fe[0]: fe[1] for fe in f_edges.items() if fe[1]}
        )

    def _get_properties(self, fetch: bool = False) -> Mapping[str, Union[str, int]]:
        props = {
            'first_seen_timestamp': self.first_seen_timestamp,
            'last_seen_timestamp': self.last_seen_timestamp,
            'ip_address': self.ip_address,
        }

        return {p[0]: p[1] for p in props.items() if p[1] is not None}


# class IpAddressExtendsIpConnectionQuery(IpConnectionQuery):
#     def with_connecting_ips(
#             self: 'NQ',
#             connecting_ips_query: Optional['IIpAddressQuery'] = None
#     ) -> 'NQ':
#         connecting_ips = connecting_ips_query or IpAddressQuery()
#         connecting_ips.with_ip_connections(
#             cast(IpConnectionQuery, self)
#         )
#
#         return self
#
#
# class IpAddressExtendsIpConnectionView(IpConnectionView):
#     def get_connecting_ips(
#             self,
#     ) -> 'IpAddressView':
#         return cast(IpAddressView, self.fetch_edge("~ip_connections", IpAddressView))


def main():
    schema = IpAddressSchema()

    query = generate_plugin_query(schema)
    view = generate_plugin_view(schema)
    query_extensions = generate_plugin_query_extensions(schema)
    view_extensions = generate_plugin_view_extensions(schema)

    print(query)
    print(view)
    print(query_extensions)
    print(view_extensions)


from grapl_analyzerlib.nodes.ip_connection_node import IpConnectionSchema, IpConnectionView
from grapl_analyzerlib.schemas.schema_builder import generate_plugin_view_extensions, generate_plugin_query_extensions, \
    generate_plugin_view, generate_plugin_query, ManyToMany

if __name__ == '__main__':
    main()
