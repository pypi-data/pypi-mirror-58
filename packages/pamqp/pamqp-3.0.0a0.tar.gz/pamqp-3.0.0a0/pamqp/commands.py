"""
AMQP Classes & Methods
======================

Auto-generated, do not edit. To Generate run `.tools/codegen.py`

"""
import typing
import warnings

from pamqp import base, common, constants


class Connection:
    """Work with socket connections

    The connection class provides methods for a client to establish a network
    connection to a server, and for both peers to operate the connection
    thereafter.

    """
    __slots__ = []

    # AMQP Class Number and Mapping Index
    frame_id = 10
    index = 0x000A0000

    class Start(base.Frame):
        """Start connection negotiation

        This method starts the connection negotiation process by telling the
        client the protocol version that the server proposes, along with a list
        of security mechanisms which the client can use for authentication.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 10
        index = 0x000A000A
        name = 'Connection.Start'

        # Specifies if this is a synchronous AMQP method
        synchronous = True

        # Valid responses to this method
        valid_responses = ['Connection.StartOk']

        # AMQ Method Attributes
        __slots__ = [
            'version_major', 'version_minor', 'server_properties',
            'mechanisms', 'locales'
        ]

        # Attribute Typing
        __annotations__ = {
            'version_major': int,
            'version_minor': int,
            'server_properties': typing.Optional[common.FieldTable],
            'mechanisms': str,
            'locales': str
        }

        # Attribute AMQ Types
        _version_major = 'octet'
        _version_minor = 'octet'
        _server_properties = 'table'
        _mechanisms = 'longstr'
        _locales = 'longstr'

        def __init__(
                self,
                version_major: int = 0,
                version_minor: int = 9,
                server_properties: typing.Optional[common.FieldTable] = None,
                mechanisms: str = 'PLAIN',
                locales: str = 'en_US'):
            """Initialize the Connection.Start class

            :param version_major: Protocol major version
            :param version_minor: Protocol minor version
            :param server_properties: Server properties
            :param mechanisms: Available security mechanisms
            :param locales: Available message locales

            """
            # Protocol major version
            self.version_major = version_major

            # Protocol minor version
            self.version_minor = version_minor

            # Server properties
            self.server_properties = server_properties

            # Available security mechanisms
            self.mechanisms = mechanisms

            # Available message locales
            self.locales = locales

    class StartOk(base.Frame):
        """Select security mechanism and locale

        This method selects a SASL security mechanism.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 11
        index = 0x000A000B
        name = 'Connection.StartOk'

        # Specifies if this is a synchronous AMQP method
        synchronous = False

        # AMQ Method Attributes
        __slots__ = ['client_properties', 'mechanism', 'response', 'locale']

        # Attribute Typing
        __annotations__ = {
            'client_properties': typing.Optional[common.FieldTable],
            'mechanism': str,
            'response': str,
            'locale': str
        }

        # Attribute AMQ Types
        _client_properties = 'table'
        _mechanism = 'shortstr'
        _response = 'longstr'
        _locale = 'shortstr'

        def __init__(
                self,
                client_properties: typing.Optional[common.FieldTable] = None,
                mechanism: str = 'PLAIN',
                response: str = '',
                locale: str = 'en_US'):
            """Initialize the Connection.StartOk class

            :param client_properties: Client properties
            :param mechanism: Selected security mechanism
            :param response: Security response data
            :param locale: Selected message locale

            """
            # Client properties
            self.client_properties = client_properties

            # Selected security mechanism
            self.mechanism = mechanism

            # Security response data
            self.response = response

            # Selected message locale
            self.locale = locale

    class Secure(base.Frame):
        """Security mechanism challenge

        The SASL protocol works by exchanging challenges and responses until
        both peers have received sufficient information to authenticate each
        other. This method challenges the client to provide more information.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 20
        index = 0x000A0014
        name = 'Connection.Secure'

        # Specifies if this is a synchronous AMQP method
        synchronous = True

        # Valid responses to this method
        valid_responses = ['Connection.SecureOk']

        # AMQ Method Attributes
        __slots__ = ['challenge']

        # Attribute Typing
        __annotations__ = {'challenge': str}

        # Attribute AMQ Types
        _challenge = 'longstr'

        def __init__(self, challenge: str = ''):
            """Initialize the Connection.Secure class

            :param challenge: Security challenge data

            """
            # Security challenge data
            self.challenge = challenge

    class SecureOk(base.Frame):
        """Security mechanism response

        This method attempts to authenticate, passing a block of SASL data for
        the security mechanism at the server side.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 21
        index = 0x000A0015
        name = 'Connection.SecureOk'

        # Specifies if this is a synchronous AMQP method
        synchronous = False

        # AMQ Method Attributes
        __slots__ = ['response']

        # Attribute Typing
        __annotations__ = {'response': str}

        # Attribute AMQ Types
        _response = 'longstr'

        def __init__(self, response: str = ''):
            """Initialize the Connection.SecureOk class

            :param response: Security response data

            """
            # Security response data
            self.response = response

    class Tune(base.Frame):
        """Propose connection tuning parameters

        This method proposes a set of connection configuration values to the
        client. The client can accept and/or adjust these.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 30
        index = 0x000A001E
        name = 'Connection.Tune'

        # Specifies if this is a synchronous AMQP method
        synchronous = True

        # Valid responses to this method
        valid_responses = ['Connection.TuneOk']

        # AMQ Method Attributes
        __slots__ = ['channel_max', 'frame_max', 'heartbeat']

        # Attribute Typing
        __annotations__ = {
            'channel_max': int,
            'frame_max': int,
            'heartbeat': int
        }

        # Attribute AMQ Types
        _channel_max = 'short'
        _frame_max = 'long'
        _heartbeat = 'short'

        def __init__(self,
                     channel_max: int = 0,
                     frame_max: int = 0,
                     heartbeat: int = 0):
            """Initialize the Connection.Tune class

            :param channel_max: Proposed maximum channels
            :param frame_max: Proposed maximum frame size
            :param heartbeat: Desired heartbeat delay

            """
            # Proposed maximum channels
            self.channel_max = channel_max

            # Proposed maximum frame size
            self.frame_max = frame_max

            # Desired heartbeat delay
            self.heartbeat = heartbeat

    class TuneOk(base.Frame):
        """Negotiate connection tuning parameters

        This method sends the client's connection tuning parameters to the
        server. Certain fields are negotiated, others provide capability
        information.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 31
        index = 0x000A001F
        name = 'Connection.TuneOk'

        # Specifies if this is a synchronous AMQP method
        synchronous = False

        # AMQ Method Attributes
        __slots__ = ['channel_max', 'frame_max', 'heartbeat']

        # Attribute Typing
        __annotations__ = {
            'channel_max': int,
            'frame_max': int,
            'heartbeat': int
        }

        # Attribute AMQ Types
        _channel_max = 'short'
        _frame_max = 'long'
        _heartbeat = 'short'

        def __init__(self,
                     channel_max: int = 0,
                     frame_max: int = 0,
                     heartbeat: int = 0):
            """Initialize the Connection.TuneOk class

            :param channel_max: Negotiated maximum channels
            :param frame_max: Negotiated maximum frame size
            :param heartbeat: Desired heartbeat delay

            """
            # Negotiated maximum channels
            self.channel_max = channel_max

            # Negotiated maximum frame size
            self.frame_max = frame_max

            # Desired heartbeat delay
            self.heartbeat = heartbeat

    class Open(base.Frame):
        """Open connection to virtual host

        This method opens a connection to a virtual host, which is a collection
        of resources, and acts to separate multiple application domains within
        a server. The server may apply arbitrary limits per virtual host, such
        as the number of each type of entity that may be used, per connection
        and/or in total.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 40
        index = 0x000A0028
        name = 'Connection.Open'

        # Specifies if this is a synchronous AMQP method
        synchronous = True

        # Valid responses to this method
        valid_responses = ['Connection.OpenOk']

        # AMQ Method Attributes
        __slots__ = ['virtual_host', 'capabilities', 'insist']

        # Attribute Typing
        __annotations__ = {
            'virtual_host': str,
            'capabilities': str,
            'insist': bool
        }

        # Attribute AMQ Types
        _virtual_host = 'shortstr'
        _capabilities = 'shortstr'
        _insist = 'bit'

        def __init__(self,
                     virtual_host: str = '/',
                     capabilities: str = '',
                     insist: bool = False):
            """Initialize the Connection.Open class

            :param virtual_host: Virtual host name
            :param capabilities: Deprecated
            :param insist: Deprecated

            """
            # Virtual host name
            self.virtual_host = virtual_host

            # Deprecated
            self.capabilities = capabilities

            # Deprecated
            self.insist = insist

    class OpenOk(base.Frame):
        """Signal that connection is ready

        This method signals to the client that the connection is ready for use.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 41
        index = 0x000A0029
        name = 'Connection.OpenOk'

        # Specifies if this is a synchronous AMQP method
        synchronous = False

        # AMQ Method Attributes
        __slots__ = ['known_hosts']

        # Attribute Typing
        __annotations__ = {'known_hosts': str}

        # Attribute AMQ Types
        _known_hosts = 'shortstr'

        def __init__(self, known_hosts: str = ''):
            """Initialize the Connection.OpenOk class

            :param known_hosts: Deprecated

            """
            # Deprecated
            self.known_hosts = known_hosts

    class Close(base.Frame):
        """Request a connection close

        This method indicates that the sender wants to close the connection.
        This may be due to internal conditions (e.g. a forced shut-down) or due
        to an error handling a specific method, i.e. an exception. When a close
        is due to an exception, the sender provides the class and method id of
        the method which caused the exception.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 50
        index = 0x000A0032
        name = 'Connection.Close'

        # Specifies if this is a synchronous AMQP method
        synchronous = True

        # Valid responses to this method
        valid_responses = ['Connection.CloseOk']

        # AMQ Method Attributes
        __slots__ = ['reply_code', 'reply_text', 'class_id', 'method_id']

        # Attribute Typing
        __annotations__ = {
            'reply_code': int,
            'reply_text': str,
            'class_id': int,
            'method_id': int
        }

        # Attribute AMQ Types
        _reply_code = 'short'
        _reply_text = 'shortstr'
        _class_id = 'short'
        _method_id = 'short'

        def __init__(self,
                     reply_code: int = 0,
                     reply_text: str = '',
                     class_id: int = 0,
                     method_id: int = 0):
            """Initialize the Connection.Close class

            :param reply_code: Reply code from server
            :param reply_text: Localised reply text
            :param class_id: Failing method class
            :param method_id: Failing method ID

            """
            # Reply code from server
            self.reply_code = reply_code

            # Localised reply text
            self.reply_text = reply_text

            # Failing method class
            self.class_id = class_id

            # Failing method ID
            self.method_id = method_id

    class CloseOk(base.Frame):
        """Confirm a connection close

        This method confirms a Connection.Close method and tells the recipient
        that it is safe to release resources for the connection and close the
        socket.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 51
        index = 0x000A0033
        name = 'Connection.CloseOk'

        # Specifies if this is a synchronous AMQP method
        synchronous = False

    class Blocked(base.Frame):
        """Signal that connection is blocked

        This method signals to the client that the connection is blocked by
        RabbitMQ.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 60
        index = 0x000A003C
        name = 'Connection.Blocked'

        # Specifies if this is a synchronous AMQP method
        synchronous = False

        # AMQ Method Attributes
        __slots__ = ['reason']

        # Attribute Typing
        __annotations__ = {'reason': str}

        # Attribute AMQ Types
        _reason = 'shortstr'

        def __init__(self, reason: str = ''):
            """Initialize the Connection.Blocked class

            :param reason:

            """
            self.reason = reason

    class Unblocked(base.Frame):
        """Signal that connection is no longer blocked

        This method signals to the client that the connection is no longer
        blocked by RabbitMQ.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 61
        index = 0x000A003D
        name = 'Connection.Unblocked'

        # Specifies if this is a synchronous AMQP method
        synchronous = False

    class UpdateSecret(base.Frame):
        # AMQP Method Number and Mapping Index
        frame_id = 70
        index = 0x000A0046
        name = 'Connection.UpdateSecret'

        # Specifies if this is a synchronous AMQP method
        synchronous = True

        # Valid responses to this method
        valid_responses = ['Connection.UpdateSecretOk']

        # AMQ Method Attributes
        __slots__ = ['new_secret', 'reason']

        # Attribute Typing
        __annotations__ = {'new_secret': str, 'reason': str}

        # Attribute AMQ Types
        _new_secret = 'longstr'
        _reason = 'shortstr'

        def __init__(self, new_secret: str = '', reason: str = ''):
            """Initialize the Connection.UpdateSecret class

            :param new-secret:
            :param reason:

            """
            self.new_secret = new_secret
            self.reason = reason

    class UpdateSecretOk(base.Frame):
        # AMQP Method Number and Mapping Index
        frame_id = 71
        index = 0x000A0047
        name = 'Connection.UpdateSecretOk'

        # Specifies if this is a synchronous AMQP method
        synchronous = False


