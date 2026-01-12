print("🚀 بدأ تشغيل Crypto Genius Pro V2.0")
print("✅ البوت الآن يعمل على Koyeb 24/7")

import time
from datetime import datetime

دورة = 0
while True:
    دورة += 1
    print(f"📊 الدورة رقم {دورة} - البوت يعمل...")
    
    if دورة % 30 == 0:
        print(f"⏰ الوقت: {datetime.now()}")
        print("💓 البوت لا يزال نشطاً")
    
    time.sleep(60)
