from playwright.async_api import Playwright
ordersPayload = {"orders":[{"country": "India", "productOrderedId": "68a961459320a140fe1ca57a"}]}


class APIUtils:

    def tokenby (self, playwright: Playwright):
        log_request = playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
        log_response = log_request.post(url="api/ecom/auth/login",
                                      data={userEmail: "indhurajan019@gmail.com", userPassword: "Indhu1997#"})
        assert log_response.ok()
        print(log_response.json())
        response_body = logresponse.json()
        return response_body["token"]

    def create_order(self, playwright: Playwright):
        token = self.tokenby(playwright)
        api_request = playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
        response = api_request.post(url="api/ecom/order/create-order", data=orderspayload,
                                    headers={"Authorization": token, "content-type": "application/json"})
        print(response.json())
