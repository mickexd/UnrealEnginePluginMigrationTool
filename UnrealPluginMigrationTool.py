import flet as ft
import subprocess


def main(page: ft.Page):
    page.title = "Unreal Plugin Migration Tool"
    page.window_resizable = True
    page.update()

    # Theme selector
    def theme_changed(e):
        page.theme_mode = (
            ft.ThemeMode.LIGHT
            if page.theme_mode == ft.ThemeMode.DARK
            else ft.ThemeMode.DARK
        )
        color_switch.label = "🌙" if page.theme_mode == ft.ThemeMode.DARK else "☀️"
        page.update()

    page.theme_mode = ft.ThemeMode.DARK
    color_switch = ft.Switch(label="🌙", on_change=theme_changed)

    # File picker function
    def pick_files_result(e: ft.FilePickerResultEvent):
        selected_file.value = (
            ", ".join(map(lambda f: f.path, e.files))
            if e.files
            else "No *.uplugin file was selected!"
        )
        selected_file.update()

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_file = ft.Text()

    # Save directory function
    def save_directory_result(e: ft.FilePickerResultEvent):
        save_file_path.value = e.path if e.path else "No save directory was selected!"
        save_file_path.update()

    save_directory_dialog = ft.FilePicker(on_result=save_directory_result)
    save_file_path = ft.Text()

    # Unreal engine directory function
    def ue_get_directory_result(e: ft.FilePickerResultEvent):
        directory_path.value = (
            e.path
            if e.path
            else 'No UE root folder was selected! (Example "C:\\Program Files\\Epic Games\\UE_5.3)"'
        )
        directory_path.update()

    get_directory_dialog = ft.FilePicker(on_result=ue_get_directory_result)
    directory_path = ft.Text()

    # Hide all dialogs in overlay
    page.overlay.extend(
        [pick_files_dialog, save_directory_dialog, get_directory_dialog]
    )

    # Plugin migration function
    def plugin_migration():
        engine = rf'"{directory_path.value}"'
        plugin = rf'"{selected_file.value}"'
        destination = rf'"{save_file_path.value}"'
        command = rf"{engine}\Engine\Build\BatchFiles\RunUAT.bat BuildPlugin -plugin={plugin} -package={destination}\Migrated"
        try:
            result = subprocess.run(command, shell=True)
            if result.returncode == 0:
                fine = ft.AlertDialog(
                    title=ft.Text("Plugin migrated succesfully"),
                )
                page.dialog = fine
                fine.open = True
                page.update()
            else:
                wrong = ft.AlertDialog(
                    title=ft.Text("Something went wrong"),
                )
                page.dialog = wrong
                wrong.open = True
                page.update()

        except Exception as e:
            fail = ft.AlertDialog(
                title=ft.Text("An error has ocurred"),
                content=ft.Text(
                    "Please check the command promp to see what the error is"
                ),
            )
            page.dialog = fail
            fail.open = True
            page.update()

    # App layout
    page.add(
        ft.Row(
            [
                color_switch,
            ],
            alignment=ft.MainAxisAlignment.END,
        ),
        ft.Row(
            [
                ft.ElevatedButton(
                    "Select the .uplugin file",
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(
                        allowed_extensions=["uplugin"]
                    ),
                ),
                selected_file,
            ]
        ),
        ft.Row(
            [
                ft.ElevatedButton(
                    "Plugin destination folder",
                    icon=ft.icons.SAVE,
                    on_click=lambda _: save_directory_dialog.get_directory_path(),
                    disabled=page.web,
                ),
                save_file_path,
            ]
        ),
        ft.Row(
            [
                ft.ElevatedButton(
                    "Select UE root folder",
                    icon=ft.icons.FOLDER_OPEN,
                    on_click=lambda _: get_directory_dialog.get_directory_path(),
                    disabled=page.web,
                ),
                directory_path,
            ]
        ),
        ft.ElevatedButton(
            "Begin Migration",
            icon=ft.icons.DEW_POINT,
            on_click=lambda _: plugin_migration(),
        ),
    )


ft.app(target=main)
