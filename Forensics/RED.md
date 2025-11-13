# **RED** (Forensics)

Author: Shuailin Pan (LeConjuror)

### Description

RED, RED, RED, RED
Download the image: red.png

![image-20251113135434191](/home/meomeo/.config/Typora/typora-user-images/image-20251113135434191.png)

#### Bước 1:

- Sau khi tải red.png về bạn sẽ thấy 1 file ảnh màu đỏ.
- Đây là định dạng **png** nên tôi nghĩ ngay đến dùng **zsteg**

#### Bước 2:

- Sau khi chạy lệnh tôi nhận thấy có một đoạn mã rất khả nghi

  ![image-20251113135857785](/home/meomeo/.config/Typora/typora-user-images/image-20251113135857785.png)

> cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==

- Vậy là tôi nghĩ đến giải mã ra xem sao

  ![image-20251113140049360](/home/meomeo/.config/Typora/typora-user-images/image-20251113140049360.png)

Ồ wow quả nhiên điều chúng ta mong chờ cũng đến đó là một lá cờ: 

```
picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}
```

