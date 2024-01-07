import smtplib
content="Hello SaeeAM"
mail=smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
sender='shiva850681@gmail.com'
recipient='sivrity@gmail.com'
mail.login('shiva850681@gmail.com','******')
header='To:'+receipient+'\n'+'From:' \
+sender+'\n'+'subject:testmail\n'
content=header+content
mail.sendmail(sender, recipient, content)
mail.close()
