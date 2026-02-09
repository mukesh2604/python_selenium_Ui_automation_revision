import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import shutil
import tempfile
import os

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

    # Check if test failed
    rep = getattr(request.node, "rep_call", None)
    if KEEP_BROWSER_ON_FAIL and rep is not None and not rep.passed:
        print(f"\nTest failed! Leaving browser open for debugging. URL: {driver.current_url}")
    else:
        driver.quit()
        shutil.rmtree(temp_dir, ignore_errors=True)


# Hook to attach test result to request.node
def pytest_runtest_makereport(item, call):
    if call.when == "call":
        setattr(item, "rep_call", call)
