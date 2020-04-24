from os import listdir

import pytest

from playtopwn.src.playtopwn.pieces import System2Pwn, OpSystem, HackChallenge, Port, SystemService, Finding


def test_HackChallenge_setters():
    test_case = HackChallenge()
    test_case.name = 'Wicked hard box'
    test_case.website = 'www.toorealy.com'
    test_system1 = System2Pwn()
    test_system2 = System2Pwn()
    test_case.systems = [test_system1, test_system2]
    assert test_case.name == 'Wicked hard box'
    assert test_case.website == 'www.toorealy.com'
    assert test_case.systems == [dict(test_system1), dict(test_system2)]

def test_Finding_setters():
    test_case = Finding()
    test_case.note = "This is a note."
    test_port = Port()
    test_case.iointerest = test_port
    assert test_case.note == "This is a note."
    assert test_case.iointerest == test_port

def test_System2Pwn_setters():
    test_case = System2Pwn()
    test_os = OpSystem()
    test_os.name = "Winders"
    test_os.version = "XXL"
    test_case = System2Pwn()
    test_case.op_system = test_os
    assert str(test_case.op_system) == "Winders version XXL"
    test_case.name = 'Larry'
    assert test_case.name == 'Larry'

def test_OpSystem_setters():
    test_case = OpSystem()
    test_case.name = 'Larry'
    assert test_case.name == 'Larry'
    test_case.version = 'Jerry'
    assert test_case.version == 'Jerry'
    test_case.ttl = 128
    assert test_case.ttl == 128
    test_case.packet_size = 1000
    assert test_case.packet_size == 1000
    test_case.df_bit = 1
    assert test_case.df_bit == 1
    #test_case.etc = {'this':'interesting','that':'boring'}
    #assert test_case.etc == {'this':'interesting','that':'boring'}

def test_Port_setters():
    test_case = Port()
    test_case.port = 7357
    test_case.protocol = 'TCP'
    test_case.state = "OPEN"
    assert test_case.port == 7357
    assert test_case.protocol == 'TCP'
    assert test_case.state == "OPEN"

def test_SystemService_setters():
    test_case = SystemService()
    test_case.name = "SSH"
    test_case.version = "2.0"
    assert test_case.name == "SSH"
    assert test_case.version == "2.0"

def test_Port_saveload():
    test_case = Port()
    test_case.port = 999999
    test_case.save()
    saved_ports = [s for s in listdir("src/saves/ports")]
    assert str(test_case.port) in saved_ports
    assert test_case.show_saves() == saved_ports

    test_case.port = 741
    test_case.load(999999)
    assert test_case.port == 999999

def test_SystemService_saveload():
    test_case = SystemService()
    test_case.name = "test"
    test_case.version = "1"
    test_case.save()
    saved_services = [s for s in listdir("src/saves/services")]
    assert str(test_case.name) in saved_services
    assert test_case.show_saves() == saved_services

    test_case.version = "2"
    assert test_case.version == "2"
    test_case.load("test")
    assert test_case.version == "1"

def test_OpSystem_saveload():
    test_case = OpSystem()
    test_case.name = "Winders"
    test_case.version = "XXL"
    test_case.save()
    saved_os = [s for s in listdir("src/saves/os")]
    assert str(test_case).lower() in saved_os
    assert test_case.show_saves() == saved_os

    test_case.version = "old"
    assert test_case.version == "old"
    test_case.load("winders version xxl")
    assert test_case.version == "XXL"

def test_System2Pwn_saveload():
    test_case = System2Pwn()
    test_case.name = 'Test'
    test_port1 = Port()
    test_port1.port = 123
    test_case.add_port(test_port1)
    test_port2 = Port()
    test_port2.port = 456
    test_case.add_port(test_port2)
    test_case.op_system.name = "Winders"
    test_case.op_system.version = "XXL"
    test_case.op_system.ttl = 999
    test_case.save()
    saved_systems = [s for s in listdir("src/saves/systems")]
    assert str(test_case).lower() in saved_systems
    assert test_case.show_saves() == saved_systems

    test_case.name = 'Computer'
    test_case.op_system.name = "Lindex"
    test_case.op_system.version = "Newer"
    test_case.op_system.ttl = 111
    test_case.remove_port(test_port1)
    test_case.remove_port(test_port2)
    assert test_case.name != 'Test'
    assert test_case.op_system.name != "winders"
    assert test_case.op_system.version != "xxl"
    assert test_case.op_system.ttl != 999
    assert test_case.open_ports != [dict(test_port1), dict(test_port2)]
    test_case.load('Test')
    assert test_case.name == 'Test'
    assert test_case.op_system.name == "Winders"
    assert test_case.op_system.version == "XXL"
    assert test_case.op_system.ttl == 999
    assert test_case.open_ports == [dict(test_port1), dict(test_port2)]

def test_HackChallenge_saveload():
    test_case = HackChallenge()
    test_case.name = 'Test'
    test_system1 = System2Pwn()
    test_system1.name = 'Something'
    test_system2 = System2Pwn()
    test_system2.name = 'Else'
    test_case.add_system(test_system1)
    test_case.add_system(test_system2)
    test_case.website = 'www.pickle.com'
    test_case.save()
    test_case.name = 'Other'
    test_case.website = 'www.cucumber.io'
    test_case.remove_system(test_system2)
    assert dict(test_system1) in test_case.systems
    #assert dict(test_system2) not in test_case.systems
    test_case.load('Test')
    assert test_case.name == "Test"
    assert test_case.website == "www.pickle.com"
    assert dict(test_system2) in test_case.systems
