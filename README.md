# 📁 Recommended Folder Structure

```bash
exodia-assistant/
├── main.py                     # App entry point
├── config.py                   # App-wide constants, paths, font names
├── requirements.txt            # Dependencies
├── README.md
│
├── assets/                     # All static content
│   ├── fonts/                  # Fonts (was: Fonts/)
│   ├── html/                   # All HTML (was: HTML-files/)
│   ├── icons/                  # Icons (was: icons/)
│   └── imgs/                   # Tutorial images, keybindings, showcase, etc. (was: imgs/)
│
├── app/                        # App codebase
│   ├── core/                   # App logic & services
│   │   ├── role_manager.py     # Refactored from role.py
│   │   ├── role_service.py     # Business logic for roles
│   │   ├── settings_service.py
│   │   ├── news_service.py
│   │   └── config_loader.py    # YAML or JSON config handler
│   │
│   ├── ui/                     # UI elements
│   │   ├── windows/            # PyQt windows
│   │   │   ├── main_window.py
│   │   │   ├── internal_window.py
│   │   │   └── tweaks_window.py
│   │   ├── widgets/            # Custom widgets
│   │   │   ├── side_panel.py
│   │   │   ├── profile_pic.py
│   │   │   ├── custom_buttons.py
│   │   │   └── logo_widget.py
│   │   ├── tabs/               # Role-specific tabs
│   │   │   ├── roadmap_tab.py
│   │   │   ├── materials_tab.py
│   │   │   └── environment_tab.py
│   │   └── keybinding/         # Keyboard-specific UI
│   │       └── keybinding_widget.py
│   │
│   ├── roles/                  # Role-specific logic and data
│   │   ├── profiles/           # DevOps, Backend, Frontend, MLOps
│   │   ├── role.yaml
│   │   ├── roles_utils.py
│   │   └── __init__.py
│   │
│   └── utils/                  # Common helpers
│       ├── font_utils.py
│       ├── html_utils.py
│       ├── file_utils.py
│       ├── x11_utils.py
│       └── ui_utils.py
│
└── tests/                      # Optional: test modules
```
