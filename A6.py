import qrcode
#taking upi id as a input
upi_id=input("enter your upi id=")

#illigal link genrate

phonepe_url=f"upi://pay>pa={upi_id}&pn=Recipient%20Name&mc=1234"
paytm_url=f"upi://pay>pa={upi_id}&pn=Recipient%20Name&mc=1234"
googlepay_url=f"upi://pay>pa={upi_id}&pn=Recipient%20Name&mc=1234"


phonepe_qr=qrcode.make(phonepe_url)
paytm_qr=qrcode.make(paytm_url)
googlepay_qr=qrcode.make(googlepay_url)


#save the qr code to image file

phonepe_qr.save("phonepe_qr.png")
paytm_qr.save("paytm_qr.png")
googlepay_qr.save("googlepay_qr.png")


#display the code
phonepe_qr.show()
paytm_qr.show()
googlepay_qr.show()