def bank_bot():
    print("أهلا بك في خدمة عملاء ب   بنك  t 💬")
    print("اسألني عن: الرصيد - تحويل - أقرب فرع - خروج")

    while True:
        user_input = input("أنت: ").lower()

        if "رصيد" in user_input:
            print("البوت: رصيدك الحالي هو ١٢,٣٠٠ جنيه.")
        elif "تحويل" in user_input:
            print("البوت: من فضلك أدخل رقم الحساب المحول إليه.")
        elif "فرع" in user_input:
            print("البوت: أقرب فرع ليك في شارع التحرير، وسط البلد.")
        elif "خروج" in user_input or "exit" in user_input:
            print("البوت: شكرًا لاستخدامك خدمتنا. إلى اللقاء!")
            break
        else:
            print("البوت: آسف، مش فاهم سؤالك. ممكن تعيد صياغته؟")

# تشغيل البوت
bank_bot()
