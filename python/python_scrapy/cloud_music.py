"""
1 由于artists和hot_artists会有部分重叠，导致数据库有部分重复
2 此次爬关键是添加headers
"""
from bs4 import BeautifulSoup
import pymysql
import requests


# 连接数据库
connection = pymysql.connect(host='localhost',
                             user='t',
                             password='t',
                             db='99',
                             port=3306 ,
                             charset='utf8')
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS ARTISTS")
sql = """CREATE TABLE ARTISTS (
         ARTIST_ID  CHAR(40) NOT NULL,
         ARTIST_NAME  CHAR(40)
          )"""
cursor.execute(sql)
connection.commit()


def insert_to_Mysql(find_arts):
    for artist in find_arts:
        artist_id = artist['href'].replace('/artist?id=', '').strip()
        artist_name = artist['title'].replace('的音乐', '')
        try:
            sql = "INSERT INTO `artists` (`ARTIST_ID`, `ARTIST_NAME`) VALUES (%s, %s)"
            cursor.execute(sql, (artist_id, artist_name))
            connection.commit()
        except Exception as e:
            # 打印错误日志
            print(e)

def save_artist(url):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'Connection': 'keep-alive',
        'Cookie': '_iuqxldmzr_=32; _ntes_nnid=41f441510623e189c2995610882d24ae,1536374059740; _ntes_nuid=41f441510623e189c2995610882d24ae; WM_TID=tMpXuHtbNHTCNDbqkXxME4RAgcbGmNx0; __remember_me=true; hb_MA-BFF5-63705950A31C_source=blog.csdn.net; __f_=1536718172717; usertrack=ezq0o1uY2GtGuik4BCVyAg==; _ga=GA1.2.372327600.1536743534; Province=010; City=010; UM_distinctid=165e6ad52a39b-09b68878398796-5701631-13c680-165e6ad5317101; vjuids=1a36efe5d2.165e6ad6631.0.fd49a57c2f1e5; vjlast=1537173448.1537173448.30; NNSSPID=1583f72fe27d4878bf162609be39c88a; vinfo_n_f_l_n3=068a00707c31a886.1.0.1537173448295.0.1537173490932; __utmc=94650624; playerid=59777621; WM_NI=fzlfafS0tWc50XqCZDNcexDBWhpeqUTNHyRGxdXuQLdLWrKc44ygSbIutmcFPPURj6%2Bl6fYqUHcVxGolKhv6yCbINBNLHiTCPo8%2FB0akGVNZe7TM1rCwL8tvEt%2BiqwyHaEU%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed1b243898cacaccd64f195a1d0bb539786ff85c8489aae9fb5bb4d86eea695d12af0fea7c3b92aa6a6a487e46e91f0bcb8e23ff488bfa4d9508ebdab99c74a95b8c086f45f9892889ad14dbcbc9896d448a8949993ca69f8ecb788d26a8babbc8ee24e94909bb3e93ee9b4fa87dc7b9798adb7fb4dadb48589f53ebb9daeaacd4a8e94888ad74994b1f8d0c13ca3b589b7cd52a7e99caeb47a81a984d9f77e87ace58af47dbb98afa6d837e2a3; JSESSIONID-WYYY=YesgP1BW7Up58QWKJkN7kEQEqvNuWZAJP0PT1gh2A1Je8I7WdnRZVGT79ksVKaSTGJTY1b%2BWMZBllo%5CX%2Bu1W1qSof6bwqKhBi1Np99oGx5sJUPTMQxH5fEElGeXOC8gFdmR5Nq1P0ifJYkfJqHuFxM4AnIr%2B26XS4td0rK8KYX70R7D2%3A1537255770703; MUSIC_U=33ba7b46705aae6168dd9df03de68026bcd0ddbf445b52d44bd19af436aea0a349609a48468fd56156ab30084d7f67b9a70b41177f9edcea; __csrf=21690531aeb580db033207573527f388; __utma=94650624.1507091701.1536374061.1537251376.1537254412.8; __utmz=94650624.1537254412.8.5.utmcsr=jianshu.com|utmccn=(referral)|utmcmd=referral|utmcct=/p/c2ce89b75a9f; __utmb=94650624.4.10.1537254412',
        'Host': 'music.163.com',
        'Referer': 'https://music.163.com/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
    }

    r = requests.get(url , headers=headers)
    # 网页解析
    soup = BeautifulSoup(r.content.decode(), 'html.parser')
    body = soup.body

    hot_artists = body.find_all('a', attrs={'class': 'msk'})
    artists = body.find_all('a', attrs={'class': 'nm nm-icn f-thide s-fc0'})

    insert_to_Mysql(hot_artists)
    print('-------%s -------%s-------hot_artists' %(i ,j))
    insert_to_Mysql(artists)
    print('-------%s -------%s-------artists' %(i ,j))


group_id =  [2002, 2003]  # id的值
initial = [ 65, 66] #67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]  # initial的值
for i in group_id:
    for j in initial:
        url = 'http://music.163.com/discover/artist/cat?id=' + str(i) + '&initial=' + str(j)
        save_artist(url)

print('Ye------------- headers matters ')
