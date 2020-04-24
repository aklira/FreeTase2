# FreeTase2
Free and open implementation of the IEC 60870-6 TASE.2 protocol based on libIEC61850 from mz-automation.

Content:

* [Overview](#overview)
* [Features](#features)
* [Examples](#examples)
* [Licensing](#commercial-licenses-and-support)
* [Contributing](#contributing)

## Overview
FreeTase2 is a free and open source Python library for the Intercontrol Center Communications Protocol (ICCP) per the IEC 60870-6 TASE.2 standards. It enables the application or device developer to develop robust interoperable ICCP-TASE.2 applications and devices quickly using their favorite language. FreeTase2 aims to provide everything needed to build ICCP-TASE.2 interfaces for large SCADA applications running on data center or cloud infrastructures but also to scale down to a compact devices for embedded applications.

## Features
### ICCP FUNDAMENTALS
ICCP (TASE.2) protocol relies on a subset of services of the MMS (ISO 9506) protocol.

### VCC, ICC and Domains
ICCP Objects exists in a VCC (Virtual Control Center). This represents the objects present in a physical control Center. This is the main object under which all other objects such as variables are stored. MMS refers to this as a VMD (Virtual Manufacturing Device). More than one Client Control Center has access to VCC objects.
Some Objects exist in a localized domain. This is a subset of the VCC. ICCP refers to this as ICC. Access to ICC specific objects is limited to only one control center.
All ICCP objects must have a specific object scope, either VCC or ICC.

### Client and Server Relationship
These terms represent the service role in ICCP. A Client is an application or device that asks for data or an action from the server. A Server is an application or device that maintains data objects and performs operations on behalf of clients. An application can be a Client or a Server or both depending on the operation. Clients always send a request. Servers receive an Indication. Servers send a Response and Clients receive a Confirmation.
Connection Roles are Calling and Called. The application that initiates the association is Calling. The application that Listens for the connection is Called.

### ICCP Conformance Building Blocks
The following Conformance Building Blocks (CBBs) will be supported by FreeTase2 on first release:

### Block 1 – Basic Services
All ICCP implementations must support Block 1. Block 1 includes association establishment, Data Value and Data Set Objects, and Data Set Transfer Set Objects.

### Block 2 – Extended Condition Monitoring
Block 2 is also referred to as report-by-exception, or RBE.
Block 2 is used to provide the capability to transfer power system data in more ways than as just periodic reports (block 1).  
Report-by-exception allows the client to specify that power system objects will be reported only when a change is detected or when an integrity check is performed. TASE.2 does this by having the server monitor a number of conditions and when one or more of those conditions are satisfied, the data that has changed is sent to the client. The client sets the conditions to be monitored in the transfer set at the server.

### Block 4 – Information Message
Block 4 provides a general message transfer mechanism that also includes the ability to transfer ASCII text or binary files. 
Block 4 adds the Information Message Transfer Set server object with the associated Information Buffer data object.

### Block 5 – Device Control
Block 5 provides a mechanism for transferring a ‘request to operate a device’ from one TASE.2 implementation to another. TASE.2 does not directly control the device, rather it communicates a client’s request to operate a device to the server.
Block 5 adds the Device server object and associated Control Point data object.

## Examples
## Licensing
## Contributing



