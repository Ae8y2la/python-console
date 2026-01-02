# Research: Console Todo App

## Decision: Architecture Pattern
**Rationale**: Selected layered architecture with TodoManager core component, in-memory storage, and console interface based on user requirements. This pattern provides clear separation of concerns while maintaining simplicity for a console application.

**Alternatives considered**:
- MVC pattern: More complex than needed for simple console app
- Functional approach: Would not provide clear separation of concerns
- Event-driven: Unnecessary complexity for simple todo operations

## Decision: Python Version
**Rationale**: Using Python 3.13+ as specified in requirements. This provides access to latest language features while ensuring compatibility with modern development practices.

**Alternatives considered**:
- Python 3.11 or 3.12: Would still work but not meet specified requirement
- Earlier versions: Would lack modern features and security updates

## Decision: Storage Approach
**Rationale**: In-memory storage only as specified in requirements. This keeps implementation simple and meets the constraint of no persistence beyond session.

**Alternatives considered**:
- File-based storage: Would violate "in-memory only" constraint
- Database storage: Would violate "in-memory only" constraint
- JSON persistence: Would violate "in-memory only" constraint

## Decision: Testing Framework
**Rationale**: Using pytest as the standard testing framework for Python projects. It's well-supported, feature-rich, and appropriate for this project scope.

**Alternatives considered**:
- unittest: Built into Python but more verbose than pytest
- nose2: No longer actively maintained
- Custom testing: Would reinvent existing solutions

## Decision: Command Parsing
**Rationale**: Using Python's built-in argparse module for command-line parsing. This is part of the standard library and provides robust argument parsing capabilities.

**Alternatives considered**:
- Click: Would require external dependency
- docopt: Would require external dependency
- Manual parsing: Would be error-prone and reinvent existing solutions