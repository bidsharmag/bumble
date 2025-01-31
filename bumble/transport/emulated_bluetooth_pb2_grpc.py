# Copyright 2021-2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import emulated_bluetooth_packets_pb2 as emulated__bluetooth__packets__pb2
from . import emulated_bluetooth_pb2 as emulated__bluetooth__pb2


class EmulatedBluetoothServiceStub(object):
    """An Emulated Bluetooth Service exposes the emulated bluetooth chip from the
    android emulator. It allows you to register emulated bluetooth devices and
    control the packets that are exchanged between the device and the world.

    This service enables you to establish a "virtual network" of emulated
    bluetooth devices that can interact with each other.

    Note: This is not yet finalized, it is likely that these definitions will
    evolve.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.registerClassicPhy = channel.stream_stream(
            '/android.emulation.bluetooth.EmulatedBluetoothService/registerClassicPhy',
            request_serializer=emulated__bluetooth__pb2.RawData.SerializeToString,
            response_deserializer=emulated__bluetooth__pb2.RawData.FromString,
        )
        self.registerBlePhy = channel.stream_stream(
            '/android.emulation.bluetooth.EmulatedBluetoothService/registerBlePhy',
            request_serializer=emulated__bluetooth__pb2.RawData.SerializeToString,
            response_deserializer=emulated__bluetooth__pb2.RawData.FromString,
        )
        self.registerHCIDevice = channel.stream_stream(
            '/android.emulation.bluetooth.EmulatedBluetoothService/registerHCIDevice',
            request_serializer=emulated__bluetooth__packets__pb2.HCIPacket.SerializeToString,
            response_deserializer=emulated__bluetooth__packets__pb2.HCIPacket.FromString,
        )


class EmulatedBluetoothServiceServicer(object):
    """An Emulated Bluetooth Service exposes the emulated bluetooth chip from the
    android emulator. It allows you to register emulated bluetooth devices and
    control the packets that are exchanged between the device and the world.

    This service enables you to establish a "virtual network" of emulated
    bluetooth devices that can interact with each other.

    Note: This is not yet finalized, it is likely that these definitions will
    evolve.
    """

    def registerClassicPhy(self, request_iterator, context):
        """Connect device to link layer. This will establish a direct connection
        to the emulated bluetooth chip and configure the following:

        - Each connection creates a new device and attaches it to the link layer
        - Link Layer packets are transmitted directly to the phy

        This should be used for classic connections.

        This is used to directly connect various android emulators together.
        For example a wear device can connect to an android emulator through
        this.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def registerBlePhy(self, request_iterator, context):
        """Connect device to link layer. This will establish a direct connection
        to root canal and execute the following:

        - Each connection creates a new device and attaches it to the link layer
        - Link Layer packets are transmitted directly to the phy

        This should be used for BLE connections.

        This is used to directly connect various android emulators together.
        For example a wear device can connect to an android emulator through
        this.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def registerHCIDevice(self, request_iterator, context):
        """Connect the device to the emulated bluetooth chip. The device will
        participate in the network. You can configure the chip to scan, advertise
        and setup connections with other devices that are connected to the
        network.

        This is usually used when you have a need for an emulated bluetooth chip
        and have a bluetooth stack that can interpret and handle the packets
        correctly.

        For example the apache nimble stack can use this endpoint as the
        transport layer.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EmulatedBluetoothServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'registerClassicPhy': grpc.stream_stream_rpc_method_handler(
            servicer.registerClassicPhy,
            request_deserializer=emulated__bluetooth__pb2.RawData.FromString,
            response_serializer=emulated__bluetooth__pb2.RawData.SerializeToString,
        ),
        'registerBlePhy': grpc.stream_stream_rpc_method_handler(
            servicer.registerBlePhy,
            request_deserializer=emulated__bluetooth__pb2.RawData.FromString,
            response_serializer=emulated__bluetooth__pb2.RawData.SerializeToString,
        ),
        'registerHCIDevice': grpc.stream_stream_rpc_method_handler(
            servicer.registerHCIDevice,
            request_deserializer=emulated__bluetooth__packets__pb2.HCIPacket.FromString,
            response_serializer=emulated__bluetooth__packets__pb2.HCIPacket.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'android.emulation.bluetooth.EmulatedBluetoothService', rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class EmulatedBluetoothService(object):
    """An Emulated Bluetooth Service exposes the emulated bluetooth chip from the
    android emulator. It allows you to register emulated bluetooth devices and
    control the packets that are exchanged between the device and the world.

    This service enables you to establish a "virtual network" of emulated
    bluetooth devices that can interact with each other.

    Note: This is not yet finalized, it is likely that these definitions will
    evolve.
    """

    @staticmethod
    def registerClassicPhy(
        request_iterator,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.stream_stream(
            request_iterator,
            target,
            '/android.emulation.bluetooth.EmulatedBluetoothService/registerClassicPhy',
            emulated__bluetooth__pb2.RawData.SerializeToString,
            emulated__bluetooth__pb2.RawData.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def registerBlePhy(
        request_iterator,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.stream_stream(
            request_iterator,
            target,
            '/android.emulation.bluetooth.EmulatedBluetoothService/registerBlePhy',
            emulated__bluetooth__pb2.RawData.SerializeToString,
            emulated__bluetooth__pb2.RawData.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def registerHCIDevice(
        request_iterator,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.stream_stream(
            request_iterator,
            target,
            '/android.emulation.bluetooth.EmulatedBluetoothService/registerHCIDevice',
            emulated__bluetooth__packets__pb2.HCIPacket.SerializeToString,
            emulated__bluetooth__packets__pb2.HCIPacket.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
