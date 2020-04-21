from abc import ABC
import json


def save_object(object, dest_file):
    with open(dest_file, 'w') as out_file:
        json.dump(dict(object), out_file)


def load_object(object, src_file):
    filehandler = open(src_file, 'r')
    return pickle.load(filehandler)


class PlotPoint(ABC):
    def __init__(self):
        pass


class Player(ABC):
    def __init__(self):
        self.name = None
        self.savepoints = None

    """*****************************************
    ***          Properties Section          ***
    *****************************************"""

    """This is the Name property"""
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

    """This is the Savepoints property"""
    @property
    def savepoints(self):
        return self._savepoints

    @savepoints.setter
    def savepoints(self, val):
        self._name = val
    """*****************************************
    ***        END: Properties Section       ***
    *****************************************"""


class Storyline(ABC):
    def __init__(self):
        self.title = None
        self.plotpoints = set()
        self.player = Player()

    """*****************************************
    ***          Properties Section          ***
    *****************************************"""

    """This is the Title property"""
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, val):
        self._title = val

    """*****************************************
    ***        END: Properties Section       ***
    *****************************************"""  #  The gameboard


class SavePoint(ABC):
    def __init__(self):
        pass


class HackChallenge(ABC):
    """*****************************************
    *** New Class: HackChallenge             ***
    *****************************************"""
    """ Hack Challenges are the Levels players face. They contain Systems2Pwn.
    They consist of:
    - A name
    - A website
    - A List of Systems2Pwn
    """
    def __init__(self):
        self.name = None
        self.website = None
        self.systems = []

    def __str__(self):
        return "The challenge {self.name} at {self.website}".format(self=self)

    """*****************************************
    ***          Properties Section          ***
    *****************************************"""

    """This is the Name property"""
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val


    """ This is the Website property"""
    @property
    def website(self):
        return self._website

    @website.setter
    def website(self, val):
        self._website = val

    """ This is the List of systems in the challenge"""
    @property
    def systems(self):
        return self._systems

    @systems.setter
    def systems(self, val):
        self._systems = val


    """*****************************************
    ***        END: Properties Section       ***
    *****************************************"""


class Finding(ABC):
    """*****************************************
    *** New Class: Finding             ***
    *****************************************"""
    """ Players synthesize findings by combining an Item of Interest (iointerest) and
    a note.
    """
    def __init__(self):
        self.iointerest = None
        self.note = None
    """*****************************************
    ***          Properties Section          ***
    *****************************************"""
    """ This is the Item of Interest (iointerest) property"""
    @property
    def note(self):
        return self._note

    @note.setter
    def note(self, val):
        self._note = val

    """ This is the Item of Interest (iointerest) property"""
    @property
    def iointerest(self):
        return self._iointerest

    @iointerest.setter
    def iointerest(self, val):
        self._iointerest = val
    """*****************************************
    ***        END: Properties Section       ***
    *****************************************"""


class System2Pwn(ABC):
    """*****************************************
    *** New Class: System2Pwn                 ***
    *****************************************"""
    """ Systems are objects that can be targeted by players.
    They consist of:
    - An operating system (os_system)

    """
    def __init__(self):
        self.name = None
        self.op_system = None
        self.open_ports = []

    """*****************************************
    ***          Properties Section          ***
    *****************************************"""

    """This is the Name property"""
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val


    """ This is the Operating System property"""
    @property
    def op_system(self):
        return self._op_system

    @op_system.setter
    def op_system(self, val):
        self._op_system = val

    """ This is the Open Ports property"""
    @property
    def open_ports(self):
        return self._open_ports

    @open_ports.setter
    def open_ports(self, val):
        if isinstance(val, list):
            self._open_ports = val
        else:
            raise TypeError

    """*****************************************
    ***        END: Properties Section       ***
    *****************************************"""


