import asyncio
from elements import HTMLElement
from math import ceil
import os
import pathlib
import time

AVOID_DIRS = [
    ".git",
    ".venv",
    "__pycache__",
    "images",
    "site",
]


def get_categories(base_path) -> list:
    """Walk the directory with the `base path` and get a list of all 
    subdirectories at that level.

    Args:
        base_path (str): path of the directory inside which you have to find the categories

    Returns:
        list[str]: list of categories
    """

    dirs = [
        dir
        for dir in os.listdir(base_path)
        if os.path.isdir(dir) and dir not in AVOID_DIRS
    ]
    return sorted(dirs)


def get_tils(category):
    """get all TILs from a category

    Args:
        category (str): the category

    Returns:
        list[str]: all TILs of a category
    """
    return [
        pathlib.Path(til)
        for til in os.listdir(category)
        if til.endswith(".md")
    ]


def get_title(til_file):
    """Get the title for the til

    Args:
        til_file (str): path of the til file

    Returns:
        str: Title of the til
    """
    ret = "Find Out Yourself!"
    try:
        with open(til_file, "r", encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line.startswith('#'):
                    ret = line[1:].strip()
                    return ret
    finally:
        return ret


def count_tils(category):
    return len(get_tils(category))


def count_total_tils():
    categories = get_categories('.')
    return sum([1 for category in categories for til in get_tils(category)])


def sanitize_topic(topic: str) -> str:
    # ? How do I proceed to do it from here?
    # > substitute all - with a whitespace and _ with -

    topic = " ".join(topic.split('-'))
    topic = "-".join(topic.split('_'))
    return " ".join([piece.capitalize() for piece in topic.split(' ')])


def add_categories(base_path: str):

    categories = get_categories(base_path)
    columns = 3
    rows = ceil(len(categories) / columns)
    # --------------------------------------------------------
    content = "## Categories\n\n"
    content += HTMLElement.table_start
    for row in range(rows):

        content += HTMLElement.row_start
        for col in range(columns):
            ind = row * columns + col
            if ind >= len(categories):
                break

            topic_link = categories[ind]

            cell_data = HTMLElement.href('#'+topic_link, sanitize_topic(topic_link)) + \
                HTMLElement.superscript('['+str(count_tils(topic_link))+']')

            content += HTMLElement.data_start
            content += cell_data
            content += HTMLElement.data_end + '\n'

        content += HTMLElement.row_end

    content += HTMLElement.table_end + '\n'

    return {
        "content": content,
        "dirs": categories
    }


def add_recent_tils(n=5):

    def get_modified_date(file):
        return time.ctime(os.path.getmtime(file))

    categories = get_categories('.')

    all_tils = []
    for category in categories:
        for til in get_tils(category):
            all_tils.append(str(category / til).replace('\\', '/'))

    recent_tils = sorted(
        all_tils,
        key=lambda x: get_modified_date(x),
        reverse=True
    )[:n]

    rows = ceil(len(recent_tils))
    # --------------------------------------------------------
    content = "## Recent TILs 🆕\n\n"

    content += HTMLElement.table_start
    for row in range(rows):

        content += HTMLElement.row_start

        topic_link = recent_tils[row]
        cell_data = HTMLElement.href(topic_link, get_title(topic_link))

        content += HTMLElement.data_start
        content += cell_data
        content += HTMLElement.data_end + '\n'

        content += HTMLElement.row_end

    content += HTMLElement.table_end + '\n'

    return content


def add_tils(categories: list[str]):
    """Add tils present in the directories

    Args:
        categories (list[str]): list of categories to use for the tils

    Returns:
        str: tils to be added in markdown format
    """
    # Add all tils with hyperlink to each article
    tils = {
        "content": [],
        "metadata": {

        }  # ? not yet sure of what to keep! file-name with last modified date?
    }
    for category in categories:
        til_content = f"## {sanitize_topic(category)}\n\n"
        for article in [article for article in os.listdir(category) if os.path.abspath(article).endswith(".md")]:
            til_content += \
                "- " + \
                HTMLElement.link(
                    get_title(pathlib.Path('.') / category / article),
                    f'./{category}/{article}') + \
                '\n'
        tils["content"].append(til_content)
    return tils


async def create_index():
    # assuming you have written the article,
    # now we gotta make a index.md file for the viewers to be shown
    with open("index.md", "w", encoding='utf-8') as README:

        README.write(HTMLElement.HEADER)

        README.write(f"_{count_total_tils()} TILs_ and counting...\n\n")

        categories = add_categories('.')
        README.write(categories["content"])

        task2 = add_recent_tils()
        README.write(task2)  # ❌

        task3 = add_tils(categories["dirs"])
        README.write("\n".join(task3["content"]))

        # 5. Add the FOOTER as well at the end!
        README.write("\n---\n\n" + HTMLElement.FOOTER)


async def create_readme():
    dummy_file = pathlib.Path("README.md")
    file = dummy_file

    # assuming you have written the article,
    # now we gotta make a README.md file for the viewers to be shown on github!
    # right now, not updating the original README.md for reference!
    with open(file, "w", encoding='utf-8') as README:

        README.write(HTMLElement.HEADER)
        README.write(f"_{count_total_tils()} TILs_ and counting...\n\n")

        categories = add_categories('.')
        README.write(categories["content"])

        tils = add_tils(categories["dirs"])
        README.write("\n".join(tils["content"]))

        README.write("\n---\n\n" + HTMLElement.FOOTER)


async def main():
    """TIL build script algorithm:

        1. Create an index.md file for the index of the website
        2. Create readme file for github repo
    """
    task1 = asyncio.create_task(create_index())
    task2 = asyncio.create_task(create_readme())

    await task1
    await task2

if __name__ == "__main__":
    asyncio.run(main())
