import os
import sys
import dbus
import time

bus = dbus.SystemBus()

tech_type = 'wifi'

path = '/net/connman/technology/' + tech_type
tech = dbus.Interface(bus.get_object('net.connman', path), 'net.connman.Technology')

if tech == None:
	print 'No %s technology available' % tech_type
        sys.exit()

properties = tech.GetProperties()

if not properties['Powered']:
        print 'Technology not powered. Powering up'
        tech.SetProperty('Powered', dbus.Boolean(1))

if properties['Tethering']:
    print 'Interface already tethering. Resetting'
    tech.SetProperty('Tethering', dbus.Boolean(0))
    # FIXME: If we don't wait connman complains later.
    # We should be listening for events instead of waiting
    # a fixed amount of time
    time.sleep(1)

ssid = os.environ.get('SSID', 'ResinAP')
print 'Setting SSID to: %s' % (ssid)
tech.SetProperty('TetheringIdentifier', ssid)

psk = os.environ.get('PASSPHRASE', '12345678')
print 'Setting Passphrase to: %s' % (psk)
tech.SetProperty('TetheringPassphrase', psk)

print 'Enabling tethering on %s' % tech_type
tech.SetProperty('Tethering', dbus.Boolean(1))
