# <h2 id="title"> Thư viên Schedule trên ngôn ngữ Python để chạy service background.</h2>

# Copyright: MobioVN


#### Cài đặt:
`$ pip3 install m-schedule`

#### Sử dụng:

1. Tạo class thực thi scheduler kế thừa từ class BaseScheduler
    ```python
    class TestScheduler(BaseScheduler):
        def owner_do(self):
            # TODO
            pass
    
        def get_schedule(self):
            """
            hàm xác định thời điểm chạy của scheduler, bằng cách xử dụng thư viện schedule
            Các ví dụ hướng dẫn cách xác định thời gian chạy
            1. scheduler chỉ thực hiện công việc một lần duy nhất.
                return None
            2. scheduler sẽ thực hiện mỗi 10 phút một lần.
                return schedule.every(10).minutes
            3. scheduler sẽ thực hiện hàng ngày vào lúc 10h 30 phút.
                return schedule.every().day.at("10:30")
            4. scheduler sẽ thực hiện sau mỗi giờ.
                return schedule.every().hour
            5. scheduler sẽ thực hiện vào mỗi thứ 2 hàng tuần.
                return schedule.every().monday
            6. scheduler sẽ thực hiện vào mỗi thứ 5 hàng tuần và vào lúc 13h 15'.
                return schedule.every().wednesday.at("13:15")
            """
        return schedule.every(10).minutes
    ```

2. Đăng ký scheduler với factory
    ```python
    factory = SchedulerFactory()
    factory.add(TestScheduler(name="MyScheduler", redis_uri="redis://redis-server:6379/0"))
    factory.run()
    ```