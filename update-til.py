from elements import HTMLElement
from math import ceil
import os
import time


def get_categories(base_path: str) -> list[str]:
    """Walk the directory with the `base path` and get a list of all 
    subdirectories at that level.

    Args:
        base_path (str): path of the directory inside which you have to find the categories

    Returns:
        list[str]: list of categories
    """
    avoid_dirs = [
        "images",
        "__pycache__",
    ]

    dirs = [
        dir
        for dir in os.listdir(base_path)
        if os.path.isdir(dir) and dir not in avoid_dirs and ".git" not in dir
    ]
    return sorted(dirs)


def get_tils(category):
    return [
        f"{category}/{til}"
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
    with open(til_file, "r", encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line.startswith('#'):
                return line[1:].strip()
        return "Find Out Yourself!"


def count_tils(category):
    return len([
        til
        for til in os.listdir(category)
        if til.endswith(".md")
    ])


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
            all_tils.append(til)

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
    for dir in categories:
        til_content = f"## {sanitize_topic(dir)}\n\n"
        for article in [article for article in os.listdir(dir) if os.path.abspath(article).endswith(".md")]:
            til_content += "- " + \
                HTMLElement.link(
                    get_title(f'./{dir}/{article}'), f'./{dir}/{article}')+'\n'
        tils["content"].append(til_content)
    return tils


def main():
    # assuming you have written the article,
    # now we gotta make a README.md file for the viewers to be shown
    # right now, not updating the original README.md for reference!
    with open("index.md", "w", encoding='utf-8') as README:

        # 1. Enter the header content, i.e., HEADER!
        README.write(HTMLElement.HEADER)  # ✅
        # 2. Enter the Categories section
        #     a. create a table with 3 columns in it and display the titles with the directories as their names
        #     b. each of the topics should have number of articles as superscript, so that we know about the most documented learned topic
        categories = add_categories('.')
        README.write(categories["content"])  # ✅

        # 3. We would like a recently added section as well where 5 of the recently added tils are displayed!
        task2 = add_recent_tils()
        README.write(task2)  # ❌

        # 4.
        # Topics.forEach(() => {
        #   ✅ add_topic_name_at_top()
        #   ✅ list_out_the_topics_in_a_bulleted_format()
        #   ❌ __ There could be subsections inside a topic as well
        #   ❌ __ so depending on the path of an article, we would like to give it more detailed list
        # })
        task3 = add_tils(categories["dirs"])
        README.write("\n".join(task3["content"]))

        # 5. Add the FOOTER as well at the end!
        README.write("\n---\n\n" + \
                     HTMLElement.FOOTER)  # ✅


if __name__ == "__main__":
    main()
