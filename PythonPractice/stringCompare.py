def compareStrings(a, b):
    if a == b:
        return "They were equal"
    elif a == None or b == None:
        return "One or more strings had no content"
    else:
        print(getStringDifferences(a, b))
        return "They were not equal"

a = f"""<saml2p:AuthnRequest xmlns:saml2p="urn:oasis:names:tc:SAML:2.0:protocol"
                     AssertionConsumerServiceURL="https://microfocus92-dev-ed.my.salesforce.com"
                     Destination="https://vlab026101.dom026100.lab/osp/a/FEDSSO/auth/saml2/sso"
                     ID="_2CAAAAYkoIvJqMDAwMDAwMDAwMDAwMDAwAAAA8ojZvdRXwOzJXbxamF3EXxkda6toObjoak7SxFdd3SikZV7ryTscdaDg6hCSK82Bib42LSC4aBlPIeuY3RKvt-yfcHvN_kb-_ELjvnunfOvH0yCvopY12C0Kszik4GO10AtPBZCPSy9rZiqpBD2FyvNx947oBk6WSuCaPrrDFlWJfM8NyMLktFw3paZuy-6yYQnddJkSNo8dTUvMDKBVfPkSWaKpWOOx763v3U1kA4-SnmY9C_xnQcxqPBk3XlUziw"
                     IssueInstant="2023-06-07T22:18:54.078Z"
                     ProtocolBinding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST"
                     Version="2.0"
                     >
    <saml2:Issuer xmlns:saml2="urn:oasis:names:tc:SAML:2.0:assertion">https://microfocus92-dev-ed.my.salesforce.com</saml2:Issuer>
    <ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
        <ds:SignedInfo>
            <ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#" />
            <ds:SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256" />
            <ds:Reference URI="#_2CAAAAYkoIvJqMDAwMDAwMDAwMDAwMDAwAAAA8ojZvdRXwOzJXbxamF3EXxkda6toObjoak7SxFdd3SikZV7ryTscdaDg6hCSK82Bib42LSC4aBlPIeuY3RKvt-yfcHvN_kb-_ELjvnunfOvH0yCvopY12C0Kszik4GO10AtPBZCPSy9rZiqpBD2FyvNx947oBk6WSuCaPrrDFlWJfM8NyMLktFw3paZuy-6yYQnddJkSNo8dTUvMDKBVfPkSWaKpWOOx763v3U1kA4-SnmY9C_xnQcxqPBk3XlUziw">
                <ds:Transforms>
                    <ds:Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature" />
                    <ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#" />
                </ds:Transforms>
                <ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256" />
                <ds:DigestValue>wPuwqdJDgmkxgilO7BFoWChyjKVoFwyBK+wsDYRahL0=</ds:DigestValue>
            </ds:Reference>
        </ds:SignedInfo>
        <ds:SignatureValue>duRO8yHVqS6ltoLysKhid9l/W5gZCSyB7CaMAjRjO1ddNrhru9N3I0Ob/llThDPh7POJi4wo9q11h7Ujz1fqxenKPSOrSxcrzlA+C+eWE63L1+ffx62QP+sIKXGlPNJRo6qYHuJOQyK1m5utH0WdpzF+hBmO4fmyik9zv8aAEVg6GnQ0gkhqgt3S/ynO65znRWVVnYvKuAi7xt4pSBJZjOQFjWNc1j3dfUaGOtLW/C0rpEwmFrHwp35zn2dzgMkyl4z+GucezuB8YLVBHVmdEMvjlg3Jtd2PIc3RIcZxSKnsHdN4IUjJAfQvx1hky8W2sWpi5m/097NArlEhY6ahzw==</ds:SignatureValue>
        <ds:KeyInfo>
            <ds:X509Data>
                <ds:X509Certificate>MIIErDCCA5SgAwIBAgIOAYXhGwezAAAAAGCHU40wDQYJKoZIhvcNAQELBQAwgZAxKDAmBgNVBAMM
H1NlbGZTaWduZWRDZXJ0XzI0SmFuMjAyM18yNDA4NDMxGDAWBgNVBAsMDzAwRDVmMDAwMDA5bEhz
RjEXMBUGA1UECgwOU2FsZXNmb3JjZS5jb20xFjAUBgNVBAcMDVNhbiBGcmFuY2lzY28xCzAJBgNV
BAgMAkNBMQwwCgYDVQQGEwNVU0EwHhcNMjMwMTI0MDAwODQzWhcNMjQwMTI0MDAwMDAwWjCBkDEo
MCYGA1UEAwwfU2VsZlNpZ25lZENlcnRfMjRKYW4yMDIzXzI0MDg0MzEYMBYGA1UECwwPMDBENWYw
MDAwMDlsSHNGMRcwFQYDVQQKDA5TYWxlc2ZvcmNlLmNvbTEWMBQGA1UEBwwNU2FuIEZyYW5jaXNj
bzELMAkGA1UECAwCQ0ExDDAKBgNVBAYTA1VTQTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoC
ggEBAIEu3RnSzT/wgvt/S7NBjwS+h2RM0cKKvLrzKoJEWlneZzJHVqvSOjHiT5A2bJQuo8atcdFL
t17+kZClc6AI06jw5YJRcWFqcbpJGFnByt/KyVdDvA4+iRiwLp3fl7OU2qdiqtU0gPKdlQzHqlw8
buA9AKK/Y8CHMVg+RzlcIqvsWctN3scK/ZO01V/cBAluYAGFPCqKhryHCh5ka9FFqogTbHmriaoF
VfKidDFgcH08PSW/MXP9yMS3vF2mGlHWbJWE33cZHXkzdbC3BIRAmyGZMxEJU9Qs3XZltUfOjECU
WBxDMToFckLfpqBTwytO8KyyrGDCocHvqKZKY8kJoHECAwEAAaOCAQAwgf0wHQYDVR0OBBYEFEOA
hLWuLUV5J0JZlUpJagScM1mzMA8GA1UdEwEB/wQFMAMBAf8wgcoGA1UdIwSBwjCBv4AUQ4CEta4t
RXknQlmVSklqBJwzWbOhgZakgZMwgZAxKDAmBgNVBAMMH1NlbGZTaWduZWRDZXJ0XzI0SmFuMjAy
M18yNDA4NDMxGDAWBgNVBAsMDzAwRDVmMDAwMDA5bEhzRjEXMBUGA1UECgwOU2FsZXNmb3JjZS5j
b20xFjAUBgNVBAcMDVNhbiBGcmFuY2lzY28xCzAJBgNVBAgMAkNBMQwwCgYDVQQGEwNVU0GCDgGF
4RsHswAAAABgh1ONMA0GCSqGSIb3DQEBCwUAA4IBAQAEpZXjuS+fVi3jQTnKyPNRY+ejRb8vM4Kd
Ep+LuYMRUhC3JrsTJvb4iz9au0DCn4ZlSPJUrbSZin4LtMzTFu9I94SAoEAoScs6gsyI/cI/vnzD
ePA0ut3X+wf/hYDFjfIBKe4P1e0XK8fFYAf+QaZSQCvEWW1+BYv/fyKt5igybzSWwKWQlOjhVIgR
oSKKlRX1AoNvbaUfT5Rk8o48OLKAbfP/YQoP86iPYjMiwKVhi34ulHEK1nFlZR8mFdSUdvlwgF6d
xsrQlMzlGiMSreccay94WByRwblGNzierYp6AcQDCtqYCPbci1YIgFuZzXsuNp+AHfH621eB7kai
2vu8</ds:X509Certificate>
            </ds:X509Data>
        </ds:KeyInfo>
    </ds:Signature>
</saml2p:AuthnRequest>"""
working = f"""<saml2p:AuthnRequest xmlns:saml2p="urn:oasis:names:tc:SAML:2.0:protocol"
                     AssertionConsumerServiceURL="https://microfocus92-dev-ed.my.salesforce.com"
                     Destination="https://vlab026101.dom026100.lab/osp/a/FEDSSO/auth/saml2/sso"
                     ID="_2CAAAAYkoNbu-MDAwMDAwMDAwMDAwMDAwAAAA8nY5EefJ03oIftT6TjsvRJQTe5PXYlXHDDJs646Ulgy3soUZU7PL2CMoOwqHNeYyZf2r012Vh9MaAJAd24QSRxV20powCZ3OQQcNk4lIhtTcedA291If6Bl1bRTKdKLeAIbcEi4XHnt7ZgRLgkxWpn4zrqm1JFCVQxtQzNRgX-pczxfV1jjbUmTJgStlllR2zpk2_3XUGMGigCD3jhom15XmGJG2AwD9wcVbHwCdQuYLnScKomOup3O-saDXzy-TWw"
                     IssueInstant="2023-06-07T22:39:29.927Z"
                     ProtocolBinding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST"
                     Version="2.0"
                     >
    <saml2:Issuer xmlns:saml2="urn:oasis:names:tc:SAML:2.0:assertion">https://microfocus92-dev-ed.my.salesforce.com</saml2:Issuer>
    <ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
        <ds:SignedInfo>
            <ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#" />
            <ds:SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256" />
            <ds:Reference URI="#_2CAAAAYkoNbu-MDAwMDAwMDAwMDAwMDAwAAAA8nY5EefJ03oIftT6TjsvRJQTe5PXYlXHDDJs646Ulgy3soUZU7PL2CMoOwqHNeYyZf2r012Vh9MaAJAd24QSRxV20powCZ3OQQcNk4lIhtTcedA291If6Bl1bRTKdKLeAIbcEi4XHnt7ZgRLgkxWpn4zrqm1JFCVQxtQzNRgX-pczxfV1jjbUmTJgStlllR2zpk2_3XUGMGigCD3jhom15XmGJG2AwD9wcVbHwCdQuYLnScKomOup3O-saDXzy-TWw">
                <ds:Transforms>
                    <ds:Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature" />
                    <ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#" />
                </ds:Transforms>
                <ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256" />
                <ds:DigestValue>8JSdR5Gg2EO95S3+CErvZjVL24zzsXtvBD712nXTUIA=</ds:DigestValue>
            </ds:Reference>
        </ds:SignedInfo>
        <ds:SignatureValue>L4nEvBU76gz/WDbGgQmfZ+EqL1hOygdiM1ZACbT8+mMM+WDraQaPNUKztRKliZjWFLBVv2fQFZ9tN45seq7LjI1W3SnP9TF2A4eEViTUCrSZLT+SWb8cNRgxBzeFnN2iv1Ltm1Arw2d0vIPtiXcvcPjO10PCVn5buzXuG7ro8w4GgckHIqWHxusk+g5u+xGF41F4EnQpKVTcyrpmgIW1vXQhqd1b85kFagKGHEJsjU+DTo6qyKccC+h0x4qvLUbgce7aJdif0rcN8UP0bVFzs2K8FYO277lse/OVnthYFLiINcMMxwCouWZe6RpC5sPJ8B2JLtleAF9u7Ip7skW0Rg==</ds:SignatureValue>
        <ds:KeyInfo>
            <ds:X509Data>
                <ds:X509Certificate>MIIErDCCA5SgAwIBAgIOAYXhGwezAAAAAGCHU40wDQYJKoZIhvcNAQELBQAwgZAxKDAmBgNVBAMM
H1NlbGZTaWduZWRDZXJ0XzI0SmFuMjAyM18yNDA4NDMxGDAWBgNVBAsMDzAwRDVmMDAwMDA5bEhz
RjEXMBUGA1UECgwOU2FsZXNmb3JjZS5jb20xFjAUBgNVBAcMDVNhbiBGcmFuY2lzY28xCzAJBgNV
BAgMAkNBMQwwCgYDVQQGEwNVU0EwHhcNMjMwMTI0MDAwODQzWhcNMjQwMTI0MDAwMDAwWjCBkDEo
MCYGA1UEAwwfU2VsZlNpZ25lZENlcnRfMjRKYW4yMDIzXzI0MDg0MzEYMBYGA1UECwwPMDBENWYw
MDAwMDlsSHNGMRcwFQYDVQQKDA5TYWxlc2ZvcmNlLmNvbTEWMBQGA1UEBwwNU2FuIEZyYW5jaXNj
bzELMAkGA1UECAwCQ0ExDDAKBgNVBAYTA1VTQTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoC
ggEBAIEu3RnSzT/wgvt/S7NBjwS+h2RM0cKKvLrzKoJEWlneZzJHVqvSOjHiT5A2bJQuo8atcdFL
t17+kZClc6AI06jw5YJRcWFqcbpJGFnByt/KyVdDvA4+iRiwLp3fl7OU2qdiqtU0gPKdlQzHqlw8
buA9AKK/Y8CHMVg+RzlcIqvsWctN3scK/ZO01V/cBAluYAGFPCqKhryHCh5ka9FFqogTbHmriaoF
VfKidDFgcH08PSW/MXP9yMS3vF2mGlHWbJWE33cZHXkzdbC3BIRAmyGZMxEJU9Qs3XZltUfOjECU
WBxDMToFckLfpqBTwytO8KyyrGDCocHvqKZKY8kJoHECAwEAAaOCAQAwgf0wHQYDVR0OBBYEFEOA
hLWuLUV5J0JZlUpJagScM1mzMA8GA1UdEwEB/wQFMAMBAf8wgcoGA1UdIwSBwjCBv4AUQ4CEta4t
RXknQlmVSklqBJwzWbOhgZakgZMwgZAxKDAmBgNVBAMMH1NlbGZTaWduZWRDZXJ0XzI0SmFuMjAy
M18yNDA4NDMxGDAWBgNVBAsMDzAwRDVmMDAwMDA5bEhzRjEXMBUGA1UECgwOU2FsZXNmb3JjZS5j
b20xFjAUBgNVBAcMDVNhbiBGcmFuY2lzY28xCzAJBgNVBAgMAkNBMQwwCgYDVQQGEwNVU0GCDgGF
4RsHswAAAABgh1ONMA0GCSqGSIb3DQEBCwUAA4IBAQAEpZXjuS+fVi3jQTnKyPNRY+ejRb8vM4Kd
Ep+LuYMRUhC3JrsTJvb4iz9au0DCn4ZlSPJUrbSZin4LtMzTFu9I94SAoEAoScs6gsyI/cI/vnzD
ePA0ut3X+wf/hYDFjfIBKe4P1e0XK8fFYAf+QaZSQCvEWW1+BYv/fyKt5igybzSWwKWQlOjhVIgR
oSKKlRX1AoNvbaUfT5Rk8o48OLKAbfP/YQoP86iPYjMiwKVhi34ulHEK1nFlZR8mFdSUdvlwgF6d
xsrQlMzlGiMSreccay94WByRwblGNzierYp6AcQDCtqYCPbci1YIgFuZzXsuNp+AHfH621eB7kai
2vu8</ds:X509Certificate>
            </ds:X509Data>
        </ds:KeyInfo>
    </ds:Signature>
</saml2p:AuthnRequest>"""

def getStringDifferences(inputA, inputB):
    inputAArray = inputA.split()
    inputBArray = inputB.split()
    differenceInputA = []
    differenceInputB = []
    position = 0
    for letter in inputAArray:
        if(letter != inputBArray[position]):
            differenceInputA.append({letter, position})
            differenceInputB.append({inputBArray[position], position})
        position = position+1
    return(differenceInputA, differenceInputB)

print(compareStrings(a, working))