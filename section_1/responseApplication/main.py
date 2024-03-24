from webmanager import WebContentManager

manager: WebContentManager = WebContentManager("archive", "websites.txt")
manager.print_websites_data()
manager.pull_websites_content()
