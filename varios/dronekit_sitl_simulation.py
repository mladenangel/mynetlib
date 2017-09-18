#!/usr/bin/env python
# delwin

import dronekit_sitl
from dronekit import connect, VehicleMode

# Connect to the default sitl, if not one running.
sitl = dronekit_sitl.start_default()
connection_string = sitl.connection_string()

# Connect to the Vehicle.
print("Connected: %s" % (connection_string))
vehicle = connect(connection_string, wait_ready=True)

print ("GPS: %s" % vehicle.gps_0)
print ("Battery: %s" % vehicle.battery)
print ("Last Heartbeat: %s" % vehicle.last_heartbeat)
print ("Is Armable?: %s" % vehicle.is_armable)
print ("System status: %s" % vehicle.system_status.state)
print ("Mode: %s" % vehicle.mode.name)

# Close vehicle object before exiting script
vehicle.close()

print("Completed")
