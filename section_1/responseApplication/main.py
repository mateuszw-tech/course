from webmanager import WebContentManager, ManagerGUI

manager: WebContentManager = WebContentManager("archive", "websites.txt")
manager_app: ManagerGUI = ManagerGUI()
manager.print_websites_data()
manager_app.display_menu()

