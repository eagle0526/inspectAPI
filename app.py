from playwright.sync_api import sync_playwright
import json

def capture_xhr_requests(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        
        xhr_requests = []
        
        def handle_request(request):
            if request.resource_type in ["xhr", "fetch"]:
                xhr_requests.append({
                    "url": request.url,
                    "method": request.method,
                    "headers": request.headers,
                    "post_data": request.post_data
                })
        
        page.on("request", handle_request)
        
        try:
            page.goto(url, wait_until="networkidle", timeout=60000)
        except Exception as e:
            print(f"頁面加載出錯: {e}")
        
        # 等待一段時間，以捕獲可能的延遲加載的請求
        page.wait_for_timeout(5000)
        
        print(f"在頁面 {url} 中捕獲到以下 XHR/Fetch 請求：")
        for req in xhr_requests:
            print(f"- URL: {req['url']}")
            print(f"  Method: {req['method']}")
            print(f"  Headers: {json.dumps(req['headers'], indent=2)}")
            if req['post_data']:
                print(f"  Post Data: {req['post_data']}")
            print("---")
        
        browser.close()

if __name__ == "__main__":
    # url = "https://tixcraft.com/ticket/ticket/24_mdhltour/18676/4/36"
    # url = "https://tixcraft.com/ticket/ticket/24_colde/17640/2/47"
    # url = "https://tixcraft.com/ticket/checkout"
    url = "https://tixcraft.com/ticket/finish"
    # url = "https://www.dachanfoods.com.tw/zh-TW/carts/e2a5c550718d013d06601626e4c097d2"
    capture_xhr_requests(url)

    print("end *************")    

