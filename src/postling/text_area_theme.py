from rich.style import Style
from textual.widgets.text_area import TextAreaTheme


POSTLING_THEME = TextAreaTheme(
    name="postling",
    syntax_styles={
        "json.error": Style.parse("on #dc2626"),
        "json.null": Style(color="#7DAF9C"),
        "json.label": Style(color="#569cd6", bold=True),
        "string": Style(color="#ce9178"),
        "string.documentation": Style(color="#ce9178"),
        "comment": Style(color="#6A9955"),
        "keyword": Style(color="#569cd6"),
        "operator": Style(color="#569cd6"),
        "conditional": Style(color="#569cd6"),
        "keyword.function": Style(color="#569cd6"),
        "keyword.return": Style(color="#569cd6"),
        "keyword.operator": Style(color="#569cd6"),
        "repeat": Style(color="#569cd6"),
        "exception": Style(color="#569cd6"),
        "include": Style(color="#569cd6"),
        "number": Style(color="#b5cea8"),
        "float": Style(color="#b5cea8"),
        "class": Style(color="#4EC9B0"),
        "type.class": Style(color="#4EC9B0"),
        "function": Style(color="#4EC9B0"),
        "function.call": Style(color="#4EC9B0"),
        "method": Style(color="#4EC9B0"),
        "method.call": Style(color="#4EC9B0"),
        "boolean": Style(color="#7DAF9C"),
        "constant.builtin": Style(color="#7DAF9C"),
        "tag": Style(color="#EFCB43"),
        "yaml.field": Style(color="#569cd6", bold=True),
        "toml.type": Style(color="#569cd6"),
        "heading": Style(color="#569cd6", bold=True),
        "bold": Style(bold=True),
        "italic": Style(italic=True),
        "strikethrough": Style(strike=True),
        "link": Style(color="#40A6FF", underline=True),
        "inline_code": Style(color="#ce9178"),
        "info_string": Style(color="#ce9178", bold=True, italic=True),
    },
)
