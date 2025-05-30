# PENETRATION-TESTING-TOOLKIT

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: CHANDRAKANT RAMASHANKAR JAISWAR

*INTERN ID*: CT04DL772

*DOMAIN*: CYBER SECURITY & ETHICAL HACKING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

*DISCRIPTION*:  

For this project, I created a basic Penetration Testing Toolkit using Python, aimed at simulating two primary tasks in cybersecurity: brute force login testing and port scanning. The goal was to understand the process of how attackers might attempt to gain unauthorized access and explore ways in which open ports can potentially expose system vulnerabilities. I used both VS Code and Python’s IDLE to develop and run the scripts, which helped me understand how different development environments handle Python scripts and local servers. Throughout the journey, I referred to various resources such as RealPython, GeeksforGeeks, and Python’s official documentation to troubleshoot issues and better understand the libraries I was using.

The first part of the project involved setting up a Flask-based login server. I hosted the server locally using the IP address 197.165.1.1 and port 8080. The login endpoint (/login) accepts POST requests and compares submitted credentials with hardcoded values. I configured it to recognize the username Chandrakant and password chand123 as valid. Any other combination returns a 401 Unauthorized response. This simple server was designed to simulate a login form without the need for a front-end interface, focusing purely on back-end authentication logic.

To test this login server, I wrote a brute force script using Python and the requests library. The script prompts the user to input the target URL, a username, and the path to a file containing a list of passwords. It loops through each password and submits it in a POST request to the server. If a correct password is found (detected by the presence of “Login successful” in the response), the script prints it and stops. Otherwise, it continues testing until it reaches the end of the list. Through this part, I gained a better understanding of how brute force attacks work, how to handle HTTP status codes in Python, and the importance of input sanitization.

The second part of the toolkit is a port scanner. Using Python’s socket library, I built a script that scans for open ports on a given IP address — in this case, 197.165.1.1. The scanner attempts to establish TCP connections to a range of ports (usually from 1 to 1024), and if a connection is successful, it marks the port as open. I added a timeout feature to prevent the script from hanging if the port is filtered or unresponsive. This exercise taught me how basic port scanning works, how to efficiently handle sockets in Python, and why network firewalls are crucial in cybersecurity.

A few key things I learned from this project:

1)How to simulate and test a login authentication system.
2)Writing scripts that can communicate with servers using HTTP POST requests.
3)The basics of TCP/IP and how ports can be tested for accessibility.
4)The difference between open, closed, and filtered ports.

All in all, this project gave me a solid foundation in ethical hacking and practical Python scripting. I tested the tools in both IDLE and VS Code, debugging issues ranging from incorrect port numbers to connection refusals. Despite the challenges, working on this toolkit was an eye-opening experience and a stepping stone in my journey into cybersecurity.

*OUTPUT* 

![Image](https://github.com/user-attachments/assets/498e6760-a17d-4f32-8d6f-d094c81c9b91)

![Image](https://github.com/user-attachments/assets/4e7f76c6-7c87-48de-b0d4-2e9c6113c475)

![Image](https://github.com/user-attachments/assets/f4d7e9f8-99d4-4e4d-9e6e-a37f822cc38a)

![Image](https://github.com/user-attachments/assets/21364162-4279-4fb2-80e4-8f99b374236c)
