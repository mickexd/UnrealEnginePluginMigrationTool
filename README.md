# Unreal Engine Plugin Migration Tool
This is a simple Python application that provides a graphical user interface (GUI) for migrating Unreal Engine plugins using the Unreal Automation Tool (UAT). 
It allows you to select the *.uplugin of your preference and recompile it to any Unreal Engine version you want. 


## Features

- Support for all major versions of Unreal Engine (e.g., UE4, UE5).
- Automatic plugin format detection.
- Plugin format migration if necessary.
- Handling of third-party plugin dependencies.
- Command line tool integration for batch processing.

## Usage
1. Download the latest version of the app on https://github.com/mickexd/UnrealEnginePluginMigrationTool/releases and open the application 
2. Select the `.uplugin` file you want to migrate.
3. Select the plugin destination folder .
4. Select the UE root installation folder. (Example C:\Program Files\Epic Games\UE_5.0)
5. Click on the "Begin Migration" button to start the migration process.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, feel free to create an issue or submit a pull request.

## Disclaimer
Please note that this tool is currently in development and may not be fully functional. 
Always ensure you have backups of your original plugin files and project files before using this tool.
Some plugins that have dependencies that are linked to a specific unreal engine version will fail during the migration process.
This tool is provided as-is, I'm not responsible for any potential issues or data loss that may occur during the migration process. ENJOY!