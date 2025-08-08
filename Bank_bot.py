#قاعدة بيانات بسيطة لتخزين الحسابات : username: password
accounts = {}

# دالة إنشاء حساب جديد
def signup():
    print("\n🔐 إنشاء حساب جديد")
    username = input("اختر اسم مستخدم: ").strip()
    if username in accounts:
        print("⚠️ اسم المستخدم موجود بالفعل.")
        return False
    password = input("اختر كلمة مرور: ").strip()
    accounts[username] = password
    print("✅ تم إنشاء الحساب بنجاح.\n")
    return True

# دالة تسجيل الدخول
def login():
    print("\n🔑 تسجيل الدخول")
    username = input("اسم المستخدم: ").strip()
    password = input("كلمة المرور: ").strip()
    if username in accounts and accounts[username] == password:
        print("✅ تم تسجيل الدخول بنجاح.\n")
        return True
    else:
        print("❌ اسم المستخدم أو كلمة المرور غير صحيحة.")
        return False

# دالة البوت بعد الدخول
def bank_bot():
    print("أهلا بك في خدمة عملاء بنك T 💬")
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

# نقطة بداية البرنامج
def main():
    print("👋 مرحبًا بك في نظام البنك!")
    while True:
        choice = input("\nهل تريد (1) تسجيل الدخول أم (2) إنشاء حساب؟ (أو 'خروج'): ").strip().lower()
        if choice == "1":
            if login():
                bank_bot()
                break
        elif choice == "2":
            signup()
        elif choice == "خروج":
            print("👋 إلى اللقاء!")
            break
        else:
            print("⚠️ من فضلك اختر (1) أو (2) أو 'خروج'.")

# تشغيل البرنامج
main()