class Channel:
    """Work with channels

    The channel class provides methods for a client to establish a channel to a
    server and for both peers to operate the channel thereafter.

    """
    __slots__ = []

    # AMQP Class Number and Mapping Index
    frame_id = 20
    index = 0x00140000

    class Open(base.Frame):
        """Open a channel for use

        This method opens a channel to the server.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 10
        index = 0x0014000A
        name = 'Channel.Open'

        # Specifies if this is a synchronous AMQP method
        synchronous = True

        # Valid responses to this method
        valid_responses = ['Channel.OpenOk']

        # AMQ Method Attributes
        __slots__ = ['out_of_band']

        # Attribute Typing
        __annotations__ = {'out_of_band': str}

        # Attribute AMQ Types
        _out_of_band = 'shortstr'

        def __init__(self, out_of_band: str = ''):
            """Initialize the Channel.Open class

            :param out_of_band: Protocol level field, do not use, must be zero.

            """
            # Protocol level field, do not use, must be zero.
            self.out_of_band = out_of_band

    class OpenOk(base.Frame):
        """Signal that the channel is ready

        This method signals to the client that the channel is ready for use.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 11
        index = 0x0014000B
        name = 'Channel.OpenOk'

        # Specifies if this is a synchronous AMQP method
        synchronous = False

        # AMQ Method Attributes
        __slots__ = ['channel_id']

        # Attribute Typing
        __annotations__ = {'channel_id': str}

        # Attribute AMQ Types
        _channel_id = 'longstr'

        def __init__(self, channel_id: str = ''):
            """Initialize the Channel.OpenOk class

            :param channel_id: Deprecated

            """
            # Deprecated
            self.channel_id = channel_id

    class Flow(base.Frame):
        """Enable/disable flow from peer

        This method asks the peer to pause or restart the flow of content data
        sent by a consumer. This is a simple flow-control mechanism that a peer
        can use to avoid overflowing its queues or otherwise finding itself
        receiving more messages than it can process. Note that this method is
        not intended for window control. It does not affect contents returned
        by Basic.Get-Ok methods.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 20
        index = 0x00140014
        name = 'Channel.Flow'

        # Specifies if this is a synchronous AMQP method
        synchronous = True

        # Valid responses to this method
        valid_responses = ['Channel.FlowOk']

        # AMQ Method Attributes
        __slots__ = ['active']

        # Attribute Typing
        __annotations__ = {'active': bool}

        # Attribute AMQ Types
        _active = 'bit'

        def __init__(self, active: bool = None):
            """Initialize the Channel.Flow class

            :param active: Start/stop content frames

            """
            # Start/stop content frames
            self.active = active

    class FlowOk(base.Frame):
        """Confirm a flow method

        Confirms to the peer that a flow command was received and processed.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 21
        index = 0x00140015
        name = 'Channel.FlowOk'

        # Specifies if this is a synchronous AMQP method
        synchronous = False

        # AMQ Method Attributes
        __slots__ = ['active']

        # Attribute Typing
        __annotations__ = {'active': bool}

        # Attribute AMQ Types
        _active = 'bit'

        def __init__(self, active: bool = None):
            """Initialize the Channel.FlowOk class

            :param active: Current flow setting

            """
            # Current flow setting
            self.active = active

    class Close(base.Frame):
        """Request a channel close

        This method indicates that the sender wants to close the channel. This
        may be due to internal conditions (e.g. a forced shut-down) or due to
        an error handling a specific method, i.e. an exception. When a close is
        due to an exception, the sender provides the class and method id of the
        method which caused the exception.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 40
        index = 0x00140028
        name = 'Channel.Close'

        # Specifies if this is a synchronous AMQP method
        synchronous = True

        # Valid responses to this method
        valid_responses = ['Channel.CloseOk']

        # AMQ Method Attributes
        __slots__ = ['reply_code', 'reply_text', 'class_id', 'method_id']

        # Attribute Typing
        __annotations__ = {
            'reply_code': int,
            'reply_text': str,
            'class_id': int,
            'method_id': int
        }

        # Attribute AMQ Types
        _reply_code = 'short'
        _reply_text = 'shortstr'
        _class_id = 'short'
        _method_id = 'short'

        def __init__(self,
                     reply_code: int = 0,
                     reply_text: str = '',
                     class_id: int = 0,
                     method_id: int = 0):
            """Initialize the Channel.Close class

            :param reply_code: Reply code from server
            :param reply_text: Localised reply text
            :param class_id: Failing method class
            :param method_id: Failing method ID

            """
            # Reply code from server
            self.reply_code = reply_code

            # Localised reply text
            self.reply_text = reply_text

            # Failing method class
            self.class_id = class_id

            # Failing method ID
            self.method_id = method_id

    class CloseOk(base.Frame):
        """Confirm a channel close

        This method confirms a Channel.Close method and tells the recipient
        that it is safe to release resources for the channel.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 41
        index = 0x00140029
        name = 'Channel.CloseOk'

        # Specifies if this is a synchronous AMQP method
        synchronous = False


