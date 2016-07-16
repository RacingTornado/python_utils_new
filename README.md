- This set of python utilities helps you decode a USB stream which has been captured with USBMON and wireshark.
- The pcap library which is used is pcapfile which is located here https://github.com/kisom/pypcapfile
- Save the pcapfile. Make sure it is in the PCAP format and not the PCAPNG. Then follow these steps to generate the MPSSE decoding commands:
-`python py_read_pcapng.py`
The above script assumes that you have the PCAP file stored in the same directory. It's name `my_file.pcap`. This script will iterate through all the packets and log only the data portion of the USB capture into another file whose location is also hardcoded. The file is located `/home/itsy/Downloads/packet_data.txt`
- Once the data portions of the USB has been captured, make sure to copy these contents into the python helper module. Remove BULK IN packets since these currently arent filtered out manually.
- https://github.com/RacingTornado/python_utils_new/blob/master/py_helper.py - Replace the data portion with your custom data. Make sure only USB bulk packets are being used, and BULK IN packets have been removed.
- Run this script https://github.com/RacingTornado/python_utils_new/blob/master/py_edit.py which will trace out the MPSSE packet flow.
