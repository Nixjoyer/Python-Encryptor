# Python Encryption Script

This project contains a simple Python script that:

* Computes the **MD5 hash** of an input message
* Generates a **Symmetric key**
* Encrypts and decrypts the input message using the key

## File Structure
```bash
├── encryptor.py     # The encryption script
├── flake.nix        # Contains the 
├── flake.lock        # Locks down the version
└── README.md        # This file
```

## Usage

You'll be prompted to enter a message. The script will display:

* The MD5 hash of your message
* A newly generated symmetric key
* The encrypted version of your message
* The decrypted (original) message
<img width="893" height="102" alt="Screenshot_20250712_125931" src="https://github.com/user-attachments/assets/ce5e4a99-7150-4613-9241-02f43670cbd9" />

## Requirements

* Python 3.7 or higher
* Cryptography package

# How to Run

## NixOS or Nix System (with flakes)

Make sure `flakes` are enabled in your `/etc/nixos/configuration.nix`:

```bash
nix.settings.experimental-features = [ "nix-command" "flakes" ];
```

* Clone the repo:
```bash
git@github.com:Nixjoyer/Python-Encryptor.git && cd Python-Encryptor
```

* Run directly
```bash
nix run 
```

* Or Enter Nix Shell and run it inside
```bash
nix develop
python3 encryptor.py
```

## Other Linux Distros/ MacOS

Make sure Python 3 and pip are installed.

* Debian/Ubuntu
```bash
sudo apt install python python-pip
```

* Fedora
```bash
sudo dnf install python python-pip
```

* Arch
```bash
sudo pacman -S python python-pip
```
 
* Install cryptography:

```bash
pip install cryptography
```

* Run the script:
   
```bash
python encryptor.py
```

## **Windows**

You can either:

### **1. Windows Subsystem for Linux (WSL)**

* Enable WSL and install Ubuntu or any other distro.

* Follow the `Other Linux` instructions above

### **2. Python Installer**

* Download Python from [https://www.python.org/downloads/](https://www.python.org/downloads/)

* Open Command Prompt

* Install cryptography:
```bash
pip install cryptography
```

* Run:
```bash
python encryptor.py
```
