import pytest

from playtopwn.playtopwn.pieces import System2Pwn, OpSystem, HackChallenge, Port, SystemService


def test_HackChallenge_setters():
    test_case = HackChallenge()
    test_case.name = 'Wicked hard box'
    test_case.website = 'www.toorealy.com'
    test_system1 = System2Pwn()
    test_system2 = System2Pwn()
    test_case.systems = [test_system1, test_system2]
    assert test_case.name == 'Wicked hard box'
    assert test_case.website == 'www.toorealy.com'
    assert test_case.systems == [test_system1, test_system2]


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
    test_case.etc = {'this':'interesting','that':'boring'}
    assert test_case.etc == {'this':'interesting','that':'boring'}

def test_Port_setters():
    test_case = Port()
    test_case.port = 7357
    test_case.protocol = 'TCP'
    test_case.services = []
    test_case.state = "OPEN"
    test_service = SystemService()
    test_case.services = [test_service]
    assert test_case.port == 7357
    assert test_case.protocol == 'TCP'
    assert test_case.services == [test_service]
    assert test_case.state == "OPEN"

def test_SystemService_setters():
    test_case = SystemService()
    test_case.name = "SSH"
    test_case.version = "2.0"
    assert test_case.name == "SSH"
    assert test_case.version == "2.0"
