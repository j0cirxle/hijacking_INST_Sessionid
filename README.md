# Instagram Session Hijacking Malware

## 1. Program Overview
This malicious program tricks the user into logging into the Instagram website directly, then secretly and automatically extracts the user's login session cookie called `sessionid`.  
The stolen session ID is transmitted in real-time to the attacker's server, allowing the attack to hijack the user's account session and enabling persistent remote access and account manipulation.

## 2. Main Components

### (1) instagram_bot.exe
- Disguised as a normal ChromeDriver executable file, but internally it performs automated control of the Instagram webpage and session hijacking.  
- Called by legitimate automation tools like Selenium, it secretly manipulates the browser session without the user's knowledge.

### (2) client.py
- Automatically launches the Instagram login page using Selenium, and when the user logs in, it secretly extracts the `sessionid` cookie from the browser.  
- Sends a ping every second to maintain a connection with the attacker's server, and transmits the stolen session ID to the attacker’s server via WebSocket communication.

### (3) server.py
- A WebSocket server located on the attacker’s side that receives and logs session hijacking information (cookies) from infected clients.  
- Ignores pings used for connection maintenance and collects and stores all session information sent by the clients in real-time.

## 3. Malicious Operation Flow
1. The victim launches the Instagram login page in an environment running `instagram_bot.exe`.  
2. The victim logs into their Instagram account directly, but during this process, the malware secretly extracts the session cookie in the background.  
3. The stolen `sessionid` is transmitted in real-time to the attacker’s server, resulting in a complete hijack of the victim’s Instagram session.  
4. The attacker uses the stolen session to access, manipulate, and collect information from the victim’s account without authorization.

## 4. Security Threats and Legal Issues
- This program illegally steals the victim’s Instagram account authentication token, increasing the risk of privacy violations and account theft.  
- It is a serious malicious program that goes beyond violating service terms and constitutes a cybercrime; its use and distribution are subject to criminal penalties.  
- Since it severely threatens user privacy and account security, immediate deletion is strongly recommended, and if infected, changing the password and enabling two-factor authentication are advised as security measures.

---

# Using

INST-Hijacking
Disclaimer
This project is intended for educational purposes and authorized penetration testing only. Do not use these scripts against accounts, systems, or networks you do not own or have explicit permission to test. Unauthorized use may violate computer crime laws.

Overview
INST-Hijacking is a proof-of-concept toolkit that demonstrates Instagram session hijacking.
The attacker runs a server to receive stolen session data, while the victim unknowingly executes a client script that automates Instagram login using ChromeDriver.

Components

server.py - Attacker-side listener. Waits for incoming connections from the victim client.
client.py - Victim-side script. Connects to the attacker’s IP/Port and performs automated Instagram actions.
instagram_bot.exe - ChromeDriver executable used by client.py for browser automation.

How It Works
The attacker runs server.py on their machine, listening for incoming connections.

The victim runs client.py, which:

Connects to the attacker’s IP and port

Launches instagram_bot.exe (ChromeDriver)

Performs automated Instagram actions

All traffic is sent to the attacker’s listener, enabling session hijacking.

Usage
Attacker Side
Run:
`python server.py`

When prompted:

`Enter attacker IP (e.g., 192.168.1.100)`

`Enter attacker port (e.g., 8080)`

Victim Side
Place client.py and instagram_bot.exe in the same folder.

Run:
`python client.py`

Important: instagram_bot.exe is actually chromedriver.exe and must match the Chrome version installed on the victim’s machine.

Legal Notice
This project is strictly for security research and testing in controlled environments. Do not deploy in real-world scenarios without explicit permission. Misuse may lead to criminal prosecution.



*This repository is for educational and security awareness purposes only.*
