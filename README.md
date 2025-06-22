
# 🚀 Python File Automation  
### By Pradhumnya Changdev Kalsait  
> **Automate tedious file tasks with these powerful Python scripts**  

![Python Version](https://img.shields.io/badge/Python-3.6+-blue?logo=python)  
![Platform](https://img.shields.io/badge/OS-Windows%20|%20Linux%20|%20macOS-lightgrey)  
![License](https://img.shields.io/badge/License-MIT-green)  

This repository contains **9 ready-to-use Python scripts** for automating common file and directory operations. These scripts are implemented as a **practical application of Python**, ideal for developers, data analysts, and IT professionals looking to reduce manual effort and streamline routine tasks.

Each script is independently executable and demonstrates real-world use of Python's system-level capabilities — including file handling, checksum generation, duplicate detection and removal, extension-based file organization, and more — all operable via simple command-line interfaces.

---

## 📋 Table of Contents
- [Key Features](#-key-features)
- [Complete Script Catalog](#-complete-script-catalog)
- [Requirements](#-requirements)
- [Usage Examples](#-usage-examples)
- [Notes](#-notes)
- [Contributing](#-contributing)
- [Author](#-author)

---

## ✨ Key Features
- **One-command automation** for repetitive tasks
- **Cross-platform** compatibility
- **Detailed logging** (Log.txt)
- **No dependencies** - pure Python
- **Modular design** - use only what you need

---

## 📂 Complete Script Catalog

### 🔍 File Analysis & Verification
| Script | Command | Description |
|--------|---------|-------------|
| `DirectoryChecksum.py` | `python DirectoryChecksum.py "Folder"` | Calculates MD5 checksums for all files in directory |
| `DirectoryDuplicate.py` | `python DirectoryDuplicate.py "Folder"` | Identifies duplicate files and logs to Log.txt |
| `DirectoryFileSearch.py` | `python DirectoryFileSearch.py "Folder" ".ext"` | Finds all files matching given extension |

### 🔄 File Operations
| Script | Command | Description |
|--------|---------|-------------|
| `DirectoryRename.py` | `python DirectoryRename.py "Folder" ".old" ".new"` | Bulk renames file extensions (e.g., .txt → .md) |
| `DirectoryCopy.py` | `python DirectoryCopy.py "Source" "Dest"` | Copies all files to new directory (creates destination) |
| `DirectoryCopyExt.py` | `python DirectoryCopyExt.py "Source" "Dest" ".ext"` | Copies only files with specific extension |

### 🧹 Organization & Cleanup
| Script | Command | Description |
|--------|---------|-------------|
| `FileOrganizer.py` | `python FileOrganizer.py "Folder"` | Organizes files into extension-based subfolders |
| `DirectoryDuplicateRemoval.py` | `python DirectoryDuplicateRemoval.py "Folder"` | Finds and removes duplicate files |
| `DirectoryDuplicateRemovalWithTime.py` | `python DirectoryDuplicateRemovalWithTime.py "Folder"` | Removes duplicates + measures execution time |

---

## ⚙️ Requirements
- Python 3.6+
- Any OS (Windows/Linux/macOS)
- Write permissions for target directories

---

## 🎯 Usage Examples

### Organize Files by Extension
```bash
python FileOrganizer.py "Downloads"
```
**Transforms:**
```
Downloads/
├── document.pdf
├── notes.txt
└── image.jpg
```
**Into:**
```
Downloads/
├── pdf/document.pdf
├── txt/notes.txt
└── jpg/image.jpg
```

### Remove Duplicate Files
```bash
python DirectoryDuplicateRemoval.py "Photos"
```
**Output:**
```
Found and removed 5 duplicate files
Details logged in Log.txt
```

### Verify File Integrity
```bash
python DirectoryChecksum.py "Important_Files"
```
**Output:**
```
File Checksums:
important.docx: a1b2c3d4e5...
backup.zip: f6g7h8i9j0...
```

---

## 📝 Important Notes
1. **Path Formatting**: Always quote paths containing spaces  
   `python script.py "My Folder"` not `python script.py My Folder`
2. **Extensions**: Must include the dot (`.txt` correct, `txt` incorrect)
3. **Logging**: All scripts generate `Log.txt` in current directory
4. **Performance**: For large folders, use `...WithTime.py` variants to monitor speed

---

## 🤝 Contributing
We welcome contributions! Please:
1. Open an Issue to discuss proposed changes
2. Fork the repository
3. Create a pull request with your improvements

---

## 👨💻 Author
**Pradhumnya Changdev Kalsait**  
[![GitHub](https://img.shields.io/badge/GitHub-Dexter1119-blue?logo=github)](https://github.com/Dexter1119)  
 

**⭐ Please star this repo if you find it useful!**  

---

### Why This Works Better:  
1. **Problem-Solution Focus**: Highlights **time savings** and **error reduction** upfront.  
2. **Real-World Examples**: Shows concrete before/after scenarios.  
3. **Actionable**: Clear commands and use cases for quick adoption.  
4. **Professional Yet Approachable**: Balanced tone for both beginners and experts.  
