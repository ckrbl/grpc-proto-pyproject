# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from gptest.proto import message_pb2 as gptest_dot_proto_dot_message__pb2

GRPC_GENERATED_VERSION = '1.64.0'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in gptest/proto/message_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class MyServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetSum = channel.unary_unary(
                '/gptest.MyService/GetSum',
                request_serializer=gptest_dot_proto_dot_message__pb2.SumReq.SerializeToString,
                response_deserializer=gptest_dot_proto_dot_message__pb2.SumRep.FromString,
                _registered_method=True)


class MyServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetSum(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MyServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetSum': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSum,
                    request_deserializer=gptest_dot_proto_dot_message__pb2.SumReq.FromString,
                    response_serializer=gptest_dot_proto_dot_message__pb2.SumRep.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'gptest.MyService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('gptest.MyService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class MyService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetSum(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/gptest.MyService/GetSum',
            gptest_dot_proto_dot_message__pb2.SumReq.SerializeToString,
            gptest_dot_proto_dot_message__pb2.SumRep.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
