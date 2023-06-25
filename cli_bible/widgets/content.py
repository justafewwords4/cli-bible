from textual.app import ComposeResult
from textual.widgets import MarkdownViewer

MARKDOWN_CONTENT = """
# Libro - Capítulo

primera parte en **negritas**

segunda parte en *itálica*

## otro texto del mensajero

primera parte del texto del mensajero

segunda parte del texto del mensajero

## La educación

primera parte en **negritas**

segunda parte en *itálica*

## otro texto del mensaje

primera parte del texto del mensaje

segunda parte del texto del mensaje

## La educación

primera parte en **negritas**

segunda parte en *itálica*

### otro texto

primera parte del texto

segunda parte del texto

## La educación

primera parte en **negritas**

segunda parte en *itálica*

## otro texto

primera parte del texto

segunda parte del texto

## Tables

Tables are displayed in a DataTable widget.

| Name            | Type   | Default | Description                        |
| --------------- | ------ | ------- | ---------------------------------- |
| `show_header`   | `bool` | `True`  | Show the table header              |
| `fixed_rows`    | `int`  | `0`     | Number of fixed rows               |
| `fixed_columns` | `int`  | `0`     | Number of fixed columns            |
| `zebra_stripes` | `bool` | `False` | Display alternating colors on rows |
| `header_height` | `int`  | `1`     | Height of header row               |
| `show_cursor`   | `bool` | `True`  | Show a cell cursor                 |


## Code Blocks

Code blocks are syntax highlighted, with guidelines.

```python
class ListViewExample(App):
    def compose(self) -> ComposeResult:
        yield ListView(
            ListItem(Label("One")),
            ListItem(Label("Two")),
            ListItem(Label("Three")),
        )
        yield Footer()
```
"""


class MyContent(MarkdownViewer):
    """Visor de contenido"""

    BINDINGS = [
        ("b", "back", ""),
        ("f", "forward", ""),
    ]
