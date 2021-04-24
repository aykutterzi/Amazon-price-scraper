from requests_html import HTMLSession

urllist = [
    "https://www.amazon.com/dp/B0911MSYGW/ref=syn_sd_onsite_desktop_87?psc=1&uh_it=615f5789b63b6a069d68f5af41a3a446_CT&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExUDhMUzM5U0hUQU9GJmVuY3J5cHRlZElkPUEwNjQ0MzIxMThZVU1WWlNFVVNYRiZlbmNyeXB0ZWRBZElkPUEwNTg1Nzk5MUhHUEo4V01PMkFIVSZ3aWRnZXROYW1lPXNkX29uc2l0ZV9kZXNrdG9wJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==",
    "https://www.amazon.com/Gaming-VG32VQ-Curved-Monitor-FreeSync/dp/B07VFKSGRW/ref=pd_di_sccai_5?pd_rd_w=r8pMT&pf_rd_p=c9443270-b914-4430-a90b-72e3e7e784e0&pf_rd_r=TAZXD07RJABTGBN9XAWQ&pd_rd_r=0247231d-556f-4b6f-8cd2-1beddb42802c&pd_rd_wg=OEhHf&pd_rd_i=B07VFKSGRW&psc=1",
    "https://www.amazon.com/ASUS-VG34VQL1B-DisplayPort-Adjustable-DisplayHDR/dp/B08LCMYT54/ref=pd_di_sccai_1?pd_rd_w=1sRU0&pf_rd_p=c9443270-b914-4430-a90b-72e3e7e784e0&pf_rd_r=ZFYARWJ2E8T0X8RWBEGZ&pd_rd_r=7ebe0903-461e-45dc-bf7f-ac54351b0a85&pd_rd_wg=xe99V&pd_rd_i=B08LCMYT54&psc=1",
]


def getPrice(url):
    s = HTMLSession()
    r = s.get(url)
    r.html.render(sleep=1)

    product = {
        "title": r.html.xpath("//*[@id='productTitle']", first=True).text,
        "price": r.html.xpath('//*[@id="priceblock_ourprice"]', first=True).text,
    }

    print(product)
    return product


for item in urllist:

    getPrice(item)
