CATEGORIES = [ # Titles here are used in asset_finder to find respective icons
    "CPU",
    "Memory",
    "Network",
    "Services",
    "GPU",
    "General",
    "Debloat",
    "Latency",
    "Input",
    "Power",
]

RESTORE_POINT = "batch/1Create Restore Point/Create Restore Point.lnk"

TWEAKS = {
    "CPU": {
        "CPU Cooling": {
            "batch": "batch/2CPU/CPU Cooling.bat",
            "desc": "Forces active cooling (using fans rather than throttling the CPU) for both plugged-in and battery power modes"
        },
        "CSRSS": {
            "batch": "batch/2CPU/CSRSS.reg",
            "desc": "Assigns higher CPU and disk priority to csrss.exe, a core Windows system process"
        },
        "Disable Core Parking": {
            "batch": "batch/2CPU/Disable Core Parking.bat",
            "desc": "Stops CPU cores from disabling when not in use"
        },
        "Disable Event Processor": {
            "batch": "batch/2CPU/Disable Even Processor.bat",
            "desc": "Stops Windows' event-based CPU throttling"
        },
        "Disable Throttling States": {
            "batch": "batch/2CPU/Disable Throttling States.bat",
            "desc": "Disables CPU throttling"
        },
        "Optimize Timers": {
            "batch": "batch/2CPU/Disable Timers.bat",
            "desc": "Optimizes how Windows distributes timer interrupts across CPU cores"
        },
        "Disable Virtualization": {
            "batch": "batch/2CPU/Disable Virtualization.bat",
            "desc": "" # Self explanatory
        },
        "Spectre Meltdown Protection": {
            "batch": "batch/2CPU/Spectre Meltdown Protection.reg",
            "desc": "" # Self explanatory
        },
        "Disable Ryzen C-states": {
            "batch": "batch/2CPU/AMD/Disable Ryzen Cstates.bat",
            "category": "AMD"
        },
        "6th - 11th Gen": {
            "batch": "batch/2CPU/INTEL/6th-11th Gen.bat",
            "category": "Intel",
            "desc": ""
        },
        "Disable Intel C-states": {
            "batch": "batch/2CPU/INTEL/Disable Intel Cstates.bat",
            "category": "Intel",
            "desc": "Disables throttling and sleep states for Intel CPUs"
        },
        "Intel Bonus Optimizations": {
            "batch": "batch/2CPU/INTEL/Intel Bonus Optimizations.bat",
            "category": "Intel",
            "desc": ""
        },
    },
    "Memory": {
        "Disable CFG": {
            "batch": "batch/3Memory/Disable CFG.bat",
            "desc": "Disables Control Flow Guard, which may cause stability issues in some DX12 games"
        },
        "Disable Hibernation": {
            "batch": "batch/3Memory/Disable Hibernation.bat",
            "desc": "" # Self Explanatory
        },
        "Disable Mitigations": {
            "batch": "batch/3Memory/Disable Mitigations.bat",
            "desc": ""
        },
        "Disable Superfetch": {
            "batch": "batch/3Memory/Disable Superfetch.bat"
        },
        "Extra Performance": {
            "batch": "batch/3Memory/Memory Extra Performance.bat"
        },
        "Memory Prefetch": {
            "batch": "batch/3Memory/Memory Prefetch.reg"
        },
        "SVC": {
            "batch": "batch/3Memory/SVC.bat"
        },
    },
    "Network": {
        "Disable Heuristics": {
            "batch": "batch/4Network/Disable Heuristics.bat"
        },
        "Disable Power Saving": {
            "batch": "batch/4Network/Disable Power Saving.bat"
        },
        "Flush Old Data": {
            "batch": "batch/4Network/Flush Old Data.bat",
            "repeatable": True
        },
        "Network High Priority": {
            "batch": "batch/4Network/Network High Priority.bat"
        },
        "TCP Optimizations": {
            "batch": "batch/4Network/TCP Optimizations.bat"
        },
        "Win32 Adapter Tweaks": {
            "batch": "batch/4Network/Win32 Adapter Tweaks.bat"
        },
    },
    "Services": {
        "Disable Background Services": {
            "batch": "batch/5Services/Disable Background Services.bat"
        },
        "Disable Event Collector": {
            "batch": "batch/5Services/Disable Event Collector.reg"
        },
        "Disable Global User": {
            "batch": "batch/5Services/Disable Global User.reg"
        },
        "Disable HID Service": {
            "batch": "batch/5Services/Disable HID Service.reg"
        },
        "Disable Printing Notifications": {
            "batch": "batch/5Services/Disable HID Service.reg"
        },
        "Disable Program Assistant": {
            "batch": "batch/5Services/Disable Program Assistant.reg"
        },
        "Disable Error Reporting": {
            "batch": "batch/5Services/Disable Windows Error Reporting.reg"
        },
    },
    "GPU": {
        "Disable P-state": {
            "batch": "batch/6GPU/Disable Pstate.bat"
        },
        "GPU Preemption": {
            "batch": "batch/6GPU/GPU Preemption.bat"
        },
        "MSI High Priority": {
            "batch": "batch/6GPU/MSI High Priority.bat"
        },
        "AMD GPU": {
            "batch": "batch/6GPU/AMD/AMD GPU.bat",
            "category": "AMD"
        },
        "Disable Logging": {
            "batch": "batch/6GPU/AMD/Disable AMD Logging.bat",
            "category": "AMD"
        },
        "Stop Energy Saving": {
            "batch": "batch/6GPU/AMD/Stop Energy Saving Driver.bat",
            "category": "AMD"
        },
        "(30 Series Only)": {
            "batch": "batch/6GPU/NVIDIA/30 SERIES ONLY.bat",
            "category": "NVIDIA"
        },
        "Write Combining": {
            "batch": "batch/6GPU/NVIDIA/Write Combining.bat",
            "category": "NVIDIA"
        },
    },
    "General": {
        "Disable Activity Feed": {
            "batch": "batch/7General/Disable Activity Feed.bat"
        },
        "Disable Logging": {
            "batch": "batch/7General/Disable Logging.bat"
        },
        "Disable Transparency": {
            "batch": "batch/7General/Disable Transparency.reg"
        },
        "End Maintenance": {
            "batch": "batch/7General/End Maintenance.bat"
        },
        "Game Optimizations": {
            "batch": "batch/7General/Game Optimizations.reg"
        },
        "Stop Setting Sync": {
            "batch": "batch/7General/Stop Setting Sync.bat"
        },
        "Stop Sharing User Experiences": {
            "batch": "batch/7General/Stop Sharing User Experiences.bat"
        },
    },
    "Debloat": {
        "Clean Old Data": {
            "batch": "batch/8DeBloat/Clean Old Data.bat",
            "repeatable": True
        },
        "Delete Log Files": {
            "batch": "batch/8DeBloat/Delete Log Files.cmd",
            "repeatable": True
        },
        "Delete Temporary Files": {
            "batch": "batch/8DeBloat/Delete Temporary Files.bat",
            "repeatable": True
        },
        "Delete Update Cache": {
            "batch": "batch/8DeBloat/Delete Update Cache.bat",
            "repeatable": True
        },
        "Disable Cortana": {
            "batch": "batch/8DeBloat/Disable Cortana.bat"
        },
        "Remove Background Applications": {
            "batch": "batch/8DeBloat/Remove Background Applications.bat",
            "repeatable": True
        },
        "Remove Windows Packages": {
            "batch": "batch/8DeBloat/Remove Windows Packages.bat"
        },
    },
    "Latency": {
        "End CEIP": {
            "batch": "batch/10Latency/End CEIP.bat"
        },
        "Latency BCD Tweaks": {
            "batch": "batch/10Latency/Latency BCD Tweaks.bat"
        },
        "Low Game Delay": {
            "batch": "batch/10Latency/Low Game Delay.reg"
        },
        "MMCSS": {
            "batch": "batch/10Latency/MMCSS.reg"
        },
        "System Responsiveness": {
            "batch": "batch/10Latency/System Responsiveness.bat"
        },
    },
    "Input": {
        "Disable Mouse Acceleration": {
            "batch": "batch/11KBM/Disable Mouse Acceleration.bat"
        },
        "Disable Unnecessary Keys": {
            "batch": "batch/11KBM/Disable Unnecessary Keys.bat"
        },
        "Highest Priority": {
            "batch": "batch/11KBM/Highest Priority.bat"
        },
        "Improve Key Response Time": {
            "batch": "batch/11KBM/Improve Key Response Time.bat"
        },
        "Mouse Pixel Accuracy": {
            "batch": "batch/11KBM/Mouse Pixel Accuracy.bat"
        },
        "Reduce Key Delay": {
            "batch": "batch/11KBM/Reduce Key Delay.bat"
        },
    },
    "Power": {
        "Disable Additional Power Saving": {
            "batch": "batch/12Power/Disable Additional Power Saving.bat"
        },
        "Disable Power Throttling": {
            "batch": "batch/12Power/Disable Power Throttling.reg"
        },
        "Power Optimizations": {
            "batch": "batch/12Power/Power Optimizations.bat"
        },
        "AMD Powerplan Settings": {
            "batch": "batch/12Power/AMD/(AMD) Powerplan Settings.bat",
            "category": "AMD"
        },
        "Intel Powerplan Settings": {
            "batch": "batch/12Power/Intel/(Intel) Powerplan Settings.bat",
            "category": "Intel"
        }
    }
}