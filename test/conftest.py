import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import shutil
import tempfile
import os
import allure

KEEP_BROWSER_ON_FAIL = True


@pytest.fixture(scope="session")
def driver(request):

    original_profile = r"C:\Users\mp041\AppData\Local\Google\Chrome\User Data\Profile 16"

    if not os.path.exists(original_profile):
        raise FileNotFoundError(f"Profile not found: {original_profile}")

    # Copy profile once
    temp_dir = tempfile.mkdtemp()
    temp_profile_path = os.path.join(temp_dir, "Profile16_Temp")
    shutil.copytree(original_profile, temp_profile_path, dirs_exist_ok=True)

    options = Options()
    options.add_argument(f"--user-data-dir={temp_dir}")
    options.add_argument("--profile-directory=Profile16_Temp")
    options.add_argument("--no-first-run")
    options.add_argument("--no-default-browser-check")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    yield driver

    # ✅ keep browser open logic preserved
    rep = getattr(request.node, "rep_call", None)

    if KEEP_BROWSER_ON_FAIL and rep and rep.failed:
        print(f"\nTest failed! Leaving browser open for debugging. URL: {driver.current_url}")
    else:
        driver.quit()
        shutil.rmtree(temp_dir, ignore_errors=True)


# ✅ Allure + pytest proper report hook
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    # store report for fixture access
    setattr(item, "rep_" + report.when, report)

    # ✅ attach screenshot on failure
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver:
            try:
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name="failure_screenshot",
                    attachment_type=allure.attachment_type.PNG
                )

                allure.attach(
                    driver.current_url,
                    name="failed_url",
                    attachment_type=allure.attachment_type.TEXT
                )

            except Exception:
                pass
