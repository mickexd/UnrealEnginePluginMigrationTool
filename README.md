# Unreal Engine Plugin Migration Tool

This is a simple Python application that provides a graphical user interface (GUI) for migrating Unreal Engine plugins using the Unreal Automation Tool (UAT). It allows you to select the engine path, the original plugin path, and the output path for the migrated plugin. Once configured, the tool runs the migration process and provides feedback through message boxes.

## Requirements

- Python 3.x
- Tkinter library (usually included with Python)
- Unreal Engine installed on your system
- All the escential libraries to compile UE projects (dotsdk, llvm, and others applicable to your engine version)

## Usage

1. Clone or download the repository to your local machine.

2. Make sure you have Python 3.x installed on your system.

3. Open a terminal/command prompt and navigate to the directory where the repository is located.

4. Run the following command to start the application:

5. The GUI window will appear, prompting you to provide the necessary paths:
- **Engine Path:** Select the root directory of your Unreal Engine installation.
- **Origin Path:** Select the original plugin file (`.uplugin`) you want to migrate.
- **Output Path:** Choose the directory where the migrated plugin will be saved.

6. After providing the paths, click the "Begin Plugin Migration" button. The tool will execute the migration process using UAT.

7. Once the migration is complete, a message box will appear:
- If the migration was successful, you will see a message indicating that the plugin was ported successfully.
- If there was an error during the migration, an error message will be displayed.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, feel free to create an issue or submit a pull request.

## Disclaimer

This tool is provided as-is, I'm not responsible for any potential issues or data loss that may occur during the migration process. ENJOY!


