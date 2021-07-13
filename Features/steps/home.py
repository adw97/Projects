
from behave import step
from selenium import webdriver
from time import sleep


@step("I open youtube using url")
def open_url(context):
    try:
        driver = webdriver.Chrome()
        for i in context.table:
            url = i["url"]
            print("i ===========", url)
            driver.get(url)
            print(f"opened youtube using url")
            sleep(5)
            print(f"closing youtube")
    except Exception as error:
        print(error)
        assert False


@step('I enter text "{text}" in xpath "{xpath}"')
def enter_text(context, text, xpath):
    try:
        # xpath = eval(xpath)
        driver.find_element_by_xpath(xpath).send_keys(text)
        sleep(5)
        return True
    except Exception as err:
        print(err)
        assert False


