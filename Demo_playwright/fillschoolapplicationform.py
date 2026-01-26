from playwright.sync_api import sync_playwright

def fill_skolaro_form():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://apps.skolaro.com/school/psbbmscuddalore/leads")

        # Wait for form
        page.wait_for_selector('#leads-form', timeout=20000)

        # ---------- Enquirer ----------
        page.fill('#field-lead_email', 'parent@example.com')
        page.fill('#field-36968', '9876543210')
        page.wait_for_timeout(800)
        page.select_option('#field-36956', '2025-2026')
        page.wait_for_timeout(800)

        # ---------- Student ----------
        page.fill('#field-36957', 'Aarav Kumar')
        page.wait_for_timeout(800)

        page.select_option('#field-36958', 'Male')
        page.wait_for_timeout(800)

        page.fill('#field-36959', '22/01/2026')
        page.keyboard.press('Enter')
        page.wait_for_timeout(800)

        page.select_option('#field-36962', 'V')
        page.wait_for_timeout(800)
        


        

        # Success dialog
        
        print("✅ Form submitted successfully!")
      
        browser.close()

if __name__ == "__main__":
    fill_skolaro_form()
