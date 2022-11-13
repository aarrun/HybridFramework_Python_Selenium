C:\Users\aruns\AppData\Local\Programs\Python\Python39\Scripts\pytest.exe -s -v -m "sanity" --html=./Reports/report_chrome.html
:: pytest -s -v -m "sanity or regression" --html=./Reports/report_chrome.html testCases/
:: pytest -s -v -m "sanity and regression" --html=./Reports/report_chrome.html testCases/
:: pytest -s -v -m "regression" --html=./Reports/report_chrome.html testCases/

:: pytest -s -v -m "sanity" --html=./Reports/report_firefox.html testCases/ --browser firefox
:: pytest -s -v -m "sanity or regression" --html=./Reports/report_firefox.html testCases/ --browser firefox
:: pytest -s -v -m "sanity and regression" --html=./Reports/report_firefox.html testCases/ --browser firefox
:: pytest -s -v -m "regression" --html=./Reports/report_firefox.html testCases/ --browser firefox