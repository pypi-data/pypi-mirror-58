import requests
import xmltodict


class HiPayCreditService:
    def __init__(self, ws_login, ws_password, callback_email, url_callback='', url_accept='', url_decline='',
                 url_cancel='', url_logo=''):
        self.ws_login = ws_login
        self.ws_password = ws_password
        self.callback_email = callback_email
        self.url_callback = url_callback
        self.url_accept = url_accept
        self.url_decline = url_decline
        self.url_cancel = url_cancel
        self.url_logo = url_logo

    def create_xml_envelope(data, hipay_url):
        envelope = f'''
                    <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1={hipay_url} xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
                       <SOAP-ENV:Body>
                          <ns1:generate>
                             <parameters>
                                <websiteId>{data['website_id']}</websiteId>
                                <categoryId>{data['category_id']}</categoryId>
                                <currency>{data['currency']}</currency>
                                <amount>{data['amount']}</amount>
                                <rating>{data['rating']}</rating>
                                <locale>{data['locale']}</locale>
                                <customerIpAddress>{data['customer_ip_address']}</customerIpAddress>
                                <description>{data['description']}</description>
                                <manualCapture>{data['manual_capture']}</manualCapture>
                                <customerEmail>{data['customer_email']}</customerEmail>
                                <emailCallback>{data['email_callback']}</emailCallback>
                                <urlCallback>{data['url_callback']}</urlCallback>
                                <urlAccept>{data['url_accept']}</urlAccept>
                                <urlDecline>{data['url_decline']}</urlDecline>
                                <urlCancel>{data['url_cancel']}</urlCancel>
                                <urlLogo>{data['url_logo']}</urlLogo>
                                <wsLogin>{data['ws_login']}</wsLogin>
                                <wsPassword>{data['ws_password']}</wsPassword>
                             </parameters>
                          </ns1:generate>
                       </SOAP-ENV:Body>
                    </SOAP-ENV:Envelope>
                    '''

        return envelope

    def generate_payment(self, hipay_url, website_id, category_id, amount, customer_email, currency="EUR", rating="ALL",
                         locale="pt_PT", customer_ip_address="127.0.0.1", description="Default description",
                         manual_capture=False):
        header = {'Content-type': 'text/xml'}
        request_data = {
            "website_id": website_id,
            "category_id": category_id,
            "currency": currency,
            "amount": amount,
            "rating": rating,
            "locale": locale,
            "customer_ip_address": customer_ip_address,
            "description": description,
            "manual_capture": manual_capture,
            "customer_email": customer_email,
            "email_callback": self.callback_email,
            "url_accept": self.url_accept,
            "url_callback": self.url_callback,
            "url_decline": self.url_decline,
            "url_cancel": self.url_cancel,
            "url_logo": self.url_logo,
            "ws_login": self.ws_login,
            "ws_password": self.ws_password,
        }

        envelope = create_xml_envelope(request_data, hipay_url)
        response = requests.post(url=hipay_url, data=envelope, headers=header)
        response_xml = xmltodict.parse(response.content)
        generate_result = response_xml['SOAP-ENV:Envelope']['SOAP-ENV:Body']['ns1:generateResponse']['generateResult']
        redirect_url = generate_result['redirectUrl']

        return redirect_url