class OpSystem(ABC):
    """*****************************************
    *** New Class: OpSystem                 ***
    *****************************************"""
    """ Operating systems are a component of Systems.
    They consist of:
    - Name
    - Version
    - TTL
    - Packet Size
    - DF bit
    - ...etc
    """
    def __init__(self):
        self.name = None
        self.version = None
        self.ttl = None
        self.packet_size = None
        self.df_bit = None
        self.etc = dict()

    def __repr__(self):
        return "<OpSystem({self.name} v. {self.version})>".format(self=self)

    def __str__(self):
        return "{self.name} version {self.version}".format(self=self)

    """*****************************************
    ***          Properties Section          ***
    *****************************************"""

    """This is the Name property"""
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

    """This is the Version property"""
    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, val):
        self._version = val

    """This is the TTL property"""
    @property
    def ttl(self):
        return self._ttl

    @ttl.setter
    def ttl(self, val):
        if val:
            self._ttl = int(val)

    """This is the PacketSize property"""
    @property
    def packet_size(self):
        return self._packet_size

    @packet_size.setter
    def packet_size(self, val):
        if isinstance(val, int) or val is None:
            self._packet_size = val
        else:
            raise TypeError

    """This is the DF Bit property. Can be set to '0' or '1'"""
    @property
    def df_bit(self):
        return self._df_bit

    @df_bit.setter
    def df_bit(self, val):
        if isinstance(val, int) or val is None:
            self._df_bit = val

    """This is the catchall, etc. It should be a dict of items"""
    @property
    def etc(self):
        return self._etc

    @etc.setter
    def etc(self, val):
        if isinstance(val, dict):
            self._etc = val
        else:
            raise TypeError

    """*****************************************
    ***        END: Properties Section       ***
    *****************************************"""


class Port(ABC):
    """*****************************************
    *** New Class: Port                 ***
    *****************************************"""
    """ Open ports are a component of Systems.
    They consist of:
    - Port number
    - Protocol
    - Services
    - State
    """
    def __init__(self):
        self.port = None
        self.protocol = None
        self.services = []

    def __str__(self):
        if isinstance(self.port, str):
            str_port = str(self.port)
        if self.port is None:
            str_port = ""
        return "" + str(len(self.services)) + " services running on " + self.protocol + " port " + str_port

    def __dict__(self):
        return {'port':self.port,'protocol':self.protocol,'services':self.services}

    def __iter__(self):
        for key in self.__dict__():
            yield (key, '{}'.format(self.__dict__()[key]))
        return

    def save(self):
        """ Save a port a a pickled object"""
        print("\nSaving port...")
        if self.port:
#            try:
            save_object(self, "saves/ports/" + str(self))
            print("\n Port ", self.port, "was saved.")
#            except (TypeError, NameError) as e:
#                print("Port ", self.port, "could not be saved")
        else:
            print("\nThere was no port number to save\n")


    """*****************************************
    ***          Properties Section          ***
    *****************************************"""

    """This is the Port property"""
    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, val):
        if isinstance (val, int) or val is None:
            self._port = val
        else:
            raise TypeError

    """This is the Protocol property"""
    @property
    def protocol(self):
        return self._protocol

    @protocol.setter
    def protocol(self, val):
        if isinstance(val, str) or val is None:
            self._protocol = val
        else:
            raise TypeError

    """This is the Services property"""
    @property
    def services(self):
        return self._services

    @services.setter
    def services(self, val):
        if isinstance(val, list):
            self._services = val
        else:
            raise TypeError

    """This is the State property"""
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, val):
        if isinstance(val, str):
            self._state = val
        else:
            raise TypeError


class SystemService(ABC):
    """*****************************************
    *** New Class: SystemService                 ***
    *****************************************"""
    def __init__(self):
        self.name = None
        self.version = None

    def __dict__(self):
        return {'name':self.name,'version':self.version}

    def save(self):
        """ Save a SystemService a a JSON object"""
        print("\nSaving SystemService...")
        if self.name:
            try:
                save_object(self, "saves/services/" + str(self.name))
                print("\n System Service ", self.name, "was saved.")
            except (TypeError, NameError) as e:
                print("System Service ", self.name, "could not be saved")
        else:
            print("\nThere was no System Service name to save\n")

    """*****************************************
    ***          Properties Section          ***
    *****************************************"""
    """This is the Name property"""
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

    """This is the Version property"""
    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, val):
        self._version = val

    """*****************************************
    ***        END: Properties Section       ***
    *****************************************"""