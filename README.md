# azango

مقدمه

این پروژه یک برنامه زمان‌بندی پخش فایل‌های صوتی است که می‌تواند در زمان‌های مشخص شده، فایل‌های صوتی را پخش کند. همچنین این برنامه دارای قابلیت برقراری تماس با استفاده از Asterisk Manager Interface (AMI) به ایزابل (Issabel) است.

پیش‌نیازها

برای اجرای این پروژه، به موارد زیر نیاز دارید:
- سیستم عامل لینوکس (مانند Ubuntu)
- دسترسی به ترمینال و قابلیت اجرای دستورات sudo
- اینترنت برای دانلود وابستگی‌ها

مراحل نصب

1. دانلود پروژه

ابتدا پروژه را از مخزن دانلود یا کلون کنید.

git clone git@github.com:naderii/Azan.git
cd Azan

2. تنظیم فایل‌های پروژه

اطمینان حاصل کنید که فایل‌های زیر در دایرکتوری پروژه موجود باشند:
- requirements.txt
- install.sh
- main.py (یا هر نامی که برای فایل اصلی پایتون خود انتخاب کرده‌اید)

3. اجازه اجرایی به اسکریپت نصب

به اسکریپت install.sh اجازه اجرایی بدهید:

chmod +x install.sh

4. اجرای اسکریپت نصب

اسکریپت نصب را اجرا کنید تا تمامی وابستگی‌ها نصب شده و فایل اجرایی تولید شود:

./install.sh

5. مکان فایل اجرایی

پس از اجرای موفقیت‌آمیز اسکریپت نصب، فایل اجرایی برنامه شما در دایرکتوری dist قرار خواهد گرفت.

استفاده از برنامه

اجرای فایل اجرایی

برای اجرای برنامه، به دایرکتوری dist بروید و فایل اجرایی را اجرا کنید:

cd dist
./main

رابط کاربری

برنامه دارای یک رابط کاربری گرافیکی است که به شما امکان می‌دهد زمان‌بندی‌های مختلف را اضافه کنید، برنامه را به عنوان یک سرویس پس‌زمینه اجرا کنید، پروسه را متوقف کنید و همچنین با ایزابل تماس بگیرید.

افزودن زمان‌بندی

1. ساعت و دقیقه را وارد کنید.
2. بر روی دکمه "Add Timing" کلیک کنید.
3. فایل صوتی مورد نظر خود را انتخاب کنید.

شروع زمان‌بندی

برای شروع زمان‌بندی، بر روی دکمه "Start Scheduler" کلیک کنید. این عملیات برنامه را به عنوان یک سرویس پس‌زمینه اجرا می‌کند.

توقف زمان‌بندی

برای متوقف کردن زمان‌بندی، بر روی دکمه "Stop Scheduler" کلیک کنید.

تماس با ایزابل

برای برقراری تماس با ایزابل، بر روی دکمه "Call Issabel" کلیک کنید.

تنظیمات AMI

اطمینان حاصل کنید که اطلاعات مربوط به AMI در فایل main.py به درستی تنظیم شده باشند. اطلاعات شامل هاست، پورت، نام کاربری، رمز عبور، کانتکست و اکستنشن باید با اطلاعات مربوط به ایزابل شما جایگزین شوند.

# AMI configuration
ami_host = 'your_issabel_host'
ami_port = 5038
ami_user = 'your_ami_user'
ami_secret = 'your_ami_secret'
ami_context = 'default'
ami_extension = '100'  # The extension to dial
ami_callerid = '100'  # Caller ID for the call

خطاهای متداول

- خطای دسترسی: اطمینان حاصل کنید که دستورات با دسترسی sudo اجرا می‌شوند.
- عدم وجود پایتون: بررسی کنید که پایتون و pip نصب شده باشند.
- مشکلات مربوط به کتابخانه‌ها: مطمئن شوید که تمام کتابخانه‌ها از طریق requirements.txt نصب شده باشند.

نتیجه‌گیری

این فایل راهنما شما را در مراحل مختلف نصب و اجرای برنامه هدایت می‌کند. با اجرای صحیح این مراحل، می‌توانید از برنامه زمان‌بندی پخش فایل‌های صوتی و قابلیت تماس با ایزابل بهره‌مند شوید.


استفاده برای عموم آزاد است
برای استفاده از آن به روح شهدای خدمت صلوات هدیه کنید