class Exchange:
    """Work with exchanges

    Exchanges match and distribute messages across queues. Exchanges can be
    configured in the server or declared at runtime.

    """
    __slots__ = []

    # AMQP Class Number and Mapping Index
    frame_id = 40
    index = 0x00280000

    class Declare(base.Frame):
        """Verify exchange exists, create if needed

        This method creates an exchange if it does not already exist, and if
        the exchange exists, verifies that it is of the correct and expected
        class.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 10
        index = 0x0028000A
        name = 'Exchange.Declare'

        # Specifies if this is a synchronous AMQP method
        synchronous = True

        # Valid responses to this method
        valid_responses = ['Exchange.DeclareOk']

        # AMQ Method Attributes
        __slots__ = [
            'ticket', 'exchange', 'exchange_type', 'passive', 'durable',
            'auto_delete', 'internal', 'nowait', 'arguments'
        ]

        # Attribute Typing
        __annotations__ = {
            'ticket': int,
            'exchange': str,
            'exchange_type': str,
            'passive': bool,
            'durable': bool,
            'auto_delete': bool,
            'internal': bool,
            'nowait': bool,
            'arguments': typing.Optional[common.FieldTable]
        }

        # Attribute AMQ Types
        _ticket = 'short'
        _exchange = 'shortstr'
        _exchange_type = 'shortstr'
        _passive = 'bit'
        _durable = 'bit'
        _auto_delete = 'bit'
        _internal = 'bit'
        _nowait = 'bit'
        _arguments = 'table'

        def __init__(self,
                     ticket: int = 0,
                     exchange: str = '',
                     exchange_type: str = 'direct',
                     passive: bool = False,
                     durable: bool = False,
                     auto_delete: bool = False,
                     internal: bool = False,
                     nowait: bool = False,
                     arguments: typing.Optional[common.FieldTable] = None):
            """Initialize the Exchange.Declare class

            :param ticket: Deprecated
            :param exchange:
            :param exchange_type: Exchange type
            :param passive: Do not create exchange
            :param durable: Request a durable exchange
            :param auto_delete: Automatically delete when not in use
            :param internal: Deprecated
            :param nowait: Do not send a reply method
            :param arguments: Arguments for declaration

            """
            # Deprecated
            self.ticket = ticket
            self.exchange = exchange

            # Exchange type
            self.exchange_type = exchange_type

            # Do not create exchange
            self.passive = passive

            # Request a durable exchange
            self.durable = durable

            # Automatically delete when not in use
            self.auto_delete = auto_delete

            # Deprecated
            self.internal = internal

            # Do not send a reply method
            self.nowait = nowait

            # Arguments for declaration
            self.arguments = arguments or {}

    class DeclareOk(base.Frame):
        """Confirm exchange declaration

        This method confirms a Declare method and confirms the name of the
        exchange, essential for automatically-named exchanges.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 11
        index = 0x0028000B
        name = 'Exchange.DeclareOk'

        # Specifies if this is a synchronous AMQP method
        synchronous = False

    class Delete(base.Frame):
        """Delete an exchange

        This method deletes an exchange. When an exchange is deleted all queue
        bindings on the exchange are cancelled.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 20
        index = 0x00280014
        name = 'Exchange.Delete'

        # Specifies if this is a synchronous AMQP method
        synchronous = True

        # Valid responses to this method
        valid_responses = ['Exchange.DeleteOk']

        # AMQ Method Attributes
        __slots__ = ['ticket', 'exchange', 'if_unused', 'nowait']

        # Attribute Typing
        __annotations__ = {
            'ticket': int,
            'exchange': str,
            'if_unused': bool,
            'nowait': bool
        }

        # Attribute AMQ Types
        _ticket = 'short'
        _exchange = 'shortstr'
        _if_unused = 'bit'
        _nowait = 'bit'

        def __init__(self,
                     ticket: int = 0,
                     exchange: str = '',
                     if_unused: bool = False,
                     nowait: bool = False):
            """Initialize the Exchange.Delete class

            :param ticket: Deprecated
            :param exchange:
            :param if_unused: Delete only if unused
            :param nowait: Do not send a reply method

            """
            # Deprecated
            self.ticket = ticket
            self.exchange = exchange

            # Delete only if unused
            self.if_unused = if_unused

            # Do not send a reply method
            self.nowait = nowait

    class DeleteOk(base.Frame):
        """Confirm deletion of an exchange

        This method confirms the deletion of an exchange.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 21
        index = 0x00280015
        name = 'Exchange.DeleteOk'

        # Specifies if this is a synchronous AMQP method
        synchronous = False

    class Bind(base.Frame):
        # AMQP Method Number and Mapping Index
        frame_id = 30
        index = 0x0028001E
        name = 'Exchange.Bind'

        # Specifies if this is a synchronous AMQP method
        synchronous = True

        # Valid responses to this method
        valid_responses = ['Exchange.BindOk']

        # AMQ Method Attributes
        __slots__ = [
            'ticket', 'destination', 'source', 'routing_key', 'nowait',
            'arguments'
        ]

        # Attribute Typing
        __annotations__ = {
            'ticket': int,
            'destination': str,
            'source': str,
            'routing_key': str,
            'nowait': bool,
            'arguments': typing.Optional[common.FieldTable]
        }

        # Attribute AMQ Types
        _ticket = 'short'
        _destination = 'shortstr'
        _source = 'shortstr'
        _routing_key = 'shortstr'
        _nowait = 'bit'
        _arguments = 'table'

        def __init__(self,
                     ticket: int = 0,
                     destination: str = '',
                     source: str = '',
                     routing_key: str = '',
                     nowait: bool = False,
                     arguments: typing.Optional[common.FieldTable] = None):
            """Initialize the Exchange.Bind class

            :param ticket: Deprecated
            :param destination:
            :param source:
            :param routing-key:
            :param nowait: Do not send a reply method
            :param arguments:

            """
            # Deprecated
            self.ticket = ticket
            self.destination = destination
            self.source = source
            self.routing_key = routing_key

            # Do not send a reply method
            self.nowait = nowait
            self.arguments = arguments or {}

    class BindOk(base.Frame):
        # AMQP Method Number and Mapping Index
        frame_id = 31
        index = 0x0028001F
        name = 'Exchange.BindOk'

        # Specifies if this is a synchronous AMQP method
        synchronous = False

    class Unbind(base.Frame):
        # AMQP Method Number and Mapping Index
        frame_id = 40
        index = 0x00280028
        name = 'Exchange.Unbind'

        # Specifies if this is a synchronous AMQP method
        synchronous = True

        # Valid responses to this method
        valid_responses = ['Exchange.UnbindOk']

        # AMQ Method Attributes
        __slots__ = [
            'ticket', 'destination', 'source', 'routing_key', 'nowait',
            'arguments'
        ]

        # Attribute Typing
        __annotations__ = {
            'ticket': int,
            'destination': str,
            'source': str,
            'routing_key': str,
            'nowait': bool,
            'arguments': typing.Optional[common.FieldTable]
        }

        # Attribute AMQ Types
        _ticket = 'short'
        _destination = 'shortstr'
        _source = 'shortstr'
        _routing_key = 'shortstr'
        _nowait = 'bit'
        _arguments = 'table'

        def __init__(self,
                     ticket: int = 0,
                     destination: str = '',
                     source: str = '',
                     routing_key: str = '',
                     nowait: bool = False,
                     arguments: typing.Optional[common.FieldTable] = None):
            """Initialize the Exchange.Unbind class

            :param ticket: Deprecated
            :param destination:
            :param source:
            :param routing-key:
            :param nowait: Do not send a reply method
            :param arguments:

            """
            # Deprecated
            self.ticket = ticket
            self.destination = destination
            self.source = source
            self.routing_key = routing_key

            # Do not send a reply method
            self.nowait = nowait
            self.arguments = arguments or {}

    class UnbindOk(base.Frame):
        # AMQP Method Number and Mapping Index
        frame_id = 51
        index = 0x00280033
        name = 'Exchange.UnbindOk'

        # Specifies if this is a synchronous AMQP method
        synchronous = False


