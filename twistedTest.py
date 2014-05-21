__author__ = 'kurtisjungersen'

from twisted.internet import reactor
from twisted.internet.protocol import Factory, Protocol
from txsockjs.factory import SockJSFactory


class HelloProtocol(Protocol):


    def connectionMade(self):
        self.transport.write('Hellllllooooooooo')

    def dataReceived(self, data):
        print data


reactor.listenTCP(8080, SockJSFactory(Factory.forProtocol(HelloProtocol)))
reactor.run()