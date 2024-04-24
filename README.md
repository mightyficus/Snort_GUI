# Snort Rule Builder
Snort Rule Builder is a simple graphical interface used to create rules for the Snort application, commonly used as an open-source IDS. In its current state, it has a limited set of capabilities, including creation of rules using the tcp, udp, and icmp protocols. It allows for the creation of a full header, and offers common body options and a limited set of protocol-specific body options. It compiles the supplied input into a rule in an output area.

# Author Information
Author: Cooper Hopkin
email: cooper.hopkin@protonmail.com
github.com/mightyficus

# Requirements
* Python 3
* Tkinter module

# Usage
* In the main project folder, simply run `python3 snort_gui.py`.
* In the application, each field can be changed, and the rule will automatically update
* Simple validation is in place.
	* Source and Destination IP are required.
	* The SID field is required. For custom rules, SID must be greater than 1000000.
	* Revision Number is required. This must be a number greater than 0.
	* Priority is required. In this program, this will be a number between 1 and 2147483647, with 1 being most severe
	* Class Types are restricted to the classes that are in the default `snort_defaults.lua` file included with Snort 3
	* All other fields are technically optional, but a message should always be included.
* When a protocol is chosen, the body options that are specific to that protocol will be enabled in the "Body Options" area
* Any body options that are not applicable to the chosen protocol will be disabled.
* The Rule output box is read-only.

# General Notes
This application is pre-alpha a work-in-progress. It is barebones and likely has, even in its barebones state, significant bugs. This application is not in any way guaranteed to work.

This program creates rules for the Snort 3 engine, and is not guaranteed to work in previous Snort engines. The Snort 3 rule documentation can be found here: https://docs.snort.org/