class Queue:
    """Work with queues

    Queues store and forward messages. Queues can be configured in the server
    or created at runtime. Queues must be attached to at least one exchange in
    order to receive messages from publishers.

    """
    __slots__ = []

    # AMQP Class Number and Mapping Index
    frame_id = 50
    index = 0x00320000

    class Declare(base.Frame):
        """Declare queue, create if needed

        This method creates or checks a queue. When creating a new queue the
        client can specify various properties that control the durability of
        the queue and its contents, and the level of sharing for the queue.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 10
        index = 0x0032000A
        name = 'Queue.Declare'

        # Specifies if this is a synchronous AMQP method
        synchronous = True

        # Valid responses to this method
        valid_responses = ['Queue.DeclareOk']

        # AMQ Method Attributes
        __slots__ = [
            'ticket', 'queue', 'passive', 'durable', 'exclusive',
            'auto_delete', 'nowait', 'arguments'
        ]

        # Attribute Typing
        __annotations__ = {
            'ticket': int,
            'queue': str,
            'passive': bool,
            'durable': bool,
            'exclusive': bool,
            'auto_delete': bool,
            'nowait': bool,
            'arguments': typing.Optional[common.FieldTable]
        }

        # Attribute AMQ Types
        _ticket = 'short'
        _queue = 'shortstr'
        _passive = 'bit'
        _durable = 'bit'
        _exclusive = 'bit'
        _auto_delete = 'bit'
        _nowait = 'bit'
        _arguments = 'table'

        def __init__(self,
                     ticket: int = 0,
                     queue: str = '',
                     passive: bool = False,
                     durable: bool = False,
                     exclusive: bool = False,
                     auto_delete: bool = False,
                     nowait: bool = False,
                     arguments: typing.Optional[common.FieldTable] = None):
            """Initialize the Queue.Declare class

            :param ticket: Deprecated
            :param queue:
            :param passive: Do not create queue
            :param durable: Request a durable queue
            :param exclusive: Request an exclusive queue
            :param auto_delete: Auto-delete queue when unused
            :param nowait: Do not send a reply method
            :param arguments: Arguments for declaration

            """
            # Deprecated
            self.ticket = ticket
            self.queue = queue

            # Do not create queue
            self.passive = passive

            # Request a durable queue
            self.durable = durable

            # Request an exclusive queue
            self.exclusive = exclusive

            # Auto-delete queue when unused
            self.auto_delete = auto_delete

            # Do not send a reply method
            self.nowait = nowait

            # Arguments for declaration
            self.arguments = arguments or {}

    class DeclareOk(base.Frame):
        """Confirms a queue definition

        This method confirms a Declare method and confirms the name of the
        queue, essential for automatically-named queues.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 11
        index = 0x0032000B
        name = 'Queue.DeclareOk'

        # Specifies if this is a synchronous AMQP method
        synchronous = False

        # AMQ Method Attributes
        __slots__ = ['queue', 'message_count', 'consumer_count']

        # Attribute Typing
        __annotations__ = {
            'queue': str,
            'message_count': int,
            'consumer_count': int
        }

        # Attribute AMQ Types
        _queue = 'shortstr'
        _message_count = 'long'
        _consumer_count = 'long'

        def __init__(self,
                     queue: str = '',
                     message_count: int = 0,
                     consumer_count: int = 0):
            """Initialize the Queue.DeclareOk class

            :param queue:
            :param message_count: Number of messages in queue
            :param consumer_count: Number of consumers

            """
            self.queue = queue

            # Number of messages in queue
            self.message_count = message_count

            # Number of consumers
            self.consumer_count = consumer_count

    class Bind(base.Frame):
        """Bind queue to an exchange

        This method binds a queue to an exchange. Until a queue is bound it
        will not receive any messages. In a classic messaging model, store-and-
        forward queues are bound to a direct exchange and subscription queues
        are bound to a topic exchange.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 20
        index = 0x00320014
        name = 'Queue.Bind'

        # Specifies if this is a synchronous AMQP method
        synchronous = True

        # Valid responses to this method
        valid_responses = ['Queue.BindOk']

        # AMQ Method Attributes
        __slots__ = [
            'ticket', 'queue', 'exchange', 'routing_key', 'nowait', 'arguments'
        ]

        # Attribute Typing
        __annotations__ = {
            'ticket': int,
            'queue': str,
            'exchange': str,
            'routing_key': str,
            'nowait': bool,
            'arguments': typing.Optional[common.FieldTable]
        }

        # Attribute AMQ Types
        _ticket = 'short'
        _queue = 'shortstr'
        _exchange = 'shortstr'
        _routing_key = 'shortstr'
        _nowait = 'bit'
        _arguments = 'table'

        def __init__(self,
                     ticket: int = 0,
                     queue: str = '',
                     exchange: str = '',
                     routing_key: str = '',
                     nowait: bool = False,
                     arguments: typing.Optional[common.FieldTable] = None):
            """Initialize the Queue.Bind class

            :param ticket: Deprecated
            :param queue:
            :param exchange: Name of the exchange to bind to
            :param routing_key: Message routing key
            :param nowait: Do not send a reply method
            :param arguments: Arguments for binding

            """
            # Deprecated
            self.ticket = ticket
            self.queue = queue

            # Name of the exchange to bind to
            self.exchange = exchange

            # Message routing key
            self.routing_key = routing_key

            # Do not send a reply method
            self.nowait = nowait

            # Arguments for binding
            self.arguments = arguments or {}

    class BindOk(base.Frame):
        """Confirm bind successful

        This method confirms that the bind was successful.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 21
        index = 0x00320015
        name = 'Queue.BindOk'

        # Specifies if this is a synchronous AMQP method
        synchronous = False

    class Purge(base.Frame):
        """Purge a queue

        This method removes all messages from a queue which are not awaiting
        acknowledgment.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 30
        index = 0x0032001E
        name = 'Queue.Purge'

        # Specifies if this is a synchronous AMQP method
        synchronous = True

        # Valid responses to this method
        valid_responses = ['Queue.PurgeOk']

        # AMQ Method Attributes
        __slots__ = ['ticket', 'queue', 'nowait']

        # Attribute Typing
        __annotations__ = {'ticket': int, 'queue': str, 'nowait': bool}

        # Attribute AMQ Types
        _ticket = 'short'
        _queue = 'shortstr'
        _nowait = 'bit'

        def __init__(self,
                     ticket: int = 0,
                     queue: str = '',
                     nowait: bool = False):
            """Initialize the Queue.Purge class

            :param ticket: Deprecated
            :param queue:
            :param nowait: Do not send a reply method

            """
            # Deprecated
            self.ticket = ticket
            self.queue = queue

            # Do not send a reply method
            self.nowait = nowait

    class PurgeOk(base.Frame):
        """Confirms a queue purge

        This method confirms the purge of a queue.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 31
        index = 0x0032001F
        name = 'Queue.PurgeOk'

        # Specifies if this is a synchronous AMQP method
        synchronous = False

        # AMQ Method Attributes
        __slots__ = ['message_count']

        # Attribute Typing
        __annotations__ = {'message_count': int}

        # Attribute AMQ Types
        _message_count = 'long'

        def __init__(self, message_count: int = 0):
            """Initialize the Queue.PurgeOk class

            :param message-count:

            """
            self.message_count = message_count

    class Delete(base.Frame):
        """Delete a queue

        This method deletes a queue. When a queue is deleted any pending
        messages are sent to a dead-letter queue if this is defined in the
        server configuration, and all consumers on the queue are cancelled.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 40
        index = 0x00320028
        name = 'Queue.Delete'

        # Specifies if this is a synchronous AMQP method
        synchronous = True

        # Valid responses to this method
        valid_responses = ['Queue.DeleteOk']

        # AMQ Method Attributes
        __slots__ = ['ticket', 'queue', 'if_unused', 'if_empty', 'nowait']

        # Attribute Typing
        __annotations__ = {
            'ticket': int,
            'queue': str,
            'if_unused': bool,
            'if_empty': bool,
            'nowait': bool
        }

        # Attribute AMQ Types
        _ticket = 'short'
        _queue = 'shortstr'
        _if_unused = 'bit'
        _if_empty = 'bit'
        _nowait = 'bit'

        def __init__(self,
                     ticket: int = 0,
                     queue: str = '',
                     if_unused: bool = False,
                     if_empty: bool = False,
                     nowait: bool = False):
            """Initialize the Queue.Delete class

            :param ticket: Deprecated
            :param queue:
            :param if_unused: Delete only if unused
            :param if_empty: Delete only if empty
            :param nowait: Do not send a reply method

            """
            # Deprecated
            self.ticket = ticket
            self.queue = queue

            # Delete only if unused
            self.if_unused = if_unused

            # Delete only if empty
            self.if_empty = if_empty

            # Do not send a reply method
            self.nowait = nowait

    class DeleteOk(base.Frame):
        """Confirm deletion of a queue

        This method confirms the deletion of a queue.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 41
        index = 0x00320029
        name = 'Queue.DeleteOk'

        # Specifies if this is a synchronous AMQP method
        synchronous = False

        # AMQ Method Attributes
        __slots__ = ['message_count']

        # Attribute Typing
        __annotations__ = {'message_count': int}

        # Attribute AMQ Types
        _message_count = 'long'

        def __init__(self, message_count: int = 0):
            """Initialize the Queue.DeleteOk class

            :param message-count:

            """
            self.message_count = message_count

    class Unbind(base.Frame):
        """Unbind a queue from an exchange

        This method unbinds a queue from an exchange.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 50
        index = 0x00320032
        name = 'Queue.Unbind'

        # Specifies if this is a synchronous AMQP method
        synchronous = True

        # Valid responses to this method
        valid_responses = ['Queue.UnbindOk']

        # AMQ Method Attributes
        __slots__ = ['ticket', 'queue', 'exchange', 'routing_key', 'arguments']

        # Attribute Typing
        __annotations__ = {
            'ticket': int,
            'queue': str,
            'exchange': str,
            'routing_key': str,
            'arguments': typing.Optional[common.FieldTable]
        }

        # Attribute AMQ Types
        _ticket = 'short'
        _queue = 'shortstr'
        _exchange = 'shortstr'
        _routing_key = 'shortstr'
        _arguments = 'table'

        def __init__(self,
                     ticket: int = 0,
                     queue: str = '',
                     exchange: str = '',
                     routing_key: str = '',
                     arguments: typing.Optional[common.FieldTable] = None):
            """Initialize the Queue.Unbind class

            :param ticket: Deprecated
            :param queue:
            :param exchange:
            :param routing_key: Routing key of binding
            :param arguments: Arguments of binding

            """
            # Deprecated
            self.ticket = ticket
            self.queue = queue
            self.exchange = exchange

            # Routing key of binding
            self.routing_key = routing_key

            # Arguments of binding
            self.arguments = arguments or {}

    class UnbindOk(base.Frame):
        """Confirm unbind successful

        This method confirms that the unbind was successful.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 51
        index = 0x00320033
        name = 'Queue.UnbindOk'

        # Specifies if this is a synchronous AMQP method
        synchronous = False


