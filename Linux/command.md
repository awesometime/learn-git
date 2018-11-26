history    存在/root/.bash_history

mount /dev/hda1 /mnt   把/dev/hda1挂在/mnt下

df  disk free

### 
```
生成文件的MD5、SHA、SHA256
Linux系统生成MD5、SHA、SHA256
md5sum file1.zip  >> MD5.txt

sha1sum file1.zip >> SHA1.txt

sha256sum file1.zip >> SHA256.txt



windows系统生成MD5、SHA、SHA256

certutil -hashfile file1.zip MD5 >> MD5.txt

certutil -hashfile file1.zip SHA1 >>SHA1.txt

certutil -hashfile file1.zip SHA256 >> SHA256.txt
```
