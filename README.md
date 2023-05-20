## SamplePinger-AnalyzeARP:
They are 4 files in the folder. 
```
:------`analysis_pcap_arp.py`
:------`my_arp.pcap`
:------`sample_pinger.py`
:------`README` 
```
## Part A
### Execute:
Run it by typing `python` followed by `smaple_pinger.py`  and the hostname or IP address you want to ping. You can run it like this:
```bash
$ python .\sample_pinger.py i.root-servers.net
```
### Some Test Result:
####  Ping localhost: 127.0.0.1
![Screenshot 2023-04-19 154707 1](https://github.com/Apricot0/SamplePinger-AnalyzeARP/assets/61392940/383bcdd7-455d-4dc3-ab90-5b22d639df24)
#### Ping cs.stonybrook.edu
![Screenshot 2023-04-19 154835](https://github.com/Apricot0/SamplePinger-AnalyzeARP/assets/61392940/7b2f14d0-ad86-4666-ad29-f624738423b5)
#### Ping m root server (m.root-servers.net, 202.12.27.33, 2001:dc3::35, WIDE Project)
![Screenshot 2023-04-19 155517](https://github.com/Apricot0/SamplePinger-AnalyzeARP/assets/61392940/93679bea-dc60-4569-b139-184920ad91c6)
#### Ping i root server (i.root-servers.net, 192.36.148.17, 2001:7fe::53, Netnod)
![Screenshot 2023-04-19 184634](https://github.com/Apricot0/SamplePinger-AnalyzeARP/assets/61392940/fa751b13-071b-4b27-acf8-924ea652e834)
#### Ping k root server (k.root-servers.net, 193.0.14.129, 2001:7fd::1, RIPE NCC)
![Screenshot 2023-04-19 155549 1](https://github.com/Apricot0/SamplePinger-AnalyzeARP/assets/61392940/dd4c5eda-fe4e-4a8e-a950-629e79299dc5)
### Conclusion:
From the results shown above, it is easy to see that the minimum RTT is shorter for servers geographically closer to the client.  The result is as expectation. Because one of the factors influencing RTT is distance. The length a signal has to travel correlates with the time taken for a request to reach a server and a response. So, if the server is geographically closer to the client, the signal has a shorter distance to travel. The RTT for local servers was close to 0. The only exception to the test was the i root server (Netnod). Although the search results show that Netnod's servers are located in Seden, Netnod operates root servers in multiple locations around the world, including in the United States. This makes the minimum RTT relatively short compared to other root servers outside of the US.
## Part B
### Execute:
Before run, make sure that package `dpkt` installed correctly. Then run as usual by typing `python` followed by `analysis_pcap_arp.py`:
```bash
$ python .\analysis_pcap_arp.py
```
### Logic:
The program opens a `pcap` file and iterates through each packet in the file. For each packet, it checks if the packet is an ARP packet by checking the 12th and 13th bytes of the buffer. If it is an ARP packet, it extracts relevant information from the ARP header such as hardware type, protocol type code, hardware size, protocol size, sender MAC address, sender IP address, target MAC address, and target IP address by using  byte-level programming. It then prints the information in a readable format. If the ARP opcode is 1, it means the packet is an ARP request, and if it is 2, it means the packet is an ARP reply. The code also converts certain fields to a more readable format, such as the protocol type code to a hexadecimal string format.
### Result:
*15 ARPs captured but most of them are broadcast
#### One of the captured exchange:
![Pasted image 20230419194728](https://github.com/Apricot0/SamplePinger-AnalyzeARP/assets/61392940/8d30a978-d223-4779-a46c-ba5155832971)
#### Corresponding print from program :
```
===========================================================
No: 23687, Timestamp: 1681932051.205065, APR
Type: Request
Hardware type: 1	 Protocol type code: 0x0800
Hardware size: 6	 Protocol size: 4
Sender MAC address: a6:21:b3:79:91:e4
Sender IP address: 10.1.198.239
Target MAC address: 2c:23:3a:9c:01:4c
Target IP address: 10.1.192.1
===========================================================
===========================================================
No: 23688, Timestamp: 1681932051.210284, APR
Type: Reply
Hardware type: 1	 Protocol type code: 0x0800
Hardware size: 6	 Protocol size: 4
Sender MAC address: 2c:23:3a:9c:01:4c
Sender IP address: 10.1.192.1
Target MAC address: a6:21:b3:79:91:e4
Target IP address: 10.1.198.239
===========================================================
```
### Conclusion:
In the two captured packets, the first packet is an ARP request sent by the device with MAC address a6:21:b3:79:91:e4 (which is my computer) to find the MAC address of the device with IP address 10.1.192.1. The second packet is an ARP response (10.1.192.1 is at 2c:23:3a:9c:01:4c) sent by the device with MAC address 2c:23:3a:9c:01:4c (So router is responding my request) to provide the MAC address of the device with IP address 10.1.192.1 to the requesting device. The IP address of my router appears to be 10.1.192.1 and the MAC address is 2c:23:3a:9c:01:4c.
