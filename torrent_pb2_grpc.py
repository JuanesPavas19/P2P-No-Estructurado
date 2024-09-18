# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import torrent_pb2 as torrent__pb2

GRPC_GENERATED_VERSION = '1.66.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in torrent_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class TorrentServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetTorrent = channel.unary_unary(
                '/TorrentService/GetTorrent',
                request_serializer=torrent__pb2.TorrentRequest.SerializeToString,
                response_deserializer=torrent__pb2.TorrentResponse.FromString,
                _registered_method=True)
        self.RegisterPeer = channel.unary_unary(
                '/TorrentService/RegisterPeer',
                request_serializer=torrent__pb2.PeerRequest.SerializeToString,
                response_deserializer=torrent__pb2.PeerResponse.FromString,
                _registered_method=True)
        self.SearchFile = channel.unary_unary(
                '/TorrentService/SearchFile',
                request_serializer=torrent__pb2.SearchFileRequest.SerializeToString,
                response_deserializer=torrent__pb2.SearchFileResponse.FromString,
                _registered_method=True)
        self.UploadFile = channel.unary_unary(
                '/TorrentService/UploadFile',
                request_serializer=torrent__pb2.UploadFileRequest.SerializeToString,
                response_deserializer=torrent__pb2.UploadFileResponse.FromString,
                _registered_method=True)
        self.GetFile = channel.unary_unary(
                '/TorrentService/GetFile',
                request_serializer=torrent__pb2.GetFileRequest.SerializeToString,
                response_deserializer=torrent__pb2.GetFileResponse.FromString,
                _registered_method=True)


class TorrentServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetTorrent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RegisterPeer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SearchFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UploadFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TorrentServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetTorrent': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTorrent,
                    request_deserializer=torrent__pb2.TorrentRequest.FromString,
                    response_serializer=torrent__pb2.TorrentResponse.SerializeToString,
            ),
            'RegisterPeer': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterPeer,
                    request_deserializer=torrent__pb2.PeerRequest.FromString,
                    response_serializer=torrent__pb2.PeerResponse.SerializeToString,
            ),
            'SearchFile': grpc.unary_unary_rpc_method_handler(
                    servicer.SearchFile,
                    request_deserializer=torrent__pb2.SearchFileRequest.FromString,
                    response_serializer=torrent__pb2.SearchFileResponse.SerializeToString,
            ),
            'UploadFile': grpc.unary_unary_rpc_method_handler(
                    servicer.UploadFile,
                    request_deserializer=torrent__pb2.UploadFileRequest.FromString,
                    response_serializer=torrent__pb2.UploadFileResponse.SerializeToString,
            ),
            'GetFile': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFile,
                    request_deserializer=torrent__pb2.GetFileRequest.FromString,
                    response_serializer=torrent__pb2.GetFileResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'TorrentService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('TorrentService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class TorrentService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetTorrent(request,
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
            '/TorrentService/GetTorrent',
            torrent__pb2.TorrentRequest.SerializeToString,
            torrent__pb2.TorrentResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RegisterPeer(request,
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
            '/TorrentService/RegisterPeer',
            torrent__pb2.PeerRequest.SerializeToString,
            torrent__pb2.PeerResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SearchFile(request,
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
            '/TorrentService/SearchFile',
            torrent__pb2.SearchFileRequest.SerializeToString,
            torrent__pb2.SearchFileResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UploadFile(request,
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
            '/TorrentService/UploadFile',
            torrent__pb2.UploadFileRequest.SerializeToString,
            torrent__pb2.UploadFileResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetFile(request,
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
            '/TorrentService/GetFile',
            torrent__pb2.GetFileRequest.SerializeToString,
            torrent__pb2.GetFileResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
