import flet as ft

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Load the counter value from client storage if it exists
    counter_value = page.client_storage.get("counter")
    initial_value = str(counter_value) if counter_value is not None else "0"
    txt_number = ft.TextField(value=initial_value, text_align=ft.TextAlign.RIGHT, width=100)

    def minus_click(e):
        new_value = int(txt_number.value) - 1
        txt_number.value = str(new_value)
        page.client_storage.set("counter", new_value)  # Save to client storage
        page.update()

    def plus_click(e):
        new_value = int(txt_number.value) + 1
        txt_number.value = str(new_value)
        page.client_storage.set("counter", new_value)  # Save to client storage
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.Icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.Icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(main)