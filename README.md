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

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/Audrise/bedflood.git
    cd bedflood
    ```
2. Install the necessary Python libraries:
    ```bash
    pip3 install -r requirements.txt
    ```
   Or
    ```bash
    pip3 install pystyle requests pycryptodome
    ```

3. To run BEDFLOOD, open a terminal and use the following command:
    ```bash
    python3 bedflood.py -ip [IP Address] -port [Port] -b [Bot Counts] -s [Skin Directory] -c [Chatfile.txt] -i [Intensity 1-5] -d [Duration]
    ```

    Example
    ```bash
    python3 bedflood.py -ip 120.0.0.1 -port 19132 -b 100 -s skins - c chat.txt -i 3 -d 30
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

### **1.4-BE**
- **Added input mode**

    When you are prompted to enter a value (such as **IP address, port, bot count, skin directory, chatfile, intensity, duration**), if you type **"retry"**, the program will restart the input process from the beginning, effectively resetting the entire data entry. This feature is useful if you realize the data entered was incorrect, or if you simply want to start over without restarting the entire script.

- **Example Usage:**

    Here is an example of an input section that you can use to return to the beginning using **"retry"**
    ```bash
    [?] Enter the IP Address ->
    [?] Enter the port [Press enter to set 19132] ->
    [?] Enter the bot counts [Press enter for default] ->
    [?] Enter the skin file [Press enter for default] ->
    [?] Enter the chat file [Press enter for default] ->
    [?] Enter the intensity [Press enter for default] ->
    [?] Enter the duration [Press enter for infinity] -> 
    ```
    This will take you back to the initial input step, allowing you to re-enter the IP address.

- #### **Benefits of the "retry" Feature:**
    - **Fixing Mistakes**: You can easily correct mistakes in your inputs without restarting the entire program.
    - **Flexibility**: If you're unsatisfied with the data you've entered, simply type **"retry"** to start over and input the correct values.
    - **Better User Experience**: It allows users to correct errors quickly without significant interruptions, enhancing the overall comfort of using the program.

- #### **Important Notes:**
    - You can use **"retry"** on any input, except on the **"Press enter to exit"** section.
    - The program will continue to ask for correct data and restart the input process as needed, without needing to stop or restart the script.
