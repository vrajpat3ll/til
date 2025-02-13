class HTMLElement:
    HEADER = """# Today I Learned
    
> Welcome to my digital garden / second brain where I try to dump everything I learn in its most raw form 🌱

"""

    FOOTER = """
---

Inspired from [Bhupesh-V/til](https://github.com/Bhupesh-V/til).
"""
    tab = "    "
    table_start = "<table align=center><tbody>\n"
    table_end = "</tbody></table>\n"
    row_start = "<tr>\n"
    row_end = "</tr>\n"
    data_start = "<td>"
    data_end = "</td>"
    href_end = "</a>"

    @staticmethod
    def href(topic: str) -> str:
        return f"<a href='{topic}'>"

    @staticmethod
    def link(file: str, host_url):
        t1 = ' '.join(file.split('-'))
        t1 = '-'.join(t1.split('_'))
        t2 = ' '.join(t1.split('.')[:-1])
        return f"[{t2[0].capitalize()+t2[1:]}]({host_url}/{file})"

    @staticmethod
    def superscript(text: str | int | float) -> str:
        return f"<sup>{text}</sup>\n"