class Basic:
    """Work with basic content

    The Basic class provides methods that support an industry-standard
    messaging model.

    """
    __slots__ = []

    # AMQP Class Number and Mapping Index
    frame_id = 60
    index = 0x003C0000

    class Qos(base.Frame):
        """Specify quality of service

        This method requests a specific quality of service. The QoS can be
        specified for the current channel or for all channels on the
        connection. The particular properties and semantics of a qos method
        always depend on the content class semantics. Though the qos method
        could in principle apply to both peers, it is currently meaningful only
        for the server.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 10
        index = 0x003C000A
        name = 'Basic.Qos'

        # Specifies if this is a synchronous AMQP method
        synchronous = True

        # Valid responses to this method
        valid_responses = ['Basic.QosOk']

        # AMQ Method Attributes
        __slots__ = ['prefetch_size', 'prefetch_count', 'global_']

        # Attribute Typing
        __annotations__ = {
            'prefetch_size': int,
            'prefetch_count': int,
            'global_': bool
        }

        # Attribute AMQ Types
        _prefetch_size = 'long'
        _prefetch_count = 'short'
        _global_ = 'bit'

        def __init__(self,
                     prefetch_size: int = 0,
                     prefetch_count: int = 0,
                     global_: bool = False):
            """Initialize the Basic.Qos class

            :param prefetch_size: Prefetch window in octets
            :param prefetch_count: Prefetch window in messages
            :param global_: Apply to entire connection

            """
            # Prefetch window in octets
            self.prefetch_size = prefetch_size

            # Prefetch window in messages
            self.prefetch_count = prefetch_count

            # Apply to entire connection
            self.global_ = global_

    class QosOk(base.Frame):
        """Confirm the requested qos

        This method tells the client that the requested QoS levels could be
        handled by the server. The requested QoS applies to all active
        consumers until a new QoS is defined.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 11
        index = 0x003C000B
        name = 'Basic.QosOk'

        # Specifies if this is a synchronous AMQP method
        synchronous = False

    class Consume(base.Frame):
        """Start a queue consumer

        This method asks the server to start a "consumer", which is a transient
        request for messages from a specific queue. Consumers last as long as
        the channel they were declared on, or until the client cancels them.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 20
        index = 0x003C0014
        name = 'Basic.Consume'

        # Specifies if this is a synchronous AMQP method
        synchronous = True

        # Valid responses to this method
        valid_responses = ['Basic.ConsumeOk']

        # AMQ Method Attributes
        __slots__ = [
            'ticket', 'queue', 'consumer_tag', 'no_local', 'no_ack',
            'exclusive', 'nowait', 'arguments'
        ]

        # Attribute Typing
        __annotations__ = {
            'ticket': int,
            'queue': str,
            'consumer_tag': str,
            'no_local': bool,
            'no_ack': bool,
            'exclusive': bool,
            'nowait': bool,
            'arguments': typing.Optional[common.FieldTable]
        }

        # Attribute AMQ Types
        _ticket = 'short'
        _queue = 'shortstr'
        _consumer_tag = 'shortstr'
        _no_local = 'bit'
        _no_ack = 'bit'
        _exclusive = 'bit'
        _nowait = 'bit'
        _arguments = 'table'

        def __init__(self,
                     ticket: int = 0,
                     queue: str = '',
                     consumer_tag: str = '',
                     no_local: bool = False,
                     no_ack: bool = False,
                     exclusive: bool = False,
                     nowait: bool = False,
                     arguments: typing.Optional[common.FieldTable] = None):
            """Initialize the Basic.Consume class

            :param ticket: Deprecated
            :param queue:
            :param consumer-tag:
            :param no_local: Do not deliver own messages
            :param no_ack: No acknowledgement needed
            :param exclusive: Request exclusive access
            :param nowait: Do not send a reply method
            :param arguments: Arguments for declaration

            """
            # Deprecated
            self.ticket = ticket
            self.queue = queue
            self.consumer_tag = consumer_tag

            # Do not deliver own messages
            self.no_local = no_local

            # No acknowledgement needed
            self.no_ack = no_ack

            # Request exclusive access
            self.exclusive = exclusive

            # Do not send a reply method
            self.nowait = nowait

            # Arguments for declaration
            self.arguments = arguments or {}

    class ConsumeOk(base.Frame):
        """Confirm a new consumer

        The server provides the client with a consumer tag, which is used by
        the client for methods called on the consumer at a later stage.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 21
        index = 0x003C0015
        name = 'Basic.ConsumeOk'

        # Specifies if this is a synchronous AMQP method
        synchronous = False

        # AMQ Method Attributes
        __slots__ = ['consumer_tag']

        # Attribute Typing
        __annotations__ = {'consumer_tag': str}

        # Attribute AMQ Types
        _consumer_tag = 'shortstr'

        def __init__(self, consumer_tag: str = ''):
            """Initialize the Basic.ConsumeOk class

            :param consumer-tag:

            """
            self.consumer_tag = consumer_tag

    class Cancel(base.Frame):
        """End a queue consumer

        This method cancels a consumer. This does not affect already delivered
        messages, but it does mean the server will not send any more messages
        for that consumer. The client may receive an arbitrary number of
        messages in between sending the cancel method and receiving the cancel-
        ok reply.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 30
        index = 0x003C001E
        name = 'Basic.Cancel'

        # Specifies if this is a synchronous AMQP method
        synchronous = True

        # Valid responses to this method
        valid_responses = ['Basic.CancelOk']

        # AMQ Method Attributes
        __slots__ = ['consumer_tag', 'nowait']

        # Attribute Typing
        __annotations__ = {'consumer_tag': str, 'nowait': bool}

        # Attribute AMQ Types
        _consumer_tag = 'shortstr'
        _nowait = 'bit'

        def __init__(self, consumer_tag: str = '', nowait: bool = False):
            """Initialize the Basic.Cancel class

            :param consumer_tag: Consumer tag
            :param nowait: Do not send a reply method

            """
            # Consumer tag
            self.consumer_tag = consumer_tag

            # Do not send a reply method
            self.nowait = nowait

    class CancelOk(base.Frame):
        """Confirm a cancelled consumer

        This method confirms that the cancellation was completed.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 31
        index = 0x003C001F
        name = 'Basic.CancelOk'

        # Specifies if this is a synchronous AMQP method
        synchronous = False

        # AMQ Method Attributes
        __slots__ = ['consumer_tag']

        # Attribute Typing
        __annotations__ = {'consumer_tag': str}

        # Attribute AMQ Types
        _consumer_tag = 'shortstr'

        def __init__(self, consumer_tag: str = ''):
            """Initialize the Basic.CancelOk class

            :param consumer_tag: Consumer tag

            """
            # Consumer tag
            self.consumer_tag = consumer_tag

    class Publish(base.Frame):
        """Publish a message

        This method publishes a message to a specific exchange. The message
        will be routed to queues as defined by the exchange configuration and
        distributed to any active consumers when the transaction, if any, is
        committed.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 40
        index = 0x003C0028
        name = 'Basic.Publish'

        # Specifies if this is a synchronous AMQP method
        synchronous = False

        # AMQ Method Attributes
        __slots__ = [
            'ticket', 'exchange', 'routing_key', 'mandatory', 'immediate'
        ]

        # Attribute Typing
        __annotations__ = {
            'ticket': int,
            'exchange': str,
            'routing_key': str,
            'mandatory': bool,
            'immediate': bool
        }

        # Attribute AMQ Types
        _ticket = 'short'
        _exchange = 'shortstr'
        _routing_key = 'shortstr'
        _mandatory = 'bit'
        _immediate = 'bit'

        def __init__(self,
                     ticket: int = 0,
                     exchange: str = '',
                     routing_key: str = '',
                     mandatory: bool = False,
                     immediate: bool = False):
            """Initialize the Basic.Publish class

            :param ticket: Deprecated
            :param exchange:
            :param routing_key: Message routing key
            :param mandatory: Indicate mandatory routing
            :param immediate: Request immediate delivery

            """
            # Deprecated
            self.ticket = ticket
            self.exchange = exchange

            # Message routing key
            self.routing_key = routing_key

            # Indicate mandatory routing
            self.mandatory = mandatory

            # Request immediate delivery
            self.immediate = immediate

    class Return(base.Frame):
        """Return a failed message

        This method returns an undeliverable message that was published with
        the "immediate" flag set, or an unroutable message published with the
        "mandatory" flag set. The reply code and text provide information about
        the reason that the message was undeliverable.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 50
        index = 0x003C0032
        name = 'Basic.Return'

        # Specifies if this is a synchronous AMQP method
        synchronous = False

        # AMQ Method Attributes
        __slots__ = ['reply_code', 'reply_text', 'exchange', 'routing_key']

        # Attribute Typing
        __annotations__ = {
            'reply_code': int,
            'reply_text': str,
            'exchange': str,
            'routing_key': str
        }

        # Attribute AMQ Types
        _reply_code = 'short'
        _reply_text = 'shortstr'
        _exchange = 'shortstr'
        _routing_key = 'shortstr'

        def __init__(self,
                     reply_code: int = 0,
                     reply_text: str = '',
                     exchange: str = '',
                     routing_key: str = ''):
            """Initialize the Basic.Return class

            :param reply_code: Reply code from server
            :param reply_text: Localised reply text
            :param exchange:
            :param routing_key: Message routing key

            """
            # Reply code from server
            self.reply_code = reply_code

            # Localised reply text
            self.reply_text = reply_text
            self.exchange = exchange

            # Message routing key
            self.routing_key = routing_key

    class Deliver(base.Frame):
        """Notify the client of a consumer message

        This method delivers a message to the client, via a consumer. In the
        asynchronous message delivery model, the client starts a consumer using
        the Consume method, then the server responds with Deliver methods as
        and when messages arrive for that consumer.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 60
        index = 0x003C003C
        name = 'Basic.Deliver'

        # Specifies if this is a synchronous AMQP method
        synchronous = False

        # AMQ Method Attributes
        __slots__ = [
            'consumer_tag', 'delivery_tag', 'redelivered', 'exchange',
            'routing_key'
        ]

        # Attribute Typing
        __annotations__ = {
            'consumer_tag': str,
            'delivery_tag': int,
            'redelivered': bool,
            'exchange': str,
            'routing_key': str
        }

        # Attribute AMQ Types
        _consumer_tag = 'shortstr'
        _delivery_tag = 'longlong'
        _redelivered = 'bit'
        _exchange = 'shortstr'
        _routing_key = 'shortstr'

        def __init__(self,
                     consumer_tag: str = '',
                     delivery_tag: int = None,
                     redelivered: bool = False,
                     exchange: str = '',
                     routing_key: str = ''):
            """Initialize the Basic.Deliver class

            :param consumer_tag: Consumer tag
            :param delivery_tag: Server-assigned delivery tag
            :param redelivered: Message is being redelivered
            :param exchange:
            :param routing_key: Message routing key

            """
            # Consumer tag
            self.consumer_tag = consumer_tag

            # Server-assigned delivery tag
            self.delivery_tag = delivery_tag

            # Message is being redelivered
            self.redelivered = redelivered
            self.exchange = exchange

            # Message routing key
            self.routing_key = routing_key

    class Get(base.Frame):
        """Direct access to a queue

        This method provides a direct access to the messages in a queue using a
        synchronous dialogue that is designed for specific types of application
        where synchronous functionality is more important than performance.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 70
        index = 0x003C0046
        name = 'Basic.Get'

        # Specifies if this is a synchronous AMQP method
        synchronous = True

        # Valid responses to this method
        valid_responses = ['Basic.GetOk', 'Basic.GetEmpty']

        # AMQ Method Attributes
        __slots__ = ['ticket', 'queue', 'no_ack']

        # Attribute Typing
        __annotations__ = {'ticket': int, 'queue': str, 'no_ack': bool}

        # Attribute AMQ Types
        _ticket = 'short'
        _queue = 'shortstr'
        _no_ack = 'bit'

        def __init__(self,
                     ticket: int = 0,
                     queue: str = '',
                     no_ack: bool = False):
            """Initialize the Basic.Get class

            :param ticket: Deprecated
            :param queue:
            :param no_ack: No acknowledgement needed

            """
            # Deprecated
            self.ticket = ticket
            self.queue = queue

            # No acknowledgement needed
            self.no_ack = no_ack

    class GetOk(base.Frame):
        """Provide client with a message

        This method delivers a message to the client following a get method. A
        message delivered by 'get-ok' must be acknowledged unless the no-ack
        option was set in the get method.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 71
        index = 0x003C0047
        name = 'Basic.GetOk'

        # Specifies if this is a synchronous AMQP method
        synchronous = False

        # AMQ Method Attributes
        __slots__ = [
            'delivery_tag', 'redelivered', 'exchange', 'routing_key',
            'message_count'
        ]

        # Attribute Typing
        __annotations__ = {
            'delivery_tag': int,
            'redelivered': bool,
            'exchange': str,
            'routing_key': str,
            'message_count': int
        }

        # Attribute AMQ Types
        _delivery_tag = 'longlong'
        _redelivered = 'bit'
        _exchange = 'shortstr'
        _routing_key = 'shortstr'
        _message_count = 'long'

        def __init__(self,
                     delivery_tag: int = None,
                     redelivered: bool = False,
                     exchange: str = '',
                     routing_key: str = '',
                     message_count: int = 0):
            """Initialize the Basic.GetOk class

            :param delivery_tag: Server-assigned delivery tag
            :param redelivered: Message is being redelivered
            :param exchange:
            :param routing_key: Message routing key
            :param message_count: Number of messages in queue

            """
            # Server-assigned delivery tag
            self.delivery_tag = delivery_tag

            # Message is being redelivered
            self.redelivered = redelivered
            self.exchange = exchange

            # Message routing key
            self.routing_key = routing_key

            # Number of messages in queue
            self.message_count = message_count

    class GetEmpty(base.Frame):
        """Indicate no messages available

        This method tells the client that the queue has no messages available
        for the client.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 72
        index = 0x003C0048
        name = 'Basic.GetEmpty'

        # Specifies if this is a synchronous AMQP method
        synchronous = False

        # AMQ Method Attributes
        __slots__ = ['cluster_id']

        # Attribute Typing
        __annotations__ = {'cluster_id': str}

        # Attribute AMQ Types
        _cluster_id = 'shortstr'

        def __init__(self, cluster_id: str = ''):
            """Initialize the Basic.GetEmpty class

            :param cluster_id: Deprecated

            """
            # Deprecated
            self.cluster_id = cluster_id

    class Ack(base.Frame):
        """Acknowledge one or more messages

        This method acknowledges one or more messages delivered via the Deliver
        or Get-Ok methods. The client can ask to confirm a single message or a
        set of messages up to and including a specific message.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 80
        index = 0x003C0050
        name = 'Basic.Ack'

        # Specifies if this is a synchronous AMQP method
        synchronous = False

        # AMQ Method Attributes
        __slots__ = ['delivery_tag', 'multiple']

        # Attribute Typing
        __annotations__ = {'delivery_tag': int, 'multiple': bool}

        # Attribute AMQ Types
        _delivery_tag = 'longlong'
        _multiple = 'bit'

        def __init__(self, delivery_tag: int = 0, multiple: bool = False):
            """Initialize the Basic.Ack class

            :param delivery_tag: Server-assigned delivery tag
            :param multiple: Acknowledge multiple messages

            """
            # Server-assigned delivery tag
            self.delivery_tag = delivery_tag

            # Acknowledge multiple messages
            self.multiple = multiple

    class Reject(base.Frame):
        """Reject an incoming message

        This method allows a client to reject a message. It can be used to
        interrupt and cancel large incoming messages, or return untreatable
        messages to their original queue.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 90
        index = 0x003C005A
        name = 'Basic.Reject'

        # Specifies if this is a synchronous AMQP method
        synchronous = False

        # AMQ Method Attributes
        __slots__ = ['delivery_tag', 'requeue']

        # Attribute Typing
        __annotations__ = {'delivery_tag': int, 'requeue': bool}

        # Attribute AMQ Types
        _delivery_tag = 'longlong'
        _requeue = 'bit'

        def __init__(self, delivery_tag: int = None, requeue: bool = True):
            """Initialize the Basic.Reject class

            :param delivery_tag: Server-assigned delivery tag
            :param requeue: Requeue the message

            """
            # Server-assigned delivery tag
            self.delivery_tag = delivery_tag

            # Requeue the message
            self.requeue = requeue

    class RecoverAsync(base.Frame):
        """Redeliver unacknowledged messages

        This method asks the server to redeliver all unacknowledged messages on
        a specified channel. Zero or more messages may be redelivered.  This
        method is deprecated in favour of the synchronous Recover/Recover-Ok.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 100
        index = 0x003C0064
        name = 'Basic.RecoverAsync'

        # Specifies if this is a synchronous AMQP method
        synchronous = False

        # AMQ Method Attributes
        __slots__ = ['requeue']

        # Attribute Typing
        __annotations__ = {'requeue': bool}

        # Attribute AMQ Types
        _requeue = 'bit'

        def __init__(self, requeue: bool = False):
            """Initialize the Basic.RecoverAsync class

            :param requeue: Requeue the message

            .. deprecated:: 0-9-1
                This command is deprecated in AMQP 0-9-1

            """
            # Requeue the message
            self.requeue = requeue

            # This command is deprecated in AMQP 0-9-1
            warnings.warn(constants.DEPRECATION_WARNING,
                          category=DeprecationWarning)

    class Recover(base.Frame):
        """Redeliver unacknowledged messages

        This method asks the server to redeliver all unacknowledged messages on
        a specified channel. Zero or more messages may be redelivered.  This
        method replaces the asynchronous Recover.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 110
        index = 0x003C006E
        name = 'Basic.Recover'

        # Specifies if this is a synchronous AMQP method
        synchronous = True

        # Valid responses to this method
        valid_responses = ['Basic.RecoverOk']

        # AMQ Method Attributes
        __slots__ = ['requeue']

        # Attribute Typing
        __annotations__ = {'requeue': bool}

        # Attribute AMQ Types
        _requeue = 'bit'

        def __init__(self, requeue: bool = False):
            """Initialize the Basic.Recover class

            :param requeue: Requeue the message

            """
            # Requeue the message
            self.requeue = requeue

    class RecoverOk(base.Frame):
        """Confirm recovery

        This method acknowledges a Basic.Recover method.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 111
        index = 0x003C006F
        name = 'Basic.RecoverOk'

        # Specifies if this is a synchronous AMQP method
        synchronous = False

    class Nack(base.Frame):
        # AMQP Method Number and Mapping Index
        frame_id = 120
        index = 0x003C0078
        name = 'Basic.Nack'

        # Specifies if this is a synchronous AMQP method
        synchronous = False

        # AMQ Method Attributes
        __slots__ = ['delivery_tag', 'multiple', 'requeue']

        # Attribute Typing
        __annotations__ = {
            'delivery_tag': int,
            'multiple': bool,
            'requeue': bool
        }

        # Attribute AMQ Types
        _delivery_tag = 'longlong'
        _multiple = 'bit'
        _requeue = 'bit'

        def __init__(self,
                     delivery_tag: int = 0,
                     multiple: bool = False,
                     requeue: bool = True):
            """Initialize the Basic.Nack class

            :param delivery_tag: Server-assigned delivery tag
            :param multiple:
            :param requeue:

            """
            # Server-assigned delivery tag
            self.delivery_tag = delivery_tag
            self.multiple = multiple
            self.requeue = requeue

    class Properties(base.BasicProperties):
        """Content Properties"""

        name = 'Basic.Properties'

        __slots__ = [
            'content_type', 'content_encoding', 'headers', 'delivery_mode',
            'priority', 'correlation_id', 'reply_to', 'expiration',
            'message_id', 'timestamp', 'message_type', 'user_id', 'app_id',
            'cluster_id'
        ]

        # Flag Values
        flags = {
            'content_type': 32768,
            'content_encoding': 16384,
            'headers': 8192,
            'delivery_mode': 4096,
            'priority': 2048,
            'correlation_id': 1024,
            'reply_to': 512,
            'expiration': 256,
            'message_id': 128,
            'timestamp': 64,
            'message_type': 32,
            'user_id': 16,
            'app_id': 8,
            'cluster_id': 4
        }

        # Class Attribute Types
        _content_type = 'shortstr'
        _content_encoding = 'shortstr'
        _headers = 'table'
        _delivery_mode = 'octet'
        _priority = 'octet'
        _correlation_id = 'shortstr'
        _reply_to = 'shortstr'
        _expiration = 'shortstr'
        _message_id = 'shortstr'
        _timestamp = 'timestamp'
        _message_type = 'shortstr'
        _user_id = 'shortstr'
        _app_id = 'shortstr'
        _cluster_id = 'shortstr'

        frame_id = 60
        index = 0x003C

        def __init__(self,
                     content_type: str = '',
                     content_encoding: str = '',
                     headers: typing.Optional[common.FieldTable] = None,
                     delivery_mode: int = None,
                     priority: int = None,
                     correlation_id: str = '',
                     reply_to: str = '',
                     expiration: str = '',
                     message_id: str = '',
                     timestamp: common.Timestamp = None,
                     message_type: str = '',
                     user_id: str = '',
                     app_id: str = '',
                     cluster_id: str = ''):
            """Initialize the Basic.Properties class

            Note that the AMQP property type is named message_type as to
            not conflict with the Python type keyword

            :param content_type: MIME content type
            :param content_encoding: MIME content encoding
            :param headers: Message header field table
            :param delivery_mode: Non-persistent (1) or persistent (2)
            :param priority: Message priority, 0 to 9
            :param correlation_id: Application correlation identifier
            :param reply_to: Address to reply to
            :param expiration: Message expiration specification
            :param message_id: Application message identifier
            :param timestamp: Message timestamp
            :param message_type: Message type name
            :param user_id: Creating user id
            :param app_id: Creating application id
            :param cluster_id: Deprecated

            """
            # MIME content type
            self.content_type = content_type

            # MIME content encoding
            self.content_encoding = content_encoding

            # Message header field table
            self.headers = headers

            # Non-persistent (1) or persistent (2)
            self.delivery_mode = delivery_mode

            # Message priority, 0 to 9
            self.priority = priority

            # Application correlation identifier
            self.correlation_id = correlation_id

            # Address to reply to
            self.reply_to = reply_to

            # Message expiration specification
            self.expiration = expiration

            # Application message identifier
            self.message_id = message_id

            # Message timestamp
            self.timestamp = timestamp

            # Message type name
            self.message_type = message_type

            # Creating user id
            self.user_id = user_id

            # Creating application id
            self.app_id = app_id

            # Deprecated
            self.cluster_id = cluster_id


class Tx:
    """Work with transactions

    The Tx class allows publish and ack operations to be batched into atomic
    units of work.  The intention is that all publish and ack requests issued
    within a transaction will complete successfully or none of them will.
    Servers SHOULD implement atomic transactions at least where all publish or
    ack requests affect a single queue.  Transactions that cover multiple
    queues may be non-atomic, given that queues can be created and destroyed
    asynchronously, and such events do not form part of any transaction.
    Further, the behaviour of transactions with respect to the immediate and
    mandatory flags on Basic.Publish methods is not defined.

    """
    __slots__ = []

    # AMQP Class Number and Mapping Index
    frame_id = 90
    index = 0x005A0000

    class Select(base.Frame):
        """Select standard transaction mode

        This method sets the channel to use standard transactions. The client
        must use this method at least once on a channel before using the Commit
        or Rollback methods.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 10
        index = 0x005A000A
        name = 'Tx.Select'

        # Specifies if this is a synchronous AMQP method
        synchronous = True

        # Valid responses to this method
        valid_responses = ['Tx.SelectOk']

    class SelectOk(base.Frame):
        """Confirm transaction mode

        This method confirms to the client that the channel was successfully
        set to use standard transactions.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 11
        index = 0x005A000B
        name = 'Tx.SelectOk'

        # Specifies if this is a synchronous AMQP method
        synchronous = False

    class Commit(base.Frame):
        """Commit the current transaction

        This method commits all message publications and acknowledgments
        performed in the current transaction.  A new transaction starts
        immediately after a commit.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 20
        index = 0x005A0014
        name = 'Tx.Commit'

        # Specifies if this is a synchronous AMQP method
        synchronous = True

        # Valid responses to this method
        valid_responses = ['Tx.CommitOk']

    class CommitOk(base.Frame):
        """Confirm a successful commit

        This method confirms to the client that the commit succeeded. Note that
        if a commit fails, the server raises a channel exception.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 21
        index = 0x005A0015
        name = 'Tx.CommitOk'

        # Specifies if this is a synchronous AMQP method
        synchronous = False

    class Rollback(base.Frame):
        """Abandon the current transaction

        This method abandons all message publications and acknowledgments
        performed in the current transaction. A new transaction starts
        immediately after a rollback. Note that unacked messages will not be
        automatically redelivered by rollback; if that is required an explicit
        recover call should be issued.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 30
        index = 0x005A001E
        name = 'Tx.Rollback'

        # Specifies if this is a synchronous AMQP method
        synchronous = True

        # Valid responses to this method
        valid_responses = ['Tx.RollbackOk']

    class RollbackOk(base.Frame):
        """Confirm successful rollback

        This method confirms to the client that the rollback succeeded. Note
        that if an rollback fails, the server raises a channel exception.

        """
        # AMQP Method Number and Mapping Index
        frame_id = 31
        index = 0x005A001F
        name = 'Tx.RollbackOk'

        # Specifies if this is a synchronous AMQP method
        synchronous = False


