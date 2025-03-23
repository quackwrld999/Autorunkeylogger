# Autorunkeylogger

🚀 Keylogger Project 

Recently worked on a Keylogger Project to understand how keystroke logging works and how attackers exploit this technique. This project was built for ethical hacking and cybersecurity awareness, aiming to learn about detection and prevention mechanisms. 🔍

🔹 Tech Stack: Python, pynput, logging, threading.
🔹 What I Learned: Practical insights into cybersecurity, ethical hacking, and security countermeasures.
🔹 Why It Matters: Awareness of security risks helps better protect against cyber threats.

⚠️Prevention & Countermeasures
1. use anti-keylogger software.
2. Keep software and OS updated.
3. Use virtual keyboards for sensitive data.
4. Monitor system processes for suspicious activities.

🔹Optional feature ( you can modify )
1. Email Feature: Sends logs via SMTP
2. Local host: Sends logs via Apache2 (code for autorun apache2)
3. Upload Logs to Cloud Storage (Google Drive/Dropbox)


🔹You can customize the code and run the key log right after the machine starts
Regedit ->HKEY_CURRENT_USER -> SOFTWARE -> Microsoft -> Windows ->CurrentVersion ->Run
In the run section right click and set a new string value (add the file path in value data)
