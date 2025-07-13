<h1 align="center">BEDFLOOD</h1>

<div align=center>
    <strong>DoS Attack Tool for Minecraft Bedrock</strong>
</div>
<br>

<div align=center>
    <img src="https://img.shields.io/badge/Python-FFDD00?style=for-the-badge&logo=python&logoColor=blue"/>
    <img src="https://img.shields.io/badge/Version-1.3 BE-blue?style=for-the-badge"/>
    <br>
    <img src="https://img.shields.io/github/stars/Audrise/bedflood?style=social">
</div>

## Description
**BEDFLOOD** is a tool designed for launching **Denial of Service (DoS)** attacks on Minecraft Bedrock Edition servers. This tool floods the server with multiple methods to overload the server’s resources, resulting in an unresponsive state.

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
1. You must have **Python 3.xx**. If you don't have it you can download and install [**Python**](https://www.python.org/downloads/).<br>
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

<h1 align="center"><strong>WARNING</strong></h1>

**BEDFLOOD** is developed strictly for **educational** and **research** purposes within a **controlled environment**. This tool must only be used with the **explicit permission** of the **server owner**.

Any **unauthorized use**, including attempting to **disrupt**, **overload**, or **damage** servers, is strictly **prohibited** and may be considered **illegal** under applicable laws. Such actions can lead to **severe consequences** for both the target systems and the individuals involved.

Please use this tool **responsibly** and **only** for legitimate **security testing** and **academic purposes**. **Misuse** of this tool is **unethical**, potentially **unlawful**, and strongly **discouraged**.

## Ethical Guidelines
- **Do not use this tool on any server without explicit permission.**
- **Only use this tool in a controlled environment, such as a local server.**
- **Educate others on the risks and consequences of launching DoS/DDoS attacks.**
- **Never attempt to attack a public or private server without authorization.**

## Credits
- Thanks to **[BillyTheGoat356](https://github.com/billythegoat356)** which provides the **[PyStyle](https://github.com/billythegoat356/pystyle.git)** module for very nice terminal styling and **[Hyperion](https://github.com/billythegoat356/hyperion.git)** for nice obfuscation tool
- Thanks to **[mcstatus.io](https://mcstatus.io)** which provides API to check server easily and quickly.

## **Latest Update**
#### **1.2-BE**
In this version, every time a target is launched, important execution details will be automatically logged to a file named **target_history.txt**. This includes:

``` bash
=============================
- Date       : 09 July 2025
- Time       : II:MM AM/PM
- IP         : 127.0.0.1
- Port       : 8080
- Bot Counts : 5 Bots
- Skin Dir   : skins
- Chat File  : chat.txt
- Intensity  : Level 3
- Duration   : 60 Seconds
=============================
```

#### **1.3-BE**
- Improved -s (Skin Directory) Argument Handling
We’ve added validation checks for the -s argument to make the script more robust and user-friendly:

    - 📁 The script now checks if the provided skin directory exists.

    - 📄 It also verifies that at least one .json skin file is present in the directory.

    - 🚫 If validation fails, the script will display a friendly error message and exit gracefully.

- Enhanced Payload in make_login_packet Function
We’ve significantly improved the structure of the payload used in the make_login_packet function. The new payload includes more detailed skin information to provide greater flexibility and control over the skin-related data sent.

    - Changes:
    Additional fields added: More data points for handling custom skin settings such as **SkinGeometry**, **CapeData**, **ArmSize**, and **Skin animation data**.

    - Support for premium and trusted skins: More detailed flags like **PremiumSkin**, **PersonaSkin**, **TrustedSkin**, and **IsTrustedSkin** ensure smoother skin handling with different use cases.

    - Default values for all fields: In case any of the skin parameters are missing, the payload will fall back to predefined defaults.
    
    **Payload Example:**
    ```bash
    {
        "username": "YourUsername",
        "SkinId": "Standard_Custom",
        "PlayFabId": "00000000-0000-0000-0000-000000000000",
        "SkinResourcePatch": "",
        "SkinGeometry": "",
        "SkinGeometryData": "",
        "SkinData": "",
        "CapeId": "",
        "CapeData": "",
        "ArmSize": "wide",
        "SkinAnimationData": "",
        "PremiumSkin": false,
        "PersonaSkin": false,
        "CapeOnClassicSkin": false,
        "TrustedSkin": true,
        "FullSkinId": "Standard_Custom_Full",
        "OverwriteSkinAnimation": false,
        "IsTrustedSkin": true
    } 
    ```
