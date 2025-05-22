from Lab02.task1.Classes import WebSite, MobileApp, ManagerCall

def main():
    website_creator = WebSite.WebSite()
    mobile_app_creator = MobileApp.MobileApp()
    manager_call_creator = ManagerCall.ManagerCall()

    sub1 = website_creator.create_subscription("domestic")
    sub2 = mobile_app_creator.create_subscription("premium")
    sub3 = manager_call_creator.create_subscription("educational")

    print("\nСтворені підписки:")
    print(sub1)
    print(sub2)
    print(sub3)


if __name__ == "__main__":
    main()
