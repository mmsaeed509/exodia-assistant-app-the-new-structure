#####################################
#                                   #
#  @author      : 00xWolf           #
#    GitHub    : @mmsaeed509       #
#    Developer : Mahmoud Mohamed   #
#  﫥  Copyright : Mahmoud Mohamed   #
#                                   #
#####################################

import os
import subprocess
import yaml
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QCheckBox, QGroupBox, QScrollArea, QFrame, QLineEdit, QToolTip, QSizePolicy, QGridLayout)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon
from ..utils import roles_utils

def create_setup_environment_tab(self, tab_widget):
    """
    Create the Setup Environment tab content with a modern, developer-friendly UI.
    Args:
        self: The Role instance (for access to fonts, etc.)
        tab_widget (QTabWidget): The tab widget to add the tab to
    """
    setup_tab = QWidget()
    setup_tab.setStyleSheet("background-color: #151A21;")
    main_layout = QVBoxLayout(setup_tab)
    main_layout.setAlignment(Qt.AlignTop)
    main_layout.setContentsMargins(20, 20, 20, 20)
    main_layout.setSpacing(15)

    # Header Section
    header_frame = QFrame()
    header_frame.setStyleSheet("""
        QFrame {
            background-color: #1E252B;
            border-radius: 10px;
            padding: 15px;
        }
    """)
    header_layout = QVBoxLayout(header_frame)
    header_layout.setSpacing(10)

    # Title
    title_label = QLabel("Environment Setup")
    title_label.setFont(self.predator_font)
    font_family = self.predator_font.family()
    title_label.setStyleSheet(f"""
        color: #00B0C8;
        font-family: '{font_family}';
        font-size: 24px;
        font-weight: bold;
    """)
    header_layout.addWidget(title_label)

    # Subtitle
    subtitle_label = QLabel("Check   `/usr/share/exodia/exodia-assistant/app/roles/`   For New Roles and Role Updates")
    subtitle_label.setFont(self.predator_font)
    subtitle_label.setStyleSheet(f"""
        color: #8B9CB3;
        font-family: '{font_family}';
        font-size: 14px;
    """)
    header_layout.addWidget(subtitle_label)

    main_layout.addWidget(header_frame)

    # Action Toolbar
    toolbar_frame = QFrame()
    toolbar_frame.setStyleSheet("""
        QFrame {
            background-color: #1E252B;
            border-radius: 10px;
            padding: 10px;
        }
    """)
    toolbar_layout = QHBoxLayout(toolbar_frame)
    toolbar_layout.setSpacing(15)

    # Select All Checkbox
    select_all_checkbox = QCheckBox("Select All Tools")
    select_all_checkbox.setFont(self.predator_font)
    select_all_checkbox.setStyleSheet(f"""
        QCheckBox {{
            color: #00B0C8;
            font-family: '{font_family}';
            font-size: 14px;
            spacing: 8px;
        }}
        QCheckBox::indicator {{
            width: 18px;
            height: 18px;
            border: 2px solid #00B0C8;
            border-radius: 4px;
        }}
        QCheckBox::indicator:checked {{
            background-color: #00B0C8;
            image: url(check.png);
        }}
    """)
    toolbar_layout.addWidget(select_all_checkbox)

    # Search Bar
    search_bar = QLineEdit()
    search_bar.setPlaceholderText("Search tools...")
    search_bar.setFont(self.predator_font)
    search_bar.setStyleSheet(f"""
        QLineEdit {{
            background-color: #151A21;
            color: #00B0C8;
            border: 2px solid #00B0C8;
            border-radius: 5px;
            padding: 5px 10px;
            font-family: '{font_family}';
            font-size: 14px;
        }}
        QLineEdit:focus {{
            border: 2px solid #00D0E8;
        }}
    """)
    toolbar_layout.addWidget(search_bar)

    # Update Status Button
    update_status_button = QPushButton("Update Status")
    update_status_button.setFont(self.predator_font)
    update_status_button.setStyleSheet(f"""
        QPushButton {{
            background-color: #1E252B;
            color: #00B0C8;
            border: 2px solid #00B0C8;
            border-radius: 5px;
            padding: 8px 20px;
            font-family: '{font_family}';
            font-size: 14px;
            font-weight: bold;
        }}
        QPushButton:hover {{
            background-color: #00B0C8;
            color: white;
        }}
        QPushButton:pressed {{
            background-color: #008C9E;
            color: white;
        }}
    """)
    toolbar_layout.addWidget(update_status_button)

    # Update Button
    update_button = QPushButton("Save")
    update_button.setFont(self.predator_font)
    update_button.setStyleSheet(f"""
        QPushButton {{
            background-color: #00B0C8;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 8px 20px;
            font-family: '{font_family}';
            font-size: 14px;
            font-weight: bold;
        }}
        QPushButton:hover {{
            background-color: #00D0E8;
        }}
        QPushButton:pressed {{
            background-color: #008C9E;
        }}
    """)
    toolbar_layout.addWidget(update_button)

    main_layout.addWidget(toolbar_frame)

    # Content Area
    content_frame = QFrame()
    content_frame.setStyleSheet("""
        QFrame {
            background-color: #1E252B;
            border-radius: 10px;
            padding: 15px;
        }
    """)
    content_layout = QVBoxLayout(content_frame)
    content_layout.setSpacing(15)

    # Get the selected role from role.yaml
    selected_role = roles_utils.load_role_from_yaml()

    if not selected_role:
        # Display a message if no role is selected
        no_role_label = QLabel("Please select a role to view environment setup options.")
        no_role_label.setFont(self.predator_font)
        no_role_label.setStyleSheet(f"""
            color: #8B9CB3;
            font-family: '{font_family}';
            font-size: 16px;
        """)
        content_layout.addWidget(no_role_label)
    else:
        # Construct the path to the tools.yaml file for the selected role
        config_dir = os.path.expanduser("~/.config/exodia-assistant")
        os.makedirs(config_dir, exist_ok=True)
        tools_path = os.path.join(config_dir, f"profiles/{selected_role}/tools.yaml")

        if not os.path.exists(tools_path):
            error_label = QLabel(f"Tools configuration file not found for {selected_role}")
            error_label.setFont(self.predator_font)
            error_label.setStyleSheet(f"""
                color: #FF6B6B;
                font-family: '{font_family}';
                font-size: 16px;
            """)
            content_layout.addWidget(error_label)
        else:
            try:
                with open(tools_path, 'r') as file:
                    tools_data = yaml.safe_load(file)

                # Function to check if a package is installed
                def is_package_installed(package):
                    if package.startswith("bash "):
                        return False
                    try:
                        result = subprocess.run(
                            ["pacman", "-Q", package.strip()], 
                            stdout=subprocess.PIPE, 
                            stderr=subprocess.PIPE,
                            text=True
                        )
                        return result.returncode == 0
                    except Exception:
                        return False

                # Function to update the tools.yaml file
                def update_tools_yaml():
                    with open(tools_path, 'w') as file:
                        yaml.dump(tools_data, file, default_flow_style=False)

                # Function to validate tool data
                def validate_tool(tool):
                    if not isinstance(tool, dict):
                        return False, "Invalid tool format: must be a dictionary"
                    
                    if 'name' not in tool:
                        return False, "Missing required field: name"
                    
                    if 'pkg' not in tool:
                        return False, f"Missing required field: pkg for tool {tool['name']}"
                    
                    # Validate optional fields
                    for field in ['pre-install', 'post-install', 'pre-remove', 'remove', 'post-remove']:
                        if field in tool and tool[field] is not None:
                            if not isinstance(tool[field], (str, list)):
                                return False, f"Invalid {field} format for tool {tool['name']}: must be string or list"
                    
                    return True, None

                # Function to show error message in UI
                def show_error_message(message, is_critical=False):
                    error_label = QLabel(message)
                    error_label.setFont(self.predator_font)
                    error_label.setStyleSheet(f"""
                        color: #FF6B6B;
                        font-family: '{font_family}';
                        font-size: 14px;
                        padding: 10px;
                        background-color: #4A1C1C;
                        border-radius: 5px;
                        margin: 5px;
                    """)
                    if is_critical:
                        error_label.setStyleSheet(error_label.styleSheet() + "border: 2px solid #FF6B6B;")
                    content_layout.addWidget(error_label)
                    return error_label

                # Function to execute commands in Alacritty with error handling
                def execute_in_alacritty(commands):
                    if not commands:
                        return True, None

                    # Add error handling for each command
                    validated_commands = []
                    for cmd in commands:
                        cmd = cmd.strip()
                        if cmd:
                            # Add error handling and logging for each command
                            validated_commands.append(
                                f"echo 'Executing: {cmd}' && "
                                f"({cmd}) || {{ "
                                f"echo 'Error executing: {cmd}' >&2; "
                                f"echo 'Command failed with exit code $?' >&2; "
                                f"exit 1; "
                                f"}}"
                            )

                    # Add final status check
                    command_str = " && ".join(validated_commands)
                    command_str += " && echo 'All commands executed successfully'"

                    try:
                        # Execute in Alacritty with proper error handling
                        process = subprocess.run(
                            ["alacritty", "-e", "bash", "-c", command_str],
                            check=True,
                            capture_output=True,
                            text=True
                        )
                        return True, None
                    except subprocess.CalledProcessError as e:
                        error_msg = f"Error executing commands:\n{e.stderr}"
                        return False, error_msg
                    except Exception as e:
                        error_msg = f"Unexpected error: {str(e)}"
                        return False, error_msg

                # Function to install a tool
                def install_tool(tool):
                    commands = []
                    
                    if tool.get('pre-install'):
                        pre_exec_commands = tool['pre-install'].split(',') if tool['pre-install'] else []
                        for cmd in pre_exec_commands:
                            cmd = cmd.strip()
                            if cmd:
                                commands.append(cmd)

                    pkgs = tool.get('pkg', '')
                    if pkgs:
                        if pkgs.startswith("bash "):
                            commands.append(pkgs)
                        else:
                            package_list = [pkg.strip() for pkg in pkgs.split(',')]
                            commands.append(f"sudo pacman -S --noconfirm {' '.join(package_list)}")

                    if tool.get('post-install'):
                        post_exec_commands = tool['post-install'].split(',') if tool['post-install'] else []
                        for cmd in post_exec_commands:
                            cmd = cmd.strip()
                            if cmd:
                                commands.append(cmd)

                    execute_in_alacritty(commands)
                    tool['status'] = 'Installed'
                    update_tools_yaml()

                # Function to uninstall a tool
                def uninstall_tool(tool):
                    commands = []
                    
                    if tool.get('pre-remove'):
                        pre_remove_commands = tool['pre-remove'].split(',') if tool['pre-remove'] else []
                        for cmd in pre_remove_commands:
                            cmd = cmd.strip()
                            if cmd:
                                commands.append(cmd)

                    if tool.get('remove'):
                        remove_commands = tool['remove'].split(',') if tool['remove'] else []
                        for cmd in remove_commands:
                            cmd = cmd.strip()
                            if cmd:
                                commands.append(cmd)
                    else:
                        pkgs = tool.get('pkg', '')
                        if pkgs and not pkgs.startswith("bash "):
                            package_list = [pkg.strip() for pkg in pkgs.split(',')]
                            commands.append(f"sudo pacman -R --noconfirm {' '.join(package_list)}")

                    if tool.get('post-remove'):
                        post_remove_commands = tool['post-remove'].split(',') if tool['post-remove'] else []
                        for cmd in post_remove_commands:
                            cmd = cmd.strip()
                            if cmd:
                                commands.append(cmd)

                    execute_in_alacritty(commands)
                    tool['status'] = 'UnInstalled'
                    update_tools_yaml()

                # Dictionary to store all checkboxes
                all_checkboxes = {}
                category_checkboxes = {}
                tool_checkboxes = {}
                category_tools_dict = {}

                # Create category groups and tool checkboxes
                for category, tools in tools_data.items():
                    # Create category group
                    category_group = QGroupBox(category)
                    category_group.setFont(self.predator_font)
                    category_group.setStyleSheet(f"""
                        QGroupBox {{
                            color: #00B0C8;
                            font-family: '{font_family}';
                            font-size: 16px;
                            font-weight: bold;
                            border: 2px solid #00B0C8;
                            border-radius: 8px;
                            margin-top: 15px;
                            padding-top: 15px;
                        }}
                        QGroupBox::title {{
                            subcontrol-origin: margin;
                            left: 10px;
                            padding: 0 5px;
                        }}
                    """)
                    category_layout = QVBoxLayout(category_group)
                    category_layout.setSpacing(10)

                    # Create category checkbox
                    category_checkbox = QCheckBox(category)
                    category_checkbox.setFont(self.predator_font)
                    category_checkbox.setStyleSheet(f"""
                        QCheckBox {{
                            color: #00B0C8;
                            font-family: '{font_family}';
                            font-size: 14px;
                            spacing: 8px;
                        }}
                        QCheckBox::indicator {{
                            width: 18px;
                            height: 18px;
                            border: 2px solid #00B0C8;
                            border-radius: 4px;
                        }}
                        QCheckBox::indicator:checked {{
                            background-color: #00B0C8;
                            image: url(check.png);
                        }}
                    """)
                    category_layout.addWidget(category_checkbox)
                    category_checkboxes[category] = category_checkbox
                    all_checkboxes[category] = category_checkbox

                    # Create a grid layout for tools
                    tools_grid = QGridLayout()
                    tools_grid.setSpacing(15)  # Space between tools
                    tools_grid.setContentsMargins(20, 0, 20, 0)  # Left and right margins

                    # Create tool checkboxes
                    category_tools_checkboxes = []
                    for i, tool in enumerate(tools):
                        # Check installation status
                        if 'status' not in tool or not tool['status']:
                            if 'pkg' in tool and tool['pkg']:
                                if tool['pkg'].startswith("bash "):
                                    tool['status'] = 'UnInstalled'
                                else:
                                    packages = [pkg.strip() for pkg in tool['pkg'].split(',')]
                                    if all(is_package_installed(pkg) for pkg in packages):
                                        tool['status'] = 'Installed'
                                    else:
                                        tool['status'] = 'UnInstalled'
                            else:
                                tool['status'] = 'UnInstalled'
                            update_tools_yaml()

                        # Create tool container
                        tool_container = QWidget()
                        tool_layout = QHBoxLayout(tool_container)
                        tool_layout.setContentsMargins(0, 0, 0, 0)
                        tool_layout.setSpacing(10)

                        # Create tool checkbox
                        tool_checkbox = QCheckBox(tool['name'])
                        tool_checkbox.setChecked(tool['status'] == 'Installed')
                        tool_checkbox.setFont(self.predator_font)
                        tool_checkbox.setStyleSheet(f"""
                            QCheckBox {{
                                color: #8B9CB3;
                                font-family: '{font_family}';
                                font-size: 14px;
                                spacing: 8px;
                            }}
                            QCheckBox::indicator {{
                                width: 16px;
                                height: 16px;
                                border: 2px solid #00B0C8;
                                border-radius: 4px;
                            }}
                            QCheckBox::indicator:checked {{
                                background-color: #00B0C8;
                                image: url(check.png);
                            }}
                        """)
                        tool_layout.addWidget(tool_checkbox)

                        # Create status label
                        status_label = QLabel("✔ Installed" if tool['status'] == 'Installed' else "✘ UnInstalled")
                        status_label.setFont(self.predator_font)
                        status_label.setStyleSheet(f"""
                            color: {'#4CAF50' if tool['status'] == 'Installed' else '#FF6B6B'};
                            font-family: '{font_family}';
                            font-size: 12px;
                            padding: 2px 8px;
                            border-radius: 10px;
                            background-color: {'#1B4332' if tool['status'] == 'Installed' else '#4A1C1C'};
                        """)
                        tool_layout.addWidget(status_label)

                        # Add tooltip with package details
                        if tool.get('pkg'):
                            tool_checkbox.setToolTip(f"Packages/Scripts: {tool['pkg']}")

                        tool_layout.addStretch()

                        # Add tool container to grid
                        row = i // 2  # Integer division to determine row
                        col = i % 2   # Modulo to determine column
                        tools_grid.addWidget(tool_container, row, col)

                        # Store tool data and connect signals
                        tool_checkbox.tool_data = tool
                        tool_checkboxes[tool['name']] = tool_checkbox
                        all_checkboxes[tool['name']] = tool_checkbox
                        category_tools_checkboxes.append(tool_checkbox)

                        def toggle_tool_state(checked, t=tool, checkbox=tool_checkbox, status=status_label):
                            # Only update UI state, don't execute commands
                            if checked:
                                status.setText("✔ Installed")
                                status.setStyleSheet("""
                                    color: #4CAF50;
                                    font-family: '{font_family}';
                                    font-size: 12px;
                                    padding: 2px 8px;
                                    border-radius: 10px;
                                    background-color: #1B4332;
                                """)
                            else:
                                status.setText("✘ UnInstalled")
                                status.setStyleSheet("""
                                    color: #FF6B6B;
                                    font-family: '{font_family}';
                                    font-size: 12px;
                                    padding: 2px 8px;
                                    border-radius: 10px;
                                    background-color: #4A1C1C;
                                """)

                            # Update category checkboxes
                            for cat, tools_checkboxes in category_tools_dict.items():
                                cat_checkbox = category_checkboxes[cat]
                                cat_checkbox.setChecked(all(cb.isChecked() for cb in tools_checkboxes))

                            # Update the "Select All" checkbox
                            select_all_checkbox.setChecked(all(cb.isChecked() for cb in all_checkboxes.values()))

                        tool_checkbox.toggled.connect(toggle_tool_state)

                    # Add the tools grid to the category layout
                    category_layout.addLayout(tools_grid)

                    # Store category's tools checkboxes
                    category_tools_dict[category] = category_tools_checkboxes

                    # Connect category checkbox
                    def toggle_category(checked, cat=category, tools_checkboxes=category_tools_checkboxes):
                        for checkbox in tools_checkboxes:
                            checkbox.setChecked(checked)

                    category_checkbox.toggled.connect(toggle_category)
                    category_checkbox.setChecked(all(cb.isChecked() for cb in category_tools_checkboxes))

                    content_layout.addWidget(category_group)

                # Connect Select All checkbox
                def toggle_all_tools(checked):
                    for checkbox in all_checkboxes.values():
                        checkbox.setChecked(checked)

                select_all_checkbox.toggled.connect(toggle_all_tools)
                select_all_checkbox.setChecked(all(cb.isChecked() for cb in all_checkboxes.values()))

                # Connect Save button with enhanced error handling
                def apply_changes():
                    try:
                        tools_to_install = []
                        tools_to_uninstall = []
                        validation_errors = []

                        # Validate and collect tools that need changes
                        for category, tools in tools_data.items():
                            for tool in tools:
                                # Validate tool data
                                is_valid, error_msg = validate_tool(tool)
                                if not is_valid:
                                    validation_errors.append(f"{category}/{tool.get('name', 'Unknown')}: {error_msg}")
                                    continue

                                tool_checkbox = tool_checkboxes[tool['name']]
                                if tool_checkbox.isChecked() and tool['status'] != 'Installed':
                                    tools_to_install.append(tool)
                                elif not tool_checkbox.isChecked() and tool['status'] != 'UnInstalled':
                                    tools_to_uninstall.append(tool)

                        # Show validation errors if any
                        if validation_errors:
                            show_error_message("Validation errors found:\n" + "\n".join(validation_errors), True)
                            return

                        if not tools_to_install and not tools_to_uninstall:
                            return

                        # Build command pipeline
                        commands = []
                        packages_to_install = []
                        packages_to_remove = []

                        # 1. Pre-install scripts
                        for tool in tools_to_install:
                            if tool.get('pre-install'):
                                pre_install_commands = tool['pre-install'].split(',') if isinstance(tool['pre-install'], str) else tool['pre-install']
                                for cmd in pre_install_commands:
                                    cmd = cmd.strip()
                                    if cmd:
                                        commands.append(cmd)

                        # 2. Collect packages to install
                        for tool in tools_to_install:
                            if tool.get('pkg'):
                                if tool['pkg'].startswith("bash "):
                                    commands.append(tool['pkg'])
                                else:
                                    package_list = [pkg.strip() for pkg in tool['pkg'].split(',')]
                                    packages_to_install.extend(package_list)

                        # 3. Post-install scripts
                        for tool in tools_to_install:
                            if tool.get('post-install'):
                                post_install_commands = tool['post-install'].split(',') if isinstance(tool['post-install'], str) else tool['post-install']
                                for cmd in post_install_commands:
                                    cmd = cmd.strip()
                                    if cmd:
                                        commands.append(cmd)

                        # 4. Pre-remove scripts
                        for tool in tools_to_uninstall:
                            if tool.get('pre-remove'):
                                pre_remove_commands = tool['pre-remove'].split(',') if isinstance(tool['pre-remove'], str) else tool['pre-remove']
                                for cmd in pre_remove_commands:
                                    cmd = cmd.strip()
                                    if cmd:
                                        commands.append(cmd)

                        # 5. Collect packages to remove
                        for tool in tools_to_uninstall:
                            if tool.get('remove'):
                                remove_commands = tool['remove'].split(',') if isinstance(tool['remove'], str) else tool['remove']
                                for cmd in remove_commands:
                                    cmd = cmd.strip()
                                    if cmd:
                                        commands.append(cmd)
                            elif tool.get('pkg') and not tool['pkg'].startswith("bash "):
                                package_list = [pkg.strip() for pkg in tool['pkg'].split(',')]
                                packages_to_remove.extend(package_list)

                        # 6. Post-remove scripts
                        for tool in tools_to_uninstall:
                            if tool.get('post-remove'):
                                post_remove_commands = tool['post-remove'].split(',') if isinstance(tool['post-remove'], str) else tool['post-remove']
                                for cmd in post_remove_commands:
                                    cmd = cmd.strip()
                                    if cmd:
                                        commands.append(cmd)

                        # Add package installation command if there are packages to install
                        if packages_to_install:
                            commands.append(f"sudo pacman -S --noconfirm {' '.join(packages_to_install)}")

                        # Add package removal command if there are packages to remove
                        if packages_to_remove:
                            commands.append(f"sudo pacman -Rns --noconfirm {' '.join(packages_to_remove)}")

                        # Execute all commands in a single terminal session
                        if commands:
                            success, error_msg = execute_in_alacritty(commands)
                            if not success:
                                show_error_message(error_msg, True)
                                return

                            # Update tool statuses after successful execution
                            for tool in tools_to_install:
                                tool['status'] = 'Installed'
                            for tool in tools_to_uninstall:
                                tool['status'] = 'UnInstalled'
                            
                            try:
                                update_tools_yaml()
                            except Exception as e:
                                show_error_message(f"Error updating tools.yaml: {str(e)}", True)
                                return

                            # Refresh UI to reflect new statuses
                            refresh_tool_statuses()

                    except Exception as e:
                        show_error_message(f"Unexpected error: {str(e)}", True)

                update_button.clicked.connect(apply_changes)

                # Connect Search bar
                def filter_tools(text):
                    for category, tools in tools_data.items():
                        category_group = category_checkboxes[category].parent()
                        category_group.setVisible(False)
                        for tool in tools:
                            tool_checkbox = tool_checkboxes[tool['name']]
                            if text.lower() in tool['name'].lower():
                                category_group.setVisible(True)
                                tool_checkbox.parent().setVisible(True)
                            else:
                                tool_checkbox.parent().setVisible(False)

                search_bar.textChanged.connect(filter_tools)

                # Function to refresh tool statuses
                def refresh_tool_statuses():
                    try:
                        # Get all installed packages from pacman
                        result = subprocess.run(
                            ["pacman", "-Q"], 
                            stdout=subprocess.PIPE, 
                            stderr=subprocess.PIPE,
                            text=True
                        )
                        
                        if result.returncode != 0:
                            print(f"Error getting installed packages: {result.stderr}")
                            return
                            
                        # Create a set of installed packages for faster lookup
                        installed_packages = set()
                        for line in result.stdout.splitlines():
                            package_name = line.split()[0]  # Get package name from "package version"
                            installed_packages.add(package_name)

                        # Update each tool's status
                        for category, tools in tools_data.items():
                            for tool in tools:
                                if 'pkg' in tool and tool['pkg']:
                                    if tool['pkg'].startswith("bash "):
                                        # For script-based installations, we can't check
                                        continue
                                        
                                    # Check if all packages are installed
                                    packages = [pkg.strip() for pkg in tool['pkg'].split(',')]
                                    is_installed = all(pkg in installed_packages for pkg in packages)
                                    
                                    # Update tool status in YAML
                                    tool['status'] = 'Installed' if is_installed else 'UnInstalled'
                                    
                                    # Update UI
                                    tool_checkbox = tool_checkboxes[tool['name']]
                                    tool_checkbox.setChecked(is_installed)
                                    
                                    # Update status label
                                    status_label = tool_checkbox.parent().findChild(QLabel)
                                    if status_label:
                                        status_label.setText("✔ Installed" if is_installed else "✘ UnInstalled")
                                        status_label.setStyleSheet(f"""
                                            color: {'#4CAF50' if is_installed else '#FF6B6B'};
                                            font-family: '{font_family}';
                                            font-size: 12px;
                                            padding: 2px 8px;
                                            border-radius: 10px;
                                            background-color: {'#1B4332' if is_installed else '#4A1C1C'};
                                        """)

                        # Update category checkboxes
                        for cat, tools_checkboxes in category_tools_dict.items():
                            cat_checkbox = category_checkboxes[cat]
                            cat_checkbox.setChecked(all(cb.isChecked() for cb in tools_checkboxes))

                        # Update the "Select All" checkbox
                        select_all_checkbox.setChecked(all(cb.isChecked() for cb in all_checkboxes.values()))

                        # Update the YAML file
                        update_tools_yaml()
                        
                    except Exception as e:
                        print(f"Error refreshing tool statuses: {str(e)}")

                # Connect Update Status button
                update_status_button.clicked.connect(refresh_tool_statuses)

            except Exception as e:
                error_label = QLabel(f"Error loading tools configuration: {str(e)}")
                error_label.setFont(self.predator_font)
                error_label.setStyleSheet(f"""
                    color: #FF6B6B;
                    font-family: '{font_family}';
                    font-size: 16px;
                """)
                content_layout.addWidget(error_label)

    # Create scroll area for content
    scroll_area = QScrollArea()
    scroll_area.setWidgetResizable(True)
    scroll_area.setWidget(content_frame)
    scroll_area.setStyleSheet("""
        QScrollArea { 
            border: none;
            background-color: transparent;
        }
        QScrollBar:vertical {
            background: #151A21;
            width: 10px;
            margin: 0;
        }
        QScrollBar::handle:vertical {
            background: #00B0C8;
            border-radius: 5px;
        }
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
            background: #00B0C8;
        }
        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
            background: #151A21;
        }
    """)

    main_layout.addWidget(scroll_area)

    # Add the tab to the tab widget
    tab_widget.addTab(setup_tab, "Environment")