class Confirm:
    __slots__ = []

    # AMQP Class Number and Mapping Index
    frame_id = 85
    index = 0x00550000

    class Select(base.Frame):
        # AMQP Method Number and Mapping Index
        frame_id = 10
        index = 0x0055000A
        name = 'Confirm.Select'

        # Specifies if this is a synchronous AMQP method
        synchronous = True

        # Valid responses to this method
        valid_responses = ['Confirm.SelectOk']

        # AMQ Method Attributes
        __slots__ = ['nowait']

        # Attribute Typing
        __annotations__ = {'nowait': bool}

        # Attribute AMQ Types
        _nowait = 'bit'

        def __init__(self, nowait: bool = False):
            """Initialize the Confirm.Select class

            :param nowait: Do not send a reply method

            """
            # Do not send a reply method
            self.nowait = nowait

    class SelectOk(base.Frame):
        # AMQP Method Number and Mapping Index
        frame_id = 11
        index = 0x0055000B
        name = 'Confirm.SelectOk'

        # Specifies if this is a synchronous AMQP method
        synchronous = False


# AMQP Class.Method Index Mapping
INDEX_MAPPING = {
    0x000A000A: Connection.Start,
    0x000A000B: Connection.StartOk,
    0x000A0014: Connection.Secure,
    0x000A0015: Connection.SecureOk,
    0x000A001E: Connection.Tune,
    0x000A001F: Connection.TuneOk,
    0x000A0028: Connection.Open,
    0x000A0029: Connection.OpenOk,
    0x000A0032: Connection.Close,
    0x000A0033: Connection.CloseOk,
    0x000A003C: Connection.Blocked,
    0x000A003D: Connection.Unblocked,
    0x000A0046: Connection.UpdateSecret,
    0x000A0047: Connection.UpdateSecretOk,
    0x0014000A: Channel.Open,
    0x0014000B: Channel.OpenOk,
    0x00140014: Channel.Flow,
    0x00140015: Channel.FlowOk,
    0x00140028: Channel.Close,
    0x00140029: Channel.CloseOk,
    0x0028000A: Exchange.Declare,
    0x0028000B: Exchange.DeclareOk,
    0x00280014: Exchange.Delete,
    0x00280015: Exchange.DeleteOk,
    0x0028001E: Exchange.Bind,
    0x0028001F: Exchange.BindOk,
    0x00280028: Exchange.Unbind,
    0x00280033: Exchange.UnbindOk,
    0x0032000A: Queue.Declare,
    0x0032000B: Queue.DeclareOk,
    0x00320014: Queue.Bind,
    0x00320015: Queue.BindOk,
    0x0032001E: Queue.Purge,
    0x0032001F: Queue.PurgeOk,
    0x00320028: Queue.Delete,
    0x00320029: Queue.DeleteOk,
    0x00320032: Queue.Unbind,
    0x00320033: Queue.UnbindOk,
    0x003C000A: Basic.Qos,
    0x003C000B: Basic.QosOk,
    0x003C0014: Basic.Consume,
    0x003C0015: Basic.ConsumeOk,
    0x003C001E: Basic.Cancel,
    0x003C001F: Basic.CancelOk,
    0x003C0028: Basic.Publish,
    0x003C0032: Basic.Return,
    0x003C003C: Basic.Deliver,
    0x003C0046: Basic.Get,
    0x003C0047: Basic.GetOk,
    0x003C0048: Basic.GetEmpty,
    0x003C0050: Basic.Ack,
    0x003C005A: Basic.Reject,
    0x003C0064: Basic.RecoverAsync,
    0x003C006E: Basic.Recover,
    0x003C006F: Basic.RecoverOk,
    0x003C0078: Basic.Nack,
    0x005A000A: Tx.Select,
    0x005A000B: Tx.SelectOk,
    0x005A0014: Tx.Commit,
    0x005A0015: Tx.CommitOk,
    0x005A001E: Tx.Rollback,
    0x005A001F: Tx.RollbackOk,
    0x0055000A: Confirm.Select,
    0x0055000B: Confirm.SelectOk
}
