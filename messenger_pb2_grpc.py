# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import messenger_pb2 as messenger__pb2


class MaphiaStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.WaitForGame = channel.unary_stream(
                '/Maphia/WaitForGame',
                request_serializer=messenger__pb2.InitClient.SerializeToString,
                response_deserializer=messenger__pb2.InitClient.FromString,
                )
        self.GetClients = channel.unary_stream(
                '/Maphia/GetClients',
                request_serializer=messenger__pb2.Empty.SerializeToString,
                response_deserializer=messenger__pb2.InitClient.FromString,
                )
        self.Connect = channel.unary_unary(
                '/Maphia/Connect',
                request_serializer=messenger__pb2.InitClient.SerializeToString,
                response_deserializer=messenger__pb2.Empty.FromString,
                )
        self.EndDay = channel.unary_unary(
                '/Maphia/EndDay',
                request_serializer=messenger__pb2.InitClient.SerializeToString,
                response_deserializer=messenger__pb2.Empty.FromString,
                )
        self.VoteKill = channel.unary_unary(
                '/Maphia/VoteKill',
                request_serializer=messenger__pb2.InitClient.SerializeToString,
                response_deserializer=messenger__pb2.Empty.FromString,
                )
        self.KillNight = channel.unary_unary(
                '/Maphia/KillNight',
                request_serializer=messenger__pb2.InitClient.SerializeToString,
                response_deserializer=messenger__pb2.Empty.FromString,
                )
        self.Check = channel.unary_unary(
                '/Maphia/Check',
                request_serializer=messenger__pb2.InitClient.SerializeToString,
                response_deserializer=messenger__pb2.CheckResult.FromString,
                )
        self.PostMessage = channel.unary_unary(
                '/Maphia/PostMessage',
                request_serializer=messenger__pb2.ChatMessage.SerializeToString,
                response_deserializer=messenger__pb2.Empty.FromString,
                )
        self.GetMessages = channel.unary_stream(
                '/Maphia/GetMessages',
                request_serializer=messenger__pb2.InitClient.SerializeToString,
                response_deserializer=messenger__pb2.ChatMessage.FromString,
                )
        self.GetRole = channel.unary_unary(
                '/Maphia/GetRole',
                request_serializer=messenger__pb2.InitClient.SerializeToString,
                response_deserializer=messenger__pb2.Universal.FromString,
                )
        self.StartDay = channel.unary_stream(
                '/Maphia/StartDay',
                request_serializer=messenger__pb2.InitClient.SerializeToString,
                response_deserializer=messenger__pb2.InitClient.FromString,
                )


class MaphiaServicer(object):
    """Missing associated documentation comment in .proto file."""

    def WaitForGame(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetClients(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Connect(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EndDay(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VoteKill(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def KillNight(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Check(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PostMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMessages(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRole(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartDay(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MaphiaServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'WaitForGame': grpc.unary_stream_rpc_method_handler(
                    servicer.WaitForGame,
                    request_deserializer=messenger__pb2.InitClient.FromString,
                    response_serializer=messenger__pb2.InitClient.SerializeToString,
            ),
            'GetClients': grpc.unary_stream_rpc_method_handler(
                    servicer.GetClients,
                    request_deserializer=messenger__pb2.Empty.FromString,
                    response_serializer=messenger__pb2.InitClient.SerializeToString,
            ),
            'Connect': grpc.unary_unary_rpc_method_handler(
                    servicer.Connect,
                    request_deserializer=messenger__pb2.InitClient.FromString,
                    response_serializer=messenger__pb2.Empty.SerializeToString,
            ),
            'EndDay': grpc.unary_unary_rpc_method_handler(
                    servicer.EndDay,
                    request_deserializer=messenger__pb2.InitClient.FromString,
                    response_serializer=messenger__pb2.Empty.SerializeToString,
            ),
            'VoteKill': grpc.unary_unary_rpc_method_handler(
                    servicer.VoteKill,
                    request_deserializer=messenger__pb2.InitClient.FromString,
                    response_serializer=messenger__pb2.Empty.SerializeToString,
            ),
            'KillNight': grpc.unary_unary_rpc_method_handler(
                    servicer.KillNight,
                    request_deserializer=messenger__pb2.InitClient.FromString,
                    response_serializer=messenger__pb2.Empty.SerializeToString,
            ),
            'Check': grpc.unary_unary_rpc_method_handler(
                    servicer.Check,
                    request_deserializer=messenger__pb2.InitClient.FromString,
                    response_serializer=messenger__pb2.CheckResult.SerializeToString,
            ),
            'PostMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.PostMessage,
                    request_deserializer=messenger__pb2.ChatMessage.FromString,
                    response_serializer=messenger__pb2.Empty.SerializeToString,
            ),
            'GetMessages': grpc.unary_stream_rpc_method_handler(
                    servicer.GetMessages,
                    request_deserializer=messenger__pb2.InitClient.FromString,
                    response_serializer=messenger__pb2.ChatMessage.SerializeToString,
            ),
            'GetRole': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRole,
                    request_deserializer=messenger__pb2.InitClient.FromString,
                    response_serializer=messenger__pb2.Universal.SerializeToString,
            ),
            'StartDay': grpc.unary_stream_rpc_method_handler(
                    servicer.StartDay,
                    request_deserializer=messenger__pb2.InitClient.FromString,
                    response_serializer=messenger__pb2.InitClient.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Maphia', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Maphia(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def WaitForGame(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Maphia/WaitForGame',
            messenger__pb2.InitClient.SerializeToString,
            messenger__pb2.InitClient.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetClients(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Maphia/GetClients',
            messenger__pb2.Empty.SerializeToString,
            messenger__pb2.InitClient.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Connect(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Maphia/Connect',
            messenger__pb2.InitClient.SerializeToString,
            messenger__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EndDay(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Maphia/EndDay',
            messenger__pb2.InitClient.SerializeToString,
            messenger__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def VoteKill(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Maphia/VoteKill',
            messenger__pb2.InitClient.SerializeToString,
            messenger__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def KillNight(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Maphia/KillNight',
            messenger__pb2.InitClient.SerializeToString,
            messenger__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Check(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Maphia/Check',
            messenger__pb2.InitClient.SerializeToString,
            messenger__pb2.CheckResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PostMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Maphia/PostMessage',
            messenger__pb2.ChatMessage.SerializeToString,
            messenger__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMessages(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Maphia/GetMessages',
            messenger__pb2.InitClient.SerializeToString,
            messenger__pb2.ChatMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRole(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Maphia/GetRole',
            messenger__pb2.InitClient.SerializeToString,
            messenger__pb2.Universal.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StartDay(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Maphia/StartDay',
            messenger__pb2.InitClient.SerializeToString,
            messenger__pb2.InitClient.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
