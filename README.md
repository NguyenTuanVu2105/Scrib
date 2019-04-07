## Nhóm 7
### Thành viên:
- Nguyễn Thị Phương Đông
- Lê Mai An
- Nguyễn Tuấn Vũ
- Nguyễn Duy Chương
- Phạm Minh Đức

### Tên ứng dụng: Scrib.
### Đối tượng hướng đến: Các doanh nghiệp, công ty, trường học,....
### Mô tả tóm tắt phần mềm:
 + Ứng dụng book lịch họp cho các công ty, đội nhóm, ...
 + Người quản lý sẽ tạo ra cuộc họp và các khung giờ họp, rồi mời nhân viên chọn thời gian phù hợp
 + Nhân viên sẽ chọn các khung giờ mình có thể tham gia
 + Quản lý sẽ chọn ra khung giờ có đông số lượng người tham gia nhất
### Công nghệ sử dụng: html, css, js, jquery, Django.

### Hướng dẫn cài đặt (linux)

1. Trước tiên ta cần cài đặt trình quản lý gói cho Python nếu chưa có:

    `$ sudo easy_install pip`
   
2. Cài đặt gói virtualenv:

    `$ pip install --upgrade virtualenv`

3. Tạo Virtual Environment

     `$ virtualenv [project_name]`

  Virtualenv sẽ tạo ra một thư mục có tên là [project_name] chứa tất cả những gì cần thiết
  
4. Khởi động Virtual Environment

    `$ source [project_name]/bin/activate`
    
5. Cài đặt môi trường với requirements.txt

    `pip install requirements.txt`
    
6. Chỉnh sửa database trong Scrib/setting.py`

    ```
    DATABASES = {
      'default': {
        'ENGINE': 'django.db.backends.mysql'
        'HOST': 'localhost',
        'NAME': 'scrib',
        'USER': 'kennen',
        'PASSWORD': '',
      }
   }
   ```

* Lưu ý tạo database scrib trong cơ sở dữ liệu 

7.  Migrate database
	
    `python manage.py migrate`
    
8. Create superuser

	  `python manage.py createsuperuser`
    
9. Run

	  `python manage.py runserver [port] (default: 8000)`
