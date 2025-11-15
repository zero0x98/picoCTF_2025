# Sleuthkit Apprentice (Forensics)

Bước 1:

- Xác định loại tệp ổ đĩa và giải nén
- Trong bài này tôi giải nén bằng **gunzip**

```
$ gunzip disk.flag.img.gz
```



Bước 2:

- Sử dụng **mmls** để xem có bao nhiêu phân vùng

```
$ mmls disk.flag.img
```



Bước 3: 

- Sử dụng fsstat để xem chi tiết thông tin của một phân vùng nào đó

```
$ fsstat -o 2048 disk.flag.img 
```



Bước 4:

- Sử dụng **fls** để liệt kê các file và thư mục trong phân vùng

```
$ fls -i raw -f ext4 -o 2048 -r disk.flag.img 
```



Bước 5:

- Sử dụng **fls** kết hợp với **grep** để tìm các file hoặc thư mục có chữ **flag**

```
$ fls -i raw -f ext4 -o 360448 -r disk.flag.img | grep flag
```



Bước 6:

- Sử dụng icat để hiện nội dung trong file

```
$ icat -i raw -f ext4 -o 360448 -r disk.flag.img 2371
```

