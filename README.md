<h1 align="center">BEDFLOOD</h1>

<div align=center>
    <strong>DoS Attack Tool for Minecraft Bedrock</strong>
</div>
<br>

<div align=center>
    <img src="https://img.shields.io/badge/Python-FFDD00?style=for-the-badge&logo=python&logoColor=blue"/>
    <img src="https://img.shields.io/badge/Version-1.1 BE-blue?style=for-the-badge"/>
    <br>
    <img src="https://img.shields.io/github/stars/Audrise/bedflood?style=social">
</div>

## Description
BEDFLOOD is a tool designed for launching **Denial of Service (DoS)** attacks on Minecraft Bedrock Edition servers. This tool floods the server with multiple methods to overload the server’s resources, resulting in an unresponsive state.

## Features

- **Flooding Methods**:
    - Magic Packets
    - Login Data Flooding with usernames and skins
    - Chat Message Flooding
    - Variation Payload Flooding
    - UDP Fragmentation Flooding
  
- **AES Encryption**:
    - Encrypts the login and skin data using AES with ECB mode, securing the data being sent.
  
- **Bot Simulation**:
    - Simulates multiple Minecraft Bedrock bots that connect to the server and send repeated packets to overload the server.

- **Multithreading**:
    - Uses a lock mechanism to ensure that multiple operations (like counting the total packets sent) don't conflict with each other.

- **Check Server Status**:
    - To check the server status directly with the api provided by **[mcstatus.io](https://mcstatus.io)**. Use the parameter **python3 bedflood.py -api < IP Address >**

## How to use
1. You must have **Python 3.xx**.If you don't have it you can download and install **Python** from [here](https://www.python.org/downloads/).<br>
    After that run this command in your terminal
    ```bash
    python3 --version
    ```
2. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/Audrise/bedflood.git
    cd bedflood
    ```
3. Install the necessary Python libraries:
    ```bash
    pip3 install -r requirements.txt
    ```
   Or
    ```bash
    pip3 install pystyle requests pycryptodome
    ```

4. To run BEDFLOOD, open a terminal and use the following command:
    ```bash
    python3 bedflood.py -ip [IP Address] -port [Port] -b [Bot Counts] -s [Skin Directory] -c [Chatfile.txt] -i [Intensity 1-5] -d [Duration]
    ```

    Example
    ```bash
    python3 bedflood.py -ip 120.0.0.1 -port 19132 -b 100 -s skins - c chat.txt -i 3 -d 60
    ```
<br>

<h1 align="center">WARNING</h1>

**BEDFLOOD** is intended solely for educational purposes in a controlled environment. 
Use this tool **only** with explicit permission from the server owner. 
Unauthorized use to attack or overload servers is illegal and can cause serious damage. **Please use this tool responsibly and **only** for authorized testing and research purposes. Unauthorized use is illegal and can cause significant harm** and **Please use this tool responsibly and **only** for authorized testing and research purposes. Unauthorized use is illegal and can cause significant harm.**

## Ethical Guidelines
- **Do not use this tool on any server without explicit permission.**
- **Only use this tool in a controlled environment, such as a local server.**
- **Educate others on the risks and consequences of launching DoS/DDoS attacks.**
- **Never attempt to attack a public or private server without authorization.**

## Credits
- Thanks to **[BillyTheGoat356](https://github.com/billythegoat356)** to provide the **[PyStyle](https://github.com/billythegoat356/pystyle.git)** module for very nice terminal styling and **[Hyperion](https://github.com/billythegoat356/hyperion.git)** for nice obfuscation tool
- Thanks to **[mcstatus.io](https://mcstatus.io)** To provide an API for checking servers very easily and quickly.
