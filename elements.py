class HTMLElement:
    HEADER = """# Today I Learned
    
> Welcome to my digital garden / second brain where I try to dump everything I learn in its most raw form 🌱

"""

    FOOTER = """## About

Inspired from [Bhupesh-V/til](https://github.com/Bhupesh-V/til).
"""
    tab = "\t"
    table_start = "<table align=center><tbody>\n"
    table_end = "</tbody></table>\n"
    row_start = "<tr>\n"
    row_end = "</tr>\n"
    data_start = "<td>"
    data_end = "</td>"

    @staticmethod
    def href(topic_link: str, topic: str) -> str:
        return f"<a href='{topic_link}'>{topic}</a>"

    @staticmethod
    def link(title:str, url: str):
        return f"[{title}]({url})"

    @staticmethod
    def superscript(text: str | int | float) -> str:
        return f"<sup>{text}</sup>"
