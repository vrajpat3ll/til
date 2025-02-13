from math import ceil
import os
from elements import HTMLElement


def sanitize_topic(topic: str) -> str:
    # ? How do I proceed to do it from here?
    # > substitute all - with a whitespace and _ with -

    topic = " ".join(topic.split('-'))
    topic = "-".join(topic.split('_'))
    return " ".join([piece.capitalize() for piece in topic.split(' ')])


def count_articles(topic: str) -> int:
    # ? Create a map object and store it in JSON to retrieve it later?
    return len([dir for dir in os.listdir(topic) if os.path.abspath(dir).endswith(".md")])


def dirs_to_avoid(base_path: str) -> list[str]:
    return sorted([str(dir) for dir in os.listdir(base_path) if dir.startswith("_") or '.' in dir] + ["__pycache__"])


def dirs_to_include(base_path: str, exclude: list[str] = []) -> list[str]:
    return sorted([str(dir) for dir in os.listdir(base_path) if os.path.isdir(dir) and dir not in exclude])


def add_categories(base_path: str):

    avoid_dirs = dirs_to_avoid(base_path)
    dirs_to_consider = dirs_to_include(base_path, exclude=avoid_dirs)

    columns = 3
    rows = ceil(len(dirs_to_consider) / 3)
    # --------------------------------------------------------
    categories = "## Categories\n\n"
    categories += HTMLElement.table_start
    for row in range(rows):
        categories += HTMLElement.row_start

        for col in range(columns):
            ind = row * columns + col
            if ind >= len(dirs_to_consider):
                continue

            topic_link = dirs_to_consider[ind]
            # ------------------------------

            categories += HTMLElement.data_start

            # link to Topic in README
            cell_data = HTMLElement.href(
                '#'+topic_link) + sanitize_topic(topic_link) + HTMLElement.href_end
            cell_data += HTMLElement.superscript(count_articles(topic_link))

            categories += cell_data
            categories += HTMLElement.data_end

        categories += HTMLElement.row_end

    categories += HTMLElement.table_end + '\n'

    return {
        "content": categories,
        "dirs": dirs_to_consider
    }


def add_recent_tils():
    # From all articles available, align them with the date modified
    # sort them by date modified, take the latest 5
    # append the recent ones in a table
    return ""


def add_tils(dirs: list[str]):
    """Add tils present in the directories

    Args:
        dirs (list[str]): list of directories in which we have to check for the tils

    Returns:
        str: tils to be added in markdown format
    """
    # Add all tils with hyperlink to each article
    tils = {
        "content": "",
        "metadata": {}  # ? not yet sure of what to keep! file-name with last modified date?

    }
    for dir in dirs:
        tils["content"] += f"## {sanitize_topic(dir)}\n\n"
        for article in [article for article in os.listdir(dir) if os.path.abspath(article).endswith(".md")]:
            tils["content"] += "- " + \
                HTMLElement.link(article, f'./{dir}')+'\n\n'
            # tils["metadata"]
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
        README.write(task3["content"])

        # 5. Add the FOOTER as well at the end!
        README.write(HTMLElement.FOOTER)  # ✅


if __name__ == "__main__":
    main()
