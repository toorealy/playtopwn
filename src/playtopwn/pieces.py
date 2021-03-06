from abc import ABC
import ast
import json
from os import listdir

#from playtopwn.saveload import save_object, show_saves, load_object
#from playtopwn.saveload import *

def save_object(object, dest_file):
    with open(dest_file.lower(), 'w') as out_file:
        json.dump(dict(object), out_file)

def show_saves(folder: str) -> list:
    return [s for s in listdir("src/saves/" + folder)]


def load_object(src_file):
    filehandler = open(src_file.lower(), 'r')
    return json.load(filehandler)



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

    def __repr__(self):
        return "HackChallenge<{},{},{}".format(self.name, self.website, str(self.systems))

    def __dict__(self):
        return {'name':self.name,'website':self.website,'systems':str(self.systems)}

    def __iter__(self):
        for key in self.__dict__():
            yield (key, '{}'.format(self.__dict__()[key]))

    def save(self):
        """ Save a HackChallenge as JSON"""
        print("\nSaving Challenge...")
        if self.name:
            try:
                save_object(self, "src/saves/challenges/" + str(self.name))
                print("\n Challenge ", self.name, "was saved.")
            except (TypeError, NameError) as e:
                print("Challenge ", self.name, "could not be saved")
        else:
            print("\nThere was no challenge name to save\n")

    def show_saves(self, *, silent=False) -> list:
        if not silent:
            print("\nThese saved challenges are available:")
        saves = show_saves('challenges')
        for save in saves:
            if not silent:
                print("- ",save)
        return saves

    def save_as(self, name):
        target = HackChallenge()
        target.name = name
        target.website = self.website
        target.systems = self.systems
        target.save()
        self.load(target.name)

    def reset_challenge(self, name):
        if len(name) > 0:
            new_challenge = HackChallenge()
            self.name = name
            self.website = new_challenge.website
            self.systems = new_challenge.systems

    def load(self, challenge_name):
        """Load from JSON and cast back to proper data type"""
        loaded_obj = load_object("src/saves/challenges/" + str(challenge_name))
        self.name = loaded_obj['name']  #  key value for class
        self.website = loaded_obj['website']
        self.systems = ast.literal_eval(loaded_obj['systems'])
        return self

    def add_system(self, system_name):
        system_object = System2Pwn()
        system_object.name = str(system_name)
        if dict(system_object) in self.systems:
            print("You have attempted to add a duplicate system")
        else:
            self.systems.append(dict(system_object))
            system_object.save(self.name + "_")
            print("System added")
            self.show_systems()

    def remove_system(self, system_name):
        system_object = System2Pwn()
        try:
            system_object.load(self.name + "_" + str(system_name))
        except FileNotFoundError:
            pass
        if dict(system_object) in self.systems:
            self.systems.remove(dict(system_object))

    def show_systems(self, *,silent=False):
        return_list = []
        for pwn in self.systems:
            if not silent:
                print(" - ", pwn['name'])
            return_list.append(pwn['name'])
        return return_list

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
        if isinstance(val, list):
            dict_systems = []
            for v in val:
                dict_systems.append(dict(v))
            self._systems = dict_systems
        else:
            raise TypeError


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
        self.name = None  #  key value for class
        self.op_system = OpSystem()
        self.open_ports = []

    def __repr__(self):
        return "System2Pwn<{},{},{}>".format(self.name, str(self.op_system), str(open_ports))

    def __str__(self):
        return str(self.name)

    def __dict__(self):
        return {'name':self.name,'op_system':dict(self.op_system),'open_ports':str(self.open_ports)}

    def __iter__(self):
        for key in self.__dict__():
            yield (key, '{}'.format(self.__dict__()[key]))

    def save(self, prefix=""):
        """ Save a System2Pwn as JSON"""
        print("\nSaving System...")
        if self.name:
            try:
                save_object(self, "src/saves/systems/" + prefix + str(self.name))
                print("\n System ", self.name, "was saved.")
            except (TypeError, NameError) as e:
                print("System ", self.name, "could not be saved")
        else:
            print("\nThere was no system name to save\n")

    def show_saves(self) -> list:
        print("\nThese ports are available:")
        saves = show_saves('systems')
        for save in saves:
            print("- ",save)
        return saves

    def load(self, system_name):
        """Load from JSON and cast back to proper data type"""
        loaded_obj = load_object("src/saves/systems/" + str(system_name))
        self.name = loaded_obj['name']  #  key value for class
        os_component = ast.literal_eval(loaded_obj['op_system'])
        if os_component['name'] != "None":
            self.op_system.name = os_component['name']
        else:
            None
        if os_component['version'] != "None":
            self.op_system.version = os_component['version']
        else:
            None
        if os_component['ttl'] != "None":
            self.op_system.ttl = int(os_component['ttl'])
        else:
            None
        if os_component['packet_size'] != "None":
            self.op_system.packet_size = int(os_component['packet_size'])
        else:
            None
        if os_component['df_bit'] != "None":
            self.op_system.df_bit = int(os_component['df_bit'])
        else:
            None
        self.open_ports = ast.literal_eval(loaded_obj['open_ports'])


    def add_port(self, port_object):
        if dict(port_object) in self.open_ports:
            pass
        else:
            self.open_ports.append(dict(port_object))

    def remove_port(self, port_object):
        if dict(port_object) in self.open_ports:
            print("Open: ", self.open_ports)
            print("Remove: ", dict(port_object))
            self.open_ports.remove(dict(port_object))


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
            dict_ports = []
            for v in val:
                dict_ports.append(dict(v))
            self._open_ports = dict_ports
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
        self.name = None  # key value for class
        self.version = None
        self.ttl = None
        self.packet_size = None
        self.df_bit = None
        #self.etc = dict()  #  TODO: Implement later

    def __repr__(self):
        return "<OpSystem({self.name},{self.version})>".format(self=self)

    def __str__(self):
        return "{self.name} version {self.version}".format(self=self)

    def __dict__(self):
        return {'name':str(self.name),'version':str(self.version),'ttl':str(self.ttl),'packet_size':str(self.packet_size),'df_bit':str(self.df_bit)}

    def __iter__(self):
        for key in self.__dict__():
            yield (key, '{}'.format(self.__dict__()[key]))

    def save(self):
        """ Save an operating system as JSON"""
        print("\nSaving OS...")
        if self.name:
            try:
                save_object(self, "src/saves/os/" + str(self))
                print("\n OS ", str(self), "was saved.")
            except (TypeError, NameError) as e:
                print("OS ", str(self), "could not be saved")
        else:
            print("\nThere was no OS name to save\n")

    def show_saves(self) -> list:
        print("\nThese OSes are available:")
        saves = show_saves('os')
        for save in saves:
            print("- ",save)
        return saves

    def load(self, os_string):
        """Load from JSON and cast back to proper data type"""
        loaded_obj = load_object("src/saves/os/" + str(os_string))
        self.name = loaded_obj['name']
        self.version = loaded_obj['version']
        if loaded_obj['ttl'] != "None":
            self.ttl = int(loaded_obj['ttl'])
        else:
            self.ttl = None
        if loaded_obj['packet_size'] != "None":
            self.packet_size = int(loaded_obj['packet_size'])
        else:
            self.packet_size = None
        if loaded_obj['df_bit'] != "None":
            self.df_bit = int(loaded_obj['df_bit'])
        else:
            self.df_bit = None

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
        elif val is None:
            self._ttl = None

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
    """
    @property
    def etc(self):
        return self._etc

    @etc.setter
    def etc(self, val):
        if isinstance(val, dict):
            self._etc = val
        else:
            raise TypeError
    """
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
        self.state = None

    def __repr__(self):
        return "Port<" + str(self.port) + ">"

    def __str__(self):
        if self.port and not isinstance(self.port, str):
            str_port = str(self.port)
        elif self.port is None:
            str_port = ""
        if self.protocol and not isinstance(self.protocol, str):
            str_protocol = str(self.protocol)
        elif self.protocol is None:
            str_protocol = ""
        # TODO: probably could get rid of everything above this return line
        return "" + str_protocol + " port " + str_port

    def __dict__(self):
        return {'port':self.port, 'protocol':self.protocol, 'state':self.state}

    def __iter__(self):
        for key in self.__dict__():
            yield (key, '{}'.format(self.__dict__()[key]))

    def save(self):
        print("\nSaving port...")
        if self.port:
            try:
                save_object(self, "src/saves/ports/" + str(self.port))
                print("\n Port ", self.port, "was saved.")
            except (TypeError, NameError) as e:
                print("Port ", self.port, "could not be saved")
        else:
            print("\nThere was no port number to save\n")

    def show_saves(self) -> list:
        print("\nThese ports are available:")
        saves = show_saves('ports')
        for save in saves:
            print("- ",save)
        return saves

    def load(self, port_number):
        loaded_obj = load_object("src/saves/ports/" + str(port_number))
        self.port = int(loaded_obj['port'])
        self.protocol = loaded_obj['protocol']
        self.state = loaded_obj['state']

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

    """This is the State property"""
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, val):
        if isinstance(val, str) or val is None:
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

    def __repr__(self):
        return "SystemService<" + str(self.name) + "," + str(self.version) + ">"

    def __str__(self):
        return "" + str(self.name) + " version " + str(self.version)

    def __dict__(self):
        return {'name':self.name, 'version':self.version}

    def __iter__(self):
        for key in self.__dict__():
            yield (key, '{}'.format(self.__dict__()[key]))

    def save(self):
        """ Save a system service as JSON"""
        print("\nSaving service...")
        if self.name:
            try:
                save_object(self, "src/saves/services/" + str(self.name))
                print("\n", self.name, "was saved.")
            except (TypeError, NameError) as e:
                print(self.name, "could not be saved")
        else:
            print("\nThere was no service name to save\n")

    def show_saves(self) -> list:
        print("\nThese services are available:")
        saves = show_saves('services')
        for save in saves:
            print("- ",save)
        return saves

    def load(self, service_name):
        """Load from JSON and cast back to proper data type"""
        loaded_obj = load_object("src/saves/services/" + str(service_name))
        self.name = loaded_obj['name']
        self.version = loaded_obj['version']

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
