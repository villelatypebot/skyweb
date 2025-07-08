import asyncio
from playwright.async_api import async_playwright

async def get_cheapest_flight(origin, destination, departure_date, return_date, adults=1, cabin_class='economy', proxy=None):
    async with async_playwright() as p:
        browser = None
        try:
            launch_options = {"headless": True}
            if proxy:
                # Parse the proxy string to extract components
                # Assuming format: http://username:password@ip:port
                proxy_parts = proxy.replace("http://", "").split("@")
                auth_parts = proxy_parts[0].split(":")
                server_parts = proxy_parts[1].split(":")

                launch_options["proxy"] = {
                    "server": f"{server_parts[0]}:{server_parts[1]}",
                    "username": auth_parts[0],
                    "password": auth_parts[1]
                }

            browser = await p.chromium.launch(**launch_options)
            page = await browser.new_page()

            # Construir URL sem usar backslashes em f-strings
            departure_clean = departure_date.replace('-', '')
            return_clean = return_date.replace('-', '')
            url = f"https://www.skyscanner.com.br/transporte/passagens-aereas/{origin.lower()}/{destination.lower()}/{departure_clean}/{return_clean}/?adultsv2={adults}&cabinclass={cabin_class}&inboundaltsenabled=false&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1"
            
            await page.goto(url, wait_until='domcontentloaded', timeout=90000)

            # Aceitar cookies se o pop-up aparecer
            try:
                await page.click('button:has-text("Concordo")', timeout=5000)
            except Exception:
                pass

            # Tirar um screenshot para depuração
            await page.screenshot(path="screenshot_before_mais_barato.png")

            # Esperar até que os resultados da busca estejam visíveis
            await page.wait_for_selector('button:has-text("Mais barato")', timeout=60000)

            # Clicar no botão 'Mais barato'
            await page.click('button:has-text("Mais barato")')

            # Esperar que os detalhes do voo sejam carregados
            await page.wait_for_selector('div[data-testid="details-card"]', timeout=60000)

            # Clicar em 'Veja mais' para expandir os detalhes
            await page.wait_for_selector('button:has-text("Veja mais")', timeout=10000)
            await page.click('button:has-text("Veja mais")')

            # Esperar a página carregar os detalhes do voo
            await page.wait_for_selector('div[data-testid="details-card"]', timeout=60000)

            # Extrair informações do voo mais barato
            price = await page.locator('div[data-testid="details-card"] span[data-testid="price"]').first.text_content()
            
            # Extrair detalhes da ida
            departure_details_elements = await page.locator('div[data-testid="details-card"] div.leg-info').nth(0).all_text_contents()
            departure_details = " ".join(departure_details_elements).strip()

            # Extrair detalhes da volta
            return_details_elements = await page.locator('div[data-testid="details-card"] div.leg-info').nth(1).all_text_contents()
            return_details = " ".join(return_details_elements).strip()

            # Extrair companhia aérea
            airline_elements = await page.locator('div[data-testid="details-card"] div.airline-names').all_text_contents()
            airline = " / ".join([a.strip() for a in airline_elements if a.strip()])

            # Capturar o link direto
            await page.wait_for_selector('a:has-text("Selecionar")', timeout=10000)
            await page.click('a:has-text("Selecionar")')
            await page.wait_for_load_state('networkidle')
            direct_link = page.url

            return {
                "price": price,
                "currency": "BRL",
                "departure_date": departure_date,
                "return_date": return_date,
                "airline": airline,
                "departure_details": departure_details,
                "return_details": return_details,
                "direct_link": direct_link
            }
        except Exception as e:
            print(f"Erro durante o scraping: {e}")
            return None
        finally:
            if browser:
                await browser.close()

