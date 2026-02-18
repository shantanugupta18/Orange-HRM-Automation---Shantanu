$ts = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"

pytest --alluredir=tests/reports/allure-results-$ts

allure generate tests/reports/allure-results-$ts `
-o tests/reports/allure-report-$ts