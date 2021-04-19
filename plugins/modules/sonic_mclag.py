#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for sonic_mclag
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = """
---
module: sonic_mclag
version_added: 1.0.0
notes:
- Tested against Enterprise SONiC Distribution by Dell Technologies.
- Supports C(check_mode).
short_description: Manages multi chassis link aggregation groups of Enterprise SONiC domain
description:
  - This module manages mclag domain attributes of Enterprise SONiC.
author: Abirami N (@abirami-n)

options:
  config:
    description: Dict of mclag domain configurations.
    type: dict
    suboptions:
      domain_id:
        description:
          - ID of the mclag domain (MCLAG domain).
        type: int
        required: True
      peer_address:
        description:
          - The IPV4 peer-ip for corresponding MCLAG.
        type: str
      source_address:
        description:
          - The IPV4 source-ip for corresponding MCLAG.
        type: str
      peer_link:
        description:
          - Peer-link for corresponding MCLAG.
        type: str
      keepalive:
        description:
          - MCLAG session keepalive-interval in secs.
        type: int
      session_timeout:
        description:
          - MCLAG session timeout value in secs.
        type: int
      unique_ip:
        description: Holds Vlan dictionary for mclag unique ip.
        suboptions:
          vlans:
            description:
              - Holds list of VLANs for which a separate IP addresses is enabled for Layer 3 protocol support over MCLAG.
            type: list
            elements: dict
            suboptions:
              vlan:
                description: Holds a VLAN ID.
                type: str
        type: dict
      members:
        description: Holds portchannels dictionary for an MCLAG domain.
        suboptions:
          portchannels:
            description:
              - Holds a list of portchannels for configuring as an MCLAG interface.
            type: list
            elements: dict
            suboptions:
              lag:
                description: Holds a PortChannel ID.
                type: str
        type: dict
  state:
    description:
      - The state that the configuration should be left in.
    type: str
    choices:
     - merged
     - deleted
    default: merged
"""
EXAMPLES = """
# Using merged
#
# Before state:
# -------------
#
# sonic# show mclag brief
# MCLAG Not Configured
#
- name: Merge provided configuration with device configuration
  dellemc.enterprise_sonic.sonic_mclag:
    config:
      domain_id: 1
      peer_address: 1.1.1.1
      source_address: 2.2.2.2
      peer_link: 'Portchannel1'
      keepalive: 1
      session_timeout: 3
      unique_ip:
          vlans:
            - vlan: Vlan4
      members:
          portchannles:
            - lag: PortChannel10
    state: merged
#
# After state:
# ------------
#
# sonic# show mclag brief
#
# Domain ID            : 1
# Role                 : standby
# Session Status       : down
# Peer Link Status     : down
# Source Address       : 2.2.2.2
# Peer Address         : 1.1.1.1
# Peer Link            : PortChannel1
# Keepalive Interval   : 1 secs
# Session Timeout      : 3 secs
# System Mac           : 20:04:0f:37:bd:c9
#
#
# Number of MLAG Interfaces:1
#-----------------------------------------------------------
# MLAG Interface       Local/Remote Status
#-----------------------------------------------------------
# PortChannel10            down/down
#
# admin@sonic:~$ show runningconfiguration all
# {
# ...
# "MCLAG_UNIQUE_IP": {
#        "Vlan4": {
#            "unique_ip": "enable"
#        }
#    },
# ...
# }
#
#
# Using merged
#
# Before state:
# ------------
#
# sonic# show mclag brief
#
# Domain ID            : 1
# Role                 : standby
# Session Status       : down
# Peer Link Status     : down
# Source Address       : 2.2.2.2
# Peer Address         : 1.1.1.1
# Peer Link            : PortChannel1
# Keepalive Interval   : 1 secs
# Session Timeout      : 3 secs
# System Mac           : 20:04:0f:37:bd:c9
#
#
# Number of MLAG Interfaces:1
#-----------------------------------------------------------
# MLAG Interface       Local/Remote Status
#-----------------------------------------------------------
# PortChannel10            down/down
#
# admin@sonic:~$ show runningconfiguration all
# {
# ...
# "MCLAG_UNIQUE_IP": {
#        "Vlan4": {
#            "unique_ip": "enable"
#        }
#    },
# ...
# }
#
#
- name: Merge device configuration with the provided configuration
  dellemc.enterprise_sonic.sonic_mclag:
    config:
      domain_id: 1
      source_address: 3.3.3.3
      keepalive: 10
      session_timeout: 30
      unique_ip:
        vlans:
          - vlan: Vlan5
      members:
        portchannels:
          - lag: PortChannel12
    state: merged
#
# After state:
# ------------
#
# sonic# show mclag brief
#
# Domain ID            : 1
# Role                 : standby
# Session Status       : down
# Peer Link Status     : down
# Source Address       : 3.3.3.3
# Peer Address         : 1.1.1.1
# Peer Link            : PortChannel1
# Keepalive Interval   : 10 secs
# Session Timeout      : 30 secs
# System Mac           : 20:04:0f:37:bd:c9
#
#
# Number of MLAG Interfaces:2
#-----------------------------------------------------------
# MLAG Interface       Local/Remote Status
#-----------------------------------------------------------
# PortChannel10            down/down
# PortChannel12            down/down
#
# admin@sonic:~$ show runningconfiguration all
# {
# ...
# "MCLAG_UNIQUE_IP": {
#        "Vlan4": {
#            "unique_ip": "enable"
#        },
#         "Vlan5": {
#            "unique_ip": "enable"
#        }
#    },
# ...
# }
#
#
# Using deleted
#
# Before state:
# ------------
#
# sonic# show mclag brief
#
# Domain ID            : 1
# Role                 : standby
# Session Status       : down
# Peer Link Status     : down
# Source Address       : 3.3.3.3
# Peer Address         : 1.1.1.1
# Peer Link            : PortChannel1
# Keepalive Interval   : 10 secs
# Session Timeout      : 30 secs
# System Mac           : 20:04:0f:37:bd:c9
#
#
# Number of MLAG Interfaces:1
#-----------------------------------------------------------
# MLAG Interface       Local/Remote Status
#-----------------------------------------------------------
# PortChannel10            down/down
#
# admin@sonic:~$ show runningconfiguration all
# {
# ...
# "MCLAG_UNIQUE_IP": {
#        "Vlan4": {
#            "unique_ip": "enable"
#        }
#    },
# ...
# }
#
- name: Delete device configuration based on the provided configuration
  dellemc.enterprise_sonic.sonic_mclag:
   config:
     domain_id: 1
     source_address: 3.3.3.3
     keepalive: 10
     members:
       portchannels:
         - lag: PortChannel10
   state: deleted
#
# After state:
# ------------
#
# sonic# show mclag brief
#
# Domain ID            : 1
# Role                 : standby
# Session Status       : down
# Peer Link Status     : down
# Source Address       :
# Peer Address         : 1.1.1.1
# Peer Link            : PortChannel1
# Keepalive Interval   : 1 secs
# Session Timeout      : 15 secs
# System Mac           : 20:04:0f:37:bd:c9
#
#
# Number of MLAG Interfaces:0
#
# admin@sonic:~$ show runningconfiguration all
# {
# ...
# "MCLAG_UNIQUE_IP": {
#        "Vlan4": {
#            "unique_ip": "enable"
#        }
#    },
# ...
# }
#
#
#
# Using deleted
#
# Before state:
# ------------
#
# sonic# show mclag brief
#
# Domain ID            : 1
# Role                 : standby
# Session Status       : down
# Peer Link Status     : down
# Source Address       : 3.3.3.3
# Peer Address         : 1.1.1.1
# Peer Link            : PortChannel1
# Keepalive Interval   : 10 secs
# Session Timeout      : 30 secs
# System Mac           : 20:04:0f:37:bd:c9
#
#
# Number of MLAG Interfaces:1
#-----------------------------------------------------------
# MLAG Interface       Local/Remote Status
#-----------------------------------------------------------
# PortChannel10            down/down
#
# admin@sonic:~$ show runningconfiguration all
# {
# ...
# "MCLAG_UNIQUE_IP": {
#        "Vlan4": {
#            "unique_ip": "enable"
#        }
#    },
# ...
# }
#
- name: Delete all device configuration
  dellemc.enterprise_sonic.sonic_mclag:
    config:
    state: deleted
#
# After state:
# ------------
#
# sonic# show mclag brief
# MCLAG Not Configured
#
# admin@sonic:~$ show runningconfiguration all | grep MCLAG_UNIQUE_IP
# admin@sonic:~$
#
#
# Using deleted
#
# Before state:
# ------------
#
# sonic# show mclag brief
#
# Domain ID            : 1
# Role                 : standby
# Session Status       : down
# Peer Link Status     : down
# Source Address       : 3.3.3.3
# Peer Address         : 1.1.1.1
# Peer Link            : PortChannel1
# Keepalive Interval   : 10 secs
# Session Timeout      : 30 secs
# System Mac           : 20:04:0f:37:bd:c9
#
#
# Number of MLAG Interfaces:2
#-----------------------------------------------------------
# MLAG Interface       Local/Remote Status
#-----------------------------------------------------------
# PortChannel10            down/down
# PortChannel12            down/sown
#
# admin@sonic:~$ show runningconfiguration all
# {
# ...
# "MCLAG_UNIQUE_IP": {
#        "Vlan4": {
#            "unique_ip": "enable"
#        }
#    },
# ...
# }
- name: Delete device configuration based on the provided configuration
  dellemc.enterprise_sonic.sonic_mclag:
    config:
      domain_id: 1
      source_address: 3.3.3.3
      keepalive: 10
      members:
        portchannels:
          - lag: PortChannel10
    state: deleted
#
# After state:
# ------------
#
# sonic# show mclag brief
#
# Domain ID            : 1
# Role                 : standby
# Session Status       : down
# Peer Link Status     : down
# Source Address       :
# Peer Address         : 1.1.1.1
# Peer Link            : PortChannel1
# Keepalive Interval   : 1 secs
# Session Timeout      : 15 secs
# System Mac           : 20:04:0f:37:bd:c9
#
#
# Number of MLAG Interfaces:0
#
# admin@sonic:~$ show runningconfiguration all
# {
# ...
# "MCLAG_UNIQUE_IP": {
#        "Vlan4": {
#            "unique_ip": "enable"
#        }
#    },
# ...
# }
#
#
"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  type: list
  sample: >
    The configuration returned always in the same format
     of the parameters above.
after:
  description: The resulting configuration model invocation.
  returned: when changed
  type: list
  sample: >
    The configuration returned always in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['command 1', 'command 2', 'command 3']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.mclag.mclag import MclagArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.config.mclag.mclag import Mclag


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=MclagArgs.argument_spec,
                           supports_check_mode=True)

    result = Mclag(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
