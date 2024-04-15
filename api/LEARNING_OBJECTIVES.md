# Learning Objectives

- [What Bash scripting should not be used for](#What-Bash-scripting-should-not-be-used-for)
- [What is an API](#Wha-tis-an-API)
- [What is a REST API](#What-is-a-REST-API)
- [What are microservices](#What-are-microservices)
- [What is the CSV format](#What-is-the-CSV-format)
- [What is the JSON format](#Wha-tis-the-JSON-format)
- [Pythonic Package and module name style](#Pythonic-Package-and-module-name-style)
- [Pythonic Class name style](#Pythoni-cClass-name-style)
- [Pythonic Variable name style](#Pythonic-Variable-name-style)
- [Pythonic Function name style](#Pythonic-Function-name-style)
- [Pythonic Constant name style](#Pythonic-Constant-name-style)
- [Significance of CapWords or CamelCase in Python](#Significance-of-CapWords-or-CamelCase-in-Python)


## What Bash scripting should not be used for
Bash scripting, while versatile, may not always be the best choice for certain tasks. Here are some scenarios where it's generally not recommended to use Bash scripting:

- Performance-Critical Applications:
Bash scripting might not be the best choice for applications requiring high performance or efficiency, such as real-time systems or heavy computational tasks. Other languages like C, C++, or Go are more suitable for such cases.

- Large-Scale Projects:
While Bash can handle small to medium-sized scripts effectively, it may become unwieldy and difficult to maintain in large-scale projects. Using a more robust programming language like Python, Ruby, or JavaScript might be a better choice for complex applications.

- Cross-Platform Development:
Bash scripting is primarily designed for Unix-like operating systems (such as Linux and macOS). While it's possible to run Bash scripts on Windows using tools like Cygwin or Windows Subsystem for Linux (WSL), it's not a native environment, and portability might be an issue. For cross-platform compatibility, consider using a language with better cross-platform support, such as Python or Java.

- Complex Data Manipulation:
While Bash provides basic text manipulation capabilities, handling complex data structures like JSON or XML can be cumbersome. Higher-level languages with built-in libraries for data manipulation, such as Python or Ruby, are more suitable for such tasks.

- Graphical User Interface (GUI) Development:
Bash scripting is primarily focused on command-line interfaces and lacks native support for graphical user interfaces. For GUI development, languages like Java (with Swing or JavaFX), Python (with Tkinter or PyQt), or JavaScript (with Electron) are more appropriate.

- Long-Term Maintenance:
Bash scripts can become difficult to maintain over time, especially if they lack proper documentation, error handling, or modular design. For long-term projects, using a more structured and maintainable language with strong community support can ensure easier maintenance and scalability.

- Highly Portable Scripts:
While Bash scripts are portable across Unix-like systems, they might encounter compatibility issues on different distributions due to variations in shell versions, utilities, or filesystem layouts. For highly portable scripts, consider using POSIX-compliant shell scripting or a language like Python that offers better cross-platform support.

## What is an API

It's a broad term that encompasses any interface allowing communication between different software systems.
APIs can follow various architectural styles and protocols, such as SOAP (Simple Object Access Protocol), GraphQL, RPC (Remote Procedure Call), and more.
APIs can be designed and implemented in various ways, and they may not necessarily adhere to the principles of REST.

## What is a REST API
It's a specific type of API that follows the principles of REST.
REST APIs are based on a client-server architecture, where clients send requests to servers to manipulate resources.
REST APIs use standard HTTP methods (GET, POST, PUT, DELETE, etc.) for performing operations on resources.
They typically use URIs (Uniform Resource Identifiers) to identify and address resources, and responses are sent back in standardized formats like JSON or XML.
REST APIs are stateless, meaning each request contains all necessary information for the server to process it, and the server does not store client state between requests.

## What are microservices
Microservices are an architectural approach to building software applications as a collection of small, independent services, each focused on a specific business function and operating independently of one another. Instead of building a monolithic application where all features and functions are tightly coupled within a single codebase, microservices architecture decomposes the application into a set of loosely coupled services, each running in its own process and communicating with lightweight mechanisms such as HTTP or messaging queues.
## What is the CSV format
CSV stands for "Comma-Separated Values." 
```bash
Name, Age, Email
John Doe, 30, john@example.com
Jane Smith, 25, jane@example.com

```
## What is the JSON format
JSON (JavaScript Object Notation) is a lightweight data interchange format.

- Each key-value pair is separated by a colon (:).
- Key-value pairs are separated by commas (,).
- The entire JSON object is enclosed in curly braces {}.
- JSON supports the following data types:

### String: Enclosed in double quotes (").
- Number: Integer or floating-point numbers.
- Boolean: true or false.
- Array: Ordered list of values enclosed in square brackets [].
- Object: Unordered collection of key-value pairs enclosed in curly braces {}.
```json
{
  "key1": "value1",
  "key2": 123,
  "key3": true,
  "key4": ["item1", "item2", "item3"],
  "key5": {
    "nested_key": "nested_value"
  }
}

```
## Pythonic Package and module name style
### Package Names:

- Package names should be lowercase.
- If multiple words are needed, they should be separated by underscores.
- Avoid using names that are too generic or too similar to existing Python modules or packages.
Example: my_package, utils, data_processing

### Module Names:

- Module names should also be lowercase.
- If multiple words are needed, they should be separated by underscores.
- Module names should be descriptive and reflect the purpose or content of the module.
Example: data_utils.py, string_processing.py, config_reader.py

### Avoid Conflicts:

- Be mindful of potential conflicts with built-in Python modules or packages, as well as popular third-party packages.
- If your package or module name conflicts with a standard library or commonly used package, consider using a different name or prefix to avoid confusion.

### Use of Underscores:

- Python conventionally uses underscores to separate words in names (snake_case), rather than camelCase or mixedCase.
- This applies to both package/module names and variable/function names, contributing to the overall consistency of Python code.

## Pythonic Class name style
### CapWords Convention:

- Class names should start with an uppercase letter.
- If the class name consists of multiple words, each word should start with an uppercase letter.
- Do not use underscores to separate words in class names.
## Pythonic Variable name style
### snake_case Convention:

- Variable names should be all lowercase.
- Words within variable names should be separated by underscores (_).
- Use descriptive and meaningful names that convey the purpose or content of the variable.

## Pythonic Function name style
snake_case Convention
## Pythonic Constant name style
In Python, there is no strict convention for naming constants, but a common convention is to use ALL_CAPS_WITH_UNDERSCORES to differentiate constants from variables.
```python
PI = 3.14159
MAX_ATTEMPTS = 5
DEFAULT_TIMEOUT = 30
```
## Significance of CapWords or CamelCase in Python

- Readability:
CapWords/CamelCase makes class and module names easier to read and distinguish from other identifiers in the code. It helps quickly identify class definitions and differentiate them from variables, functions, or other elements.

- Consistency:
Following a consistent naming convention throughout your codebase enhances readability and maintainability. When all class and module names adhere to the CapWords/CamelCase convention, it creates a uniform style that makes the codebase easier to understand for both the original developer and anyone else who may need to work with the code.
