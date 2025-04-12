# SafeStorage Application

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)](https://docs.python.org/3/library/tkinter.html)

A secure desktop application for storing and retrieving sensitive text information with encryption.

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Files in the Project](#files-in-the-project)
- [Installation](#installation)
- [Usage](#usage)
- [Security Notes](#security-notes)
- [Development Status](#development-status)
- [Future Improvements](#future-improvements)
- [Caution](#caution)

## 🔍 Overview

SafeStorage is a Python-based desktop application that allows users to securely store and retrieve sensitive text information. The application encrypts all stored data using a custom encryption algorithm and stores the encryption keys separately from the content, providing an additional layer of security.

## ✨ Features

- **Secure Data Storage**: Store text entries with custom encryption
- **Data Retrieval**: Access your stored information using the correct key pairing
- **Data Management**: Delete individual files or wipe all stored data
- **Simple User Interface**: Easy-to-use GUI built with Tkinter

## 📁 Files in the Project

| File | Description |
|------|-------------|
| `SafeStorage.py` | Main application file with the GUI implementation |
| `EncryptionMethod.py` | Contains the encryption and decryption algorithms |
| `WindowMethod.py` | Handles file operations and interactions between the UI and encryption |
| `passwordSaver.py` | An additional utility for storing password pairs (currently in development) |

## 🚀 Installation

1. Ensure you have Python 3.x installed on your system
2. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/SafeStorage.git
   cd SafeStorage
   ```
3. Install the required dependencies:
   ```bash
   pip install tk
   ```

## 📝 Usage

1. Run the main application file:
   ```bash
   python SafeStorage.py
   ```

2. **Setting Up**
   - When the application starts, you'll need to specify:
     - **Key Storage Path**: The directory where encryption keys will be stored
     - **Text Storage Path**: The directory where encrypted text files will be stored

3. **Adding New Entries**
   - Click "Add entry" on the home screen
   - Enter a title for your entry
   - Type your content in the text field
   - Click "submit" to save

4. **Accessing Stored Data**
   - Click "Interact with Data" on the home screen
   - Select a file from the list or enter the filename
   - Click "search" to retrieve and decrypt the content

5. **Data Management**
   - Delete individual files using the "delete file" button
   - Wipe all stored data using the "Wipe files" button (use with caution)

## 🔒 Security Notes

- The application uses a custom encryption algorithm
- Encryption keys are stored separately from the content
- Once files are deleted, they cannot be recovered
- For maximum security, store the key files on a separate device or location

## 🚧 Development Status

- The main SafeStorage application is fully functional
- The passwordSaver utility is currently under development

## 🔮 Future Improvements

- [ ] Enhanced encryption methods
- [ ] Password protection for the application itself
- [ ] Cloud backup options
- [ ] Mobile application version

## ⚠️ Caution

> **Warning**: Always remember your storage paths. If the key file is lost or deleted, encrypted data cannot be recovered.

## 🔄 How the Encryption Works

```
┌─────────────────┐       ┌─────────────────┐
│                 │       │                 │
│     Text        │──────►│  Encryption     │
│                 │       │  Algorithm      │
└─────────────────┘       └────────┬────────┘
                                   │
                                   ▼
┌─────────────────┐       ┌─────────────────┐
│                 │       │                 │
│  Key Storage    │◄──────┤ Encrypted Text  │
│                 │       │     Storage     │
└─────────────────┘       └─────────────────┘
```

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

<div align="center">
  <b>Made with ❤️ for secure data storage</b>
</div>
