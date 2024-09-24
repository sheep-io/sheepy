from sheepy.sheeptest import SheepyTestCase  

class TestHttpBinApi(SheepyTestCase):
    """ Expected output:

    Test Results:
        TestHttpBinApi.test_delete_resource: OK
        TestHttpBinApi.test_get_json: OK
        TestHttpBinApi.test_get_status: OK
        TestHttpBinApi.test_post_data: OK
        TestHttpBinApi.test_put_data: OK

    """
    def __init__(self):        
        super().__init__(base_url="https://httpbin.org")

    def test_get_status(self):
        
        response = self.api.get("/status/200")
        self.assertStatusCode(response, 200)  

    def test_get_json(self):
        
        response = self.api.get("/json")
        self.assertStatusCode(response, 200)  
        self.assertJsonResponse(response)  
        self.assertResponseContains(response, "slideshow")  

    def test_post_data(self):
        
        payload = {"name": "SheepyTest", "framework": "unittest"}
        response = self.api.post("/post", json=payload)
        self.assertStatusCode(response, 200)  
        self.assertJsonResponse(response)  
        self.assertResponseContains(response, "json")  
        self.assertEqual(response.json()["json"], payload)  

    def test_put_data(self):
        
        payload = {"key": "value"}
        response = self.api.put("/put", json=payload)
        self.assertStatusCode(response, 200)  
        self.assertJsonResponse(response)  
        self.assertResponseContains(response, "json")
        self.assertEqual(response.json()["json"], payload) 

    def test_delete_resource(self):
        
        response = self.api.delete("/delete")
        self.assertStatusCode(response, 200)  
        self.assertJsonResponse(response)  
