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
│   └── images/                 # Tutorial images, keybindings, showcase, etc. (was: imgs/)
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
│       ├── font_loader.py
│       ├── html_loader.py
│       ├── file_utils.py
│       ├── x11_utils.py
│       └── ui_helpers.py
│
└── tests/                      # Optional: test modules
```

## 1. Project Structure
```
exodia-assistant/
├── src/                      # Source code root
│   ├── core/                 # Core application logic
│   │   ├── config/          # Configuration management
│   │   ├── services/        # Business logic services
│   │   └── models/          # Data models
│   ├── ui/                  # User interface components
│   │   ├── views/          # Main window and views
│   │   ├── widgets/        # Reusable UI components
│   │   ├── styles/         # UI styling and themes
│   │   └── resources/      # UI resources (icons, images)
│   ├── utils/              # Utility functions and helpers
│   └── data/               # Data storage and management
├── tests/                   # Test suite
│   ├── unit/              # Unit tests
│   ├── integration/       # Integration tests
│   └── fixtures/          # Test fixtures and mocks
├── docs/                   # Documentation
├── scripts/               # Build and utility scripts
└── resources/             # Application resources
    ├── fonts/            # Custom fonts
    ├── icons/            # Application icons
    └── themes/           # UI themes
```

## 2. Clean Code Principles to Apply

### 2.1. Single Responsibility Principle (SRP)
- Split large classes into smaller, focused ones
- Separate UI logic from business logic
- Create dedicated classes for specific functionalities

### 2.2. Interface Segregation
- Create clear interfaces for services
- Split large interfaces into smaller, specific ones
- Use abstract base classes for common functionality

### 2.3. Dependency Inversion
- Use dependency injection for services
- Create service interfaces
- Implement service locator pattern

### 2.4. DRY (Don't Repeat Yourself)
- Create reusable components
- Extract common functionality into utility classes
- Use inheritance and composition effectively

### 2.5. SOLID Principles
- Single Responsibility
- Open/Closed
- Liskov Substitution
- Interface Segregation
- Dependency Inversion

## 3. Code Organization

### 3.1. Core Module
```python
# src/core/config/settings.py
class Settings:
    """Application settings management."""
    pass

# src/core/services/base.py
class BaseService:
    """Base class for all services."""
    pass

# src/core/models/role.py
class Role:
    """Role model."""
    pass
```

### 3.2. UI Module
```python
# src/ui/views/main_window.py
class MainWindow:
    """Main application window."""
    pass

# src/ui/widgets/tool_card.py
class ToolCard:
    """Tool card widget."""
    pass
```

### 3.3. Utils Module
```python
# src/utils/validators.py
class Validator:
    """Input validation utilities."""
    pass

# src/utils/logger.py
class Logger:
    """Logging utilities."""
    pass
```

## 4. Naming Conventions

### 4.1. Files and Directories
- Use lowercase with underscores for files
- Use descriptive, purpose-indicating names
- Group related files in appropriate directories

### 4.2. Classes and Functions
- Use PascalCase for classes
- Use camelCase for methods
- Use descriptive, action-indicating names

## 5. Documentation

### 5.1. Code Documentation
- Add docstrings to all classes and methods
- Use type hints consistently
- Document complex algorithms and business logic

### 5.2. Project Documentation
- Create README.md with setup instructions
- Document architecture decisions
- Include API documentation

## 6. Testing Strategy

### 6.1. Unit Tests
- Test individual components
- Use mocking for dependencies
- Follow AAA pattern (Arrange, Act, Assert)

### 6.2. Integration Tests
- Test component interactions
- Test service integrations
- Test UI workflows

## 7. Error Handling

### 7.1. Exception Hierarchy
```python
class ExodiaError(Exception):
    """Base exception for Exodia OS Assistant."""
    pass

class ConfigError(ExodiaError):
    """Configuration related errors."""
    pass

class ServiceError(ExodiaError):
    """Service related errors."""
    pass
```

### 7.2. Error Logging
- Implement comprehensive logging
- Use appropriate log levels
- Include context in error messages

## 8. Configuration Management

### 8.1. Settings Structure
```python
class AppConfig:
    """Application configuration."""
    def __init__(self):
        self.ui = UIConfig()
        self.services = ServicesConfig()
        self.paths = PathsConfig()
```

### 8.2. Environment Management
- Use environment variables
- Implement configuration validation
- Support different environments (dev, prod)

## 9. UI/UX Improvements

### 9.1. Component Architecture
- Create reusable UI components
- Implement MVVM pattern
- Use Qt signals and slots effectively

### 9.2. Styling
- Use QSS for styling
- Implement theme support
- Create consistent design system

## 10. Performance Optimization

### 10.1. Resource Management
- Implement proper cleanup
- Use resource pooling
- Optimize memory usage

### 10.2. Caching
- Implement caching for expensive operations
- Use appropriate cache invalidation
- Monitor cache performance

## 11. Security

### 11.1. Input Validation
- Validate all user inputs
- Sanitize data
- Implement proper error handling

### 11.2. Resource Access
- Implement proper permissions
- Secure sensitive data
- Use secure communication

## 12. Build and Deployment

### 12.1. Build Process
- Use setuptools for packaging
- Implement proper versioning
- Create build scripts

### 12.2. Deployment
- Create installation scripts
- Implement update mechanism
- Handle dependencies properly

## 13. Monitoring and Maintenance

### 13.1. Logging
- Implement comprehensive logging
- Use appropriate log levels
- Include context in logs

### 13.2. Performance Monitoring
- Monitor resource usage
- Track performance metrics
- Implement health checks

## 14. Code Quality Tools

### 14.1. Static Analysis
- Use pylint for code analysis
- Implement type checking
- Use mypy for static typing

### 14.2. Code Formatting
- Use black for code formatting
- Implement isort for import sorting
- Use flake8 for style checking

## 15. Version Control

### 15.1. Git Workflow
- Use feature branches
- Implement proper commit messages
- Use pull requests for code review

### 15.2. Version Management
- Use semantic versioning
- Maintain changelog
- Tag releases properly

## Implementation Steps

1. Set up new project structure
2. Create base classes and interfaces
3. Implement core services
4. Create UI components
5. Add utility functions
6. Implement testing framework
7. Add documentation
8. Set up build process
9. Implement monitoring
10. Add security measures

## Success Criteria

1. Code is maintainable and readable
2. Tests cover critical functionality
3. Documentation is comprehensive
4. Performance meets requirements
5. Security measures are in place
6. Build process is automated
7. Deployment is streamlined
8. Monitoring is effective 
